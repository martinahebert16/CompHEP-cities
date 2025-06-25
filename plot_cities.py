import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",41.88, -87.63],
          ["Boston", 42.36, -71.06], 
          ["Salt Lake City", 40.76, -111.89],
          ["San Fransisco", 37.77, -122.42]]
scale = 5

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

map.shadedrelief()

map.drawstates()
map.drawcoastlines()
map.drawmapboundary(fill_color='blue')
map.fillcontinents(color='yellow', lake_color='blue')
map.drawcountries()
map.drawrivers(color='blue')
map.drawparallels(range(20, 60, 10), labels=[1,0,0,0])
map.drawmeridians(range(-130, -60, 10), labels=[0,0,0,1])

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
plt.show()
