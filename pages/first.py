"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.markdown("# first π")
st.sidebar.markdown("# first π")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.title("μ λͺ©")
st.header("ν€λ")
st.subheader("μλΈν€λ")

st.image("https://item.kakaocdn.net/do/fd0050f12764b403e7863c2c03cd4d2d7154249a3890514a43687a85e6b6cc82")
st.caption("μ§±κ΅¬")
