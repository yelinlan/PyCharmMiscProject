import gradio as gr


def calc(file):
    # 返回文本内容
    return file


with gr.Blocks() as demo:
    file = gr.File(label="上传文件", file_count="single", file_types=[".txt"])
    textbox = gr.Textbox(label="输出结果")
    file.upload(calc, inputs=[file], outputs=[textbox])

if __name__ == "__main__":
    demo.launch()
