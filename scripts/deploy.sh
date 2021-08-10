#!/bin/bash


# copy over compose yaml to manager 
scp -i ~/.ssh/id_rsa.pub docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/id_rsa.pub jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file docker-compose.yaml draft
EOF