import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from config import API_KEY_METEOSTAT

DB_PATH = "Weather_Data_3.db"
#start_date = "2026-01-01" # Time format example: "2025-09-30", this could also be resolved with an input prompt like start_date = input("choose a start Date: ")
#end_date = "2026-01-15" # Time format example equially to start_date, could also be resolved as a input prompt
start_date = input("Set a starting Date (Format: '2025-01-01'): ")
end_date = input("Set a ending Date (Format: '2025-01-01'): ")

# Get Data from API (Output: Dict, "meta" + "data")
def load_weather_data():
    url = "https://meteostat.p.rapidapi.com/stations/hourly"
    querystring = {"station":"10727","start": start_date,"end": end_date,"tz":"Europe/Berlin"}
    headers = {
    	"x-rapidapi-key": API_KEY_METEOSTAT,
    	"x-rapidapi-host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return(data)

# Clearing Output from API -> getting only "data" and the specific columns we need by putting them in list
def clean_weather_data(json_data):
    weather_dict_list = []
    
    for weather_reading in json_data['data']:
        weather_dict = {'time' : weather_reading['time'],
                        'temp' : weather_reading['temp'],
                        'prcp' : weather_reading['prcp'],
                        'snow' : weather_reading['snow'],
                        'wdir' : weather_reading['wdir'],
                        'wspd' : weather_reading['wspd'],
                        'tsun' : weather_reading['tsun']}
        weather_dict_list.append(weather_dict)
    return weather_dict_list

# creating a SQL-DataFrame to easily view and display the data
def create_SQL(df):
    table_name = input("Type in a new Table-Name or the Table that the Data should append to:")
    engine = create_engine(f"sqlite:///{DB_PATH}")
    df.to_sql(f"{table_name}", con=engine, if_exists="append", index=False)
    print(f"{len(df)} Datensätze wurden in die Datenbank geschrieben am {datetime.now().strftime('%Y-%m-%d')} um {datetime.now().strftime('%H:%M:%S')} für folgenden Zeitraum: \n{start_date} - {end_date} ")
    return df

# Loading all the functions and defining df as a DataFrame to convert the list Data from previous to a SQL-DataFrame
if __name__ == '__main__':
    data = load_weather_data()
    weather = clean_weather_data(data)
    df = pd.DataFrame(weather)
    create_SQL(df)