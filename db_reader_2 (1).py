import sqlite3

conn = sqlite3.connect("nextbike_data.db")
cur = conn.cursor()

# 1. Tabellen anzeigen
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tabellen:", tables)

# 2. Erste Tabelle untersuchen
table = tables[0][0]
cur.execute(f"PRAGMA table_info({table});")
print(f"Spalten von {table}:", cur.fetchall())

conn.close()

#Ausführen führt zu den verschiedenen Tabellen und deren Spalten in der Datenbank.Zeigt außerdem den Typ an (Integer, Text, etc.).