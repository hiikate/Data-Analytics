import numpy as np
from numpy import random

guessmade = 0
number = np.random.randint(low=1, high=100)
print('Try to guess your lucky number from 1 to 100')
while guessmade < 3:
    print('Your guess is:')
    guess = input()
    guess = int(guess)
    guessmade = guessmade + 1
    if guess < number:
        print('Your guess is too low!')
    if guess > number:
        print('Your guess is too high!')
    if guess == number:
        break
if guess == number:
    guessmade('Nice! You guessed the lucky number in'+guessmade+'guess!')
if guess != number:
    number = str(number)
    print('Oops! The lucky number was ' +number)

    

