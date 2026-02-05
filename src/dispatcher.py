def assign_drone(drones, order):
    candidates = []

    for drone in drones:
        if drone.available and drone.battery > 30:
            distance = drone.distance_to(order.x, order.y)
            candidates.append((distance, drone))

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]
