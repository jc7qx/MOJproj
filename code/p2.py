import streamlit as st

col1, col2 = st.columns(2)
f1year = col1.number_input('第一年犯案次數', min_value=0, max_value=20, step=1)
f2year = col2.number_input('第2年犯案次數', min_value=0, max_value=20, step=1)
st.write(f1year)
st.write(f2year)