#!/bin/sh

docker build -f el7-miniconda-ufs_pyutils.dockerfile --tag noaaufsrnr/el7-miniconda-ufs_pyutils:latest .
docker push noaaufsrnr/el7-miniconda-ufs_pyutils:latest

docker build -f ubuntu20.04-miniconda-ufs_pyutils.dockerfile --tag noaaufsrnr/ubuntu20.04-miniconda-ufs_pyutils:latest .
docker push noaaufsrnr/ubuntu20.04-miniconda-ufs_pyutils:latest

docker build -f ubuntu20.04.hello_world.dockerfile --tag noaaufsrnr/ubuntu20.04.hello_world:latest .
docker push noaaufsrnr/ubuntu20.04.hello_world:latest
