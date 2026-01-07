from meteostat import Daily
from datetime import datetime
import matplotlib.pyplot as plt

# Set time period
start = datetime(2025, 9, 1)
end = datetime(2025, 9, 30)

# Get Daily Data
data = Daily('10727', start, end)
data = data.fetch()
print(data)

def plot_1(data):
    # Temp, Regen, Schnee und Windgeschwindigkeit als Linien
    ax = data.plot(y=['tavg', 'prcp', 'snow', 'wspd'])
    ax.set_xlabel('Tag')
    ax.set_title(f'Durchschnitts-Temp., Regendauer/stärke, Schneehäufigkeit, Windgeschwindigkeit - Karlsruhe am {start} bis {end}')

def plot_2(data):
    # Temperatur pro Stunde als Linien
    ax = data[['tavg', 'prcp']].plot(kind='line', figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Temperatur [°C]')
    ax.set_title(f'Stündliche Temperatur und Regen – Station 10727 - Karlsruhe am {start} bis {end}')

def plot_3(data):
    # temperatur und sonnenschein - stündlich 
    ax = data[['tavg', 'snow']].plot(kind='bar', stacked=True, figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Temperatur / Schneehöhe')
    ax.set_title(f'Temperatur & Schnee – gestapelt am {start} bis {end}')

def plot_4(data):
    # Gestapelte Balken temperatur und Sonnenscheindauer
    ax = data[['tavg', 'prcp']].plot(kind='bar', figsize=(12, 4))
    ax.set_xlabel('Stunde')
    ax.set_ylabel('Wert')
    ax.set_title(f'Niederschlag & Regendauer – stündlich am {start} bis {end}')

if __name__ == "__main__":
    plot_1(data)
    plot_2(data)
    plot_3(data)
    plot_4(data)
    plt.tight_layout()
    plt.show()
