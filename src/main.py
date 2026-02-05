from drone import Drone
from order import Order
from dispatcher import assign_drone
from security import validate_command

drones = [
    Drone(1, 0, 0, 80),
    Drone(2, 5, 5, 50),
    Drone(3, 10, 10, 20)
]

order = Order(101, 3, 4, priority=1)

if validate_command("CONTROL_CENTER"):
    assigned = assign_drone(drones, order)
    if assigned:
        print(f"Order {order.order_id} assigned to Drone {assigned.drone_id}")
    else:
        print("No available drone!")
else:
    print("Unauthorized command detected!")
