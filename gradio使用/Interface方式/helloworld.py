import random

import gradio as gr
import numpy as np

operator = ["+", "-", "x", "÷"]


def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


def calculator(num1, operation, num2):
    if operation == operator[0]:
        return num1 + num2
    elif operation == operator[1]:
        return num1 - num2
    elif operation == operator[2]:
        return num1 * num2
    elif operation == operator[3]:
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2
    return None


def greet(name, intensity, random_number, input_img, num1, operation, num2):
    print(calculator(num1, operation, num2))
    if random_number:
        return name * int(intensity), random.randrange(0, 100, 2), sepia(input_img), calculator(num1, operation, num2)
    return name * int(intensity), 99999, sepia(input_img), calculator(num1, operation, num2)


demo = gr.Interface(
    fn=greet,
    inputs=[gr.Text(label="输入框", placeholder="请输入文本", value="hello ", info="信息"),
            gr.Slider(minimum=0, maximum=100, step=1, label="进度条", info="这里是重复几次文字", value=5),
            gr.Checkbox(label="复选框", info="是否生成随机数", value=True),
            gr.Image(label="图片"),
            ],
    additional_inputs=[
        gr.Number(label="数字", info="这里是数字信息", value=5),
        gr.Radio(operator, label="选择运算符", info="这里是运算符信息",
                 value="add"),
        gr.Number(label="数字", info="这里是数字信息", value=5)
    ],
    outputs=[gr.Text(label="输出结果", info="这里是输出结果信息", lines=8),
             gr.Number(label="数字", info="这里是数字信息"),
             gr.Image(label="图片"),
             gr.Number(label="数字", info="这里是数字信息"),
             ],
    title="Greeting App",
    article=" APPPPPPPPPPPPPPPPPP",
    description="A demo of Gradio",
    flagging_options=["非常nice！", "unbelievable！", "Oh! God!"],
)

# demo.launch(share=True)
demo.launch()
