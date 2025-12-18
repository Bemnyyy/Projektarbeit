import sqlite3
import pandas as pd

con=sqlite3.connect('nextbike_data_old.db')
query='SELECT * FROM stations'
data=pd.read_sql(query, con)
data.to_csv('stations.csv')
con.close()