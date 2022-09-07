class Pet:
    def __init__(self, name, age, hunger, playful):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful

    # getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_hunger(self):
        return self.hunger

    def get_playful(self):
        return self.playful

    # Setter
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_hunger(self, hunger):
        self.hunger = hunger

    def set_playful(self, play):
        self.playful = play

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"


class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, favourite_toy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favourite_toy = favourite_toy

    def want_to_play(self):
        if self.playful == True:
            return "Dog wants to play with" + self.favourite_toy
        else:
            return "Dog doesn't want to play"


class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.favourite_place_to_sit = place

    def wants_to_sit(self):
        if self.playful == False:
            print("the cat wants to sit in " + self.favourite_place_to_sit)
        else:
            print("the cat want to play")

    def __str__(self):
        return self.name + " likes to sit in " + self.favourite_place_to_sit


class Human:
    def __init__(self, name, Pets):
        self.name = name
        self.Pets = Pets

    def has_pets(self):
        if len(self.Pets) != 0:
            return "Yes"
        else:
            return "No"


husky_dog = Dog("Snoopy", 5, False, True, "Husky", "stick")
play = husky_dog.want_to_play()
print(play)

husky_dog.playful = False
play = husky_dog.want_to_play()
print(play)

typical_cat = Cat("Fluffy", 3, False, False, "the sun ray")
typical_cat.wants_to_sit()

print(typical_cat)
print(husky_dog)

your_average_human = Human("Alice", [husky_dog, typical_cat])
has_pet = your_average_human.has_pets()

print(has_pet)
print(your_average_human.Pets[0])
print(your_average_human.Pets[1].name)