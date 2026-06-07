from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    summary = summarizer(
        text,
        max_length=128,
        min_length=64,
        do_sample=False,
        clean_up_tokenization_spaces=True
    )
    return summary
