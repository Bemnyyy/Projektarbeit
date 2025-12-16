from datetime import datetime
from meteostat import Hourly
import matplotlib.pyplot as plt

# Set time period
start = datetime(2025, 9, 1) 
end = datetime(2025, 9, 2, 23, 59) 

# Get hourly data
data = Hourly('10727', start, end)
data = data.fetch()

def plot_1(data):
    data.plot(y=['temp', 'prcp', 'snow', 'wspd', 'tsun'])
    plt.show()
    return data
    

def plot_2(data):
    # Temperatur pro Stunde als Balken
    ax = data[['temp']].plot(kind='line', figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Temperatur [°C]')
    ax.set_title(f'Stündliche Temperatur – Station 10727 - Karlsruhe am {start} bis {end}')
    plt.show()
    return data

'''
# Niederschlag und sonnenschein - stündlich 
ax = data[['prcp', 'tsun']].plot(kind='bar', stacked=True, figsize=(12, 4))
ax.set_xlabel('Stunde')
ax.set_ylabel('Niederschlag / Schneehöhe')
ax.set_title('Niederschlag & Schnee – gestapelt')
'''

'''
# Gestapelte Balken Niederschlag und Sonnenscheindauer
ax = data[['prcp', 'tsun']].plot(kind='bar', figsize=(12, 4))
ax.set_xlabel('Stunde')
ax.set_ylabel('Wert')
ax.set_title('Niederschlag & Sonnenscheindauer – stündlich')
plt.tight_layout()
plt.show()
'''

if __name__ == "__main__":
    plot_1(data)
    plot_2(data)