import random

class JeuDeNim:
    def __init__(self, joueur1, joueur2):
        self.joueurs = [joueur1, joueur2]
        self.tour = 0
        self.allumettes_restantes = 21

    def afficher_etat(self):
        print(f"\nAllumettes restantes : {self.allumettes_restantes}")
        print(f"C'est au tour de {self.joueurs[self.tour]}")

    def jouer_tour(self, choix):
        if choix < 1 or choix > 3 or choix > self.allumettes_restantes:
            print("Choix invalide. Veuillez choisir entre 1 et 3 allumettes.")
            return False

        self.allumettes_restantes -= choix
        self.tour = 1 - self.tour  # Changer de joueur
        return True

    def joueur_gagnant(self):
        return self.joueurs[self.tour]

def joueur_vs_joueur():
    joueur1 = input("Nom du joueur 1 : ")
    joueur2 = input("Nom du joueur 2 : ")

    jeu = JeuDeNim(joueur1, joueur2)

    while jeu.allumettes_restantes > 0:
        jeu.afficher_etat()
        choix = int(input("Combien d'allumettes voulez-vous enlever (1-3) ? "))
        
        if not jeu.jouer_tour(choix):
            continue

    print(f"\nBravo ! {jeu.joueur_gagnant()} a gagné.")

def joueur_vs_ordinateur():
    joueur = input("Nom du joueur : ")
    ordinateur = "Ordinateur"

    jeu = JeuDeNim(joueur, ordinateur)

    while jeu.allumettes_restantes > 0:
        jeu.afficher_etat()

        if jeu.tour == 1:  # Tour de l'ordinateur
            choix = intelligent_ordinateur(jeu.allumettes_restantes)
        else:
            choix = int(input("Combien d'allumettes voulez-vous enlever (1-3) ? "))

        jeu.jouer_tour(choix)

    print(f"\nBravo ! {jeu.joueur_gagnant()} a gagné.")

def intelligent_ordinateur(allumettes_restantes):
    # L'ordinateur enlève un nombre d'allumettes pour maximiser ses chances de gagner.
    if allumettes_restantes % 4 == 0:
        return random.choice([1, 2, 3])
    else:
        return allumettes_restantes % 4

# Exécution du jeu
mode = input("Choisissez le mode de jeu (1 pour joueur vs joueur, 2 pour joueur vs ordinateur) : ")

if mode == "1":
    joueur_vs_joueur()
elif mode == "2":
    joueur_vs_ordinateur()
else:
    print("Mode invalide. Veuillez choisir 1 ou 2. ")