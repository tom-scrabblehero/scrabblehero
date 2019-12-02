## Set up

Start the docker services.

```
docker-compose up -d
```

Seed the database.

```
docker-compose exec api flask seed words
```

## Testing

Run the tests.

```
docker-compose exec api pytest
```

## Deploying

Pushes to master that pass the test suite will be deployed automatically.
