from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


cities = ['Tehran', 'Tabriz', 'Shiraz', 'Isfahan', 'Mashhad', 'Karaj', 'Qom', 'Hamadan', 'Ahvaz']
lons = [51.389, 46.291, 52.541, 51.675, 59.568, 50.978, 50.880, 48.512, 48.670]
lats = [35.689, 38.080, 29.591, 32.654, 36.297, 35.835, 34.641, 34.798, 31.320]
population = [16800, 1700, 2000, 2200, 3400, 1970, 1200, 1740, 1300]


colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']


fig = plt.figure(figsize=(10, 8))
m = Basemap(llcrnrlon=44, llcrnrlat=25, urcrnrlon=63, urcrnrlat=40, resolution='l', projection='merc')


m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='aqua')
m.drawmapboundary(fill_color='aqua')


x, y = m(lons, lats)


for i in range(len(cities)):
    m.scatter(x[i], y[i], s=population[i] / 20, c=colors[i], alpha=0.8, edgecolors='black', label=cities[i], zorder=5)


for i, city in enumerate(cities):
    plt.text(x[i], y[i], city, fontsize=12, ha='right', color='black')


plt.legend(loc='lower left', title="Cities")


plt.title('Cities of Iran with Population-based Size and Unique Colors')
plt.show()