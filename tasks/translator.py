from transformers import pipeline
import torch

translator_pipeline = pipeline("translation", model="facebook/nllb-200-distilled-600M")


def translate(text, src, tgt):
    if src == tgt:
        return text

    if not text.strip():
        return "Please type some text to translate."

    langs = {
        "English": "eng_Latn",
        "Spanish": "spa_Latn",
        "French": "fra_Latn",
        "Italian": "ita_Latn",
        "German": "deu_Latn",
        "Arabic": "arb_Arab",
        "Turkish": "tur_Latn"
    }

    src_lang_code = langs.get(src, "en")
    tgt_lang_code = langs.get(tgt, "fr")

    result = translator_pipeline(
        text,
        src_lang=src_lang_code,
        tgt_lang=tgt_lang_code
    )

    return result[0]['translation_text']
