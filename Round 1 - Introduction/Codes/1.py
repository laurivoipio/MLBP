#Important libraries to import:
# NumPy: is the fundamental package for scientific computing with Python.
# matplotlib.pyplot: provides a MATLAB-like plotting framework.

import matplotlib.pyplot as plt #define shorthand "plt" for package matlobplit.pyplot
import numpy as np #define shorthand "np" for the numpy package 
from scipy.misc import derivative
import math

def example_func(x):
    f_x = 1/(1+np.exp(-x))
    return f_x

range_x = np.arange(-6 , 6 , 0.01)

f_x = np.empty(len(range_x))

for i in range(len(range_x)):
    f_x[i] = example_func(range_x[i])

### STUDENT TASK ###
#1) plot the results, for example use plot function in matplotlib.pyplot. 
# Remember to show() the plot.
# YOUR CODE HERE
f, ax = plt.subplots()
ax.plot(range_x, f_x, label="plot")
ax.set_title("Result")

#raise NotImplementedError()
### STUDENT TASK ###
#2) find the first derivative of the mentioned function and plot it
# YOUR CODE HERE
g_x = np.empty(len(range_x))
g_x = np.gradient(example_func(range_x))
print(g_x)
#for i in range(len(range_x)):
 #   g_x[i] = np.gradient(example_func(range_x[i]))
ax.plot(range_x, g_x)
plt.show()
#raise NotImplementedError()