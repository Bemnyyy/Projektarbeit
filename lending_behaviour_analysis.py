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

# convert "timestamp" from the database into a pandas datatime object
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

# loading weather data for sep + oct
print("Loading Weather-Data...")
conn_w = sqlite3.connect("Weather_Data_3.db") 

weather_query = """
SELECT time, temp, prcp, wspd FROM karlsruhe_weather_09_2025
UNION ALL
SELECT time, temp, prcp, wspd FROM karlsruhe_weather_10_2025
"""
weather_df = pd.read_sql_query(weather_query, conn_w)
weather_df['time'] = pd.to_datetime(weather_df['time'])
weather_df['date'] = weather_df['time'].dt.date.astype(str)
weather_df['hour'] = weather_df['time'].dt.hour.astype(int)
weather_df['weekday'] = weather_df['time'].dt.weekday.astype(int)

print("Weather-Data successfully loaded!")
conn_w.close()

# merging
merged = pd.merge(hourly_bikes, weather_df[['date', 'hour', 'temp', 'prcp', 'wspd']], on=['date', 'hour'], how='left')
print("merge successfully!")

# define day-types for celebration-days in the time period (03.10 Tag der Dt. Einheit)
holidays = ['2025-10-03']
merged['date_str'] = merged['date'].astype(str)
merged['day_type'] = np.where(merged['date_str'].isin(holidays), 'Feiertag', np.where(merged['weekday'] >= 5, 'Wochenende', 'Werktag'))

print(f"Data analysed: {len(merged)} Stunden, {merged['day_type'].value_counts().to_dict()}")

# set correlation
corrs = {
    'Temperatur': round(merged['rent_rate'].corr(merged['temp']), 3),
    'Niederschlag': round(merged['rent_rate'].corr(merged['prcp']), 3),
    'Wind': round(merged['rent_rate'].corr(merged['wspd']), 3)
}

print("\nCorrelation of borrowing behavior:", corrs)

# Setting grafics
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Nextbike Ausleihverhalten vs. Wetter - Karlsruhe Sep/Okt 2025', fontsize=16)

# 1: Correlation
ax1 = axes[0,0]
x = range(len(corrs))
ax1.bar(x, corrs.values(), color=['orange', 'blue', 'gray'])
ax1.set_title('Korrelationen mit Ausleihquote')
ax1.set_xticks(x)
ax1.set_xticklabels(corrs.keys(), rotation=0)
ax1.axhline(0, color='black', lw=0.5)

# 2 hourly lending by day-type
ax2 = axes[0,1]
hourly_avg = merged.groupby(['hour', 'day_type'])['rent_rate'].mean().unstack()
hourly_avg.plot(ax=ax2, marker='o')
ax2.set_title('Stündliche Ausleihmuster nach Tagstyp')
ax2.set_xlabel('Uhrzeit')
ax2.set_ylabel('Ausleihquote')
ax2.legend(title='Tagstyp')

# 3 lending by temp
ax3 = axes[1,0]
merged['temp_bin'] = pd.cut(merged['temp'], bins=5, labels=['<5°C','5-10°C','10-15°C','15-20°C','>20°C'])
temp_stats = merged.groupby(['day_type', 'temp_bin'])['rent_rate'].mean().unstack()
temp_stats.plot(kind='bar', ax=ax3)
ax3.set_title('Ausleihquote nach Temperatur')
ax3.legend(title='Tagstyp', bbox_to_anchor=(1.05, 1), loc='upper left')
ax3.tick_params(axis='x', rotation=45)
ax3.set_ylabel('Ausleihquote')

# 4 temp vs lending behaviour
ax4 = axes[1,1]
colors = {'Werktag':'blue', 'Wochenende':'green', 'Feiertag':'red'}
for day_type, color in colors.items():
    subset = merged[merged['day_type'] == day_type]
    ax4.scatter(subset['temp'], subset['rent_rate'], 
               c=color, label=day_type, alpha=0.6, s=10)
ax4.set_xlabel('Temperatur [°C]')
ax4.set_ylabel('Ausleihquote')
ax4.set_title('Temperatur vs Ausleihverhalten')
ax4.legend()

plt.tight_layout()
plt.savefig('nextbike_weather_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# 7 summary table
summary_stats = merged.groupby('day_type').agg({
    'rent_rate': ['mean', 'std'],
    'temp': 'mean',
    'prcp': 'mean',
    'wspd': 'mean'
}).round(3)
print("\n==== SUMMARY ====")
print(summary_stats)
print(f"\nTotal Period: {merged['date'].min()} till {merged['date'].max()}")
print("Graphics saved: nextbike_weather_analysis.png")