import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
data = pd.read_csv(url)


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

if selected_year > 0 :
   data = data[data.model_year == selected_year]


# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]


data