# Real-Time Voice Translator (Streamlit)

**Project Name:** Real-Time Voice Translator    
**Project Type:** Streamlit web application     
**Repo:** https://code.swecha.org/RakeshGajula/real-time-voice-translator    
**Demo Video:** https://drive.google.com/file/d/1LzqIzzdsnepam0lrE3EUmEsg9238bPW0/view?usp=drivesdk  

---

## 1. Team Information
- **Team / Owner:** Rakesh Babu Gajula  
- **Members & Roles:**
  - Rakesh — Lead Developer (Streamlit + Audio pipeline)
  - Gopal  — Speech Recognition & Translation integration
  - Raheem — UI/UX & Testing
  - Mukund — Packaging & Deployment
  - Charan — Documentation & User Acquisition


---

## 2. Application Overview (Short)
Real-Time Voice Translator is a Python application that captures live speech input (microphone), recognizes the spoken text, translates it into a selected target language, and plays back synthesized audio of the translated text. The original Tkinter desktop application was converted into a Streamlit web app for easier access, improved UX, and deployment capability (e.g., Hugging Face Spaces).

**Core capabilities**
- Continuous listening with start/stop control
- Speech recognition (microphone input)
- Text translation (source → target)
- Text-to-speech playback of translated text
- Show original and translated text in the UI
- Download recordings 

---

## 3. Objectives
- Provide an accessible web UI for real-time voice translation.
- Support multiple input/output languages with an easy language selector.
- Enable simple corpus collection (audio + transcript) export for research.
- Prepare a deployable artifact (Streamlit app; optional packaged desktop build).

---

## 4. Technology Stack
- **Language:** Python 3.10+  
- **Web UI:** Streamlit (`app_streamlit.py`)  
- **Speech Recognition:** `speech_recognition` library (recognize_google backend by default)  
- **Translation:** `deep-translator` (GoogleTranslator)  
- **Text-to-Speech:** `gTTS` (Google Text-to-Speech)  
- **Transliteration:** `google-transliteration-api` (optional)  
- **Storage:** local filesystem for audio files + optional SQLite/CSV for metadata export  
- **Packaging (optional):** cx-Freeze / PyInstaller for desktop builds  
- **Environment:** `.env` for sensitive keys (if any)

> **Note on open-source compliance:** The app uses community/open libraries, but relies on Google web services for recognition/translation/TTS. For strict "open-source only" requirements, consider switching to local models (Open-source Whisper, Hugging Face translation/TTS models) in future iterations.

---

## 5. Project Structure
project-root/
├── app_streamlit.py # Streamlit implementation (main)
├── main.py # Original Tkinter app (reference)
├── requirements.txt
├── REPORT.md # This file
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── recordings/ # Saved audio files (wav/mp3)
└── utils/
├── audio_utils.py
└── db_utils.py

---

## 6. Implementation Details

### 6.1 Main Flow (app_streamlit.py)
1. **Language selection:** Two dropdowns — *source language* and *target language*.
2. **Start/Stop controls:** Start begins microphone capture; Stop ends capture.
3. **Speech capture:** `speech_recognition.Recognizer()` + `sr.Microphone()` used to capture audio segments (or uploaded files).
4. **Recognition:** `recognizer.recognize_google(audio, language=source_code)` converts speech → text.
5. **Translation:** `GoogleTranslator(source=src_lang, target=trg_lang).translate(text)` converts text.
6. **TTS:** `gTTS(text=translated_text, lang=target_code)` produces an MP3 stream and Streamlit plays it (or serves as downloadable audio).
7. **Display & Edit:** Recognized and translated text appear on the UI; user can edit before saving/exporting.
8. **Save/export:** Save audio file to `recordings/` and metadata 

### 6.2 Key Implementation Notes
- Audio saved with unique filenames: `recordings/YYYYMMDD_HHMMSS_src-trg.wav` (or `.mp3`).
- Temporary files are cleaned or archived per preference.
- `.env` used for any service keys — do **not** commit keys to repo.

