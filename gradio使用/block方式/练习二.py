import gradio as gr


with gr.Blocks() as demo:
     gr.HTML("<h1>Hello, World!</h1>")
     alpha = ["A", "B", "C"]
     dropdown = gr.Dropdown(alpha, label="INPUT", value=alpha[0])
     textbox = gr.Textbox(label="OUTPUT", value=alpha[0])
     dropdown.change(fn=lambda x: x, inputs=[dropdown], outputs=[textbox])

if __name__ == "__main__":
    demo.launch()
