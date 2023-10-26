import random
import hashlib

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


def miseEnGageColoriage(couleurs, valeurs_aleatoires):
    if len(couleurs) != 20 or len(valeurs_aleatoires) != 20:
        raise ValueError("Les tableaux doivent avoir une taille de 20.")

    valeurs_mises_en_gage = []

    for i in range(20):
        couleur = couleurs[i]
        valeur_aleatoire = valeurs_aleatoires[i]

        # Concaténer la couleur et la valeur aléatoire en tant que chaîne de caractères
        # Calculer le hachage SHA-1
     
        hachage= hashlib.sha1((str(valeur_aleatoire) + couleur).encode()).hexdigest()

        valeurs_mises_en_gage.append(hachage)

    return valeurs_mises_en_gage

def preuveColoriage(matrice, valeurs_mises_en_gage, i, j, colors, random_values):
    # Vérifier les engagements
    if valeurs_mises_en_gage[i] != hashlib.sha1((str(random_values[i]) + colors[i]).encode()).hexdigest():
        return False
    if valeurs_mises_en_gage[j] != hashlib.sha1((str(random_values[j]) + colors[j]).encode()).hexdigest():
        return False

    # Vérifier qu'ils sont connectés
    if matrice[i][j] == 0:
        return False

    # Vérifier que les couleurs sont différentes
    if colors[i] == colors[j]:
        return False
        
    return True

if __name__ == "__main__":
    # Générer des valeurs aléatoires
 random_values = [random.randint(0, 2**128 - 1) for _ in range(20)]
 n = 20  # Nombre de nœuds dans le graphe
 graphe = genererGraphe3Coloriable(n)
    # Mise en gage des couleurs
 commitments = miseEnGageColoriage(graphe.coloriage, random_values)
 print (commitments)

    # Test du protocole
 authentifie = True
 for _ in range(400):
        i, j = random.choice([(i, j) for i in range(20) for j in range(20) if graphe.matrice_adjacence[i][j] == 1])
        if not preuveColoriage(graphe.matrice_adjacence, commitments, i, j, graphe.coloriage, random_values):
            authentifie = False
            break
     

 if authentifie:
        print("L'utilisateur est authentifié!")
 else:
        print("L'utilisateur n'a pas pu être authentifié.")




