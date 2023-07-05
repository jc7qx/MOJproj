import streamlit as st

with st.form(key="form1"):
    st.header("預測案例資料輸入")
    st.subheader("個案資料")
    col1, col2 = st.columns(2)
    name = col1.text_input("觀護案號")
    pid = col2.text_input("統號")
    xxx = st.form_submit_button("提交")

if xxx:
    st.write(name)