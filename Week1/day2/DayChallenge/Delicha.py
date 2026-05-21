# Exercice1

mot = input("Entrez un mot : ")

dictionnaire = {}

for index, lettre in enumerate(mot):

    if lettre in dictionnaire:
        dictionnaire[lettre].append(index)

    else:
        dictionnaire[lettre] = [index]

print(dictionnaire)