import os
from sqlalchemy import create_engine
import pandas as pd
import requests as rs
from datetime import datetime, date as dt_date
import time
import json
from config import API_KEY

LAT = 49.006889
LON = 8.403653
UNITS = "metric"
DB_PATH = "Weather_Data.db"
COUNTER_FILE = "weather_counter.json"
DAILY_LIMIT = 800 # Max. eigentlich 1000 aber zur Sicherheit 800
MIN_INTERVAL = 900 # 5 Minuten in sek.(300)

def load_weather_data():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units={UNITS}&appid={API_KEY}'
    response = rs.get(url)
    return [response.json()] # Liste für DataFrame-Kompatibilität

def create_SQL(df):
    df_flat = pd.json_normalize(df.to_dict(orient="records")) # API Antwort "flach" auflösen aufgrund von verschachtelung der daten von der API
    df_flat['weather'] = df_flat['weather'].apply(json.dumps)
    engine = create_engine(f"sqlite:///{DB_PATH}")
    df_flat.to_sql("karlsruhe_weather", con=engine, if_exists="append", index=False)
    print(f"{len(df_flat)} Datensätze wurden in die Datenbank geschrieben am {datetime.now().strftime('%Y-%m-%d')} um {datetime.now().strftime('%H:%M:%S')}")
    return df_flat

def read_counter():
    if not os.path.exists(COUNTER_FILE):
        return {"date": str(dt_date.today()), "count": 0}
    with open(COUNTER_FILE, "r") as f:
        return json.load(f)
    
def write_counter(counter):
    with open(COUNTER_FILE, "w") as f:
        json.dump(counter, f)

if __name__ == '__main__':
    while True:
        counter = read_counter()
        today = str(dt_date.today())
        print(type(dt_date))
        if counter["date"] != today:
            counter = {"date": today, "count": 0} # Neues Tageslimit

        if counter["count"] >= DAILY_LIMIT:
            print("Tageslimit erreicht, warte bis nächster Tag.") # Warte bis Mitternacht
            seconds_until_midnight = (
                (datetime.combine(dt_date.today(), 
                datetime.min.time()).replace(day=dt_date.today().day+1) - datetime.now()).seconds
            )
            time.sleep(seconds_until_midnight + 1)
            continue
        weather = load_weather_data()
        df = pd.DataFrame(weather)
        create_SQL(df)
        counter["count"] += 1
        write_counter(counter)
        time.sleep(MIN_INTERVAL)