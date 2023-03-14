import pandas as pd
import streamlit as st

st.set_page_config(page_title="DSKaggle Data", page_icon=":bar_chart:", layout="wide")

@st.cache(persist=True)
def load_data():
    data = pd.read_csv("DSKaggle.csv", encoding="latin1")
    return data

df = load_data()

# Remove "India" from the list of countries
countries = list(df["Country"].unique())
countries.remove("India")
countries.insert(0, "All")

# Sidebar filters
country_filter = st.sidebar.selectbox(
    label="Select a country",
    options=countries)

roles = list(df["Current Role"].unique())
roles.insert(0, "All")
role_filter = st.sidebar.selectbox(
    label="Select a current role",
    options=roles)
    
# Filtered dataframe
if country_filter == "All":
    filtered_df = df[df["Current Role"] == role_filter]
else:
    filtered_df = df[(df["Country"] == country_filter) & (df["Current Role"] == role_filter)]

# Drop empty rows in "Current Role" column
filtered_df = filtered_df.dropna(subset=["Current Role"])
filtered_df = filtered_df[filtered_df["Country"] != "India"]

st.dataframe(filtered_df)
