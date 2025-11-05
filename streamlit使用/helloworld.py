
import streamlit as st

st.title("Nova文生文")
prompt = st.chat_input("请输入你的问题")
if prompt:
    user_say = st.chat_message("user")
    user_say.write(prompt)
    ai_say = st.chat_message("AI")
    ai_say.write("正在思考中...")

#  python -m streamlit run .\streamlit使用\helloworld.py