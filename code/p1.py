import pandas as pd
import numpy as np
import streamlit as st
from datetime import date
    
def genderCode(x):
    if x=='男':
        return 0
    if x=='女':
        return 1
    
def eduCode(x):
    if x in ['博士','碩士','大學']:
        return 0
    if x in ['專科','高中']:
        return 1
    if x in ['其他']:
        return 2
    
def healthCode(x):
    if x in ['良好','健康']:
        return 0
    if x in ['欠佳','不健康']:
        return 1
    if x in ['罹病']:
        return 2
    if x in ['其他']:
        return 3
    
def ageCode(x):
    if x < 24:
        return 0
    elif 24 <= x < 29:
        return 1
    elif 29 <= x <34:
        return 2
    elif 34 <= x <39:
        return 3
    elif 39 <= x <44:
        return 4
    elif 44 <= x < 48:
        return 5
    else:
        return 6
    
def lenCode(x):
    if x < 7:
        return 0
    elif 7 <= x < 13:
        return 1
    elif 13 <= x < 19:
        return 2
    elif 19 <= x < 25:
        return 3
    elif 25 <= x < 31:
        return 4
    elif 31 <= x < 37:
        return 5
    else:
        return 6

def vioCode(x):
    if x < 1:
        return 0
    elif 1 <= x < 5:
        return 1
    elif 5 <= x < 9:
        return 2
    else:
        return 3
    
def awardCode(x):
    if x <1:
        return 0
    elif 1 <= x < 11:
        return 1
    elif 11 <= x <21:
        return 2
    elif 21 <= x < 31:
        return 3
    elif 31 <= x <41:
        return 4
    else:
        return 5
    
def againCode(x):
    if x in ["未註記","初犯"]:
        return 0
    if x in ["初再犯同罪","初再犯異罪"]:
        return 1
    if x in ["再犯","再犯同罪","再犯異罪"]:
        return 2
    if x in ["初累犯同罪","初累犯異罪"]:
        return 3
    if x in ["其他累犯"]:
        return 4

def crimeageCode(x):
    if x < 21:
        return 0
    elif 21 <= x < 31:
        return 1
    elif 31 <= x < 41:
        return 2
    elif 41 <= x < 51:
        return 3
    elif 51 <= x < 61:
        return 4
    elif 61 <= x < 71:
        return 5
    else:
        return 6



def factorcoding():
    factorsCode=[]
    factorsCode.append(genderCode(fgender))
    factorsCode.append(eduCode(fedulevel))
    factorsCode.append(healthCode(fhealth))
    factorsCode.append(ageCode(fage))
    factorsCode.append(furtest)
    factorsCode.append(lenCode(flength))
    factorsCode.append(vioCode(fviolate))
    factorsCode.append(awardCode(faward))
    factorsCode.append(againCode(fagain))
    factorsCode.append(f1year)
    factorsCode.append(f2year)
    factorsCode.append(f3year)
    factorsCode.append(f4year)
    factorsCode.append(f5year)
    factorsCode.append(fcrimeage)
    st.write(factorsCode)


if __name__ == "__main__":
    
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
        
    with st.form(key="mojform"):
        gender_code = ["男","女"]
        st.header("預測案例資料輸入")
        st.markdown("""---""")
        st.subheader("個案資料")
        col1, col2 = st.columns(2)
        cid = col1.text_input("觀護案號")
        pid = col2.text_input("統號")
        col3, col4, col5 = st.columns(3)
        name=col3.text_input("姓名")
        gender = col4.selectbox("性別",["男","女"])
        bdate = col5.date_input("生日", min_value=date(1900,1,1), max_value=date(2050,12,31))
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
        idx = gender_code.index(gender)
        today = date.today()
        age = today.year - bdate.year
        
        col9, col10, col11 = st.columns(3)
        fgender = col9.selectbox("性別", ("男","女"), idx, key="test1")
        fedulevel = col10.selectbox("教育程度", ("碩士","大學","高中","專科","其他"),4)
        fhealth = col11.selectbox("健康情形",("良好","健康","欠佳","不健康","罹病","其他"),0)
        fage=st.slider("年齡", min_value=5, max_value=120, value=age, step=1)
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
        factorcoding()
    
    
    
        
    


   
