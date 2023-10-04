import hashlib

def miseEnGageColoriage(colors, random_values):
    assert len(colors) == len(random_values) == 20
    commitments = []
    for color, random_val in zip(colors, random_values):
        hashed_value = hashlib.sha1((str(random_val) + color).encode()).hexdigest()
        commitments.append(hashed_value)
    return commitments
