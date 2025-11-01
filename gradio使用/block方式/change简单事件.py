import gradio as gr


def calc(x):
    print(bin(x))
    return bin(x)[2:]


with gr.Blocks() as demo:
    slider = gr.Slider(minimum=0, maximum=100, step=1, label="转二进制")
    textbox3 = gr.Textbox(label="结果")
    slider.change(fn=calc, inputs=[slider], outputs=textbox3)

if __name__ == "__main__":
    demo.launch()
