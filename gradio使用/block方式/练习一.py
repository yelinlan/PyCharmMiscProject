import gradio as gr


def greet(name, age):
    return "Hello " + name + ", you are " + str(age) + " years old"


with gr.Blocks() as demo:
    with gr.Row():
        textbox = gr.Textbox(label="Enter your name", placeholder="Your name here...", info="This is a textbox")
        slider = gr.Slider(0, 100, value=50, label="Slider", info="your age")
    gr_textbox = gr.Textbox(label="Output")
    button = gr.Button("greet")
    button.click(fn=greet, inputs=[textbox, slider], outputs=gr_textbox)

if __name__ == "__main__":
    demo.launch()
