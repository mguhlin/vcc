import importlib.util
import struct
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location('apk_checks', Path(__file__).with_name('check_android_release.py'))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class APKChecks(unittest.TestCase):
    def test_native_alignment_reads_program_headers(self):
        elf = bytearray(120)
        elf[:6] = b'\x7fELF\x02\x01'
        struct.pack_into('<Q', elf, 32, 64)
        struct.pack_into('<HH', elf, 54, 56, 1)
        struct.pack_into('<I', elf, 64, 1)
        struct.pack_into('<Q', elf, 112, 16384)
        self.assertEqual(checks.elf_alignment(elf), [16384])
        struct.pack_into('<Q', elf, 112, 4096)
        self.assertEqual(checks.elf_alignment(elf), [4096])
        with self.assertRaises(ValueError):
            checks.elf_alignment(b'not ELF')

    def test_dangerous_compiled_manifest_is_not_a_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            apk = Path(temporary)/'synthetic.apk'
            with zipfile.ZipFile(apk, 'w') as package:
                package.writestr('assets/publisher.p12', b'synthetic fixture, not a key')
            def tool(command):
                args = ' '.join(str(x) for x in command)
                if 'badging' in args:
                    return "targetSdkVersion:'25'\napplication-debuggable\n"
                if 'xmltree' in args:
                    return '\n E: application\n A: allowBackup=true\n A: usesCleartextTraffic=true\n  E: service\n   A: exported=true\n'
                if 'permissions' in args:
                    return "uses-permission: name='android.permission.READ_CONTACTS'"
                if 'apksigner' in args:
                    return 'Verifies\nSigner #1 certificate DN: CN=Android Debug\n'
                return ''
            with patch.object(checks, 'run', side_effect=tool):
                result = {r['check']: r['status'] for r in checks.inspect(apk, Path('/synthetic-tools'), 36)}
            for name in ['release-debug-flag', 'declared-target', 'cleartext-disabled', 'backup-disabled',
                         'minimal-permissions', 'exposed-components', 'private-material-paths', 'signature']:
                self.assertEqual(result[name], 'FAIL', name)

    def test_missing_verification_tool_is_an_error(self):
        with self.assertRaises(FileNotFoundError):
            checks.run(['/nonexistent-vcc-android-tool'])


if __name__ == '__main__':
    unittest.main()
