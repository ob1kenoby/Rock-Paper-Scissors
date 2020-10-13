import random


def write_rating():
    rating_file_out = open('rating.txt', 'w')
    for key in rating.keys():
        rating_file_out.write("{0} {1}\n".format(key, rating[key]))
    rating_file_out.close()


rating_file_in = open('rating.txt', 'r')
rating = {}
for player in rating_file_in:
    temp = player.split()
    rating[temp[0]] = int(temp[1])
rating_file_in.close()

winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

name = input('Enter your name: ')
print("Hello, " + name)
if name not in rating:
    rating[name] = 0

chosen_options = input()
if len(chosen_options) > 0:
    options = chosen_options.split(',')
else:
    options = ('rock', 'paper', 'scissors')

print("Okay, let's start")

while True:
    computer_choice = random.choice(options)

    user_input = input()
    if user_input == '!exit':
        print('Bye!')
        write_rating()
        break
    elif user_input == '!rating':
        print("Your rating: {0}".format(rating[name]))
    elif user_input not in options:
        print("Invalid input")
    elif user_input == computer_choice:
        print("There is a draw ({0})".format(computer_choice))
        rating[name] += 50
    elif user_input in winning_cases[computer_choice]:
        print("Sorry, but the computer chose {0}".format(computer_choice))
    elif user_input not in options:
        print("Invalid input")
    else:
        print("Well done. The computer chose {0} and failed".format(computer_choice))
        rating[name] += 100
