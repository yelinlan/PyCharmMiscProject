import gradio as gr


def response(message):
    return [[f"我：{message}", f"你：{message} \n 我正在思考中..."]]


with gr.Blocks() as demo:
    gr.HTML("<h1 align = 'center'>欢迎使用聊天机器人</h1>")
    chatbot = gr.Chatbot(show_label=False, scale=3, show_copy_button=True)
    textbox = gr.Textbox(placeholder="请输入你的问题", show_label=False)
    textbox.submit(fn=response, inputs=[textbox], outputs=[chatbot])

if __name__ == "__main__":
    demo.launch()
