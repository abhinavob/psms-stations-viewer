import requests
from bs4 import BeautifulSoup
import pandas as pd

def make_csv(url):
    with open(url, "r") as f:
        html_content = f.read()

    station_details = []

    soup = BeautifulSoup(html_content, "lxml")

    table = soup.find("table", class_="table tblcontent tblnocheck")
    table_rows = table.find("tbody").find_all("tr")
    for row in table_rows:
        table_data = row.find_all("td")
        station_name = table_data[0].text.strip()
        link = table_data[1].find("a")["href"]
        domain = table_data[2].text.strip()
        city = table_data[3].text.strip()
        state = table_data[4].text.strip()
        country = table_data[5].text.strip()
        station_details.append({"Station Name": station_name, "View Details": link, "Domain": domain, "City": city, "State": state, "Country": country})

    df = pd.DataFrame(station_details)
    df.to_csv("station_details.csv", index=False)