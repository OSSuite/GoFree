# GoFree: Insanely simple golinks

## Install it in 1 minute and 13 seconds
[![Speedrunning installing GoFree](https://img.youtube.com/vi/u19ETNmI5BA/0.jpg)](https://www.youtube.com/watch?v=u19ETNmI5BA)

## Prerequisites
* PostgreSQL (hey -- there's a Docker container for that!)
* Nothing else!

## Running example
This example runs GoFree on port 80, connecting to local postgres with user
postgres and password violetlocaldev, with the database `gofree`.
```
sudo docker run -p 80:8080 -e GOFREE_PG_DSN=postgres://postgres:violetlocaldev@172.17.0.1:5432/gofree wtfviolet/gofree
```

## How to use
Edit your DNS hosts to point `go` to the server GoFree is running on. Then use
it like this:

### Adding links
Visit this URL in your browser:
```
go/add link-name https://google.com
```

### Visiting links
```
go/link-name
```
