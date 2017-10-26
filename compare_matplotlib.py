"""
Sample commands for a simple comparison of matplotlib.pyplot with bokeh.figure
"""

# make some x and y points
import numpy as np
x = np.arange(0.0, 2.0*np.pi, 0.01*np.pi)
y = np.sin(x)

# plot a line with matplotlib.pyplot
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# plot a line with bokeh.plotting
from bokeh.plotting import figure
from bokeh.io import show, output_file
output_file('sample.html')
fig = figure()
fig.line(x,y)
show(fig)


# scatterplot with matplotlib.pyplot
fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()

# scatterplot with bokeh.plotting
fig = figure()
fig.circle(x,y)
show(fig)
