class House:
    def __init__(self, household_type, total_area):
        self.type = household_type
        self.total_area = total_area
        self.furniture = []
        print(
            "Total area in the", household_type, ':', 
            self.total_area, 'sq m.', end='  '
            )
        print('Furnitures in the', household_type, ':', self.furniture, '\n')

    def add_furniture(self, name, area):
        self.name = name
        self.area = area
        self.total_area = self.total_area - self.area
        self.furniture.append(name)
        print(name, 'has been added to the', self.type)
        print(
            "\nFree area in the", self.type, ':', 
        house.total_area, 'sq m.', end='  '
        )
        print('Furnitures in the', self.type, house.furniture)

house = House('Mansion', 15)
house.add_furniture('Bed', 4)
house.add_furniture('Wardrobe', 2)
house.add_furniture('Table', 1.5)


