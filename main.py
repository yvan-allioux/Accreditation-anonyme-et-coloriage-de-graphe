import random
import hashlib

class Graphe:
    def __init__(self, nodes=20):
        self.nodes = nodes
        self.adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.colors = []

    def genererGraphe3Coloriable(self):
        # Étape 1: Assigner une couleur à chaque noeud
        couleurs = ["rouge", "vert", "bleu"]
        self.colors = [random.choice(couleurs) for _ in range(self.nodes)]
        
        # Étape 2: Construire la matrice d'adjacence
        for i in range(self.nodes):
            for j in range(i+1, self.nodes):
                if self.colors[i] != self.colors[j]: # Connecter seulement si les couleurs sont différentes
                    if random.choice([True, False]): # Avec une probabilité de 1/2
                        self.adj_matrix[i][j] = self.adj_matrix[j][i] = 1
                        
        return self

def miseEnGageColoriage(colors, random_values):
    assert len(colors) == len(random_values) == 20
    commitments = []
    for color, random_val in zip(colors, random_values):
        hashed_value = hashlib.sha1((str(random_val) + color).encode()).hexdigest()
        commitments.append(hashed_value)
    return commitments

def preuveColoriage(matrice, commitments, i, j, colors, random_values):
    # Vérifier les engagements
    if commitments[i] != hashlib.sha1((str(random_values[i]) + colors[i]).encode()).hexdigest():
        return False
    if commitments[j] != hashlib.sha1((str(random_values[j]) + colors[j]).encode()).hexdigest():
        return False

    # Vérifier qu'ils sont connectés
    if matrice[i][j] == 0:
        return False

    # Vérifier que les couleurs sont différentes
    if colors[i] == colors[j]:
        return False
        
    return True

def main():
    # Générer un graphe 3-coloriable
    g = Graphe()
    g.genererGraphe3Coloriable()

    # Générer des valeurs aléatoires
    random_values = [random.randint(0, 2**128 - 1) for _ in range(20)]

    # Mise en gage des couleurs
    commitments = miseEnGageColoriage(g.colors, random_values)

    # Test du protocole
    authentifie = True
    for _ in range(400):
        i, j = random.choice([(i, j) for i in range(20) for j in range(20) if g.adj_matrix[i][j] == 1])
        if not preuveColoriage(g.adj_matrix, commitments, i, j, g.colors, random_values):
            authentifie = False
            break

    if authentifie:
        print("L'utilisateur est authentifié!")
    else:
        print("L'utilisateur n'a pas pu être authentifié.")

if __name__ == "__main__":
    main()
