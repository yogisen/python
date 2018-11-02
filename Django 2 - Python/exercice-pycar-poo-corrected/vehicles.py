category_car = 'Car'
category_motorcycle = 'Motorcycle'


class Vehicle:
    def __init__(self, category, price):
        self.category = category
        self.price = price

    def honk(self):
        pass

    def __str__(self):
        return '{}, {}€'.format(self.category, self.price)


class Car(Vehicle):
    def __init__(self, price):
        super().__init__(category_car, price)

    def honk(self):
        print("Pouet!")


class Motorcycle(Vehicle):
    def __init__(self, price):
        super().__init__(category_motorcycle, price)

    def honk(self):
        print("Tsouin!")
