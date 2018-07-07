import matplotlib
import math
matplotlib.use("Agg")
from matplotlib import pyplot
from math import sin


def f(x):
    return math.sin(x)


f_output = []
x_list = list(range(-5, 6))
for x in x_list:
  f_output.append(f(x))
pyplot.plot(x_list, f_output)
pyplot.savefig('Sine.png')
pyplot.close() # start a new plot