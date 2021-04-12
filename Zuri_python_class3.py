#CLASS
class car:
    pass
car_1 = car()
car_2 = car()
print(type(car_1))
car_1.name = 'mercedes'
car_2.name = 'Benz'
print(car_1.name)
print(car_2.name)
print()
class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def accel(self):
        print(f'{self.name} accelerate at 100mph')
car_1 = car('mercedes', 'Silver')
car_2 = car('BMW', 'Bkue')
car_1.accel()
car_2.accel()
print()

class Motor:
    """
    This is a car class
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color


    """
    This is the method for my car class
    """
    def accel(self):
        print(f'The {self.color} {self.name} accelerate at 100mph')
Motor_1 = Motor('Toyota', 'Gold')
Motor_2 = Motor('Hyundai', 'Cyan')
Motor_1.accel()
Motor_2.accel()

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def Vehicle(num1, num2):
        return num1 / num2

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num1.vehicle()
