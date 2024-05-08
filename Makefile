
up: volumes_dir
	cd srcs/ && docker-compose up --build  --remove-orphans && cd .. 

volumes_dir:
	mkdir -p data/data data/db

down:
	cd srcs/ && docker-compose down --rmi all --volumes && cd ..
	docker system prune -af
	rm -rf data/

re : down up
