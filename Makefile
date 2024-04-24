
default: volumes_dir
	cd srcs/ && docker-compose up --build && cd ..

volumes_dir:
	mkdir -p data/data data/db

clean:
	cd srcs/ && docker-compose down --rmi all --volumes && cd ..
	docker system prune -af
	rm -rf data/

