import matplotlib
import math
matplotlib.use("Agg")
from matplotlib import pyplot
from numpy import arange


def f(x):
    return math.sin(x)


f_output = []
x_list = arange(-5, 6, 0.1)
for x in x_list:
  f_output.append(f(x))
pyplot.plot(x_list, f_output)
pyplot.savefig('Sine2.png')
pyplot.close() # start a new plot