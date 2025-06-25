import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",41.88, -87.63],
          ["Boston", 42.36, -71.06], 
          ["Salt Lake City", 40.76, -111.89],
          ["San Francisco", 37.77, -122.42],
          ["New York City", 40.71, -74.01],
          ["Denver", 39.74, -104.99],
          ["San Diego", 32.72, -117.16],
          ["Seattle", 47.61, -122.33],
          ["Portland", 45.52, -122.68],
          ["Atlanta", 33.75, -84.39]]
scale = 5

map = Basemap(llcrnrlon=-125,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

map.drawstates()
map.drawcoastlines()
map.drawcountries()
map.drawrivers(color='blue')
map.drawparallels(range(20, 60, 10), labels=[1,0,0,0])
map.drawmeridians(range(-130, -60, 10), labels=[0,0,0,1])
map.etopo()

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
    plt.text(x, y, city, ha='center', va='top', fontsize=8, color='white', fontweight='bold')
plt.show()
