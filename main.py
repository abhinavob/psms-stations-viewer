import pandas as pd
import streamlit as st
from make_csv import make_csv

# Only run the first time to make the CSV file with all the details from the HTML file
# make_csv("PSMSWeb.html")

df = pd.read_csv("station_details.csv")

st.set_page_config(
    page_title="PS-I Stations 2026",
    layout="wide"
)

name = st.text_input("Station Name")
place = st.selectbox("City", [""] + sorted(df["City"].unique()))
domain = st.selectbox("Business Domain", [""] + sorted(df["Domain"].unique()))

stations = df

if name:
    stations = stations[stations["Station Name"].str.casefold().str.contains(name.casefold())]
if place:
    stations = stations[stations["City"].str.casefold().str.contains(place.casefold())]
if domain:
    stations = stations[stations["Domain"] == domain]

st.write("Total Stations Found: ", len(stations))

# Header
cols = st.columns([3, 2, 2, 1])
cols[0].write("**Station Name**")
cols[1].write("**Business Domain**")
cols[2].write("**City**")
cols[3].write("**View Details**")

st.divider()

# Rows
for _, row in stations.iterrows():
    cols = st.columns([3, 2, 2, 1])

    cols[0].write(row["Station Name"])
    cols[1].write(row["Domain"])
    cols[2].write(row["City"])
    cols[3].link_button("View", row["View Details"])