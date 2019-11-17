# -*-coding:Latin-1 -*

"""fonction roulette casino"""

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # systÃ¨me d'exploitation
from random import randrange 
          
mise = input("combien voulez-vous miser ? : ")
numero = input("Quel numero choisissez-vous ? : ")
numgagnant = randrange(50)
mise = int(mise)
numero = int(numero)

def roulette(mise,numero,numgagnant):
    """Fonction permettant de vérifier si le nombre choisi est gagnant ?
    c'est à dire que le numéro choisi correspond au numero sorti
        si c'est le joueur empoche 3X sa mise de départ

        sinon si le choix du joueur est de la même couleur que le numero sorti il empoche la moitié
        de la somme qu'il a emit
        les couleurs sont noir pour les nombres pairs et blanche pour les nombres impaires"""
    if(numero == numgagnant): #test si le numero sorti est égal au choix du joueur
        mise = mise*3 #on multiplie sa mise par 3
        print("vous avez gagné la somme de :",mise)
    elif(numero != numgagnant): #si le numero sorti n'est pas celui du joueur
        #on test si la couleur du numéro sorti est la même coleur que celui du joueur
        if(numgagnant % 2 == 0 and numero % 2 == 0) or (numgagnant % 2 != 0 and numero % 2 != 0): #si le numero sorti est la même couleur que le joueur
            mise = mise/2 #si c'est le cas, le joueur empoche la moitié de sa mise
            print(int(mise))        
        else: #sinon
            print ("mise perdu") #Le joueur a perdu sa mise
    

roulette(mise,numero,numgagnant)
    
os.system("pause")
