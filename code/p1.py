import pandas as pd
import numpy as np
import streamlit as st

with st.form(key="mojform"):
    st.header("預測案例資料輸入")
    st.markdown("""---""")
    st.subheader("個案資料")
    col1, col2 = st.columns(2)
    cid = col1.text_input("觀護案號")
    pid = col2.text_input("統號")
    col3, col4, col5 = st.columns(3)
    name=col3.text_input("姓名")
    gender = col4.selectbox("性別",["男","女"])
    bdate = col5.date_input("生日")
    col6, col7, col8 = st.columns(3)
    probator_name = col6.text_input("觀護人姓名")
    DAO = col7.selectbox(label="地檢署",
        options=["基隆","新北", "臺北市","桃園","新竹","苗栗","台中","台南","高雄"],
        index = 1
        )
    pb_group = col8.selectbox(
        label="股別",
        options=["忠","孝","仁","愛","信","義","和","平"],
        index=0)
    st.markdown("""---""")
    st.subheader("影響因子")
    st.write("#### 觀護資料")
    col9, col10, col11 = st.columns(3)
    fgender = col9.selectbox("性別", ("男","女"),1)
    fedulevel = col10.selectbox("教育程度", ("碩士","大學","高中","專科","其他"),4)
    fhealth = col11.selectbox("健康情形",("良好","健康","欠佳","不健康","罹病","其他"),0)
    fage=st.slider("年齡", min_value=5, max_value=120, value=50, step=1)
    furtest = st.slider("月平均採尿次數",min_value=0.0, max_value=30.0, value=2.0, step=0.1)
    flength = st.slider("實際保護管束(月)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
    st.markdown("""---""")
    st.write("#### 獄政資料")
    fviolate = st.slider("違規數", min_value=0, max_value=100, value=50, step=1)
    faward = st.slider("獎勵數", min_value=0, max_value=100, value=50, step=1)
    fagain = st.selectbox("犯次", ["未註記","初犯","初再犯同罪","初再犯異罪",
        "再犯","再犯同罪","再犯異罪","初累犯同罪","初累犯異罪","其他累犯"],0)
    st.markdown("""---""")
    st.write("#### 刑案歷史")
    st.write("**保護管束前**")
    col12, col13, col14, col15, col16 = st.columns(5)
    f1year = col12.number_input('第一年犯案次數', min_value=0, max_value=20, step=1)
    f2year = col13.number_input('第二年犯案次數', min_value=0, max_value=20, step=1)
    f3year = col14.number_input('第三年犯案次數', min_value=0, max_value=20, step=1)
    f4year = col15.number_input('第四年犯案次數', min_value=0, max_value=20, step=1)
    f5year = col16.number_input('第五年犯案次數', min_value=0, max_value=20, step=1)
    fcrimeage = st.slider('首犯年齡', min_value=5, max_value=120, value=50, step=1)
    
    submitted = st.form_submit_button(label="提交")
if submitted:
    st.write(name)
    
    
    
        
    


   
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