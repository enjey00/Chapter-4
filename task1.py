class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
            print(
                self.name + ' ' + self.lastname + ' поступил в ' + 
                str(self.year_of_entrance) + ' году на факультет: ' 
                + self.department
            )

student1 = Student('Zhenishbek', 'Azimkanov', 'Python', 2019)
student1.get_student_info()