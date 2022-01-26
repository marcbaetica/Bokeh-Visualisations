from bokeh.io import show
from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


def generate_multi_plot_bar_graph(x, y):
    source = ColumnDataSource(data={'x': x, 'y': y})
    plot = figure(x_range=FactorRange(*x), width=1000, title='DSA Performance Results Comparison')
    cmap = {
        '1': '#0343df',
        '2': '#e50000',
    }
    fill_color = factor_cmap('x', palette=list(cmap.values()), factors=list(cmap.keys()), start=1, end=2)
    plot.vbar(x='x', top='y', width=0.9, source=source, fill_color=fill_color, line_color=fill_color)
    hover = HoverTool(tooltips=[('Seconds', '@y')])
    plot.add_tools(hover)
    show(plot)
