
from abc import ABC, abstractmethod
from typing import Dict
from random import choice, randint
from uuid import uuid4



class Animal(ABC):

    def __init__(self, power: int, speed):#: int
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest):
        pass


class Predator(Animal):

    def __repr__(self):
        return f'{self.__class__.__name__}'


    def eat(self, forest):
        victim = choice(list(forest.animals.values()))  # Choosing  victim
        if victim.id == self.id:

            print(f'The predator did not find the victim')
        else:
            if (self.speed > victim.speed) and (self.current_power > victim.current_power):
                print('Predator eats')
                restore = self.max_power - self.current_power
                current = self.current_power + self.current_power * 0.5
                if current <= self.max_power:
                    print(f'Predator restored {round(self.current_power * 0.5)} power')
                    self.current_power = current

                else:
                    self.current_power = self.max_power
                    print(f'Predator restored {round(restore)}  power')

            else:
                print('Predator did not caught target, both are tired')
                self.current_power = self.current_power - 0.3 * self.current_power
                forest.animals[victim.id].current_power = victim.current_power - 0.3 * victim.current_power


class Herbivorous(Animal):

    def __repr__(self):
        return f'{self.__class__.__name__}'


    def eat(self, forest):
        """
        Herbivorous eats and restores its power by 50%
        """
        print('Herbivorous eats')
        restore = self.max_power - self.current_power
        current = self.current_power + self.current_power * 0.5

        if current <= self.max_power:
         print(f'Herbivorous restored {round(self.current_power * 0.5)} power')
         self.current_power = current

        else:
            self.current_power = self.max_power
            print(f'Herbivorous restored {round(restore)} power')


class Forest:
    AllAnimals = [Herbivorous, Predator]

    def __init__(self):
        self.animals: Dict[str, AllAnimals] = dict()

    def add_animal(self, animal: AllAnimals):
        print(f'A new {animal} has appeared in the forest')
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AllAnimals):
        print(f'Last {animal} is  gone ')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    """
    Generated power, speed and id
    """
    while True:
        generator_animal = choice((Predator(randint(25, 100), randint(25, 100)),
                                   Herbivorous(randint(25, 100), randint(25, 100))))

        generator_animal.id = uuid4()
        yield generator_animal

if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        from time import sleep
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_power < 1 :
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('There are no predators in the forest')
            break

        for animal in forest.animals.values():
            animal.eat(forest)

        sleep(2)
