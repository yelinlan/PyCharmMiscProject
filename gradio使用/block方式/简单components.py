import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=5):
            gr.Textbox(label="Enter your name", placeholder="Your name here...", info="This is a textbox")
        with gr.Column(scale=5):
            gr.Button(value="Click me", variant="huggingface")
    with gr.Row():
        with gr.Column(scale=5):
            gr.Slider(0, 100, value=50, label="Slider", info="This is a slider")
        with gr.Column(scale=1):
            gr.Dropdown(choices=["Option 1", "Option 2", "Option 3"], label="Dropdown", info="This is a dropdown")
    gr.File(label="Upload a file", file_count="multiple", file_types=[".txt", ".pdf", ".jpg", ".png"])
    gr.Chatbot(label="Chatbot", type="messages")
if __name__ == "__main__":
    demo.launch()
