from pypdf import PdfReader
from transformers import pipeline

qna = pipeline("question-answering", model="deepset/roberta-base-squad2")


def answer(question, document):
    doc_text = ""
    file_path = document.name if hasattr(document, 'name') else document

    if file_path.lower().endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                doc_text += extracted
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            doc_text = f.read()

    if not doc_text.strip():
        return "Error: Could not extract any text."

    # 4. Query the AI
    responses = qna(question=question, context=doc_text)
    final_answer = responses.get('answer', '').strip()

    if not final_answer:
        return "The AI read the document but could not find the answer to your question."

    return final_answer
