import gradio as gr
from tasks.translator import translate
from tasks.summarizer import summarize
from tasks.qna import answer

with gr.Blocks(theme=gr.themes.Glass()) as block:
    with gr.Tabs():
        with gr.Tab("The Universal Translator"):
            gr.Markdown(
                """
                <div style="text-align: center; padding: 15px;">
                    <h1 style="color: #4338ca; margin-bottom: 5px;">The Universal Translator</h1>
                </div>
                """
            )

            with gr.Row():
                with gr.Column(scale=2):
                    srcs = gr.Dropdown(
                        choices=["English", "French", "Arabic", "Italian", "Turkish", "German", "Spanish"],
                        value="English",
                        label="Translate from:"
                    )
                with gr.Column(scale=5):
                    src_txt = gr.Textbox(
                        show_label=False,
                        placeholder="Type the text you want to translate here...",
                        lines=4
                    )

            with gr.Row():
                with gr.Column(scale=2):
                    pass
                with gr.Column(scale=5):
                    btn = gr.Button("Translate Now !", variant="primary")

            with gr.Row():
                with gr.Column(scale=2):
                    tgts = gr.Dropdown(
                        choices=["English", "French", "Arabic", "Italian", "Turkish", "German", "Spanish"],
                        value="French",
                        label="Translate to:"
                    )
                with gr.Column(scale=5):
                    tgt_txt = gr.Textbox(
                        show_label=False,
                        placeholder="Your translated text will appear here...",
                        lines=4,
                        interactive=False
                    )

            btn.click(
                fn=translate,
                inputs=[src_txt, srcs, tgts],
                outputs=[tgt_txt]
            )

        with gr.Tab("The Smart Summarizer"):
            gr.Markdown(
                """
                <div style="text-align: center; padding: 10px 0;">
                    <h1 style="color: #4338ca; margin-bottom: 5px;">The Smart Summarizer</h1>
                    <p style="color: #6b7280; margin-top: 0;">Condense long documents instantly</p>
                </div>
                """
            )
            with gr.Row():
                with gr.Column(scale=1, variant="panel"):
                    gr.Markdown("### Configuration")

                    sum_length = gr.Dropdown(
                        choices=["Short", "Medium", "Detailed"],
                        value="Medium",
                        label="Summary Length",
                        info="Choose how detailed the output should be."
                    )

                    gr.HTML("<div style='margin-top: 20px;'></div>")

                    btn_sum = gr.Button("Summarize Your Text !", variant="primary")

                with gr.Column(scale=3):
                    sum_in = gr.Textbox(
                        label="Source Text",
                        placeholder="Paste the long article, essay, or report you want to summarize here...",
                        lines=8,
                        max_lines=12
                    )

                    sum_out = gr.Textbox(
                        label="Here's Your Summary",
                        placeholder="Your summary will appear here once you click compile...",
                        lines=5,
                        interactive=False
                    )

            btn_sum.click(
                fn=summarize,
                inputs=[sum_in, sum_length],
                outputs=[sum_out]
            )

        with gr.Tab("Document Q&A"):
            gr.Markdown(
                """
                <div style="text-align: center; padding: 10px 0;">
                    <h1 style="color: #4338ca; margin-bottom: 5px;">Document Q&A Engine</h1>
                    <p style="color: #6b7280; margin-top: 0;">Extract precise, literal facts directly from your documents</p>
                </div>
                """
            )

            gr.HTML(
                """
                <div style="background-color: #e0f2fe; border-left: 4px solid #0284c7; padding: 15px; margin-bottom: 20px; border-radius: 4px; font-size: 14px;">
                    <strong style="color: #0369a1; font-size: 16px;">💡 How this strict Extractive AI works:</strong>
                    <p style="color: #0c4a6e; margin-top: 5px; margin-bottom: 10px;">
                        This AI acts like <strong>'Ctrl+F' on steroids</strong>. It will not read between the lines or guess. The exact answer must be grammatically explicit in the text.
                    </p>
                    
                    <strong style="color: #0369a1;">❌ Bad Example (Conversational):</strong>
                    <div style="background-color: #fca5a5; padding: 8px; border-radius: 4px; margin-bottom: 10px; color: #7f1d1d;">
                        <em>Document:</em> "Take a whole month to try it out before shipping it back!"<br>
                        <em>Question:</em> "What is the return window?" ➔ <strong>AI returns Blank (Failed)</strong>
                    </div>

                    <strong style="color: #0369a1;">✅ Perfect Example (Literal & Factual):</strong>
                    <div style="background-color: #bbf7d0; padding: 8px; border-radius: 4px; margin-bottom: 15px; color: #14532d;">
                        <em>Document:</em> "The standard return window is 30 days."<br>
                        <em>Question:</em> "What is the return window?" ➔ <strong>AI returns '30 days' (Success)</strong>
                    </div>

                    <strong style="color: #0369a1;">📄 Ideal Document Types:</strong>
                    <ul style="color: #0c4a6e; margin-top: 5px; margin-bottom: 0;">
                        <li><strong>HR Policies & Employee Handbooks</strong> (e.g., PTO rules, benefits)</li>
                        <li><strong>Legal Contracts & NDAs</strong> (e.g., penalty clauses, dates)</li>
                        <li><strong>Technical Manuals & IT Documentations</strong> (e.g., hardware requirements)</li>
                        <li><strong>Standard Operating Procedures (SOPs)</strong> (e.g., step-by-step instructions)</li>
                    </ul>
                </div>
                """
            )

            with gr.Row():
                with gr.Column(scale=1):
                    question_input = gr.Textbox(
                        label="Step 2: Ask a Question",
                        placeholder="What is the main finding?"
                    )
                    submit_btn = gr.Button("Find Answer", variant="primary")
                with gr.Column(scale=2):
                    document_input = gr.File(label="Step 1: Upload your Document")

                    answer_output = gr.Textbox(
                        label="Step 3: Extracted Answer",
                        interactive=False
                    )

            submit_btn.click(
                fn=answer,
                inputs=[question_input, document_input],
                outputs=[answer_output]
            )

block.launch()