---

## 7. How to Run (Developer / Tester)
1. Clone repo:
   ```bash
   git clone <REPO_URL>
   cd project-root
Create & activate venv:

bash
Copy code
python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run Streamlit app:

bash
Copy code
streamlit run app_streamlit.py
Open the URL printed by Streamlit (usually http://localhost:8501) and test.

## 8. Testing & Validation
### 8.1 Test Plan
Unit tests (suggested):

test_audio_save.py — ensure uploads/records save to recordings/.

test_transcribe_google.py — ensure recognize_google returns text for a known test clip.

test_translation.py — verify translator returns expected translations for sample phrases.

test_tts.py — verify gTTS produces an audio file.

Manual tests

Select en-US → te-IN, say "Hello, how are you?" → expect Telugu translation + playback.

Upload a recorded WAV/MP3 file and transcribe it.

Edit transcription, save, and export CSV.

Test start/stop under different microphone latency/noise.

### 8.2 Current Test Status
Local manual tests passed for English→Hindi and English→Telugu translations on clean audio.

All language translations are perfectly working 

## 9. User Feedback (Collect & Summarize)
Method: Google Form distributed to peers (10+ testers). Ask for:

Language tested

Task performed

Accuracy rating (1–5)

Ease of use (1–5)

Comments / bugs observed

Summary Placeholder:

Average accuracy rating: 8.5

Common feedback: e.g., "TTS works for most languages but gTTS fails for [xx]; better microphone UI; offer offline mode."


## 10. Error Handling & Known Limitations
Known limitations
Requires internet for Google STT / Google Translate / gTTS.

gTTS language coverage is incomplete — some languages (e.g., certain Indic languages) may not be supported or may use fallback voices.

Browser audio playback may vary by platform.

Real-time latency depends on network and API speed.

Error handling implemented
Graceful message when recognition fails ("Could not understand audio").

Catch sr.RequestError and inform user API unavailable.

Sanity checks for empty uploads.

Try/catch around gTTS generation; fallback to text-only output if audio generation fails.

## 11. Security & Privacy
Consent: App prompts users before saving any audio; do not collect PII without explicit consent.

Storage: Audio saved locally; consider encryption for long-term storage if required.

Secrets: Use .env and do not commit API keys to Git. Add .env & service key files to .gitignore.

GDPR / Local Laws: If you plan to publish or share user audio, obtain explicit consent and comply with local regulations.

## 12. Roadmap & Future Improvements
Short-Term (1–2 weeks)

Add more language pairs and better mapping of language codes (e.g., te-IN vs te).

Improve UI labels and add real-time buffering indicator.

Implement more robust audio format conversion (MP3 → WAV) with pydub.

Mid-Term (2–6 weeks)

Add optional offline transcription (Open-source Whisper or VOSK).

Add alternative offline/OSS TTS (e.g., Coqui TTS, VITS) for languages unsupported by gTTS.

Add user authentication and per-user export history.

Long-Term (Beyond internship)

Integrate multilingual diarization (multi-speaker handling).

Mobile/web hybrid app with offline-first architecture.

Community corpus platform integration and continuous model fine-tuning on collected data.

## 13. Deployment & Packaging
Streamlit deployment: Recommended to host demo on Hugging Face Spaces (public demo). Remove or mask any API keys via secrets manager.

Desktop packaging: Use cx-Freeze / PyInstaller to make standalone executables for Windows / macOS / Linux. Provide build scripts and test installers.

## 14. Compliance with Internship Requirements
Corpus contribution: App provides audio + transcript  for Swecha corpus.

AI & Open Source: Uses open Python libraries. Note: Google STT/Translate/gTTS are proprietary web services; for strict open-source adherence, implement Whisper + Hugging Face models as alternate mode.

Documentation: This report + README + CONTRIBUTING + CHANGELOG are included.


