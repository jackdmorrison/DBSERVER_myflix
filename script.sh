docker system prune -a -f;
docker-compose build; 
DOCKER_BUILDKIT=1 docker-compose up -d;
