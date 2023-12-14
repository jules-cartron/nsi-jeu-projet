def nim_game():
    # Initialisation du jeu
    pile = int(input("Entrez le nombre total d'allumettes: "))
    
    # Boucle de jeu
    while pile > 0:
        for player in [1, 2]:
            print(f"C'est au tour du joueur {player}")
            nb_allumettes = int(input(f"allumettes a retirer --> joueur {player} ="))
            
            # Vérification 
            while nb_allumettes < 1 or nb_allumettes > 3 or nb_allumettes > pile:
                print("Vous ne pouvez retirer que 1, 2 ou 3 allumettes et pas plus qu'il n'y en a dans la pile.")
                nb_allumettes = int(input(f"Combien d'allumettes voulez-vous retirer, joueur {player}? "))
            
            # Mise à jour de la pile
            pile = pile - nb_allumettes
            print(f"Il reste {pile} allumettes.")
            
            # Vérification de la fin de la partie
            if pile == 0:
                print(f"Le joueur {player} a pris la dernière allumette. Le joueur {3 - player} gagne!")
                return 

# Lancement du jeu
nim_game()