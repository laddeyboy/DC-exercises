import json
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

with open('Coordinates.json', 'r') as fh:
    data = json.load(fh)
    
x_coords = []
y_coords = []

for coordinate in data['data']:
    x_coords.append(coordinate[0])
    y_coords.append(coordinate[1])
print(x_coords)
print(y_coords)

pyplot.plot(x_coords, y_coords)
pyplot.savefig('FileIO_Ex4.png')
pyplot.close() # start a new plot

