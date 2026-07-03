#Defi 1

number = int(input("Entrez le nombre (number) : "))
length = int(input("Entrez la longueur de la liste (length) : "))

multiples_list = []

for i in range(1, length + 1):
    multiple = number * i
    multiples_list.append(multiple)

print(f"number: {number} - length {length} -> {multiples_list}")


#Defi 2
user_word = input("Entrez un mot : ")
clean_word = ""

for letter in user_word:
    if len(clean_word) == 0 or letter != clean_word[-1]:
        clean_word += letter

print(f"user's word : \"{user_word}\" -> \"{clean_word}\"")