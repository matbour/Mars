import random as rd

from Map import Map
from WaypointsPopulation import WaypointsPopulation


class Path(object):
    map = None
    waypoints_population = None

    length = 0
    sequence = []

    def __init__(self, map: Map, waypoints_population: WaypointsPopulation, sequence: list):
        self.map = map
        self.waypoints_population = waypoints_population
        self.sequence = sequence
        self.update_length()

    """
    Update path length
    """
    def update_length(self):
        self.length += self.waypoints_population.waypoints[self.sequence[0]]\
            .get_distance_from(self.map.initial_position)

        for i in range(len(self.sequence) - 2):
            self.length += self.waypoints_population.waypoints[self.sequence[i]]\
                .get_distance_between(self.waypoints_population.waypoints[self.sequence[i + 1]])

    """
    Swap two randomly selected waypoints in the sequence 
    """
    def swap(self):
        i, j = rd.randrange(0, len(self.sequence) - 1), rd.randrange(0, len(self.sequence) - 1)
        self.sequence[i], self.sequence[j] = self.sequence[j], self.sequence[i]
        self.update_length()

    """
    Normalize the path sequence
    """
    def normalize(self):
        new_sequence = []

        for i in self.sequence:
            if i >= len(self.map.waypoint_count):
                continue
            if i not in new_sequence:
                new_sequence.append(i)

        missing_waypoints_ids = []
        for i in range(self.map.waypoint_count - 1):
            if i not in new_sequence:
                missing_waypoints_ids.append(i)

        rd.shuffle(missing_waypoints_ids)

        new_sequence += missing_waypoints_ids

        self.sequence = new_sequence
        self.update_length()
