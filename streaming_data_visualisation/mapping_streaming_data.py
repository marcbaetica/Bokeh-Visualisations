from bokeh.embed import components
from bokeh.models import AjaxDataSource
from bokeh.plotting import figure
from bokeh.resources import INLINE
from flask import Flask, redirect
from jinja2 import Template


URL = 'http://127.0.0.1:5000/random-number-generator'

template = Template('''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Streaming Example</title>
        {{ js_resources }}
        {{ css_resources }}
    </head>
    <body>
    {{ plot_div }}
    {{ plot_script }}
    </body>
</html>
''')

app = Flask(__name__)


@app.route('/')
def redirect_to_plot():
    return redirect('bokeh-plot')


@app.route('/bokeh-plot')
def draw_plot():
    source = AjaxDataSource(data_url=URL, polling_interval=200, method='GET')
    plot = figure(x_range=(-1, 6), y_range=(-1, 22))
    plot.circle(x='x', y='y', source=source, radius=0.4)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(plot, INLINE)

    html = template.render(
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html


app.run(port=5001)
