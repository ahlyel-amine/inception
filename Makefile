
up: volumes_dir
	docker-compose -f ./srcs/docker-compose.yml up --build -d

volumes_dir:
	@mkdir -p /home/aahlyel/data/data /home/aahlyel/data/db

stop: 
	docker-compose -f ./srcs/docker-compose.yml stop

down:
	docker-compose -f ./srcs/docker-compose.yml down --rmi all  --volumes
	sudo rm -rf /home/aahlyel/data/data /home/aahlyel/data/db


prune: down
	docker system prune -af

start:
	docker-compose -f ./srcs/docker-compose.yml start

re: down up

network:
	@cd srcs && docker network inspect inception

s = wordpress
exec:
	@cd srcs && docker-compose exec ${s} bash

c = wordpress
logs:
	@cd srcs && docker-compose logs ${c}

volumes:
	@cd srcs && docker volume ls

volumes_rm:
	@cd srcs && docker volume rm ${v}

volume_inspect:
	@cd srcs && docker volume inspect ${v}

.PHONY: up stop down start re network exec logs volumes volumes_rm volume_inspect prune
