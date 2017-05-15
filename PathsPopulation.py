import random as rd
from Map import Map
from WaypointsPopulation import WaypointsPopulation
from Path import Path


class PathsPopulation(object):
    map = None
    waypoints_population = None

    count = 0
    probability = 0

    paths = []
    best_list = []

    def __init__(self, map: Map, waypoints_population: WaypointsPopulation, count: int, probability: float):
        self.map = map
        self.waypoints_population = waypoints_population

        self.count = count
        self.probability = probability

        self.gen_paths()

    """
    Generate paths until the count is reached
    """
    def gen_paths(self) -> None:
        ordered_sequence = list(range(self.map.waypoint_count))

        for i in range(self.count - len(self.paths)):
            rd.shuffle(ordered_sequence)
            self.paths.append(Path(self.map, self.waypoints_population, ordered_sequence))

    """
    Evolve the population ; if new population has worse path, revert to the previous one
    Also log the best length in a list for plotting later
    """
    def evolve(self) -> None:
        previous_best = self.best().length
        previous_paths = self.paths.copy()

        self.reduce()
        self.mutate()
        self.gen_paths()

        delta = previous_best - self.best().length

        if delta <= 0:
            self.paths = previous_paths
            self.best_list.append(previous_best)
        else:
            self.best_list.append(self.best().length)

    """
    Order paths based on their length (lowest is the best)
    """
    def order(self) -> None:
        self.paths.sort(key=lambda path: path.length)

    """
    Returns the best path
    """
    def best(self) -> Path:
        self.order()
        return self.paths[0]

    """
    Reduce the paths population to its half
    """
    def reduce(self) -> None:
        self.order()
        self.paths = self.paths[self.count // 2:]

    """
    Mutate paths based on the given probability
    """
    def mutate(self) -> None:
        for i in range(len(self.paths)):
            if rd.random() < self.probability:
                self.paths[i].swap()
        self.order()
