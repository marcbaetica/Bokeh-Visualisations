import json
from lib.gps_to_web_mercator import transform_gps_to_web_mercator
from lib.load_geojson_data import load_mercator_data_from_file
from bokeh.models import GeoJSONDataSource
from bokeh.palettes import Viridis6
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, CARTODBPOSITRON, ESRI_IMAGERY


# GPS coordinates bounds:
lower_left = (18, 34.5)
upper_right = (27, 42)

# Converting GPS (EPSG:4326) coordinates to Web Mercator (EPSG:3857):
x_1, y_1 = transform_gps_to_web_mercator(lower_left)
x_2, y_2 = transform_gps_to_web_mercator(upper_right)


output_file("5th_century_greek_map.html")
provider = get_provider(ESRI_IMAGERY)

# TODO: Set figure width and height relative to window size.
plot = figure(x_range=(x_1, x_2), y_range=(y_1, y_2), x_axis_type="mercator", y_axis_type="mercator", width=1700, height=950)
plot.add_tile(provider)


# Adding highlight:
spartan_area = json.dumps(load_mercator_data_from_file('sparta'))
spartan_geo_data = GeoJSONDataSource(geojson=spartan_area)
# plot.patches('xs', 'ys', source=spartan_geo_data)
plot.patches('xs', 'ys', fill_alpha=0.5, line_color='white', line_width=0.5, source=spartan_geo_data)


show(plot)
