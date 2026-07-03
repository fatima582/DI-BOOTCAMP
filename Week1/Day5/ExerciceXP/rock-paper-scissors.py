from game import Game

def get_user_menu_choice():
    print("=== MAIN MENU ===")
    print("1. Play a new game")
    print("2. Display scores")
    print("3. Quit")
    
    choice = input("Your choice (1, 2, or 3 / q to quit) : ").strip().lower()
    return choice

def print_results(results):
    print("\n=================================")
    print("      GAME RESULTS SUMMARY    ")
    print("=================================")
    print(f" Wins : {results['win']}")
    print(f" Losses : {results['loss']}")
    print(f" Draws : {results['draw']}")
    print("=================================")
    print("Thank you for playing with us! See you soon.\n")

def main():
    scores = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice in ['3', 'q', 'x']:
            print_results(scores)
            break
            
        elif user_choice == '1':
            current_game = Game()
            game_result = current_game.play()
            
            if game_result == "Win":
                scores['win'] += 1
            elif game_result == "Loss":
                scores['loss'] += 1
            elif game_result == "Draw":
                scores['draw'] += 1
                
        elif user_choice == '2':
            print(f"\n[Scores Actuels] Wins: {scores['win']} | Losses: {scores['loss']} | Draws: {scores['draw']}\n")
            
        else:
            print("\nOption inconnue, veuillez choisir 1, 2 ou 3.\n")

if __name__ == "__main__":
    main()