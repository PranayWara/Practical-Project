#!/bin/bash

ls
# copy over compose yaml to manager 
# scp ~/.ssh/id_rsa ${WORKSPACE}/Practical-Project/docker-compose.yaml jenkins@swarm-manager: docker-compose.yaml
rsync docker-compose.yaml swarm-manager:
# docker stack deploy
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    docker stack deploy --compose-file docker-compose.yaml skin-opener
EOF