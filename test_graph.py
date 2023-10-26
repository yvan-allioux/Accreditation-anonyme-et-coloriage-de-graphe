import random


class Graphe:
    def __init__(self, matrice_adjacence, coloriage):
        self.matrice_adjacence = matrice_adjacence
        self.coloriage = coloriage

def genererGraphe3Coloriable(n):
    couleurs = ["rouge", "vert", "bleu"]
    
    # Générer un coloriage aléatoire pour chaque nœud
    coloriage = [random.choice(couleurs) for _ in range(n)]

    # Initialiser la matrice d'adjacence avec des zéros
    matrice_adjacence = [[0] * n for _ in range(n)]

    # Remplir la matrice d'adjacence en évitant les arêtes entre nœuds de même couleur
    for i in range(n):
        for j in range(i + 1, n):
            if coloriage[i] != coloriage[j]:
                matrice_adjacence[i][j] = matrice_adjacence[j][i] = random.choice([0, 1])

    # Créer un objet Graphe avec la matrice d'adjacence et le coloriage
    graphe = Graphe(matrice_adjacence, coloriage)

    return graphe

#Partie 2:

# Exemple d'utilisation
if __name__ == "__main__":
    n = 5  # Nombre de nœuds dans le graphe
    graphe = genererGraphe3Coloriable(n)

    print("Matrice d'adjacence:")
    for row in graphe.matrice_adjacence:
        print(row)

    print("Coloriage des nœuds:")
    for i, couleur in enumerate(graphe.coloriage):
        print(f"Nœud {i + 1}: {couleur}")
   

