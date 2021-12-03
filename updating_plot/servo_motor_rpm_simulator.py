# RPM capped between 3k and 5k.
# Starting RPM at 4k.
# Increments or decrements between 3 and 10 rotations every quarter of a second.


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc
from functools import partial
from random import choice
from threading import Thread
from time import sleep


UPPER_LIMIT = 5000
LOWER_LIMIT = 3000
CURRENT_RPM = 4000
TIME_SERIES_POINT = 0
TIME_INCREMENT = 0.1


def instantiate_graph():
    source = ColumnDataSource(dict(x=[TIME_SERIES_POINT], y=[CURRENT_RPM]))
    doc = curdoc()
    plot = figure(width=1500, height=500)
    plot.line(x='x', y='y', source=source)
    doc.add_root(plot)
    return doc, source


def update_document(new_rpm_value, source):
    # print(source.data)
    print(100/TIME_INCREMENT, type(100/TIME_INCREMENT))
    rollover = int(100/TIME_INCREMENT) # TODO: Float to int rounds value. Need to make sure sampling is accurate.
    source.stream(new_data=dict(x=[source.data['x'][-1]+TIME_INCREMENT], y=[new_rpm_value]), rollover=rollover)


def change_rpm_by(value):
    global CURRENT_RPM
    if CURRENT_RPM + value < LOWER_LIMIT:
        CURRENT_RPM = 3000
    elif CURRENT_RPM + value > UPPER_LIMIT:
        CURRENT_RPM = 5000
    else:
        CURRENT_RPM = CURRENT_RPM + value


def run_motor_sim_and_update_doc(doc, source):
    while True:
        rpm_change_value = choice([i for i in range(3, 31)])
        rpm_change_direction = choice([-1, 1])
        change_rpm_by(rpm_change_value * rpm_change_direction)
        print(f'New RPM is: {CURRENT_RPM}')
        doc.add_next_tick_callback(partial(update_document, CURRENT_RPM, source))
        sleep(TIME_INCREMENT)


document, source = instantiate_graph()
thread = Thread(target=partial(run_motor_sim_and_update_doc, document, source))
thread.start()


# TODO: On server shutdown, kill the process.
