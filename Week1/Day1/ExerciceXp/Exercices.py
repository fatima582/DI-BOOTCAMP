
# Exercise 1
print("Hello World\n"*4)


# Exercise 2
my_result=(99**3)*8
print(my_result)


# Exercise 3
5 < 3 # False because 5 is greater than 3
3 == 3 # True
3 == "3" # False because we cannot compare a string and an integer
"3" > 3 # False because we cannot compare a string and an integer
"Hello" == "hello" # False because of the case sensitivity


# Exercise 4
computer_brand = "hp"
print("I have a " + computer_brand + " computer.")


# Exercise 5
name ="Cissé Fatoumata"
age = 21
shoe_size = 37
info = "My name is " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size)
print(info)


# Exercise 6
a = 5
b = 3
if a > b:
    print("Hello World")
    
    
# Exercise 7
    nbre=input("Enter a number: ")
if int(nbre) % 2 == 0:
    print("The number is even")
else:    print("The number is odd")

# Exercise 8
nom = " Fatimata"
Nom_utulisateur = input("Enter your name: ")
if Nom_utulisateur.lower() == nom.lower():
    print("Incroyable !on a le meme prenom")
else:    print("Dommage, on n'a pas le meme prenom")


# Exercise 9

taille = int(input("Entrez votre taille en centimètres : "))

if taille > 145:
    print("Félicitations ! Vous êtes assez grand pour monter à cheval.")
else:
    print("Désolé, vous devez encore grandir un peu pour pouvoir monter à cheval.")
