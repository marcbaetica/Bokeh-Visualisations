import json
from lib.gps_to_web_mercator import transform_gps_to_web_mercator
from lib.load_geojson_data import load_mercator_data_from_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper
)
from bokeh.palettes import Viridis6
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, CARTODBPOSITRON, ESRI_IMAGERY


# Adding GeoJSON highlights:
# TODO: Mark properties' colors. Maybe add them straight into json file?
geo_source = GeoJSONDataSource(geojson=json.dumps(load_mercator_data_from_file('sparta')))
color_mapper = LinearColorMapper(palette=Viridis6)

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

plot = figure(title="Argentina", tools=TOOLS, x_axis_location=None, y_axis_location=None, width=500, height=300)
plot.grid.grid_line_color = None

plot.patches('xs', 'ys', fill_alpha=0.7, line_color='white', line_width=0.5, source=geo_source)

hover = plot.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Provincia:", "@provincia")]

output_file("PBIar.html", title="Testing islands in bokeh")

show(plot)
