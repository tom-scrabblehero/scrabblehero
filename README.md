## Set up

Start the docker services.

```
docker-compose up -d
```

## Testing

Run the tests.

```
docker-compose exec api pytest
```

## Deploying

Pushes to master that pass the test suite will be deployed automatically.
