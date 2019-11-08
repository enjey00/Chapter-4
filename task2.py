class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
        print(make, model, year, max_speed)
    
    def take_off(self):
        self.is_flying = True
        print('Самолет взлетел')
    
    def fly(self, km):
        self.odometer = self.odometer + km

    def land(self):
        self.is_flying = False

airplane = Airplane('Jet', 'Business', 2008, 600)
print(f'Одометр самолета: {airplane.odometer}')
print(f'Fly: {airplane.is_flying}')
airplane.take_off()
airplane.fly(45)
print(f'Fly: {airplane.is_flying}')
print(f'Самолет пролетел {airplane.odometer} км и приземлился')
airplane.land()
print(f'Fly :{airplane.is_flying}')

