#سوال 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"name: {self.name}, hoghogh: {self.salary} toman")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"name: {self.name}, hoghogh: {self.salary} toman, bakhsh: {self.department}")

    def give_raise(self, employee, percent):
        increase = employee.salary * (percent / 100)
        employee.salary += increase
        print(f"hoghogh {employee.name} in andaze {percent}% afzayesh yaft.")


e1 = Employee("ali", 8000000)
e2 = Employee("amir", 9000000)
e3 = Employee("shayan", 7000000)

m1 = Manager("hanie", 15000000, "forosh")

m1.give_raise(e2, 10)

employees = [e1, e2, e3, m1]

print("\n etelaat")
for person in employees:
    person.show_info()



#سوال 2
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("motor roshan shod")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        print(f" motor mashin {self.brand} roshan shod!")


class Motor(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def start_engine(self):
        print(f"motorsiclet {self.brand} ba noe {self.type} roshan shod!")


car1 = Car("pegout", "panaroma 207", 2022, 4)
motor1 = Motor("dena", "automat", 2023, "sport")

car1.start_engine()
motor1.start_engine()



#سوال 3
class Shape:
    def area(self):
        print("")

    def perimeter(self):
        print("")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


s = Square(5)
c = Circle(3)

print("squer:")
print("masahat:", s.area())
print("mohit:", s.perimeter())

print("\n dayere:")
print("masahat:", c.area())
print("mohit:", c.perimeter())
