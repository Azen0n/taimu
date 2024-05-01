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

<details>
   <summary>
      I'm not sure how to use Ruff without creating a virtual environment or using snap,
      will look into <a href="https://github.com/astral-sh/ruff/pkgs/container/ruff">containerizing</a> later.
   </summary>

Create a virtual environment via uv and activate it
```shell
uv venv venv --python=3.12
source venv/bin/activate
```

Install Ruff
```shell
uv pip install ruff
```
</details>

### Commands

List errors. Default path is current directory (`.`)
```shell
ruff check path/to/directory/or/file.py
```

Resolve errors automatically
```shell
ruff check --fix
```

Format files. Default path is current directory (`.`)
```shell
ruff format path/to/directory/or/file.py
```
