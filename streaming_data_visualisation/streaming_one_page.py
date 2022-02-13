from flask import Flask, jsonify
from jinja2 import Template
import math

from bokeh.plotting import figure
from bokeh.models import AjaxDataSource
from bokeh.embed import components
from bokeh.resources import INLINE


app = Flask(__name__)

x, y = 0, 0


@app.route("/data", methods=['GET', 'OPTIONS'])  # GET only for testing through browser.
def get_x():
    global x, y
    x = x + 0.1
    y = math.sin(x)
    response = jsonify(x=[x], y=[y])
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


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


@app.route("/")
def simple():
    source = AjaxDataSource(data_url="http://localhost:5000/data",
                            polling_interval=1000, mode='append', method='GET')

    fig = figure(title="Streaming Example")
    print(source.data)
    fig.line('x', 'y', source=source)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig, INLINE)

    html = template.render(
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html


app.run(debug=True)
