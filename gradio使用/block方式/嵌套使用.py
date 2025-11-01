import gradio as gr


def up(x, y, z):
    z.append(x)
    z.append(y)
    return " | ".join(z)


with gr.Blocks() as demo:
    gr.HTML("<h1 align = 'center'> 选择你喜欢的字母 </h1>")
    with gr.Row():
        with gr.Column(scale=2):
            # 单选英文字母
            radio = gr.Radio(["A", "B", "C", "D", "E"], label="英文字母", value="A")
        with gr.Column(scale=2):
            # 下拉希腊字母
            dropdown = gr.Dropdown(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"], label="希腊字母", value="Alpha")
        with gr.Column(scale=2):
            # 多选日语拼音
            group = gr.CheckboxGroup(["ア", "イ", "ウ", "エ", "オ"], label="日语字母", value=["ア", "ウ"])
    textbox = gr.Textbox(label="output")
    button = gr.Button("提交")
    button.click(fn=up, inputs=[radio, dropdown, group], outputs=textbox)
if __name__ == "__main__":
    demo.launch()
