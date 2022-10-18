"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.markdown("# first 🎉")
st.sidebar.markdown("# first 🎉")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.title("제목")
st.header("헤더")
st.subheader("서브헤더")

st.image("https://item.kakaocdn.net/do/fd0050f12764b403e7863c2c03cd4d2d7154249a3890514a43687a85e6b6cc82")
st.caption("짱구")
