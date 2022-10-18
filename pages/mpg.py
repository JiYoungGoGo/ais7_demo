import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.markdown("# 자동차 연비 🎈")
st.sidebar.markdown("# 자동차 연비  🎈")

data_url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(data_url):
    data = pd.read_csv(data_url)
    return data

data_load_state = st.text('Loading data...')
mpg = load_data(data_url)
data_load_state.text("Done! (using st.cache)")


st.header("px- line")
ptx = px.line(mpg, x="weight", y="horsepower", color="origin", title="무게별마력")
ptx

ptx3 = px.scatter(mpg, x="weight", y="horsepower", color="origin", title="무게별마력")
ptx3

ptx2 = px.line(mpg, x="weight", y="mpg", color="origin", title="무게별연비")
ptx2

ptx4 = px.scatter(mpg, x="weight", y="mpg", color="origin", title="무게별연비")
ptx4

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max())))
   )

if selected_year > 0 :
   mpg_year = mpg[mpg.model_year == selected_year]


mpg_year

st.header("year - 지역별 연비")
fig, ax = plt.subplots(figsize=(10, 3))
sns.violinplot(data=mpg_year, x="origin", y="mpg").set_title(f"{selected_year}년 지역별 연비")
st.pyplot(fig)

st.header("year - 지역별 연비")
fig, ax = plt.subplots(figsize=(10, 3))
sns.swarmplot(data=mpg_year, x="origin", y="horsepower").set_title(f"{selected_year}년 지역별 마력")
st.pyplot(fig)



st.header("year")
st.bar_chart(mpg_year, x="origin", y="horsepower")

st.header("year - px")
ptx = px.histogram(mpg_year, x="origin")
ptx
st.header("year - sns")
fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=mpg_year, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

if len(selected_origin) > 0:
   origin_mpg = mpg[mpg.origin.isin(selected_origin)]
   mpg_year_origin = mpg_year[mpg_year.origin.isin(selected_origin)]

st.header("origin")
st.bar_chart(origin_mpg, x="model_year", y="horsepower")

st.header("origin - px")
st.text(selected_origin)
ptx = px.histogram(origin_mpg, x="model_year")
ptx

st.header("origin - sns")
st.text(selected_origin)
fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=origin_mpg, x="model_year").set_title("연별 자동차 연비 데이터 수")
st.pyplot(fig)


st.header("year & origin")
st.bar_chart(mpg_year_origin, x="origin", y="horsepower")