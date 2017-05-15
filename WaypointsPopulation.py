import random as rd
from Map import Map
from Waypoint import Waypoint


class WaypointsPopulation(object):
    waypoints = []

    def __init__(self, map: Map):
        self.map = map
        self.gen_waypoints()

    """
    Generate a random waypoint
    """
    def gen_waypoint(self) -> Waypoint:
        return Waypoint(rd.randrange(0, self.map.size), rd.randrange(0, self.map.size))

    """
    Generate random UNIQUE waypoints
    """
    def gen_waypoints(self) -> None:
        for i in range(self.map.waypoint_count):
            waypoint = self.gen_waypoint()

            while waypoint in self.waypoints:
                waypoint = self.gen_waypoint()

            self.waypoints.append(waypoint)

    """
    Generate the distance matrix
    """
    def gen_matrix(self):
        matrix = [[0] * (self.map.size + 1)] * (self.map.size + 1)

        for i in range(self.map.size):
            for j in range(self.map.size):
                matrix[i][j] = self.waypoints[i].get_distance_between(self.waypoints[j])

        for i in range(self.map.size):
            matrix[self.map.size][i] = matrix[self.map.size][i] = self.waypoints[i]\
                .get_distance_from(self.map.initial_position)
