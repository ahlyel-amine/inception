
up: volumes_dir
	docker compose -f ./srcs/docker-compose.yml up --build -d

volumes_dir:
	@mkdir -p /tmp/data/data /tmp/data/db

stop: 
	docker compose -f ./srcs/docker-compose.yml stop

down:
	docker compose -f ./srcs/docker-compose.yml down --rmi all  --volumes
	rm -rf /tmp/data/data /tmp/data/db


prune: down
	docker system prune -af

start:
	docker compose -f ./srcs/docker-compose.yml start

re: down up

network:
	docker network inspect inception

exec:
	docker exec -it ${s} bash

logs:
	docker compose logs ${c}

volumes:
	docker volume ls

volumes_rm:
	docker volume rm ${v}

volume_inspect:
	docker volume inspect ${v}

.PHONY: up stop down start re network exec logs volumes volumes_rm volume_inspect prune
