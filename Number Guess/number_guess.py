from random import randint
import time
num = None
def number_guess(num):
    num = randint(1, 1000)
    print('I\'m going to think of a number between 1 and 1000')
    while True:
        try:
            guess = input('\nTry to guess the number. ')
            guess = int(guess)
            if guess > num:
                print('Your guess is too high.')
            elif guess < num:
                print('Your guess is too low.')
            elif guess == num:
                print('Good Job! You guessed the number correctly!')
                time.sleep(5)
                break
        except ValueError:
            print('\nERROR: Numbers only\n')

number_guess(num)
