import gradio as gr


def up(type1):
    return " | ".join(type1)


with gr.Blocks() as demo:
    check_box_group = gr.Checkboxgroup(["png", "jpg", "jpeg"], label="Choose file type")
    textbox = gr.Textbox(label="Output")
    check_box_group.change(fn=up, inputs=check_box_group, outputs=textbox)

if __name__ == "__main__":
    demo.launch()
