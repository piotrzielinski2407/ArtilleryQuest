import random
import statistics
import json


def wind_gen():
    """
    Generator that will simulate wind behaviour, returning value from selected boundaries in m/s.
    """
    with open("physics_variables.json", "r") as json_file:
        file = json.load(json_file)
        boundaries = file["wind_boundaries"]

    def wind_tick(wind_boundaries):
        wind_tick_value = (random.random()*2 - 1)*wind_boundaries
        return wind_tick_value

    mean_len = 5
    wind = []

    for _ in range(mean_len):
        wind.append(wind_tick(boundaries))

    while True:
        wind.append(wind_tick(boundaries))
        wind.pop(0)
        yield statistics.mean(wind)
        # wind speed as float number, negative values for wind in -x direction, positive in +x dir.


if __name__ == "__main__":
    wind_object = wind_gen()
    for _ in range(10):
        print(wind_object.__next__())
