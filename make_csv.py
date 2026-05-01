from bs4 import BeautifulSoup
import pandas as pd

def make_csv(url, excel_file, output_csv="station_details.csv"):
    with open(url, "r", encoding="utf-8") as f:
        html_content = f.read()

    station_details = []

    soup = BeautifulSoup(html_content, "lxml")
    df_stations = pd.read_excel(excel_file)

    mapping = dict(zip(df_stations["Station ID"], zip(df_stations["Location (Centre)"], df_stations["Mode (Updated)"])))

    table = soup.find("table", class_="table tblcontent tblnocheck")
    table_rows = table.find("tbody").find_all("tr")
    for row in table_rows:
        table_data = row.find_all("td")
        station_name = table_data[0].text.strip()
        link = table_data[1].find("a")["href"]
        station_id = int(link.split("/")[-2])
        domain = table_data[2].text.strip()
        address = table_data[3].text.strip()
        address_maps = "https://www.google.com/maps/search/" + address.replace(" ", "+")
        state = table_data[4].text.strip()
        country = table_data[5].text.strip()
        # From excel
        centre, mode = mapping.get(station_id, ("", ""))

        station_details.append({"Station ID": station_id, "Station Name": station_name, "Domain": domain, "Centre": centre, "State": state, "Country": country, "Mode": mode, "Address": address, "Address Link": address_maps, "View Details": link})

    df = pd.DataFrame(station_details)
    df.to_csv(output_csv, index=False)