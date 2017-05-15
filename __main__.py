from Map import Map
from WaypointsPopulation import WaypointsPopulation
from PathsPopulation import PathsPopulation
import matplotlib.pyplot as plt

# Configuration
size = 500
initial_position = (0, 0)
waypoint_count = 20
paths_count = 50
probability = 0.1
generations = 1000

map = Map(size, initial_position, waypoint_count)
waypoints_population = WaypointsPopulation(map)
paths_population = PathsPopulation(map, waypoints_population, paths_count, probability)

for i in range(generations):
    paths_population.evolve()

plt.plot(paths_population.best_list)
plt.xlabel('Generation')
plt.ylabel('Best path length')
plt.show()
