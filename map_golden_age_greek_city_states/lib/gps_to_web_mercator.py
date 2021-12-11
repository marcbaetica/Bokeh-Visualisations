# Converting GPS (EPSG:4326) coordinates to Web Mercator (EPSG:3857)


from pyproj import Transformer

TRAN_4326_TO_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857")


def transform_gps_to_web_mercator(position):
    lat, lon = position
    return TRAN_4326_TO_3857.transform(lon, lat)
