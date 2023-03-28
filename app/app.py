
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# Add title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

mpg_df_raw = load_data(path="./data/mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
#st.checkbox("Show Dataframe")
if st.checkbox("Show Dataframe", value=False):
    st.subheader("This is my dataset:")
    #st.table(data=mpg_df)
    st.dataframe(data=mpg_df)

# In Matplotlib
m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(mpg_df['displ'], mpg_df['hwy'], alpha=0.7)

ax.set_title("Engine Size vs. Highway Fuel Mileage")
ax.set_xlabel('Displacement (Liters)')
ax.set_ylabel('MPG')

means = mpg_df.groupby('class').mean()
ax.scatter(means['displ'], means['hwy'], alpha=0.7, color="red")

st.pyplot(m_fig)

# Widgets: selectbox
years = ["All"]+sorted(pd.unique(mpg_df['year']))
year = st.selectbox("Choose a Year", years)
