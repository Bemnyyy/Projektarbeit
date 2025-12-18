import sqlite3
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import os

# Connection to db file
conn = sqlite3.connect("nextbike_data_old.db")
df = pd.read_sql_query("SELECT * FROM bike_locations", conn)
conn.close()

# Mid Point of Map
center_lat = df['lat'].mean()
center_lng = df['lng'].mean()

m = folium.Map(location=[center_lat, center_lng], zoom_start=13)

# marker for every row
FastMarkerCluster(df[['lat', 'lng']].values.tolist()).add_to(m)

#save map
m.save("nextbike_map.html")