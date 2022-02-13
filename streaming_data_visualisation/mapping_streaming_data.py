from bokeh.plotting import figure, show
from bokeh.models import AjaxDataSource


URL = 'http://127.0.0.1:5000/'

source = AjaxDataSource(data_url=URL, polling_interval=100)
plot = figure()
plot.circle(x='x', y='y', source=source)

# show(plot)

from time import sleep
while True:
    sleep(1)
    print(source.data)
