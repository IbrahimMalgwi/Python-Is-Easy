from random import randint

rand_value = randint(0, 100)

while True:
    guess = int(input("Please enter your guess: "))
    if guess == rand_value:
        break
    elif guess < rand_value:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

print("You guess correctly with: ", guess)
