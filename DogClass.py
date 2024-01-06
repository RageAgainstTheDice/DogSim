import random
from action_library import ellipses


class Dog:

    # constructor:

    def __init__(self, name, gender, age, fullness, stock):
        self.name = name
        self.gender = gender
        self.age = age
        self.energy = 21 - age
        self.fullness = fullness
        self.stock = stock

    # getters:

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_pronoun(self):
        if self.gender == 'male':
            return 'he'
        else:
            return 'she'

    def get_age(self):
        return self.age

    def get_energy(self):
        return self.energy

    def get_fullness(self):
        return self.fullness

    def get_stock(self):
        return self.stock

    # setters:

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_energy(self, age):
        self.energy = 21 - age

    def set_fullness(self, fullness):
        self.fullness = fullness

    def set_stock(self, stock):
        self.stock = stock

    # actions

    def fetch(self):
        item_list = ['stick', 'ball', 'Stick', 'Ball']
        fetch_prompt = str(input('What would you like to use to fetch? '))
        while fetch_prompt not in item_list:
            print('I\'m sorry, but you cannot play fetch with that item. Please enter a valid item:', end=' ')
            fetch_prompt = str(input())
        print(f'\nYou threw the {fetch_prompt} {random.gauss(100, 50):.2f} feet away.')
        ellipses()
        print(f'\nAfter a bit, {self.get_name()} came back with the {fetch_prompt}.')

    def pat(self):
        print(f'You pat {self.get_name()} on the head.\n{self.get_pronoun()} seems very pleased now.')
        ellipses()

    def give_treat(self):
        if self.get_fullness() >= 5:
            print(f'{self.get_name()} cannot eat anymore.')
        elif self.get_stock() <= 0:
            print(f'It seems you have run out of treats to give to {self.get_name()}!')
        else:
            print(f'You give {self.get_name()} a treat.\n{self.get_pronoun()} happily accepts it, chews it, and '
                  f'swallows it.')
        ellipses()
