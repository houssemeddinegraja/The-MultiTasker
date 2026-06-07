import gradio as gr
from tasks.translator import translate
from tasks.summarizer import summarize

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

block.launch()
