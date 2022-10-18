import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# second ❄️")
st.sidebar.markdown("# second ❄️")

df = pd.DataFrame({
  'first column': [15, 25, 35, 49],
  'second column': [100, 50, 60, 400],
  'third column' : [300,200,100,500]
})

st.header("df")
df 

st.header("table")
st.table(df)

st.header("bar chart")
st.bar_chart(df)

st.header("area chart")
st.area_chart(df)

st.header("line chart")
st.line_chart(df)