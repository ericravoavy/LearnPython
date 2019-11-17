# -*-coding:Latin-1 -*

nb = input("Saisissez la table :")
i=0

while i < 10: # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour de boucle
    