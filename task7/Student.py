class Student:
    def __init__(self, fullname, age, major):
        self.fullname = fullname
        self.age = age
        self.major = major
        print(f'<name: {self.fullname.title()}, age: {str(self.age)}, major: {self.major}>')

Steve = Student('Steven Schultz', 23, 'English')
