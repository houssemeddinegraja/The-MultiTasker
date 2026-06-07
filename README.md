# NLP Swiss Army Knife

A multi-task NLP web application built with **Gradio** and **Hugging Face Transformers**. Three powerful language tools — translation, summarization, and document Q&A — unified in a single clean interface.

---

## Features

### The Universal Translator
Translate text across **7 languages** in any direction.

| Supported Languages |
|---|
| English · French · Arabic · Italian · Turkish · German · Spanish |

- Select a source and target language from the dropdowns
- Type or paste your text and hit **Translate Now!**
- Instant output in the target language

---

### The Smart Summarizer
Condense long articles, reports, or essays into concise summaries.

- Choose a summary length: **Short**, **Medium**, or **Detailed**
- Paste any long-form text and hit **Summarize Your Text!**
- Get a clean, readable summary tuned to your chosen detail level

---

### Document Q&A Engine
An **extractive** QA tool that finds literal answers directly inside your documents — no hallucination, no inference.

> Think of it as **Ctrl+F on steroids**.

| Works well for | Not ideal for |
|---|---|
| HR Policies & Employee Handbooks | Conversational or implied answers |
| Legal Contracts & NDAs | Questions requiring reasoning |
| Technical Manuals & SOPs | Open-ended or generative responses |
| IT Documentation | Ambiguous phrasing |

**Workflow:**
1. Upload your document
2. Ask a factual question
3. The model extracts the exact answer span from the text

---

## Project Structure

```
NLP-Swiss-Army-Knife/
├── app.py                  # Gradio UI — all three tabs
└── tasks/
    ├── translator.py       # Translation logic
    ├── summarizer.py       # Summarization logic
    └── qna.py              # Extractive Q&A logic
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/houssemeddinegraja/NLP-Swiss-Army-Knife.git
cd NLP-Swiss-Army-Knife
pip install -r requirements.txt
```

> **Note:** A `requirements.txt` is not yet included. At minimum you will need:
> ```
> gradio
> transformers
> torch
> ```

### Running the app

```bash
python app.py
```

Then open your browser at `http://localhost:7860`.

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | [Gradio](https://www.gradio.app/) (`gr.Blocks`, Glass theme) |
| NLP Models | [Hugging Face Transformers](https://huggingface.co/docs/transformers) |
| Language | Python |

---

## Notes

- The Document Q&A tab uses **strict extractive** inference — the answer must be grammatically present in the uploaded document. Implicit or conversational phrasing will not be resolved.
- Model first-run downloads may take a moment depending on your connection.

---

## Author

**Houssem Eddine Graja**  
[github.com/houssemeddinegraja](https://github.com/houssemeddinegraja)
