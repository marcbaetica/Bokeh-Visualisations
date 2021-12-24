from lib.gps_to_web_mercator import transform_gps_to_web_mercator
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, CARTODBPOSITRON, ESRI_IMAGERY


# GPS coordinates bounds:
lower_left = (20, 43.5)
upper_right = (30, 48.4)

# Converting GPS (EPSG:4326) coordinates to Web Mercator (EPSG:3857):
x_1, y_1 = transform_gps_to_web_mercator(lower_left)
x_2, y_2 = transform_gps_to_web_mercator(upper_right)


output_file("ro_highways.html")
# provider = get_provider(ESRI_IMAGERY)
provider = get_provider(CARTODBPOSITRON)

# TODO: Set figure width and height relative to window size.
plot = figure(x_range=(x_1, x_2), y_range=(y_1, y_2), x_axis_type="mercator", y_axis_type="mercator",
              width=1700, height=950, active_scroll='wheel_zoom')
plot.add_tile(provider)

show(plot)
