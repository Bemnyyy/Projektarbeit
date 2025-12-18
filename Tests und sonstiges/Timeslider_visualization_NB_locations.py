import sqlite3
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson


# !!!DO NOT USE THIS FILE UNLESS U HAVE MORE THAN 16 GB OF RAM !!!


conn = sqlite3.connect("nextbike_data_old.db")
df = pd.read_sql_query("SELECT * FROM bike_locations", conn)
conn.close()

df["time"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%dT%H:%M:%S")

features = []
for _, row in df.iterrows():
    feat = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row["lng"], row["lat"]],
        },
        "properties": {
            "time": row["time"],
            "popup": f"{row['name']} (Bike {row['bike_number']})",
            "icon": "circle",
            "iconstyle": {
                "fillColor": "red",
                "fillOpacity": 0.7,
                "stroke": "false",
                "radius": 4,
            },
        },
    }
    features.append(feat)

data = {
    "type": "FeatureCollection",
    "features": features,
}

m = folium.Map(location=[df["lat"].mean(), df["lng"].mean()], zoom_start=13)

TimestampedGeoJson(
    data,
    period="PT1H",                 
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options="YYYY-MM-DD HH:mm:ss",
    time_slider_drag_update=True,
).add_to(m)

m.save("nextbike_timeslider.html")
