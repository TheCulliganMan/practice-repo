# colin-practice-repo

Colin Ryan Colab Flask Docker Compose

## To start

The following command will pull and build the docker files described in the docker-compose.yml

```bash
docker-compose build
```

Now we want to start the app.

```bash
docker-compose up -d  # d is for daemon
```

Now the app should be running with its' copies of mongodb and redis. (this  can be shortened to `docker-compose up --build -d`)

It is probably about time to check the logs of the application.  We can do this by typing:

```bash
docker-compose logs -f  # f is for follow
```