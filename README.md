# 🚀 Python Domain Driven example using FastAPI

## ⚙️ Makefile Commands

| Command | Description |
| --- | --- |
| `pipenv-env` | Create project python environment |
| `install` | Install project dependencies |
| `test` | Run unit tests |
| `black` | Format code with black |
| `pylint` | Perform code checking & analysis with pylint |
| `coverage` | Run and report tests coverage |
| `docker-build` | Build docker images |
| `docker-run` | Run docker containers |
| `generate-migrations` | Generate migrations using Alembic |
| `apply-migrations` | Apply the generated migration to database |
| `help` | Show Makefile commands help |

**Usage**: make <-target->

**Note**: Database tables are not created after running docker containers you should generate db migrations using `make generate-migrations` and then apply them with `make apply-migrations`

**Access API docs**: http://localhost:8000/docs

