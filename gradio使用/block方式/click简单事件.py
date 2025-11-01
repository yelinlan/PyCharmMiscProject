import gradio as gr


def calc(x, o, y):
    return eval(str(x) + str(o) + str(y))


with gr.Blocks() as demo:
    textbox1 = gr.Textbox(placeholder="输入数")
    radio = gr.Radio(choices=["+", "-", "*", "/"])
    textbox2 = gr.Textbox(placeholder="输入数")
    textbox3 = gr.Textbox(label="结果")
    button = gr.Button("计算")
    button.click(fn=calc, inputs=[textbox1, radio, textbox2], outputs=textbox3)

if __name__ == "__main__":
    demo.launch()
