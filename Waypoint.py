import math


class Waypoint(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Get the distance from given coordinates
    """
    def get_distance_from(self, coords: tuple) -> float:
        return math.sqrt((coords[0] - self.x) ** 2 + (coords[0] - self.y) ** 2)

    """
    Get distance between a given waypoint
    """
    def get_distance_between(self, waypoint) -> float:
        return math.sqrt((self.x - waypoint.x) ** 2 + (self.y - waypoint.y) ** 2)
