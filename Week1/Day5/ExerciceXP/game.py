import random

class Game:
    def __init__(self):
        self.valid_choices = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        while True:
            user_choice = input("Choose your move (rock, paper, scissors) : ").strip().lower()
            if user_choice in self.valid_choices:
                return user_choice
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(self.valid_choices)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        
        win_conditions = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        if result == "draw":
            print(f"\nYou chose {user_item}. The computer chose {computer_item}. It's a draw!\n")
        elif result == "win":
            print(f"\nYou chose {user_item}. The computer chose {computer_item}. You win!\n")
        else:
            print(f"\nYou chose {user_item}. The computer chose {computer_item}. You lose...\n")
            
        return result