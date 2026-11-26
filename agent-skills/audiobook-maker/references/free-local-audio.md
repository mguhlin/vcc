# Free local audio path

This is the optional narration stage after Audiobook Maker has produced and checked a listening edition. It uses downloaded software on your own computer rather than a paid narration service. Software/model downloads need internet access; narration can run offline once the selected engine and all required voice/language assets are installed and verified. Your computer still supplies the processing time, storage, and electricity.

**Practical route:** approved chapter text → local Piper voice → WAV chapter masters → MP3 chapter files, or one M4B with chapter metadata → your audiobook player.

## Use the PageSpindle companion app

[PageSpindle](https://mguhlin.github.io/pagespindle/) brings import, optional local AI preparation, side-by-side comparison, voice preview, and audiobook export into one workspace. [Open the browser workbench directly](https://mguhlin.github.io/pagespindle/browser/?v=0.3.1), paste or open text, then choose Create audiobook. Passage checks and AI cleanup are optional. The browser automatically downloads the English voice on first use; optional browser AI uses WebGPU. Windows/macOS/Linux installers open the desktop app in its own window, install the required runtimes, and automatically download verified models during first launch. The desktop app includes FFmpeg for WAV, MP3 and M4B output. Both editions work locally after setup. PageSpindle credits Lance Eaton and follows VCC’s four protections. Save a project backup and audition a short voice sample; comparison is available when you want it. Its [source and release evidence](https://github.com/mguhlin/pagespindle) explain unsigned installers, hardware, offline-cache, input and job-size limits.

PageSpindle removes recognized Markdown formatting from derived speech: heading hashes, emphasis, bullet/quote markers, code fences and table separators are silent. Link labels and image alternative text are read without fetching their hidden destinations. Literal hashtags, arithmetic symbols, citations and code content remain. Source documents, prepared passages, listening-text masters and project backups keep their Markdown. This requires no AI pass; generate audio again to apply it to an existing project. Audition the result, especially technical text and tables.

The optional chatbot handoff copies a passage with the skill’s conservative preparation instructions. A local chatbot can keep that step offline; pasting it into a hosted chatbot transfers the passage to that provider. Review the result before pasting it back into the prepared passage. The app’s built-in Qwen model avoids that manual handoff.

## Choose an engine

| Route | Suitable starting point | Tradeoff |
| --- | --- | --- |
| **Piper, local command line** | A repeatable workflow on a compatible Python installation; a useful first choice for this Linux workspace | Setup and voice selection take some work. Pilot pronunciation and long-form comfort before a whole book. |
| **Kokoro, local Python** | An alternative voice audition if Piper's voices do not suit you | Different Python/phonemizer dependencies and model downloads; compare samples on the same paragraph. Do not assume a hosted demo is local. |
| **Balabolka, Windows desktop** | A graphical route using an installed compatible Windows speech voice | Freeware application; available voices and their separate terms vary. Use its installed-voice mode for local processing, rather than online TTS options. |

[Piper](https://github.com/OHF-Voice/piper1-gpl) is a local speech engine. Its engine is GPL-3.0-or-later; **each voice has separate terms** in its model card. Follow any training/base-model links needed to understand a voice's licensing. [Kokoro's official library](https://github.com/hexgrad/kokoro) documents local inference; its [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M) identifies Apache-2.0 weights. [Balabolka's developer](https://www.cross-plus-a.com/balabolka.htm) describes installed-voice support and saving speech as audio. None of those software/model licenses grants rights to publish a recording of somebody else's book.

## 1. Keep chapter text as the master

Use the clean UTF-8 text produced during preparation. Avoid extracting it back out of a PDF when you already have a checked text master. Save numbered files in the intended order: `01-introduction.txt`, `02-chapter-one.txt`, and so on. Keep the spoken chapter title in each file. Put notes, bibliography, and other optional listening matter into separate files; keep the review ledger outside narration inputs.

Read the beginning, a difficult passage, and the ending of each chapter. Preserve the faithful master; pronunciation adjustments belong in a separate narration copy or pronunciation dictionary, with a record of the changes.

## 2. Install and audition Piper

These are instructions, not software installed by VCC. On Linux/macOS, create a dedicated folder and Python virtual environment using a Python version supported by the chosen release. Review the official package and selected voice before running installation commands. Windows can use the same Python module approach with its virtual environment's activation command.

```sh
python3 -m venv .venv-audio
source .venv-audio/bin/activate
python -m pip install piper-tts
python -m piper.download_voices
```

The final command lists voices. Preview candidates using the [linked voice samples](https://rhasspy.github.io/piper-samples/), then download one voice. The following is the upstream documentation's example voice, **not a blanket recommendation of its license for every use**:

```sh
python -m piper.download_voices en_US-lessac-medium
python -m piper -m en_US-lessac-medium -f pilot.wav --input-file pilot.txt
```

Create `pilot.txt` from a few paragraphs including names, dates, abbreviations, a note transition, and a table narration. Listen to `pilot.wav` before processing the full book. Choose a voice and pace you can comfortably hear for a long session. Package availability and speed depend on the machine; no performance benchmark is implied here.

The [official CLI documentation](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/CLI.md) covers installation, voice downloads, file inputs, and voice options. Check `python -m piper --help` for your installed version. Record the working package version, model identity, and settings for repeatable output. Test an offline pilot to confirm all required assets are present and no remote narration service is involved.

## 3. Generate chapter WAVs

Run the same tested command for each chapter, changing input and output names:

```sh
python -m piper -m en_US-lessac-medium -f 01-introduction.wav --input-file 01-introduction.txt
python -m piper -m en_US-lessac-medium -f 02-chapter-one.wav --input-file 02-chapter-one.txt
```

For a very long chapter, use paragraph-aligned chunks with a ledger of their order and completion. Keep identical voice and audio settings for all parts. Regenerate a failed chunk rather than the whole book. Piper's CLI reloads the model on each invocation; an authorized local batch implementation using its Python API can reuse the loaded model later. A network server is unnecessary for this first route.

Check that every expected output exists, has nonzero duration, and contains the correct chapter opening and ending. Listen to a middle sample and difficult passages too. Duration alone cannot establish that every word was spoken correctly. Keep the WAVs until final listening checks pass.

## 4. Choose the audiobook format

**Simplest: numbered MP3 chapters.** With an installed [FFmpeg](https://ffmpeg.org/download.html), convert each WAV individually. This example produces mono speech at 96 kb/s; audition it and choose a different quality setting if needed:

```sh
ffmpeg -n -i 01-introduction.wav -ac 1 -c:a libmp3lame -b:a 96k 01-introduction.mp3
```

Use an FFmpeg build with the requested encoder. `-n` refuses to overwrite an existing file. Transfer the ordered MP3 files to a player that remembers position. This route already gives you a listenable audiobook without making an M4B.

**Optional: one M4B with chapters.** Prepare a concat list in the same folder as the WAVs:

```text
file '01-introduction.wav'
file '02-chapter-one.wav'
```

Save it as `chapters.txt`. Inputs must have compatible audio parameters. Create `book.ffmetadata` with real cumulative boundaries from the WAV durations. Here, the two 10-second chapters are illustrative placeholders, not measured book timings:

```text
;FFMETADATA1
title=Example Listening Edition
artist=Example Author
[CHAPTER]
TIMEBASE=1/1000
START=0
END=10000
title=Introduction
[CHAPTER]
TIMEBASE=1/1000
START=10000
END=20000
title=Chapter One
```

Then encode and import the chapter metadata:

```sh
ffmpeg -n -f concat -safe 1 -i chapters.txt -f ffmetadata -i book.ffmetadata -map 0:a:0 -map_metadata 1 -map_chapters 1 -c:a aac -b:a 96k -movflags +faststart -f mp4 book.m4b
ffprobe -v error -show_chapters -show_format book.m4b
```

Use simple relative filenames as shown. Escape metadata special characters when inserting real titles; follow FFmpeg's [concat](https://ffmpeg.org/ffmpeg-formats.html#concat) and [metadata](https://ffmpeg.org/ffmpeg-formats.html#Metadata-1) documentation. Renaming an MP3 to `.m4b` does not create an M4B or chapter markers. Resume behavior belongs to the chosen player; test seeking, chapter names, and restart/resume there.

## 5. Finish with evidence

Keep the original book, faithful listening master, narration copies, voice/settings record, ordered chapter WAVs, final files, and review ledger. Verify the final chapter count and order, duration, opening/ending audio, note handling, pronunciation, and actual player behavior. Label remaining OCR or synthesis uncertainties. A transcript is still useful for searching, quotations, and accessibility; an audio recording is not a substitute for checking the source when citing it.

VCC supplies this path as documentation. It does not bundle speech engines, model weights, FFmpeg, or recorded books, and does not claim a complete book has been synthesized or auditioned. This reference is original VCC educational guidance by Miguel Guhlin under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); upstream software and model terms remain separate.
