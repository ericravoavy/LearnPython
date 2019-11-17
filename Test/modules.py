# -*-coding:Latin-1 -*
def table(nb, max=10):
    i = 0
    while i < max: # Tant que i est strictement inférieure à la variable max,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
