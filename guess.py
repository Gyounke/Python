import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('wrong mf, too low ')
        elif guess > random_number:
            print('wrong too high')
    print('yay GG BG WP')
        
guess(10)