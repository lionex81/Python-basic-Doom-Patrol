#1
class Vehicle():
    def __init__(self, model, max_speed, mileage):
        """Засiб пересування"""
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage
my_veh = Vehicle('I-van', 120, 20000)

print(f"My Vehicle {my_veh.model} has max_speed {my_veh.max_speed} km/h and it's mileage is {my_veh.mileage} km")
#2
class Bus(Vehicle):
    def __init__(self, model, max_speed, mileage, capacity):
        """Автобус"""
        super().__init__(model, max_speed, mileage)
        self.capacity = capacity

my_bus = Bus('Setra', 150, 20000, 30)
print(f"My bus {my_bus.model} has max_speed {my_bus.max_speed} km/h, it's mileage is {my_bus.mileage} km and it has {my_bus.capacity} seats.")
#3
print(type(my_bus))
#4
school_bus = Bus('Bogdan', 12, 10000, 22)
print(isinstance(school_bus, Vehicle))
#5
class School():
    def __init__(self, name, id, stud_num):
        """Школа(назва, номер школи, к-сть студ."""
        self.name = name
        self.id = id
        self.stud_num = stud_num
my_school = School('Hill', 5, 100)
print(f"school: {my_school.name}, school number {my_school.id}, students: {my_school.stud_num} persons")
#6
class SchoolBus(School, Bus):
    def __init__(self, name, id, stud_num, model, max_speed, mileage, capacity, bus_school_color):
        School.__init__(self, name, id, stud_num)
        Bus.__init__(self, model, max_speed, mileage, capacity)
        self.bus_school_color = bus_school_color
my_school_bus = SchoolBus('Hill', 5, 100, "Setra", 150, 20000, 30, 'yellow')
print(f"My school {my_school_bus.name} has bus {my_school_bus.model} with max_speed {my_school_bus.max_speed} km/h, "
      f"\nit has {my_school_bus.capacity} seats and its color is {my_school_bus.bus_school_color}")
#7
class Bear():
    def __init__(self, age):
        self.age = age
    def make_sound(self):
            print('GRRRRRR')
class Wolf():
    def __init__(self, age):
        self.age = age
    def make_sound(self):
            print('AUUUU')
bear1 = Bear(10)
wolf1 = Wolf(8)
for animal in (bear1, wolf1):
    animal.make_sound()
#8
class City():
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __call__(self):
        if self.population >= 1500:
            return self.name
        else:
            return f'Your city too small'
city1 = City('Hill', 2000)
print(city1.__call__())



