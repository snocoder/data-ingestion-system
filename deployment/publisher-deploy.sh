aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin 851237194675.dkr.ecr.ap-south-1.amazonaws.com
sudo docker-compose -f docker-compose-publisher.yml pull
sudo docker-compose -f docker-compose-publisher.yml up -d