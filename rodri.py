import requests
import pandas as pd

url = "https://opensky-network.org/api/states/all"

response = requests.get(url)

data = response.json()

columns = [
    "icao24",
    "callsign",
    "origin_country",
    "time_position",
    "last_contact",
    "longitude",
    "latitude",
    "baro_altitude",
    "on_ground",
    "velocity",
    "true_track",
    "vertical_rate",
    "sensors",
    "geo_altitude",
    "squawk",
    "spi",
    "position_source"
]

df = pd.DataFrame(data["states"], columns=columns)

df.index = range(1, len(df)+ 1)

print(df[["longitude", "latitude"]])




