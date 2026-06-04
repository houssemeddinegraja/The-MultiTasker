import gradio as gr


with gr.Blocks(theme=gr.themes.Glass()) as block:
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
                    choices=["English", "French", "Arabic", "Italian", "Turkish", "German"],
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
                    choices=["English", "French", "Arabic", "Italian", "Turkish", "German"],
                    value="French",
                    label="Translate to:"
                )
            with gr.Column(scale=5):
                tgt_txt = gr.Textbox(
                    show_label=False,
                    placeholder="Your translation will appear here...",
                    lines=4,
                    interactive=False
                )




block.launch()
