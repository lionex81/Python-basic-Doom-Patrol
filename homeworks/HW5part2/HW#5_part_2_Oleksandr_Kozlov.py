#1 Composition
class Laptop():
    def __init__(self):
        battery = Battery("This is HP laptop battery(capacity 2300mAh)")
        self.battery = battery

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

laptop = Laptop()
print(laptop.battery.capacity)

#2 Agregation
class Guitar():
    def __init__(self, string):

        self.string = string

class String:
    def __init__(self):
        pass

string = String()
guitar = Guitar(string)

#3 class Calc
class Calc():
    @staticmethod
    def add_num(a, b, c):
     return a+b+c
Calc.add_nums = staticmethod(Calc.add_num)
#sum = Calc.add_num(4,6,8)
print(Calc.add_num(4,6,8))

#4 Pasta
class Pasta():
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pasta({self.ingredients!r})'
    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])
x = Pasta.carbonara()
y = Pasta.bolognaise()
print(x,y)


#5 Concert
class Concert():
     max_visitors_num = 0
     def __init__(self):
         self._visitors_count = 0

     @property
     def visitors_count(self):
         return self._visitors_count

     @visitors_count.setter
     def visitors_count(self, value):
         if value > self.max_visitors_num:
             self._visitors_count = self.max_visitors_num

x = Concert()
x.max_visitors_num = 50
x.visitors_count = 1000
print(x.visitors_count)

#6 AddressBookDataClass
import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

my_address = AddressBookDataClass(key= 123456, name= "Lex", phone_number= '2345678',
                                  address= 'Ukraine', email= 'lex@ukr.net', birthday= '16.04.81', age= 40)
print(my_address)

#7 using NamedTuple
from collections import namedtuple
AddressBookDataClassNT = namedtuple('AddressBookDataClassNT', ['key','name','phone', 'address', 'email'])
my_addressNT = AddressBookDataClassNT(123456, 'Lex', 2345678, 'Ukraine', 'lex@ukr.net')
print(my_addressNT[0])
print(my_addressNT.name)

#8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"addressbook {self.key}, {self.name}, {self.phone_number}, {self.address}, " \
               f"{self.email}, {self.birthday},{self.age}"

addressbook = AddressBook(key=123456, name= 'Lex', phone_number=2345678, address='Ukraine', email='lex@ukr.net',
                          birthday='16.04.81', age=40)
print(addressbook)

#9
class Person():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def person_age(self):
        return self.age

    @person_age.setter
    def person_age(self, value):
        self.age = value

person = Person('John', 36, 'USA')
#print(person.age)
person.person_age = 40
print(person.age)


#10
class Student():
    id = 0
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(1, 'Lex')
#print(student.id)
#print(student.name)
setattr(student, 'email', 'lex@ukr.net')
print(getattr(student, 'email'))

#11
class Celsius():
    def __init__(self, temp = 0):
        self._temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, fahr):
        self._temp = fahr

fahr_temp = Celsius(36)
fahr_temp.temp = fahr_temp.temp * 1.8 +32
print(fahr_temp.temp)














