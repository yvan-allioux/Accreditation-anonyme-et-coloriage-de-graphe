# Utilise l'image Docker officielle pour Python 3.10.6
FROM python:3.10.6

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier main.py dans le conteneur
COPY main.py .

# Définir l'entrypoint pour python et exécuter main.py par défaut
ENTRYPOINT ["python"]
CMD ["main.py"]


# COMMANDE

#docker build -t accreditation_anonyme .

#docker run -it accreditation_anonyme

#python main.py


