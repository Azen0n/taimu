# Taimu
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Issue tracking system API.

## Usage

1. Rename `example.env` to `.env` and set values
    ```shell
    mv example.env .env
    ```

2. Run via Docker Compose
    ```shell
    docker compose up --build
    ```

## New Dependencies

To include new dependencies, add packages to the dependencies list in the
pyproject.toml file, then compile them using
```shell
uv pip compile pyproject.toml -o requirements.txt
```
I use [uv](https://github.com/astral-sh/uv#getting-started) here, but you can 
use the default pip instead.

## Ruff

To use `docker compose exec`, you need to have a web container running.

### Commands

List errors. Default path is current directory (`.`)
```shell
docker compose exec web ruff check path/to/directory/or/file.py
```

Resolve errors automatically
```shell
docker compose exec web ruff check --fix
```

Format files. Default path is current directory (`.`)
```shell
docker compose exec web ruff format path/to/directory/or/file.py
```

### Alternative to `docker compose exec`

Create a virtual environment via uv and activate it
```shell
uv venv venv --python=3.12
source venv/bin/activate
```

Install Ruff
```shell
uv pip install ruff
```
Now you don't need running containers to use Ruff, just run `ruff check`.
