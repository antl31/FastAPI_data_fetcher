api-build:
	docker-compose \
	-f docker-compose.api.yml \
	-f docker-compose.rq.yml \
	build --force-rm \

db-up:
	docker-compose \
	-f docker-compose.db.yml \
	up -d

api-up:
	docker-compose \
	-f docker-compose.api.yml \
	-f docker-compose.rq.yml \
	-f docker-compose.redis.yml \
	up

worker-up:
	docker-compose \
	-f docker-compose.rq.yml \
	up

redis-up:
	docker-compose -f docker-compose.redis.yml up

redis-down:
	docker-compose -f docker-compose.redis.yml down


up: db-up api-up

down:
	docker-compose \
	-f docker-compose.api.yml \
	-f docker-compose.db.yml \
	-f docker-compose.redis.yml \
	-f docker-compose.rq.yml \
	down