import random

class JeuDeNim:
    def __init__(self, joueur1, joueur2):
        self.joueurs = [joueur1, joueur2] # Crée une liste des joueurs 
        self.tour = 0 # Indique le tour actuel (0 pour le joueur1, 1 pour le joueur2)
        self.allumettes_restantes = 21 # nombre d'allumettes dans le jeu de base 

    def afficher_etat(self):
        print(f"\nAllumettes restantes : {self.allumettes_restantes}") # affiche le nombre d'allumettes restantes
        print(f"C'est au tour de {self.joueurs[self.tour]}") # affiche le tour du joueurs qui doit jouer 

    def jouer_tour(self, choix):
        if choix < 1 or choix > 3 or choix > self.allumettes_restantes: # le joueur doit choisir entre 1 et 3 allumettes sinon un message d'erreur s'affiche 
            print("Choix invalide. Veuillez choisir entre 1 et 3 allumettes.")
            return False 

        self.allumettes_restantes -= choix # enlève le nombre d'allumettes choisi par le joueur 
        self.tour = 1 - self.tour  # Changer de joueur (tour passe au joueur suivant)
        return True

    def joueur_gagnant(self):
        return self.joueurs[self.tour] # renvoie le joueur qui a gagné

def joueur_vs_joueur():
    joueur1 = input("Nom du joueur 1 : ") # indiquer le nom du joueur 1 
    joueur2 = input("Nom du joueur 2 : ") # indiquer le nom du joueur 2

    jeu = JeuDeNim(joueur1, joueur2) # Crée une instance de la classe JeuDeNim avec les joueurs donnés

    while jeu.allumettes_restantes > 0: # tant qu'il reste des allumettes dans le jeu
        jeu.afficher_etat() # affiche l'état actuel du jeu
        choix = int(input("Combien d'allumettes voulez-vous enlever (1-3) ? ")) # le joueur doit choisir entre 1 et 3 allumettes sinon un message d'erreur s'affiche 
        
        if not jeu.jouer_tour(choix): # exécute le tour du joueur et si le choix est invalide, continue la boucle while
            continue

    print(f"\nBravo ! {jeu.joueur_gagnant()} a gagné.") # affiche le nom du joueur qui a gagné

def joueur_vs_ordinateur():
    joueur = input("Nom du joueur : ") # indiquer le nom du joueur 
    ordinateur = "Ordinateur" # nom de l'ordinateur

    jeu = JeuDeNim(joueur, ordinateur) # Crée une instance de la classe JeuDeNim avec le joueur et l'ordinateur

    while jeu.allumettes_restantes > 0: # tant qu'il reste des allumettes dans le jeu
        jeu.afficher_etat() # affiche l'état actuel du jeu

        if jeu.tour == 1:  # Tour de l'ordinateur
            choix = intelligent_ordinateur(jeu.allumettes_restantes) # l'ordinateur choisit un nombre intelligent d'allumettes à enlever
        else:
            choix = int(input("Combien d'allumettes voulez-vous enlever (1-3) ? ")) # le joueur doit choisir entre 1 et 3 allumettes sinon un message d'erreur s'affiche

        jeu.jouer_tour(choix) # exécute le tour du joueur (ou de l'ordinateur)

    print(f"\nBravo ! {jeu.joueur_gagnant()} a gagné.") # affiche le nom du joueur ou de l'ordinateur qui a gagné

def intelligent_ordinateur(allumettes_restantes):
    # L'ordinateur enlève un nombre d'allumettes pour maximiser ses chances de gagner.
    if allumettes_restantes % 4 == 0: # si le nombre d'allumettes restantes est un multiple de 4
        return random.choice([1, 2, 3]) # l'ordinateur choisit aléatoirement entre 1, 2 et 3 allumettes
    else:
        return allumettes_restantes % 4 # l'ordinateur choisit de retirer le reste de la division par 4 du nombre d'allumettes restantes

# execution du Jeu
# Demande à l'utilisateur de choisir le mode de jeu
mode = input("Choisissez le mode de jeu (1 pour joueur vs joueur, 2 pour joueur vs ordinateur) : ")

# Vérifie le mode choisi et exécute la fonction correspondante
if mode == "1":
    joueur_vs_joueur()
elif mode == "2":
    joueur_vs_ordinateur()
else:
    print("Mode invalide. Veuillez choisir 1 ou 2. ")

# Boucle principale pour permettre à l'utilisateur de continuer à jouer
while True:
    # Demande à l'utilisateur de choisir le mode de jeu ou de quitter
    mode = input("Choisissez le mode de jeu (1 pour joueur vs joueur, 2 pour joueur vs ordinateur, ou Exit pour quitter) : ")

    # Vérifie le mode choisi et exécute la fonction correspondante
    if mode == "1":
        joueur_vs_joueur()
    elif mode == "2":
        joueur_vs_ordinateur()
    elif mode.lower() == "Exit": # La méthode lower() renvoie une chaîne où tous les caractères sont en minuscules. Les symboles et les nombres sont ignorés. 
        # Sort de la boucle si l'utilisateur choisit de quitter
        break # l’instruction break vous donne la possibilité de quitter une boucle au moment où une condition externe est déclenchée.
    else:
        print("Mode invalide. Veuillez choisir 1, 2 ou Exit.")

# Affiche un message de remerciement
print("Merci d'avoir joué ! Au revoir.") 
