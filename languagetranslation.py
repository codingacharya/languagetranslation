import streamlit as st
from googletrans import Translator, LANGUAGES

def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def main():
    st.title("Language Translator")
    
    text = st.text_area("Enter text to translate:")
    
    target_language = st.selectbox("Select target language:", list(LANGUAGES.values()))
    target_lang_code = [k for k, v in LANGUAGES.items() if v == target_language][0]
    
    if st.button("Translate"):
        if text:
            translated_text = translate_text(text, target_lang_code)
            st.success(f"Translated Text: {translated_text}")
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()