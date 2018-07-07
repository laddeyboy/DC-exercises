import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import matplotlib.patches as mpatches



def f(x):
    return x

def g(x):
    return x * (9/5) + 32


f_output = []
g_output = []
x_list = list(range(-5, 6))
for x in x_list:
  f_output.append(f(x))
  g_output.append(g(x))
pyplot.plot(x_list, f_output, 'bo', x_list, g_output, 'ro')

red_patch = mpatches.Patch(color='red', label='Fahrenheit')
first_legend = pyplot.legend(handles=[red_patch], loc=1)
ax = pyplot.gca().add_artist(first_legend)

blue_patch = mpatches.Patch(color='blue', label='Celsius')
pyplot.legend(handles=[blue_patch], loc=4)

pyplot.savefig('DegreeConvert.png')
pyplot.close() # start a new plot