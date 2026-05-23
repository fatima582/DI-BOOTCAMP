import random

class Game:
    def __init__(self):
        self.valid_choices = ['pierre', 'feuille', 'ciseaux']

    def get_user_item(self):
        while True:
            user_choice = input("Choisissez votre coup (pierre, feuille, ciseaux) : ").strip().lower()
            if user_choice in self.valid_choices:
                return user_choice
            print("Choix invalide. Veuillez réessayer.")

    def get_computer_item(self):
        return random.choice(self.valid_choices)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "match nul"
        
        win_conditions = {
            'pierre': 'ciseaux',
            'feuille': 'pierre',
            'ciseaux': 'feuille'
        }
        
        if win_conditions[user_item] == computer_item:
            return "victoire"
        else:
            return "défaite"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        if result == "match nul":
            print(f"\nVous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez fait match nul !\n")
        elif result == "victoire":
            print(f"\nVous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné !\n")
        else:
            print(f"\nVous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu...\n")
            
        return result