sudo yum install docker -y;
sudo yum install git -y;
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose;
sudo chmod +x /usr/local/bin/docker-compose;
sudo usermod -aG docker $USER;
cd DBSERVER_myflix;
docker-compose up -d