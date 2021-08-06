#!/bin/bash


# copy over compose yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file docker-compose.yaml draft
EOF