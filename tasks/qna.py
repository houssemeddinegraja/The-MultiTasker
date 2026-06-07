from pypdf import PdfReader
from transformers import pipeline

qna = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer(question, document):
    reader = PdfReader(document)
    doc_text = ""
    for page in reader.pages:
        doc_text += page.extract_text()
    responses = qna(question=question, context=doc_text)
    return responses['answer']
