import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x * x


f_output = []
x_list = list(range(-100, 100))
for x in x_list:
  f_output.append(f(x))
pyplot.plot(x_list, f_output)
pyplot.savefig('SquareX.png')
pyplot.close() # start a new plot