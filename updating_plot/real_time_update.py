from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc, show
from functools import partial
from random import choice
from threading import Thread
from time import sleep


Popen(f'bokeh serve --show {__file__}')

doc = curdoc()


y = [0, 0, 0]
x = list(range(1, len(y)+1))
data_source = ColumnDataSource(data=dict(x=x, y=y))

p = figure()
p.vbar(x='x', top='y', source=data_source, width=0.8)
doc.add_root(p)


def non_blocking_new_data():
    while all([item < 50 for item in y]):
        index = choice([0, 1, 2])
        y[index] = y[index] + choice(list(range(1, 4)))
        # This gets called only when there has been some change on the data source. Its purpose is to update the table.
        doc.add_next_tick_callback(callback=partial(update_plot, x, y))
        print(data_source.data)
        sleep(0.25)
        print([item < 50 for item in y])


# from tornado import gen
# @gen.coroutine
def update_plot(x, y):
    data_source.stream(new_data=dict(x=x, y=y), rollover=3)
    # TODO: Convert to patch instead -> rollover doesn't make sense in this example's context.


thread = Thread(target=non_blocking_new_data)
thread.start()
