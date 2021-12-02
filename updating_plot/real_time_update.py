from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc, show
from functools import partial
from random import choice
from threading import Thread
from time import sleep


increment_amount = [i for i in range(1, 4)]
print(increment_amount)

x = [1, 2, 3]
y = [1, 1, 1]

doc = curdoc()
source = ColumnDataSource(data=dict(x=x, y=y))


def non_blocking_new_data():
    while all([item < 50 for item in y]):
        index = choice([0, 1, 2])
        y[index] = y[index] + choice(increment_amount)
        # This gets called only when there has been some change on the data source. Its purpose is to update the table.
        doc.add_next_tick_callback(callback=partial(update_plot, x, y))
        print(source.data)
        sleep(0.25)
        print([item < 50 for item in y])


# from tornado import gen
# @gen.coroutine
def update_plot(x, y):
    source.stream(new_data=dict(x=x, y=y), rollover=3)


p = figure()
p.vbar(x='x', top='y', source=source, width=0.8)
doc.add_root(p)


thread = Thread(target=non_blocking_new_data)
thread.start()


# bokeh serve --show updating_plot\real_time_update.py
