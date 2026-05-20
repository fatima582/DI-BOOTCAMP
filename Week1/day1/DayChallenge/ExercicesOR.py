
#Exercice 1
mois = int(input("Entrez un numéro de mois (de 1 à 12) : "))


if 3 <= mois <= 5:
    print("La saison est : Spring")

elif 6 <= mois <= 8:
    print("La saison est : Summer")

elif 9 <= mois <= 11:
    print("La saison est : Autumn")


elif mois == 12 or mois == 1 or mois == 2:
    print("La saison est : Winter")

else:
    print("Erreur : Le nombre saisi doit être compris entre 1 et 12.")



#Exercice 2
print(" Nombres de 1 à 20 inclus ")

for i in range(1, 21):
    print(i)

print("\n Nombres pairs de 1 à 20 ")

for i in range(1, 21):
    if i % 2 == 0:  
        print(i)



#Exercice 3

mon_nom = "Cissé"
nom_saisi = ""

while nom_saisi != mon_nom:
    nom_saisi = input("Veuillez saisir votre nom : ")

print("Bravo ! Vous avez enfin trouvé le bon nom.")


#Exercice 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("Entrez un nom : ")
if name in names:
    position = names.index(name)
    print(f"Le nom '{name}' figure dans la liste. Son premier index est : {position}")
else:
    print(f"Le nom '{name}' ne figure pas dans la liste.")


#Exercice 5

num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

if num1 >= num2 and num1 >= num3:
    plus_grand = num1
elif num2 >= num1 and num2 >= num3:
    plus_grand = num2
else:
    plus_grand = num3

print(f"The greatest number is: {plus_grand}")


#Exercice 6
import random
parties_gagnees = 0
parties_perdues = 0

print(" Bienvenue dans le jeu du nombre mystère ! ")

continuer_a_jouer = True

while continuer_a_jouer:
    nombre_secret = random.randint(1, 9)
    
    saisie = int(input("\nDevinez le nombre secret (entre 1 et 9 inclus) : "))
    
    if saisie == nombre_secret:
        print("Gagnant")
        parties_gagnees += 1 
    else:
        print("Meilleure chance la prochaine fois")
        parties_perdues += 1  # Ajoute 1 au compteur de défaites
        
    
    reponse = input("Voulez-vous rejouer ? (Tapez 'non' pour arrêter, ou entrée pour continuer) : ")
    if reponse.lower() == 'non':
        continuer_a_jouer = False

print("\n Partie terminée !")
print(f"Total de parties gagnées : {parties_gagnees}")
print(f"Total de parties perdues : {parties_perdues}")