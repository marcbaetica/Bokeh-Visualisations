from bokeh.embed import components
from bokeh.plotting import figure, curdoc
from bokeh.resources import INLINE
from bokeh.models import ColumnDataSource
from flask import Flask, render_template
from random import randint
from subprocess import run


app = Flask(__name__)


@app.route('/')
def index():
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

    script, div = components(plot)
    return render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),
    ).encode(encoding='UTF-8')


# run(['bokeh', 'serve', '--show', 'flask_app_update_data.py'])
app.run(debug=True)
