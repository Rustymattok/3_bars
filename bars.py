import json


# 'This method load json and convert it to dictionary format.  '


def load_data(filepath):
    file = open(filepath)
    data = json.load(file)
    return data


# 'This method return the biggest bar(sort by number of seats).  "


def get_biggest_bar(data):
    biggest_bar = max(data["features"],
                      key=lambda k: k
                      ["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar


# 'This method return the smallest bar(sort by number of seats).  "


def get_smallest_bar(data):
    smallest_bar = min(data["features"],
                       key=lambda k:
                       k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar


# 'This method return the closest bar.  "


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data["features"],
                      key=lambda k:
                      (k["geometry"]['coordinates'][0] - longitude) ** 2 +
                      (k["geometry"]['coordinates'][1] - latitude) ** 2)
    return closest_bar


if __name__ == '__main__':
    print(get_biggest_bar(load_data('./bars.json')))
    print(get_smallest_bar(load_data('./bars.json')))
    print(get_closest_bar(load_data('./bars.json'), 37.2, 55.2))
