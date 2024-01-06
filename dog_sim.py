import random
import action_library
import list_library  # (remember that list_library.breed_list is incomplete)
import status_library  # (remember that some states still need to be defined and implemented)
from edit_distance import distance

print('\nWelcome to my text-based dog sim game!')
print('(Note: when entering information about your dog\'s breed, make sure to follow typical English title '
      'capitalization rules.)\n')
while True:
    dog_name = str(input('What is your dog\'s name? '))
    gender_names = ['male', 'female']
    acceptable_responses_gender = gender_names + ['choose for me']
    dog_gender = str(input('What gender is your dog? (If you can\'t decide, type "choose for me.") '))
    while dog_gender not in acceptable_responses_gender:
        print(f'Please enter a valid response:', end=' ')
        dog_gender = str(input())
    else:
        if dog_gender == 'choose for me':
            dog_gender = random.choice(gender_names)
    dog_pronoun = ''
    dog_pronoun_caps = ''
    if dog_gender == 'male':
        dog_pronoun = 'he'
        dog_pronoun_caps = 'He'
    elif dog_gender == 'female':
        dog_pronoun = 'she'
        dog_pronoun_caps = 'She'
    acceptable_responses_age = list_library.age_range + ['choose for me']
    dog_age = input('How old is your dog? (If you can\'t decide, type "choose for me.") ')
    while dog_age not in acceptable_responses_age:
        print('The dog\'s age must be between zero and twenty years. Please enter an appropriate value:', end=' ')
        dog_age = input()
    else:
        if dog_age == 'choose for me':
            dog_age = random.randrange(21)
    dog_breed = str(input('What breed is your dog? (If you can\'t decide, type "choose for me.") '))
    acceptable_responses_breed = list_library.breed_list + ['choose for me']
    while dog_breed not in acceptable_responses_breed:
        print(f'"{dog_breed}" is not a registered breed.', end=' ')
        for breed in list_library.breed_list:
            if distance(breed, dog_breed) < 3:
                print(f'Could you have possibly meant "{breed}?" If so, then please type it out:', end=' ')
                break
        else:
            print('Please enter an existing dog breed:', end=' ')
        dog_breed = str(input())
    else:
        if dog_breed == 'choose for me':
            dog_breed = random.choice(list_library.breed_list)
    print()
    confirmation = input(f'So your dog is a {dog_age}-year old {dog_gender} {dog_breed} named {dog_name}. Would you '
                         f'like to proceed with these choices? ')
    while confirmation not in list_library.valid_responses:
        print('Please enter either an affirmative or a negative response:', end=' ')
        confirmation = input()
    else:
        if confirmation in list_library.negative_responses:
            print('Okay, I\'ll let you reënter the information from scratch.\n')
            continue
        else:
            print(f'Great! Let\'s start interacting with {dog_name} then!\n')
    break
status_list = ['upright', 'sitting', 'reclining', 'asleep', 'exhausted']
action_list = ['fetch', 'pat', 'give treat']
# note: more actions to come (remember to update action_library in tandem with this list.)
dog_energy = 21 - int(dog_age)
dog_fullness = 0
treat_stock = 5
dog_status = status_library.upright()
while True:
    action_prompt = str(input(f'What would you like to do with {dog_name}? '))
    while action_prompt not in action_list:
        print(f'{dog_name} doesn\'t seem to understand that. Try something else!', end=' ')
        action_prompt = str(input())
    else:
        if action_prompt == action_list[0]:
            action_library.fetch(dog_name)
            dog_energy -= 1
            dog_fullness -= 1
        elif action_prompt == action_list[1]:
            action_library.pat(dog_name, dog_pronoun_caps)
        elif action_prompt == action_list[2]:
            action_library.give_treat(dog_name, dog_pronoun_caps, dog_fullness, treat_stock)
            dog_energy += 1
            dog_fullness += 1
            treat_stock -= 1
    if dog_energy <= 0:
        dog_status = status_library.exhausted(dog_name, dog_pronoun)
        break
    else:
        print(f'\n{dog_name} patiently anticipates what you will do next.')
    continuation = input(f'Would you like to do anything else with {dog_name}? ')
    while continuation not in list_library.valid_responses:
        print('Please enter either an affirmative or a negative response:', end=' ')
        continuation = input()
    else:
        if continuation in list_library.affirmative_responses:
            if dog_status == status_library.asleep():
                dog_energy += 1
                dog_fullness -= 1
            continue
        else:
            print('Okay, see you next time. Goodbye!')
    break
print(end='')
