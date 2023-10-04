import random

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
