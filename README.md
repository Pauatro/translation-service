Hi! 

This is a small translation service developed in python/FastAPI for the backend and react/typescript in the frontend.

This README belongs to the backend project.

## Environment

I managed the local environment, dependencies and versions using [Poetry](https://python-poetry.org/docs/).

if you don't have poetry installed, you'll first need to install pipx if you don't have it:

```pip3 install pipx```

then you can install poetry:

```pipx install poetry```

dependencies are specified in the pyproject.toml and the exact versions are in the poetry.lock. Dependencies should be installed using the command:

```poetry install```


## Initialization

To run the backend in development mode, run the following command inside the src folder:

```uvicorn main:app --reload```

The app will run on port 8000.

## Documentation

Once run locally, API documentation is automatically generated [here](http://localhost:8000/docs)

## Deployment

The app is automatically deployed to heroku when there's a push to the main branch or a PR is merged to main.