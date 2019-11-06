import json


def load_data(filepath):
    with open(filepath) as f:
        json_string = f.read()
        json_list = json.loads(json_string)
    return json_list


def get_biggest_bar(json_list):
    biggest_bar = max(
        json_list["features"],
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar  # max value SeatsCount in json list.


def get_smallest_bar(json_list):
    smallest_bar = min(
        json_list["features"],
        key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar  # min value SeatsCount in json list.


def get_closest_bar(json_list, longitude, latitude):
    closest_bar = min(
        json_list["features"], key=lambda k:
        (k["geometry"]['coordinates'][0] - longitude) ** 2 +
        (k["geometry"]['coordinates'][1] - latitude) ** 2)
    return closest_bar  # closest bar by value of coordinates.


def main():
    filepath = input('enter file way: ')
    if filepath[-5:len(filepath)] != '.json':  # for format .json
        print('not correct format')
        return
    pos_x = input('enter your position X: ')
    pos_y = input('enter your position y: ')
    try:
        json_list = load_data(filepath)
        print(get_biggest_bar(json_list))
        print(get_smallest_bar(json_list))
        print(get_closest_bar(json_list, float(pos_x), float(pos_y)))
    except FileNotFoundError:
        print("not found file")


if __name__ == '__main__':
    main()
