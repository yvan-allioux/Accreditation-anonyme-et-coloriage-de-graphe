#!/bin/bash

# Construire l'image Docker
docker build -t accreditation_anonyme .

echo ----run container----

# Exécuter le conteneur. Il exécutera python main.py à cause de l'entrypoint et de la CMD définie dans le Dockerfile
docker run -it accreditation_anonyme

