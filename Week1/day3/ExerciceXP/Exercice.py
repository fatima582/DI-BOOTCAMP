#Exercice1
class Cat():
   def __init__(self, name, age):
      self.name = name
      self.age = age

cat1 = Cat("Milou", 1)
cat2 = Cat("Snowy",3)
cat3 = Cat("Garfield", 5)

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")

#Exercice2
class Dog():
   def __init__(self, name, height):
      self.name = name
      self.height = height

   def bark(self):
        print(f"{self.name} fait ouaf !")
   def jump(self):
         x = self.height * 2
         print(f"{self.name} saute {x} cm de haut !")

davids_dog = Dog("Bobi", 50)
sarahs_dog = Dog("Luna", 30)
print(f"Le chien de David s'appelle {davids_dog.name} et mesure {davids_dog.height} cm.")
davids_dog.bark()
davids_dog.jump()

print(f"Le chien de Sarah s'appelle {sarahs_dog.name} et mesure {sarahs_dog.height} cm.")
sarahs_dog.bark()
sarahs_dog.jump()

def compare_dogs(dog1, dog2):
    if dog1.height > dog2.height:
        print(f"Le plus grand chien est {dog1.name}.")
    elif dog2.height > dog1.height:
        print(f"Le plus grand chien chante_moi_un_songchante_moi_un_songest {dog2.name}.")
    else:
        print("Les deux chiens ont la même taille !")

compare_dogs(davids_dog, sarahs_dog)


          
#Exercice3
         
class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def chante_moi_un_song(self):
     for line in self.lyrics:
            print(line)

stairway_fr = Song([
    "Il y a une dame qui est certaine",
    "que tout ce qui brille est de l'or",
    "et elle achète un escalier vers le paradis"
])

stairway_fr.chante_moi_un_song()

#Exercice4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} a été ajouté au zoo.")
        else:
            print(f"{new_animal} est déjà présent dans le zoo !")

    def get_animals(self):
        print(f"\n--- Animaux dans le zoo '{self.name}' ---")
        for animal in self.animals:
            print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"Impossible de vendre {animal_sold}, il n'est pas dans le zoo.")

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups

    def get_groups(self):
        animal_groups = self.sort_animals()
        print(f"\n--- Groupes d'animaux par lettre ---")
        for letter, list_of_animals in animal_groups.items():
            print(f"{letter}: {list_of_animals}")


brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Bear") 

brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Cat")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()