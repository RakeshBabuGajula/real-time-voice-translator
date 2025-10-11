# Changelog

## [Unreleased]

### Planned / in-progress items (for next iteration)
- Add offline speech-to-text and offline translation options (Whisper / local HF models) to reduce reliance on cloud APIs.
- Improve UI/UX: better controls for audio level, visual feedback while listening, language autodetect.
- Expand language support (add more Indic languages and dialect variants).
- Replace or add alternative TTS engines for better support of some Indian languages (address gTTS limitations).
- Implement user authentication and per-user history tracking (secure storage of contributions).
- Add automatic upload/export workflow to Swecha corpus portal (ZIP of audio + CSV metadata).
- Add automated tests and CI checks (basic unit tests and linting).
- Performance and reliability improvements for long running/continuous-listen mode.

## [1.0.0] — Streamlit Migration / Internship Submission

### Summary
First major public release of the application as a Streamlit web app (converted from the original Tkinter prototype). Prepared and packaged for the Viswam/Swecha internship submission.

### Added
- `app_streamlit.py` — main Streamlit web application implementing the voice translator UI and flows.
- Streamlit UI for selecting input/output languages, start/stop continuous listening, and showing recognized/translated text.
- Audio recording and upload support (microphone-based live capture + file upload fallback).
- Real-time speech recognition pipeline (via SpeechRecognition or configured STT backend).
- Translation pipeline using deep-translator (GoogleTranslator).
- Text-to-speech generation using gTTS and in-browser audio playback.
- Export function to generate CSV of corpus entries (audio filename, timestamp, source/target language, transcription, translation, notes).
- Core feature: continuous listen → recognize → translate → speak pipeline with start/stop controls.
- Multilingual UI labels (English + initial support for Telugu in the interface).
- Error handling for recognition/translation failures with user-friendly messages.
- Local audio storage pattern: saved audio files stored in a `recordings/` directory (with unique timestamped filenames).
- Database / export: CSV export for collected corpus (ready to be uploaded to Swecha).
- Documentation added/updated:
  - README.md — usage, install, run instructions.
  - REPORT.md — detailed project report (architecture, testing, roadmap).
  - CONTRIBUTING.md, CHANGELOG.md, LICENSE.
- Packaging notes and sample requirements.txt for reproducible setup.

### Changed
- Converted desktop Tkinter app (`main.py`) into a web-first Streamlit experience (improved accessibility and easier demoing/deployment).
- Reorganized repository layout to emphasize Streamlit app as the primary entrypoint.

### Fixed
- Resolved major UX issues present in the prototype (single-click start/stop, clearer user messaging).
- Fixed several audio saving and file-path issues to ensure saved audio is accessible for export and transcription.

### Known Limitations (documented)
- Requires internet connectivity for translation and cloud-based speech recognition when configured that way.
- gTTS does not support all languages equally (some Indian languages may fail or use fallback voices).
- Browser audio playback behavior varies by platform and browser (some browsers may block autoplay).
- Performance: speech recognition and TTS are subject to latency depending on the chosen backend and network speed.
- Some edge cases with continuous listening in noisy environments can reduce recognition quality.

## [0.1.0] — Tkinter Prototype (original)

### Summary
Initial desktop prototype implemented with Tkinter to validate concept and core flows.

### Added
- `main.py` — original Tkinter-based desktop app:
  - Basic GUI (language selection, start/stop, show recognized and translated text).
  - Proof-of-concept pipeline: microphone → speech recognition → translation → TTS playback.
  - Basic packaging instructions using cx-Freeze (Windows build notes).

### Limitations
- Desktop-only (Tkinter), limited accessibility for reviewers/users without building an exe.
- Several stability/usability issues discovered that motivated migration to Streamlit.
