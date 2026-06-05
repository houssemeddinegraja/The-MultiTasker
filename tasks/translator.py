from transformers import pipeline

translator_pipeline = pipeline("translation", model="facebook/m2m100_418M")


def translate(text, src, tgt):
    if src == tgt:
        return text

    if not text.strip():
        return "Please type some text to translate."

    langs = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Italian": "it",
        "German": "de",
        "Arabic": "ar",
        "Turkish": "tr"
    }

    src_lang_code = langs.get(src, "en")
    tgt_lang_code = langs.get(tgt, "fr")

    result = translator_pipeline(
        text,
        src_lang=src_lang_code,
        tgt_lang=tgt_lang_code
    )

    return result[0]['translation_text']
