from game import Game

def get_user_menu_choice():
    print("=== MENU PRINCIPAL ===")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("3. Quitter")
    
    choice = input("Votre choix (1, 2, ou 3 / q pour quitter) : ").strip().lower()
    return choice

def print_results(results):
    print("\n=================================")
    print("      RÉCAPITULATIF DES SCORES    ")
    print("=================================")
    print(f" Victoires : {results['win']}")
    print(f" Défaites  : {results['loss']}")
    print(f" Matchs nuls : {results['draw']}")
    print("=================================")
    print("Merci d'avoir joué avec nous ! À bientôt.\n")

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
            
            if game_result == "victoire":
                scores['win'] += 1
            elif game_result == "défaite":
                scores['loss'] += 1
            elif game_result == "match nul":
                scores['draw'] += 1
                
        elif user_choice == '2':
            print(f"\n[Scores Actuels] Victoires: {scores['win']} | Défaites: {scores['loss']} | Nuls: {scores['draw']}\n")
            
        else:
            print("\nOption inconnue, veuillez choisir 1, 2 ou 3.\n")

if __name__ == "__main__":
    main()