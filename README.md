# GoFree: Insanely simple golinks

## Prerequisites
* PostgreSQL (hey -- there's a Docker container for that!)
* Nothing else!

## Running example
This example runs GoFree on port 80, connecting to local postgres with user
postgres and password postgres, with the database `gofree`.
```
sudo docker run -p 80:8080 -e GOFREE_PG_DNS=postgres://postgres:violetlocaldev@172.17.0.1:5432 gofree
```
