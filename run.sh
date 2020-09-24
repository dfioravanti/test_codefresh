docker stack rm test

docker build -t myclient -f Dockerfile.client .
docker build -t myserver -f Dockerfile.server .
docker build -t mytest -f Dockerfile.test .

sleep 5

docker stack deploy -c docker-compose.yml test