 <h1 align="center"> BLU Services 🌔 </h1>

<p align="center">
  <a href="https://github.com/dj-io/blu-cli/actions">
    <img src="https://img.shields.io/badge/Status-OK-yellow" alt="Build Status">
  </a>
  <a href="https://github.com/dj-io/blu/blob/main/blu-cli/LICENSE">
    <img src="https://img.shields.io/github/license/dj-io/blu-cli.svg" alt="License">
  </a>
  <a href="https://github.com/dj-io/blu-cli/actions">
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Build Status">
  </a>
  <!-- <a href="https://coveralls.io/github/psf/blu?branch=main"> -->
    <img src="https://img.shields.io/badge/coverage-36%25-yellow" alt="Coverage Status">
  <!-- </a> -->
  </a>
    <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style">
  </a>
</p>

# Getting Started

### clone the repo

```sh
git clone https://github.com/dj-io/blu.git
cd blu-services
```
### Create an .env file, copy the [.env.sample](/.env.sample) variables and pass in the required values

Build and run using Docker Compose: _This will build the Docker image from the provided Dockerfile and create the required volumes_
```sh
docker-compose up --build
```

Managing Volumes:
_Docker Compose will automatically create any required volumes as defined in docker-compose.yml._

To list volumes, run:

```sh
docker volume ls
```

To remove a volume (e.g., if you need to reset persistent data), run:

```sh
docker volume rm <volume_name>
```

Managing migrations: _Blu services uses alembic to manage db migrations, whenever starting a new container run the following_

```sh
- docker-compose run <app-container-name> alembic -c Resource/alembic.ini revision --autogenerate -m "V<num> Migration"
- docker-compose run <app-container-name> alembic -c Resource/alembic.ini upgrade head
```

Managing local database:

To connect to postgres run:

 1. get the container name or ID
```sh
docker ps
```
2. Open a shell inside the postgres container
```sh
docker exec -it <db container name> psql -U postgres
```
3. connect to the database
```sh
\l (list database)
\c <db-name> (connect to database)
or
\q (exit shell)
```

> Note: For local development, the Docker Compose setup creates a self-contained environment. If you’re using persistent volumes, they will retain data even if you recreate containers. If you prefer a clean start, remove the volumes as needed.

**Happy coding!**
