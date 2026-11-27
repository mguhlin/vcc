#!/usr/bin/env python3
"""Evidence-based APK preflight. No uploads, hook installation or store certification.

Original VCC checks informed by mjmirza/app-store-compliance and Android docs.
Run against final signed bytes, then do the runtime/manual checks in the guide.
"""
import argparse
import hashlib
import json
import re
import struct
import subprocess
import tempfile
import zipfile
from pathlib import Path


def run(command):
    result = subprocess.run([str(x) for x in command], text=True, capture_output=True, timeout=90)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or 'Tool failed')
    return result.stdout


def elf_alignment(data):
    """Return PT_LOAD alignments from little/big-endian ELF32/64, without executing it."""
    if data[:4] != b'\x7fELF' or len(data) < 64:
        raise ValueError('Invalid ELF')
    endian = '<' if data[5] == 1 else '>' if data[5] == 2 else None
    if endian is None:
        raise ValueError('Unknown ELF byte order')
    if data[4] == 2:
        offset = struct.unpack_from(endian+'Q', data, 32)[0]
        size, count = struct.unpack_from(endian+'HH', data, 54)
        fmt, align_offset = 'Q', 48
    elif data[4] == 1:
        offset = struct.unpack_from(endian+'I', data, 28)[0]
        size, count = struct.unpack_from(endian+'HH', data, 42)
        fmt, align_offset = 'I', 28
    else:
        raise ValueError('Unknown ELF class')
    if not size or count > 4096:
        raise ValueError('Invalid program headers')
    return [struct.unpack_from(endian+fmt, data, offset+i*size+align_offset)[0]
            for i in range(count)
            if struct.unpack_from(endian+'I', data, offset+i*size)[0] == 1]


def inspect(apk, tools, minimum_target):
    checks = []

    def check(name, passed, detail):
        checks.append({'check': name, 'status': 'PASS' if passed else 'FAIL', 'evidence': detail})

    badging = run([tools/'aapt2', 'dump', 'badging', apk])
    tree = run([tools/'aapt2', 'dump', 'xmltree', '--file', 'AndroidManifest.xml', apk])
    permissions = run([tools/'aapt2', 'dump', 'permissions', apk])
    check('release-debug-flag', 'application-debuggable' not in badging,
          'Compiled APK badging; release must not be debuggable')
    target = re.search(r"targetSdkVersion:'(\d+)'", badging)
    check('declared-target', bool(target) and int(target[1]) >= minimum_target,
          f'Compiled target {target[1] if target else "unknown"}; requested floor {minimum_target}. Revalidate current channel policy.')
    check('cleartext-disabled', bool(re.search(r'usesCleartextTraffic[^\n]*=(?:false|0x0)\b', tree)),
          'Compiled manifest explicitly disables cleartext traffic')
    check('backup-disabled', bool(re.search(r'allowBackup[^\n]*=(?:false|0x0)\b', tree)),
          'Compiled manifest disables backup; independently inspect transfer rules/device behavior')
    declared = re.findall(r"uses-permission: name='([^']+)'", permissions)
    sensitive = [p for p in declared if p != 'android.permission.INTERNET']
    check('minimal-permissions', not sensitive,
          {'declared': declared, 'needs_app_specific_review': sensitive})
    # Each exposed component is a review item. Launcher is an intended public entry.
    components = []
    for block in re.split(r'(?=\n\s*E: (?:activity|service|receiver|provider)\b)', tree)[1:]:
        first = block.split('\n', 2)[1] if block.startswith('\n') else block.splitlines()[0]
        component = block.split('\n      E:', 1)[0]
        if re.search(r'exported[^\n]*=(?:true|0xffffffff)', component):
            launcher = 'android.intent.action.MAIN' in component and 'android.intent.category.LAUNCHER' in component
            components.append({'component': first.strip(), 'launcher': launcher})
    check('exposed-components', all(c['launcher'] for c in components), components)
    with zipfile.ZipFile(apk) as package:
        names = package.namelist()
        check('unique-archive-paths', len(names) == len(set(names)) and not any(
            Path(n).is_absolute() or '..' in Path(n).parts for n in names), 'APK ZIP names are unique and confined')
        libraries = [n for n in names if n.startswith('lib/') and n.endswith('.so')]
        native = {}
        for name in libraries:
            info = package.getinfo(name)
            if info.file_size > 256*1024*1024:
                native[name] = []; continue
            native[name] = elf_alignment(package.read(name))
        check('native-16kb-elf', all(v and min(v) >= 16384 for v in native.values()),
              native or 'No native libraries: Java/Kotlin-only APK. Runtime testing still required.')
        suspect = [n for n in names if re.search(r'(^|/)(?:\.env(?:\..*)?|.*\.(?:p12|jks|keystore|pem|key)|reader\.db|catalog\.sqlite)$', n, re.I)]
        check('private-material-paths', not suspect, suspect or 'No recognized key/env/catalog paths; not a complete secrets scan')
    signature = run(['java', '-jar', tools/'lib/apksigner.jar', 'verify', '--verbose', '--print-certs', apk])
    check('signature', 'Verifies' in signature and 'CN=Android Debug' not in signature,
          [line for line in signature.splitlines() if 'SHA-256 digest:' in line or 'scheme' in line])
    run([tools/'zipalign', '-c', '-P', '16', '4', apk])
    check('package-alignment', True, 'zipalign -c -P 16 4 passed on signed APK')
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('apk', type=Path)
    parser.add_argument('--build-tools', type=Path, required=True)
    parser.add_argument('--minimum-target', type=int, required=True, help='Explicit policy floor; not a permanent hardcoded store requirement')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        checks = inspect(args.apk, args.build_tools, args.minimum_target)
        passed = all(row['status'] == 'PASS' for row in checks)
        report = {'artifact': args.apk.name, 'sha256': hashlib.file_digest(args.apk.open('rb'), 'sha256').hexdigest(),
                  'result': 'PASS_SCOPED' if passed else 'FAIL', 'checks': checks,
                  'not_checked': ['installed runtime / task recovery', 'TalkBack / large text / orientation',
                                  'actual network recipients and SDK behavior', 'privacy/store declarations and account readiness',
                                  'publisher identity / store approval', 'complete secret/dependency/source security audit']}
    except Exception as exc:
        passed = False
        report = {'artifact': args.apk.name, 'result': 'NOT_CHECKED', 'error': str(exc)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
