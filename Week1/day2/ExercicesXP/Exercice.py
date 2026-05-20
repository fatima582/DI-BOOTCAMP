#Exercice1
nbre_dict = {
    'Ten': 10,
    'Twenty': 20,
    'Thirty': 30
}
print(nbre_dict)

#Exercice2
family = {"rick": 43,
                "beth": 13,
                "morty": 5,
                "summer": 8}
total_price = 0

name = input("enter a name : ")
age= int(input("enter an age : "))
family[name] = age

for key, value in family.items():
    if value < 3:
        print(f"{key} is free")
        total_price += 0
    elif value>= 3 and value <= 12:
        print(f"{key} is 10 dollars")
        total_price += 10
    else:
        print(f"{key} is 15 dollars")
        total_price += 15
print(f"the total price is {total_price} dollars")









     # Exercice3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    }
}
brand.update({"number_stores": 2})
print("Zara\'s customers are : ", brand["type_of_clothes"])
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

brand.pop("creation_date")
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())


#Exercice4
def describe_city(city, country="Inconnu"):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland") 
describe_city("Paris")


#Exercice 5
import random
def random_number(n):
    nbre = random.randint(1, 100)
    if n == nbre:
        print("Congratulations! You guessed the number.")
    else:
        print(f"Sorry, the number was {nbre}. Better luck next time!")


#Exercice 6
def make_shirt(size="Large", text="I love Python"):
    print(f"Shirt created with size {size} and text '{text}'")

make_shirt()

make_shirt("M")

make_shirt("S", "Python is great!")


#Exercice 7
def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp =get_random_temp()
    print(f"The current temperature is {temp}°C.")
    if temp < 0:
        print("Brrr, that\’s freezing! Wear some extra layers today.")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don\’t forget your coat.")
    elif temp >= 16 and temp < 23:
        print("Nice weather.")
    elif temp >= 23 and temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

#Exercice 8

ingredients = []
prix_total = 10.0  

while True:
    topping = input("Saisissez un ingrédient pour votre pizza (ou tapez 'quit' pour terminer) : ")
    
    if topping.lower() == 'quit':
        break
    
    ingredients.append(topping)
    prix_total += 2,50
    print(f"Adding {topping} to your pizza.")

print("\n--- Résumé de votre commande ---")
print("Ingrédients choisis :")
for ing in ingredients:
    print(f"- {ing}")

print(f"Prix total de la pizza : {prix_total}$")