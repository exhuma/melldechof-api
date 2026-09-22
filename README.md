> **This project is no longer maintained.** It is kept online for reference. Last activity: 2020. Issues and pull requests are not being looked at. Feel free to fork it.

# Project Setup

You need [poetry](https://python-poetry.org/) for this project. If you don't
have it yet, I suggest installing it via [pipx](https://pipxproject.github.io/pipx/).

```
poetry install
```


# Running the backend


```
poetry run uvicorn app:app
```

## Configuration

If you want to override any of the application settings, copy the file
`.env.dist` to `.env` and modify as necessary. All the settings within that
file can also be passed as environment variables.
