#!/usr/bin/env bash

aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin 851237194675.dkr.ecr.ap-south-1.amazonaws.com
sudo docker build --file Dockerfile ../app/ --tag application/coulomb:latest
sudo docker tag application/coulomb:latest 851237194675.dkr.ecr.ap-south-1.amazonaws.com/application/coulomb:latest
sudo docker push 851237194675.dkr.ecr.ap-south-1.amazonaws.com/application/coulomb:latest