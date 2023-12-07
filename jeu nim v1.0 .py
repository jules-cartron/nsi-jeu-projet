
# Etape 1 : #création de la fonction qui demande les pseudo des joueurs
 
def joueur():
    global joueur1  #La fonction globals() renvoie un dictionnaire contenant les variables définies dans le namespace global 
    global joueur2
    joueur1=str(input("Joueur 1, entrez votre pseudo : "))
    joeuer2=str(input("Joueur 2, entrez votre pseudo : ")) # On demande le pseudo du ou des joueurs 
    print("Bienvenue", joueur1, "et", joueur2)

# Etape 2 : création de la fonction qui afffiche en début de partie les allumettes en fonction du nombre choisi par les joueurs
 
def allumettesDebut():
    global nombreAllumettes
    nombreAllumettes=int(input("Combien d'alllumettes souhaitez-vous integrer dans le jeu? "))
    global allumettesOn
    global allumettesOff
    allumettesOn=(" | ")
    allumettesOff=(" . ")
    print(nombreAllumettes*allumettesOn)


    