
import hashlib

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

# Exemple d'utilisation
if __name__ == "__main__":
    couleurs = ["rouge", "vert", "bleu", "rouge", "vert", "bleu", "rouge", "vert", "bleu", "rouge",
                "vert", "bleu", "rouge", "vert", "bleu", "rouge", "vert", "bleu", "rouge", "vert"]
    valeurs_aleatoires = [12345, 67890, 98765, 54321, 101010, 111111, 222222, 333333, 444444, 555555,
                          666666, 777777, 888888, 999999, 123456, 654321, 987654, 321098, 13579, 24680]

    valeurs_mises_en_gage = miseEnGageColoriage(couleurs, valeurs_aleatoires)

    for i, valeur in enumerate(valeurs_mises_en_gage):
        print(f"Valeur mise en gage pour nœud {i + 1}: {valeur}")
