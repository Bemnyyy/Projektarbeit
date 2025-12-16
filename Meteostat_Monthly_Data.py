# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Monthly

# Set time period
start = datetime(2025, 8, 1)
end = datetime(2018, 9, 30)

# Get Monthly data
data = Monthly('10727', start, end)
data = data.fetch()
print(data)

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()

### Kein Plan was hier abgeht, checke nicht ganz wie und wo "Stations" verwendet werden soll
### In der Docu find ich auch nichts dazu irgendwie