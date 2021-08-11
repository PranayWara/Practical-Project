#!/bin/bash


# copy over compose yaml to manager 
scp ~/Practical-Project/docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/id_rsa.pub jenkins@swarm-manager << EOF
    docker stack deploy --compose-file docker-compose.yaml skin-opener
EOF