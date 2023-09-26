# FastAPI + Postgres + PgAmdin + Postgis app

## Run the app with Docker
- Clone this repo
```sh
git clone https://github.com/jvelazquez-reyes/edt-test.git
```

- Create an `.env` file to store enviroment variables for Postgres-Postgis database and PgAmdin panel
```sh
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=restaurant_db

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
```

- Run the `docker-compose.yml` file:

```sh
docker-compose up
```

- Go to port `5050` to use the PgAmdin panel:

```sh
http://127.0.0.1:5050
```

- Login to PgAming using the credentials in the `.env` file:
```sh
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
```

- Locate the navbar in the PgAmdin panel and go to `Object > Register > Server`. It will open a window to create a new server. Fill in the fields `Host name/Address: db`, `Port: 5432`, `Username: postgres`, and `Password: password`:

- Restart the `app` service. You can do this using the Docker Desktop. Locate the `app` service, hit the three dots on the right and restart the service as shown in the image below:

- Visit port `8000` to use the `FastAPI` app:
```sh
http://0.0.0.0:8000
```
- When visiting the previous endpoint you should see get the following response:
```sh
{"message":"Hello EDT Test"}
```

## Endpoints
- `GET` endpoint to get all restaurants:
```sh
http://0.0.0.1:8000/restaurant/
```

- `POST` endpoint to create a new restaurant:
```sh
http://0.0.0.1:8000/restaurant/create
```

```sh
{
    "parameter": {
        "id": "ofdoij509gdpof",
        "rating": 2,
        "name": "MyName",
        "site": "url.com",
        "email": "user@gmail.com",
        "phone": "5757577987987686",
        "street": "Street",
        "city": "Tuxpan",
        "state": "Jalisco",
        "lat": 17.67684865,
        "lng": -99.6445465
    }
}
```

- `PUT` endpoint to update the restaurant info:
```sh
http://0.0.0.1:8000/restaurant/update
```

```sh
{
    "parameter": {
        "id": "ofdoij509gdpof",
        "rating": 4,
        "name": "MyName",
        "site": "url.com",
        "email": "user@gmail.com",
        "phone": "575757798798",
        "street": "Street",
        "city": "Tuxpan",
        "state": "Jalisco",
        "lat": 17.67684865,
        "lng": -99.6445465
    }
}
```

- `DELETE` endpoint to remove a restaurant by id:
```sh
http://0.0.0.1:8000/restaurant/delete
```

```sh
{
    "parameter": {
        "id": "dsdasd4545"
    }
}
```

- `GET` statistics:
```sh
http://0.0.0.1:8000/restaurant/statistics/?latitude=17.4341231&longitude=-99.1265732&radius=138
```
