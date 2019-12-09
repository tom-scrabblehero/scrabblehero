# http://scrabblehero.com

A scrabble word recommendation engine.

## Set up

Start the docker services and seed the database.

```
docker-compose build
docker-compose up --detach
docker-compose exec api flask db upgrade
docker-compose exec api flask seed words
```

## Testing

Run the tests.

```
docker-compose exec api pytest
```

## Deploying

Pushes to master that pass the test suite will be deployed automatically.
