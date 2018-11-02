from pycar import rental


def rent(vehicle_category):
    vehicle = rental.rent(vehicle_category)
    print("You rented a", vehicle)
    vehicle.honk()

    return vehicle.price


total_price = 0
run = True
while run:
    action = input("What do you want to do? ")

    if action == 'list':
        print('Available vehicle categories:', rental.vehicle_categories)
    elif action.startswith('rent'):
        _, category = action.split(' ')
        total_price += rent(category)
    elif action == 'exit':
        run = False

print("Thank you for your purchase of {}€".format(total_price))
