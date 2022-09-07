from random import random

rand_val = random()
print(rand_val)

upper = 1.0
lower = 0.00
guess = 0.5

while True:
    if guess == rand_val:
        break
    elif guess < rand_val:
        lower = guess
    else:
        upper = guess
    guess = (upper + lower) / 2

print(guess)