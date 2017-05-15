class Map(object):
    size = 0
    initial_position = (0, 0)
    waypoint_count = 0

    def __init__(self, size, initial_position: tuple, waypoint_count: int):
        self.size = size
        self.initial_position = initial_position
        self.waypoint_count = waypoint_count