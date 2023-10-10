# Importer des modules nécessaires
import random
import hashlib

# Définir une classe pour représenter un graphe
class Graphe:
    def __init__(self, nodes=20):
        self.nodes = nodes  # Le nombre de neuds dans le graphe
        # Initialiser une matrice d'adjacence avec des zéros
        self.adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.colors = []  # Liste pour stocker les couleurs de chaque nœud

    def genererGraphe3Coloriable(self):
        # Étape 1: Assigner aléatoirement une couleur à chaque nœud
        couleurs = ["rouge", "vert", "bleu"]
        self.colors = [random.choice(couleurs) for _ in range(self.nodes)]
        
        # Étape 2: Remplir la matrice d'adjacence de manière à ce que deux neuds de la même couleur ne soient jamais connectés
        for i in range(self.nodes):
            for j in range(i+1, self.nodes):  # Pour éviter les doublons
                # Si les couleurs sont différentes et avec une probabilité de 50%, connecter les neuds
                if self.colors[i] != self.colors[j] and random.choice([True, False]):
                    self.adj_matrix[i][j] = self.adj_matrix[j][i] = 1
                        
        return self

# Fonction pour engager (ou chiffrer) les couleurs des neuds
def miseEnGageColoriage(colors, random_values):
    commitments = []
    for color, random_val in zip(colors, random_values):
        # Concaténer la couleur avec une valeur aléatoire et la hasher
        hashed_value = hashlib.sha1((str(random_val) + color).encode()).hexdigest()
        # Ajouter l'engagement (couleur chiffrée) à la liste
        commitments.append(hashed_value)
    return commitments

# Fonction pour vérifier si l'utilisateur connaît vraiment la coloration valide du graphe
def preuveColoriage(matrice, commitments, i, j, colors, random_values):
    # Vérifier que les engagements correspondent
    if commitments[i] != hashlib.sha1((str(random_values[i]) + colors[i]).encode()).hexdigest():
        return False
    if commitments[j] != hashlib.sha1((str(random_values[j]) + colors[j]).encode()).hexdigest():
        return False

    # Vérifier que les neuds sont connectés et ont des couleurs différentes
    if matrice[i][j] == 0 or colors[i] == colors[j]:
        return False
        
    return True

def main():
    # Créer un graphe et le colorier
    g = Graphe()
    g.genererGraphe3Coloriable()

    # Générer des valeurs aléatoires pour l'engagement
    random_values = [random.randint(0, 2**128 - 1) for _ in range(20)]

    # Engager les couleurs
    commitments = miseEnGageColoriage(g.colors, random_values)

    # Tester le protocole 400 fois
    authentifie = True
    for _ in range(400):
        # Choisir deux neuds connectés au hasard
        i, j = random.choice([(i, j) for i in range(20) for j in range(20) if g.adj_matrix[i][j] == 1])
        # Si la vérification échoue même une seule fois, l'utilisateur n'est pas authentifié
        if not preuveColoriage(g.adj_matrix, commitments, i, j, g.colors, random_values):
            authentifie = False
            break

    # Afficher le résultat
    if authentifie:
        print("L'utilisateur est authentifié!")
    else:
        print("L'utilisateur n'a pas pu être authentifié.")

# Exécuter la fonction principale
if __name__ == "__main__":
    main()
