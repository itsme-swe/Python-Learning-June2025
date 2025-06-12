class Duck:

    def talk(self):
        print("Duck Talking")

    def walk(self):
        print("Duck Walking")


class Dog:

    def talk(self):
        print("Dog Talking")


# 💥 Global Function


def person(pet):
    pet.talk()
    if hasattr(pet, "walk"):
        pet.walk()


dog = Dog()

duck = Duck()

person(dog)  # Dog Talking

person(duck)
