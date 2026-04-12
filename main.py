import pandas as pd
import streamlit as st
from make_csv import make_csv

# Only run the first time to make the CSV file with all the details from the HTML file
# make_csv("PSMSWeb.html")

st.set_page_config(layout="wide")

df = pd.read_csv("station_details.csv")

place = st.selectbox("City", [""] + sorted(df["City"].unique()))
domain = st.selectbox("Domain", [""] + sorted(df["Domain"].unique()))

if place and domain:
    stations = df[df["City"].str.casefold().str.contains(place.casefold()) & df["Domain"].str.casefold().str.contains(domain.casefold())]
elif place:
    stations = df[df["City"].str.casefold().str.contains(place.casefold())]
elif domain:
    stations = df[df["Domain"].str.casefold().str.contains(domain.casefold())]
else:
    stations = df

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