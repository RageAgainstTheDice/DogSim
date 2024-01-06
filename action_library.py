import random
import time


def ellipses():
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)


def fetch(name):
    item_list = ['stick', 'ball', 'Stick', 'Ball']
    fetch_prompt = str(input('What would you like to use to fetch? '))
    while fetch_prompt not in item_list:
        print('I\'m sorry, but you cannot play fetch with that item. Please enter a valid item:', end=' ')
        fetch_prompt = str(input())
    print(f'\nYou threw the {fetch_prompt} {random.gauss(100, 50):.2f} feet away.')
    ellipses()
    print(f'\nAfter a bit, {name} came back with the {fetch_prompt}.')


def pat(name, pronoun):
    print(f'You pat {name} on the head.\n{pronoun} seems very pleased now.')
    ellipses()


def give_treat(name, pronoun, fullness, stock):
    if fullness >= 5:
        print(f'{name} cannot eat anymore.')
    elif stock <= 0:
        print(f'It seems you have run out of treats to give to {name}!')
    else:
        print(f'You give {name} a treat.\n{pronoun} happily accepts it, chews it, and swallows it.')
    ellipses()

# note: more actions to come (remember to update action_list in dog_sim in tandem with this module)
