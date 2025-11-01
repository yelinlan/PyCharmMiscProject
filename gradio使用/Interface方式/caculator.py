import gradio as gr


def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "x":
        return num1 * num2
    elif operation == "÷":
        if num2 == 0:
            raise gr.Error("Cannot ÷ by zero!")
        return num1 / num2


demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["+", "-", "x", "÷"]),
        "number"
    ],
    "number",
    title="Toy Calculator",
    description="Here's a sample toy calculator.",
)

demo.launch()
