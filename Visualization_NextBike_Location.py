import pandas as pd
import geopandas as gpd
from shapely import Point


# pandas: read csv
path = r'S:\Studium\3. Semester\VSMB 330 Digitalisierung und Mobilsoftware\Projektarbeit\NextBikeData as CSV\bike_locations.csv'
df = pd.read_csv(path)
#print(df.columns)

# shapely: create geometry
geometry_col = [Point(xy) for xy in zip(df['lng'], df['lat'])]
#print(geometry_col[:4])

# geopandas: host geospatial layer
spatial_data = gpd.GeoDataFrame(df, geometry= geometry_col)
spatial_data.set_crs(4326)
print(spatial_data.plot())