from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, ranges
from bokeh.plotting import figure
from bokeh.palettes import Spectral6


def create_gears_render(positions, radii):
    source = ColumnDataSource(data={
        'x': positions,
        'y': [0 for _ in range(len(positions))],
        'colors': Spectral6[:len(positions)],
        'radii': radii
    })
    graph_start = source.data['x'][0] - source.data['radii'][0]
    graph_end = source.data['x'][-1] + source.data['radii'][-1]
    graph_length = graph_end - graph_start
    plot = figure(x_range=ranges.DataRange1d(start=graph_start-graph_length/2, end=graph_end+graph_length/2), width=1750, height=950, active_scroll='wheel_zoom')
    plot.circle(x='x', y='y', radius='radii', fill_color='colors', line_color='colors', source=source)
    plot.x(x='x', y='y', size=10, color='black', source=source)
    tooltip = HoverTool()
    tooltip.tooltips = [('Position', '@x'), ('Radius', '@radii')]
    plot.add_tools(tooltip)
    show(plot)


gears_positions = [4, 30, 50]
radii_set = [[7, 19, 1], [25, 1, 19]]
for radii in radii_set:
    create_gears_render(gears_positions, radii)

gears_positions = [4, 17, 50]
radii_set = [[1, 12, 21], [12, 1, 32]]
for radii in radii_set:
    create_gears_render(gears_positions, radii)
