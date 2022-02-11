from flask import Flask, render_template
from bokeh.resources import INLINE
from bokeh.embed import components

app = Flask('bokeh_graph')


# @app.route('/')
# def main_page():
#     return render_template('index.html')

script, div = components(fig)

@app.route('/')
def main_page():
    return render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),
    ).encode(encoding='UTF-8')


app.run(debug=True)
