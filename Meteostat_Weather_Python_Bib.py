



# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Hourly
import matplotlib.pyplot as plt

# Set time period
start = datetime(2025, 11, 24)
end = datetime(2025, 11, 24, 23, 59)

# Get hourly data
data = Hourly('10727', start, end)
data = data.fetch()

#data.plot(y=['temp', 'prcp', 'snow', 'wspd', 'tsun'])
# Temperatur pro Stunde als Balken
ax = data['temp'].plot(kind='line', figsize=(12, 4))
ax.set_xlabel('Stunde')
ax.set_ylabel('Temperatur [°C]')
ax.set_title('Stündliche Temperatur – Station 10727 - Karlsruhe')
# Niederschlag und sonnenschein - stündlich 
ax = data[['prcp', 'tsun']].plot(kind='bar', stacked=True, figsize=(12, 4))
ax.set_xlabel('Stunde')
ax.set_ylabel('Niederschlag / Schneehöhe')
ax.set_title('Niederschlag & Schnee – gestapelt')

# Gestapelte Balken Niederschlag und Sonnenscheindauer
ax = data[['prcp', 'tsun']].plot(kind='bar', figsize=(12, 4))
ax.set_xlabel('Stunde')
ax.set_ylabel('Wert')
ax.set_title('Niederschlag & Sonnenscheindauer – stündlich')
plt.tight_layout()
plt.show()

'''
import numpy as np

x = np.arange(len(data.index))  # 0..n-1
width = 0.35

fig, ax = plt.subplots(figsize=(12, 4))
ax.bar(x - width/2, data['prcp'], width, label='prcp')
ax.bar(x + width/2, data['temp'], width, label='temp')
ax.set_xticks(x)
ax.set_xticklabels(data.index.strftime('%H:%M'), rotation=45)
ax.set_xlabel('Zeit')
ax.set_ylabel('Wert')
ax.set_title('Niederschlag vs. Temperatur')
ax.legend()

plt.tight_layout()
plt.show()  # [web:18][web:60][web:65]

# Print DataFrame
#print(data)
'''