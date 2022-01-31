
from abc import ABC, abstractmethod
import random

states = {0: 'nothing', 1: 'flowering', 2: 'green', 3: 'red'}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    # def show_the_garden(self):
    #     print(f'There is next vegetables in the Garden: {self.vegetables}\n')
    #     print(f'There is next fruits in the Garden: {self.fruits}\n')
    #     print(f'There is next pests in the Garden: {self.pests}\n')
    #     print(f'Gardener is {self.gardener}\n')

class Vegetables(ABC):
    def __init__(self, states, vegetable_type, name):
        self.states = states
        self.vegetable_type = vegetable_type
        self.name = name

class Tomato(Vegetables):
    def __init__(self, index, vegetable_type, states, name):
        super(Tomato, self).__init__(states, vegetable_type, name)
        self.index = index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        return self.state == 3


    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):

        print(f'{self.vegetable_type} {self.index} is {states[self.state]} ')


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index, 'Red_tomato', states, 'Cherry') for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def is_ripe_all(self): #all([True, True, True]) = True

        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def harvest(self):
        self.tomatoes = []


class Fruit(ABC):
    def __init__(self, states, fruits_type, name):
        self.states = states
        self.fruits_type = fruits_type
        self.name = name

class Apple(Fruit):
    def __init__(self, index, fruits_type, states, name):
        super(Apple, self).__init__(states, fruits_type, name)
        self.index = index
        self.fruits_type = fruits_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        return self.state == 3


    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'{self.fruits_type} {self.index} is {states[self.state]}')


class AppleTree:
    def __init__(self, num):
        self.apples = [Apple(index, 'Golden', states, 'King') for index in range(1, num + 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def is_ripe_all(self):

        return all([apple.is_ripe() for apple in self.apples])

    def harvest(self):
        self.apples = []

class Gardener(ABC):
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    @abstractmethod
    def gardener_harvest(self):
        pass

    @abstractmethod
    def poison_pests(self):
        pass

    @abstractmethod
    def handling(self):
        pass

    @abstractmethod
    def check_states(self):
        pass

class MyGardener(Gardener):
    def __init__(self, name, plants):
        super(MyGardener, self).__init__(name, plants)
        self.name = name
        self.plants = plants

    def gardener_harvest(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.is_ripe_all():
                plant.harvest()
                print(f'Harvesting is finished from {plant.__class__.__name__}.')
            else:
                print('Your plants is not ripe!')

    def handling(self):
        print('Gardner is working...')

        for plant in self.plants:
            plant.grow_all()
        print('Gardner is finished')

    def poison_pests(self):
        pests.quantity = round(pests.quantity / 2)


    def check_states(self):
        for all_plants in self.plants:
                if all_plants == 3:
                    return True
                return False



class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    @abstractmethod
    def eat(self):
        pass

class MyPests(Pests):
    def __init__(self, pests_type, quantity):
        super(MyPests, self).__init__(pests_type, quantity)
        self.pests_type = pests_type
        self.quantity = quantity

    def eat(self):
        if self.quantity == 0:
            print("There are no pests in the garden")
        else:
            plant_type = random.choice(['vegetables', 'fruits'])
            if getattr(garden, plant_type)[0].state > 1:
                if len(getattr(garden, plant_type)) - self.quantity <= 0:
                    print(f"Pests have eaten all the {getattr(garden, plant_type)[0].__class__.__name__}")
                    getattr(garden, plant_type).clear()
                else:
                    print(
                        f"Pests remained after poisoning: {pests.quantity}.\nPests have eaten {self.quantity} {getattr(garden, plant_type)[0].__class__.__name__} "
                        f"and {len(getattr(garden, plant_type)) - self.quantity} {getattr(garden, plant_type)[0].__class__.__name__} remained.")
                    for i in range(0, self.quantity):
                        getattr(garden, plant_type).pop()
            else:
                print(f'Vegetables is not ripe')

if __name__ == '__main__':

    tomato_bush = TomatoBush(12)
    apple_tree = AppleTree(8)
    pests = MyPests('worm', 11)
    bob = MyGardener('Bob', [tomato_bush, apple_tree])
    bob.poison_pests()
    garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=bob)
    #garden.show_the_garden()
    state = bob.check_states()

    for i in range(3):
        bob.handling()
    pests.eat()

    print(f'There are {len(garden.vegetables)} tomatoes and {len(garden.fruits)} apples in the garden')
    bob.gardener_harvest()

