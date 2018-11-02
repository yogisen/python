from pycar import vehicles

vehicle_categories = (vehicles.category_car, vehicles.category_motorcycle,)


def rent(vehicle_category):
    if vehicle_category == vehicles.category_car:
        return vehicles.Car(10000)
    elif vehicle_category == vehicles.category_motorcycle:
        return vehicles.Motorcycle(5000)
