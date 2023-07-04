import pandas as pd
import numpy as np
import streamlit as st

def newInputs():
    st.header("預測案例資料輸入")
    name=st.text_input("姓名")
    pid = st.text_input("統號")
    bdate = st.text_input("生日")
    gender = st.text_input("性別")
    probation_id = pid = st.text_input("案號")

newInputs()
   
with st.sidebar:
    st.title("再犯風險預測")
    model_opt = st.selectbox(
        label="預測模型",
        options=("隨機森林","XGBoost")
    )
    crime_opt = st.selectbox(
        label="犯罪案類",
        options=("毒品再犯","暴力再犯","性暴力再犯","酒駕再犯","財產罪再犯","公共危險再犯","竊盜再犯"),
        index=1
    )


st.write(model_opt+" + "+crime_opt)