from datetime import datetime
from meteostat import Hourly
import matplotlib.pyplot as plt

# Set time period
start = datetime(2025, 9, 1) 
end = datetime(2025, 9, 1, 23, 59) 

# Get hourly data
data = Hourly('10727', start, end)
data = data.fetch()

def plot_1(data):
    data.plot(y=['temp', 'prcp', 'snow', 'wspd', 'tsun'])
    
def plot_2(data):
    # Temperatur pro Stunde als Linien
    ax = data[['temp']].plot(kind='line', figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Temperatur [°C]')
    ax.set_title(f'Stündliche Temperatur – Station 10727 - Karlsruhe am {start} bis {end}')

def plot_3(data):
    # temperatur und sonnenschein - stündlich 
    ax = data[['temp', 'wspd']].plot(kind='bar', stacked=True, figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Temperatur / Schneehöhe')
    ax.set_title('Temperatur & Windgeschwindigkeit – gestapelt')

def plot_4(data):
    # Gestapelte Balken temperatur und Sonnenscheindauer
    ax = data[['prcp', 'tsun']].plot(kind='bar', figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Wert')
    ax.set_title('Niederschlag & Sonnenscheindauer – stündlich')

if __name__ == "__main__":
    plot_1(data)
    plot_2(data)
    plot_3(data)
    plot_4(data)
    plt.tight_layout()
    plt.show()