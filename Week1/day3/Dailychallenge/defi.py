class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self):
        output = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"
        output += f"\n    E-I-E-I-0!"
        return output

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        types_tries = self.get_animal_types()
        animaux_pluriel = []
        
        for animal in types_tries:
            if self.animals[animal] > 1:
                animaux_pluriel.append(f"{animal}s")
            else:
                animaux_pluriel.append(animal)
        
        if len(animaux_pluriel) > 1:
            liste_formatee = ", ".join(animaux_pluriel[:-1]) + f" et {animaux_pluriel[-1]}"
        elif len(animaux_pluriel) == 1:
            liste_formatee = animaux_pluriel[0]
        else:
            liste_formatee = "aucun animal"
            
        return f"La ferme de {self.name} possède des {liste_formatee}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal(goat=12)

print(macdonald.get_info())
print("\n" + "="*40 + "\n")
print(macdonald.get_short_info())