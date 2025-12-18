import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

# helper function for datetime formating 
def date_to_str(dt):
    return dt.strftime('%Y-%m-%d') if hasattr(dt, 'strftime') else str(dt)

# load nextbike data and calcualte lending proxy
print("Loading NextBike-Data...")
conn = sqlite3.connect('nextbike_data_old.db')

bike_df = pd.read_sql_query("""
    SELECT timestamp, bike_number, available, spot, place_type
    FROM bike_locations
    WHERE timestamp BETWEEN '2025-09-14' AND '2025-10-09'
""", conn)

bike_df['timestamp'] = pd.to_datetime(bike_df['timestamp'])
bike_df = bike_df.sort_values(['bike_number', 'timestamp'])

# check for lending behaviour --> available 1->0 or spot-change
bike_df['rented'] = (
    (bike_df.groupby('bike_number')['available'].diff() == -1) | 
    (bike_df.groupby('bike_number')['spot'].diff() != 0)
).fillna(0).astype(int)

# set hourly
bike_df['timestamp'] = pd.to_datetime(bike_df['timestamp'], errors='coerce')
bike_df = bike_df.dropna(subset=['timestamp'])

bike_df['date'] = bike_df['timestamp'].dt.date.astype(str)
bike_df['hour'] = bike_df['timestamp'].dt.hour.astype(int)
bike_df['weekday'] = bike_df['timestamp'].dt.weekday.astype(int)

bike_df['day_type_num'] = np.where(bike_df['weekday'] >= 5, 1, 0)

hourly_bikes = bike_df.groupby(['date', 'hour', 'weekday']).agg({
    'rented': 'sum',
    'bike_number': 'nunique'
}).reset_index()
hourly_bikes['rent_rate'] = hourly_bikes['rented'] / hourly_bikes['bike_number']

print("NextBike-Data successfully loaded!")
conn.close()

#TODO Loading Weather, Merging, Visualizaton