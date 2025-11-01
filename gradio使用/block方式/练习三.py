import os

import gradio as gr


def up(file1):
    return os.path.splitext(file1)[1].lower()


with gr.Blocks() as demo:
    file = gr.File(label="上传文件", file_types=[".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".png"])
    output = gr.Textbox(label="文件格式")
    file.change(fn=up, inputs=[file], outputs=[output])

if __name__ == "__main__":
    demo.launch()
