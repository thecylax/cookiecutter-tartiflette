# {{ cookiecutter.project_slug }}

## {{ cookiecutter.project_short_description}}

### Quickstart

Run the following commands to bootstrap your environment

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
    cd {{cookiecutter.project_slug}}
    pip install -r requirements.txt

You can start your local development server in two ways:

#### With livereload

    make livereload

Then you can visit localhost:8000/graphiql

#### Without livereload

    make runserver

Then you can visit localhost:8080/graphiql