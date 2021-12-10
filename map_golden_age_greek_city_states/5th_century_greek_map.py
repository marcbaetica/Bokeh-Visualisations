from bokeh.plotting import figure, show
from bokeh.tile_providers import get_provider, CARTODBPOSITRON


provider = get_provider(CARTODBPOSITRON)

plot = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000), x_axis_type="mercator", y_axis_type="mercator")
plot.add_tile(provider)

show(plot)
