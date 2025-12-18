import sqlite3
import pandas as pd
import folium
import ipywidgets as widgets
from IPython.display import display, clear_output
from datetime import datetime

def create_bike_map(bike_number):
    # connect to database
    conn = sqlite3.connect("nextbike_data_old.db")
    query = """
        SELECT *
        FROM bike_locations
        WHERE bike_number = ?
        ORDER BY timestamp
    """

    df = pd.read_sql_query(query, conn, params=(bike_number,))
    conn.close()

    if df.empty:
        print("Keine Daten für diesen Tag")
        return
    # mean of the position of all bikes
    center_lat = df['lat'].mean()
    center_lng = df['lng'].mean()

    m = folium.Map(location=[center_lat, center_lng], zoom_start=13)

    # all positions of the bike as a timeline
    for _, row in df.iterrows(): # type: ignore
        folium.CircleMarker(
            location=[row['lat'], row['lng']],
            radius=6,
            popup=f"{row['name']} (Bike {row['bike_number']})<br>{row['timestamp']}",
            color="red",
            fill=True,
            fill_opacity=0.8,
            tooltip=f"{row['timestamp'][:16]}"
        ).add_to(m)

    # line for tracing the bikes path
    folium.PolyLine(
        locations=df[['lat', 'lng']].values.tolist(),
        color="blue",
        weight=3,
        opacity=0.7,
        popup="Bewegungsverlauf dieses Bikes").add_to(m)
    
    m.save(f"bike_{bike_number}.html")
    return m

# Load all bikes
conn = sqlite3.connect("nextbike_data_old.db")
bikes_df = pd.read_sql_query("SELECT DISTINCT bike_number FROM bike_locations ORDER BY bike_number", conn)

bike_dropdown = widgets.Dropdown(
    options=bikes_df["bike_number"].tolist(),
    value=bikes_df["bike_number"].iloc[0],
    description='Bitte wählen:',
    style={'description_width': 'initial'}
)

output = widgets.Output()

def update_map(change):
    clear_output(wait=True)
    print(f"Lade Karte für Bike {change['new']}...")
    m = create_bike_map(change['new'])
    display(m)

bike_dropdown.observe(update_map, names='value')

# show UI
display(widgets.VBox([bike_dropdown, output]))
update_map({'new': bike_dropdown.value})