import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x + 1


f_output = []
x_list = list(range(-3, 5))
for x in x_list:
  f_output.append(f(x))
pyplot.plot(x_list, f_output)
pyplot.savefig('XplusOne.png')
pyplot.close() # start a new plot