action-server:
	rasa run actions
build:
	docker compose build
up:
	docker compose up
down:
	docker compose down
logs:
	docker compose logs
train:
	docker compose exec rasa train
