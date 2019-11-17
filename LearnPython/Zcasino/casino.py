# -*-coding:Latin-1 -*

"""fonction roulette casino"""

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation
from random import randrange 
          
mise = input("combien voulez-vous miser ? : ")
numero = input("Quel numero choisissez-vous ? : ")
numgagnant = randrange(50)
mise = int(mise)
numero = int(numero)

def roulette(mise,numero,numgagnant):
    """Fonction permettant de v�rifier si le nombre choisi est gagnant ?
    c'est � dire que le num�ro choisi correspond au numero sorti
        si c'est le joueur empoche 3X sa mise de d�part

        sinon si le choix du joueur est de la m�me couleur que le numero sorti il empoche la moiti�
        de la somme qu'il a emit
        les couleurs sont noir pour les nombres pairs et blanche pour les nombres impaires"""
    if(numero == numgagnant): #test si le numero sorti est �gal au choix du joueur
        mise = mise*3 #on multiplie sa mise par 3
        print("vous avez gagn� la somme de :",mise)
    elif(numero != numgagnant): #si le numero sorti n'est pas celui du joueur
        #on test si la couleur du num�ro sorti est la m�me coleur que celui du joueur
        if(numgagnant % 2 == 0 and numero % 2 == 0) or (numgagnant % 2 != 0 and numero % 2 != 0): #si le numero sorti est la m�me couleur que le joueur
            mise = mise/2 #si c'est le cas, le joueur empoche la moiti� de sa mise
            print(int(mise))        
        else: #sinon
            print ("mise perdu") #Le joueur a perdu sa mise
    

roulette(mise,numero,numgagnant)
    
os.system("pause")
