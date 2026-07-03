#Exercice1
class Pets():
    def __init__(self, animals):
        self.animals = animals
        
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

bengal_obj = Bengal("Thor", 3)
chartreux_obj = Chartreux("Mistigri", 5)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Exercice2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        score_self = self.run_speed() * self.weight
        score_other = other_dog.run_speed() * other_dog.weight
        
        if score_self > score_other:
            return f"{self.name} a gagné le combat contre {other_dog.name} !"
        elif score_other > score_self:
            return f"{other_dog.name} a gagné le combat contre {self.name} !"
        else:
            return f"Le combat entre {self.name} et {other_dog.name} se termine par une égalité !"

dog1 = Dog("Rex", 4, 25)
dog2 = Dog("Max", 2, 15)
dog3 = Dog("Luna", 6, 30)

print(dog1.bark())
print(dog2.bark())

print(f"Vitesse de {dog1.name} : {dog1.run_speed()}")
print(f"Vitesse de {dog2.name} : {dog2.run_speed()}")
print(f"Vitesse de {dog3.name} : {dog3.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))

#Exercice3
import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        score_self = self.run_speed() * self.weight
        score_other = other_dog.run_speed() * other_dog.weight
        if score_self > score_other:
            return f"{self.name} a gagné le combat contre {other_dog.name} !"
        elif score_other > score_self:
            return f"{other_dog.name} a gagné le combat contre {self.name} !"
        else:
            return f"Le combat entre {self.name} et {other_dog.name} se termine par une égalité !"

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name]
        for dog in args:
            if isinstance(dog, Dog):
                names.append(dog.name)
            else:
                names.append(str(dog))
        
        joined_names = ", ".join(names)
        print(f"{joined_names} tous jouent ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            chosen_trick = random.choice(tricks)
            print(f"{self.name} {chosen_trick}")
        else:
            print(f"{self.name} n'est pas encore dressé pour faire des tours...")

dog_parent = Dog("Rex", 4, 25)
pet1 = PetDog("Fido", 2, 10)
pet2 = PetDog("Buddy", 3, 12)

print("Test de do_a_trick() avant entraînement ")
pet1.do_a_trick()

print("\n Test de train() ")
pet1.train()

print("\n Test de do_a_trick() après entraînement ")
pet1.do_a_trick()

print("\n Test de play() avec d'autres chiens ")
pet1.play(pet2, dog_parent, "Max")

#Exercice4
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member found with the name {first_name}.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")