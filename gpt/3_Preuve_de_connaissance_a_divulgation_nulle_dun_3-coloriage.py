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
