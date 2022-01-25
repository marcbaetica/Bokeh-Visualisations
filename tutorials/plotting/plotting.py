from bokeh.io import show
from bokeh.plotting import figure

"""
# BASIC PLOT
plot = figure()
show(plot)
"""


#
p = figure(plot_width=400, plot_height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
# add a square renderer with a size, color, alpha, and sizes
p.square([1, 2, 3, 4, 5], [3, 5, 3, 2, 7], size=[10, 15, 20, 25, 30], color="firebrick", alpha=0.6)

# NOTE: All Bokeh scatter markers accept size (measured in screen space units). Circle also has a radius.
show(p)  # show the results



# import bokeh.sampledata
# from pprintpp import pprint
#
# data = bokeh.sampledata.download()



