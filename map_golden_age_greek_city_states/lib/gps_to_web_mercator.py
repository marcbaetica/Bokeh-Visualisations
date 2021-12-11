# Converting GPS (EPSG:4326) coordinates to Web Mercator (EPSG:3857)

import unittest
from pyproj import Transformer


TRAN_4326_TO_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857")


def transform_gps_to_web_mercator(position):
    lat, lon = position
    return TRAN_4326_TO_3857.transform(lon, lat)


if __name__ == '__main__':
    class TestTransformationResult(unittest.TestCase):
        def test_correct_transformation_results(self):
            point1_gps = (18, 34.5)
            point1_expected_gps_mercator = (2003750.8342789242, 4096139.0404472337)
            point2_gps = (27, 42)
            point2_expected_gps_mercator = (3005626.251418386, 5160979.444049781)

            point1_web_mercator = transform_gps_to_web_mercator(point1_gps)
            self.assertEqual(point1_web_mercator, point1_expected_gps_mercator)
            point2_web_mercator = transform_gps_to_web_mercator(point2_gps)
            self.assertEqual(point2_web_mercator, point2_expected_gps_mercator)

    unittest.main()
