import json
import os
import pathlib
from lib.gps_to_web_mercator import transform_gps_to_web_mercator
from pprintpp import pprint


geojson_folder = 'regions_highlights'


def check_if_geojson_file_exists(file):
    if geojson_folder not in os.listdir():
        raise FileNotFoundError(f'The folder {geojson_folder} does not exist under the current running'
                                f' directory {pathlib.Path.cwd()}. Existing files and folders: {os.listdir()}')
    expected_file = f'{file}.json'
    if expected_file not in os.listdir(geojson_folder):
        raise FileNotFoundError(f'The file {expected_file} does not exist under the expected GeoJSON folder'
                                f' {geojson_folder}. Existing files: {os.listdir(geojson_folder)}')


def load_mercator_data_from_file(file):
    check_if_geojson_file_exists(file)
    uri = f'{geojson_folder}/{file}.json'
    print(f'Loading data from: {uri}')
    with open(uri, 'r') as f:
        data = json.load(f)
    # pprint(data)
    data = convert_gpsjson_coodinates_to_mercator(data)
    # pprint(data)
    return data


def convert_gpsjson_coodinates_to_mercator(data):
    for feature in data['features']:
        for i, coordinate in enumerate(feature['geometry']['coordinates'][0]):
            feature['geometry']['coordinates'][0][i] = transform_gps_to_web_mercator(coordinate)
            # print(i, data, feature['geometry']['coordinates'][0][i])
    return data
