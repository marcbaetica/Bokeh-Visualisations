from flask import Flask, render_template


app = Flask('bokeh_graph')


@app.route('/')
def main_page():
    return render_template('index.html')


app.run(debug=True)
