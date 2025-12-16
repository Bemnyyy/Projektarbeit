from meteostat import Daily
from datetime import datetime
import matplotlib.pyplot as plt

# Set time period
start = datetime(2025, 9, 1)
end = datetime(2025, 9, 1)

# Get Daily Data
data = Daily('10727', start, end)
data = data.fetch()
print(data)


#data.plot(y=['temp', 'prcp', 'snow', 'wspd', 'tsun'])
#plt.show()