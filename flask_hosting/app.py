from flask import Flask, render_template
from bokeh.embed import components
from bokeh.resources import INLINE
from movies_ratings import generate_bokeh_plot

app = Flask('bokeh_graph')

# plot = generate_bokeh_plot()
# script, div = components(plot)
# show(plot)


@app.route('/')
def index():
    plot = generate_bokeh_plot()
    script, div = components(plot)
    return render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),
    ).encode(encoding='UTF-8')


app.run(debug=True)
