#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:
ssh swarm-manager << EOF
    docker stack deploy --compose-file docker-compose.yaml case-opener
EOF