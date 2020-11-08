# Project Setup

You need [poetry](https://python-poetry.org/) for this project. If you don't
have it yet, I suggest installing it via [pipx](https://pipxproject.github.io/pipx/).

```
poetry install
```


# Running the backend


```
poetry run python app.py
```

## Configuration

If you want to override any of the application settings, copy the file
`.env.dist` to `.env` and modify as necessary. All the settings within that
file can also be passed as environment variables.
