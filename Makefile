init:
	poetry install --all-extras

test:
	python -m pytest -x

build:
	docker compose -f "dockerfiles/docker-compose.yaml" build app
	
up:
	docker compose -f "dockerfiles/docker-compose.yaml" up -d

down:
	docker compose -f "dockerfiles/docker-compose.yaml" down

restart:
	docker compose -f "dockerfiles/docker-compose.yaml" restart app

bash:
	docker run -p 5000:5000 -it --name app --rm app /bin/bash

rm-all:
	docker ps -q | xargs docker stop
	docker ps -aq | xargs docker rm -f
	docker images -aq | xargs docker rmi -f
	docker system prune -af
	docker system prune --volumes -f

d-macos:
	# Get access to Docker VM machine runnig on MacOS
	docker run -it --rm --privileged --pid=host justincormack/nsenter1
	
__old:
	# docker build . -f 'dockerfiles/Dockerfile' -t app
	# docker build . -t blog  
	# docker run -p 5000:5000 -d --name blog --rm blog
	# docker run -p 5000:5000 -it --name blog --rm blog bash
	# docker run -p 5000:5000 -d --env-file ./.env --name blog --rm blog