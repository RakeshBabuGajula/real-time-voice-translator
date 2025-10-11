import os
import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import time
from google.transliteration import transliterate_text
import csv
import datetime

# Dictionary of language names and codes
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa",
}

st.title("Real-Time Voice🎙️ Translator🔊")

# Language selection
input_lang_name = st.selectbox(
    "Select Input Language:", list(language_codes.keys()), index=0
)
output_lang_name = st.selectbox(
    "Select Output Language:", list(language_codes.keys()), index=0
)

input_lang_code = language_codes[input_lang_name]
output_lang_code = language_codes[output_lang_name]

# Button to start translation
start_button = st.button("Start Translation")

if "keep_running" not in st.session_state:
    st.session_state.keep_running = False

if "current_recognized" not in st.session_state:
    st.session_state.current_recognized = ""

if "current_translated" not in st.session_state:
    st.session_state.current_translated = ""


def export_csv():
    if not os.path.exists("exports"):
        os.makedirs("exports")
    filename = f"exports/translation_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "timestamp",
            "input_lang",
            "output_lang",
            "recognized_text",
            "translated_text",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "timestamp": timestamp,
            "input_lang": input_lang_name,
            "output_lang": output_lang_name,
            "recognized_text": st.session_state.current_recognized,
            "translated_text": st.session_state.current_translated,
        }
        writer.writerow(record)
    st.success(f"Exported current translation to {filename}")


def recognize_and_translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak Now!")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        speech_text = r.recognize_google(audio)  # type: ignore
        speech_text_transliteration = (
            transliterate_text(speech_text, lang_code=input_lang_code)
            if input_lang_code not in ("auto", "en")
            else speech_text
        )
        recognized_text = st.text_area(
            "Recognized Text ⮯", value=speech_text_transliteration, height=100
        )
        st.session_state.current_recognized = recognized_text
        if speech_text.lower() in {"exit", "stop"}:
            st.session_state.keep_running = False
            st.warning("Translation stopped by user command.")
            return
        try:
            translated_text = GoogleTranslator(
                source=input_lang_code, target=output_lang_code
            ).translate(text=recognized_text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
            return
        translated_text_editable = st.text_area(
            "Translated Text ⮯", value=translated_text, height=100
        )
        st.session_state.current_translated = translated_text_editable
        # Generate speech audio
        voice = gTTS(translated_text_editable, lang=output_lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            voice.save(tmp_file.name)
            audio_bytes = open(tmp_file.name, "rb").read()
        # Remove the subheader and just display the audio player with some spacing
        st.markdown("<br>", unsafe_allow_html=True)
        st.audio(audio_bytes, format="audio/mp3")
        os.remove(tmp_file.name)

    except sr.UnknownValueError:
        st.text_area("Translated Text ⮯", value="Could not understand!", height=100)
    except sr.RequestError:
        st.text_area(
            "Translated Text ⮯", value="Could not request from Google!", height=100
        )


if start_button:
    st.session_state.keep_running = True

if st.session_state.keep_running:
    recognize_and_translate()
    # To continuously listen, rerun the app after a short delay
    time.sleep(1)
    st.rerun()

if st.session_state.current_recognized and st.session_state.current_translated:
    if st.button("Export CSV"):
        export_csv()
