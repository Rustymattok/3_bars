import json
import os
import argparse


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        data_string = file_handler.read()
        decoded_data = json.loads(data_string)
    return decoded_data


def get_biggest_bar(decoded_data):
    biggest_bar = max(
        decoded_data["features"],
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    encoded_biggest_bar = json.dumps(biggest_bar,
                                     ensure_ascii=False, indent=4)
    return encoded_biggest_bar


def get_smallest_bar(decoded_data):
    smallest_bar = min(
        decoded_data["features"],
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    encoded_smallest_bar = json.dumps(smallest_bar,
                                      ensure_ascii=False, indent=4)
    return encoded_smallest_bar


def get_closest_bar(decoded_data, longitude, latitude):
    closest_bar = min(
        decoded_data["features"], key=lambda k:
        (k["geometry"]['coordinates'][0] - longitude) ** 2 +
        (k["geometry"]['coordinates'][1] - latitude) ** 2)
    encoded_closest_bar = json.dumps(closest_bar,
                                     ensure_ascii=False, indent=4)
    return encoded_closest_bar


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        help="command - input file")
    parser.add_argument('x', type=float, help="coordinate X")
    parser.add_argument('y', type=float, help="coordinate Y")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    try:
        file_name = load_data(args.file)
        print("the biggest bar: " + '\n'
              + get_biggest_bar(file_name))
        print("the smallest bar: " + '\n'
              + get_smallest_bar(file_name))
        print("the closest bar: " + '\n'
              + get_closest_bar(file_name, args.x, args.y))
    except ValueError:
        print("not correct format")
