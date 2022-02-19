from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from random import randint
from subprocess import run


source = ColumnDataSource({
    'x': [i for i in range(10)],
    'y': [randint(1, 10) for _ in range(10)]
})

plot = figure(width=1700)
plot.line(x='x', y='y', source=source)


def update_data():
    global source
    new_y = [randint(1, 10) for _ in range(10)]
    source.data['y'] = new_y


curdoc().add_root(plot)
curdoc().add_periodic_callback(update_data, 2000)

run(['bokeh', 'serve', '--show', 'flask_app_update_data.py'])
