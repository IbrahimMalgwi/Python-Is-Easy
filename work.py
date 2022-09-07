import random

randInt = random.randint(0, 10)
print(randInt)

randFloat = random.random ()
print(randFloat)

randUniform = random.uniform(1, 11000)
print(randUniform)

simple_list = [1, 3, 6, 7, 11]
pick_element = random.choice(simple_list)
print(pick_element)
print(simple_list)
random.shuffle(simple_list)
print(simple_list)