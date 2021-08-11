#!/bin/bash

ls
# copy over compose yaml to manager 
scp ~/.ssh/id_rsa ${WORKSPACE}/docker-compose.yaml jenkins@swarm-manager:/home/horri
# rsync docker-compose.yaml swarm-manager:
# docker stack deploy
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    docker stack deploy --compose-file docker-compose.yaml skin-opener
EOF