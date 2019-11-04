import json


# 'Parameter for coordinate system.  '


POS_X = 37.2
POS_Y = 55.2


# 'This method load json and convert it to dictionary format.  '


def load_data(filepath):
    file_json = open(filepath)
    bars_list = json.load(file_json)
    return bars_list


# 'This method return the biggest bar(sort by number of seats).  "


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list["features"],
                      key=lambda k:
                      k["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar


# 'This method return the smallest bar(sort by number of seats).  "


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list["features"],
                       key=lambda k:
                       k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar


# 'This method return the closest bar.  "


def get_closest_bar(bars_list, longitude, latitude):
    closest_bar = min(bars_list["features"],
                      key=lambda k:
                      (k["geometry"]['coordinates'][0] - longitude) ** 2 +
                      (k["geometry"]['coordinates'][1] - latitude) ** 2)
    return closest_bar


if __name__ == '__main__':
    print(get_biggest_bar(load_data('./bars.json')))
    print(get_smallest_bar(load_data('./bars.json')))
    print(get_closest_bar(load_data('./bars.json'), POS_X, POS_Y))
