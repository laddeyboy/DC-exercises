import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    if(x % 2 == 0):
        return -1
    else:
        return 1



f_output = []
x_list = list(range(-5, 6))
for x in x_list:
  f_output.append(f(x))
pyplot.bar(x_list, f_output)
pyplot.savefig('OddEven.png')
pyplot.close() # start a new plot