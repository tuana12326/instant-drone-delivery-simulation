class Drone:
    def __init__(self, drone_id, x, y, battery):
        self.drone_id = drone_id
        self.x = x
        self.y = y
        self.battery = battery
        self.available = True

    def distance_to(self, target_x, target_y):
        return ((self.x - target_x) ** 2 + (self.y - target_y) ** 2) ** 0.5
