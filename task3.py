print('Сколько километров Вы хотите проехать?')
num = int(input())
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def drive(self, km):
        if km <= 700:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Let's drive!!\n")

        else:
            print("Need more fuel,please, fill more!\n")

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, km):
        km = km/10
        self.fuel -= km

car1 = Car('Toyota', 'ipsum', 2003)
print("\nBefore driving: ", car1.odometer, 'km')
print("Before driving: ", car1.fuel, 'l', '\n')
car1.drive(num)
print("After driving: ", car1.odometer, 'km')
print("After driving", car1.fuel, 'l')
