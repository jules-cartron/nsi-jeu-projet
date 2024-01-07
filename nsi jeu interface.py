import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class JeuDeNim:
    def __init__(self, joueur1, joueur2):
        self.joueurs = [joueur1, joueur2]
        self.tour = 0
        self.allumettes_restantes = 21

    def jouer_tour(self, choix):
        if choix < 1 or choix > 3 or choix > self.allumettes_restantes:
            messagebox.showwarning("Choix invalide", "Veuillez choisir entre 1 et 3 allumettes.")
            return False 

        self.allumettes_restantes -= choix
        self.tour = 1 - self.tour
        return True

    def joueur_gagnant(self):
        return self.joueurs[self.tour]

    def jouer_tour_ordinateur(self):
        if self.tour == 1:
            choix = self.ordinateur_intelligent(self.allumettes_restantes)
            self.allumettes_restantes -= choix
            self.tour = 1 - self.tour
            return choix
        return None

    def ordinateur_intelligent(self, allumettes_restantes):
        if allumettes_restantes % 4 == 0:
            return 3
        else:
            return allumettes_restantes % 4

class NimGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Nim")

        self.joueur1 = tk.StringVar()
        self.joueur2 = tk.StringVar()
        self.mode_jeu = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Nom du joueur 1:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.joueur1).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Nom du joueur 2:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.joueur2).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Choisissez le mode de jeu:").grid(row=2, column=0, padx=10, pady=5)
        tk.Radiobutton(self.master, text="Joueur vs Joueur", variable=self.mode_jeu, value="1").grid(row=2, column=1, padx=10, pady=5)
        tk.Radiobutton(self.master, text="Joueur vs Ordinateur", variable=self.mode_jeu, value="2").grid(row=2, column=2, padx=10, pady=5)

        tk.Button(self.master, text="Commencer le jeu", command=self.commencer_jeu).grid(row=3, column=1, pady=10)

        self.etat_jeu_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.etat_jeu_label.grid(row=4, column=0, columnspan=3, pady=10)

        self.choix_joueur_entry = tk.Entry(self.master)
        self.choix_joueur_entry.grid(row=5, column=1, pady=5)
        tk.Label(self.master, text="Votre choix (1-3):").grid(row=5, column=0, padx=10, pady=5)

        tk.Button(self.master, text="Valider le choix", command=self.traiter_choix_joueur).grid(row=5, column=2, pady=5)

    def commencer_jeu(self):
        nom_joueur1 = self.joueur1.get()
        nom_joueur2 = self.joueur2.get()
        mode = self.mode_jeu.get()

        if not nom_joueur1 or not nom_joueur2:
            messagebox.showwarning("Erreur", "Veuillez entrer les noms des joueurs.")
            return

        if mode not in ["1", "2"]:
            messagebox.showwarning("Erreur", "Veuillez choisir un mode de jeu.")
            return

        self.jeu_nim = JeuDeNim(nom_joueur1, nom_joueur2)
        self.mettre_a_jour_etat_jeu()

    def mettre_a_jour_etat_jeu(self):
        if self.jeu_nim.allumettes_restantes > 0:
            reste_allumettes = "I" * (self.jeu_nim.allumettes_restantes)
            self.etat_jeu_label.config(text=f"{reste_allumettes}\nC'est au tour de {self.jeu_nim.joueurs[self.jeu_nim.tour]}", font=("Arial", 12))
            if self.jeu_nim.tour == 1:
                self.traiter_tour_ordinateur()
        else:
            self.afficher_gagnant(self.jeu_nim.joueur_gagnant())

    def traiter_tour_ordinateur(self):
        choix_ordi = self.jeu_nim.jouer_tour_ordinateur()
        if choix_ordi is not None:
            self.mettre_a_jour_etat_jeu()

    def traiter_choix_joueur(self):
        try:
            choix = int(self.choix_joueur_entry.get())
        except ValueError:
            messagebox.showwarning("Erreur", "Veuillez entrer un nombre valide (1-3).")
            return

        if self.jeu_nim.jouer_tour(choix):
            self.mettre_a_jour_etat_jeu()

    def afficher_gagnant(self, gagnant):
        messagebox.showinfo("Bravo !", f"Bravo ! {gagnant} a gagné.")

if __name__ == "__main__":
    racine = tk.Tk()
    application = NimGameGUI(racine)
    racine.mainloop()
