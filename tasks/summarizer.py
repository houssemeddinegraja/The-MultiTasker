from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize(text, dropdown_choice):
    if dropdown_choice == "Short":
        max = 45
        min = 15
    elif dropdown_choice == "Detailed":
        max = 160
        min = 80
    else:
        max = 100
        min = 50

    summary = summarizer(text, max_length=max, min_length=min, do_sample=False, clean_up_tokenization_spaces=True)
    return summary[0]['summary_text']
