from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.io import show


# def generate_multi_plot_bar_graph(x, y):
#     source = ColumnDataSource(data={'x':x, 'y':y})
#     plot = figure(x_range=FactorRange(*x), width=1000, title='DSA Performance Results Comparison')
#     plot.vbar(x='x', top='y', width=0.9, source=source)
#     show(plot)


from bokeh.transform import factor_cmap


def generate_multi_plot_bar_graph(x, y):
    source = ColumnDataSource(data={'x':x, 'y':y})
    plot = figure(x_range=FactorRange(*x), width=1000, title='DSA Performance Results Comparison')
    cmap = {
        '1': '#0343df',  # '#ffff14',
        '2': '#e50000',  # '#929591',
    }
    fill_color = factor_cmap('x', palette=list(cmap.values()), factors=list(cmap.keys()), start=1, end=2)
    plot.vbar(x='x', top='y', width=0.9, source=source, fill_color=fill_color, line_color=fill_color)
    show(plot)
