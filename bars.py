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


def get_bars(decoded_data):
    bars = decoded_data['features']
    return bars


def get_biggest_bar(bars):
    biggest_bar = max(
        bars,
        key=lambda k:
        k['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(
        bars,
        key=lambda k:
        k['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bars, longitude, latitude):
    closest_bar = min(
        bars,
        key=lambda k:
        (k['geometry']['coordinates'][0] - longitude) ** 2 +
        (k['geometry']['coordinates'][1] - latitude) ** 2
    )
    return closest_bar


def get_name_bar(bar):
    name_bar = bar['properties']['Attributes']['Name']
    return name_bar


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        help="command - input file")
    parser.add_argument('x', type=float, help="coordinate X")
    parser.add_argument('y', type=float, help="coordinate Y")
    return parser


def print_bar(description, bar):
    print(description, get_name_bar(bar))


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        file_data = load_data(args.file)
        bars = get_bars(file_data)
        print_bar('самый большой бар: ', get_biggest_bar(bars))
        print_bar('самый маленькйи бар: ', get_smallest_bar(bars))
        print_bar('самый ближний бар: ', get_closest_bar(bars, args.x, args.y))
    except ValueError:
        print("not correct format")


if __name__ == '__main__':
    main()
