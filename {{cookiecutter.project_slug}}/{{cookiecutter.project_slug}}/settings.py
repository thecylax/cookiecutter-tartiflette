import os

class Settings(object):
    TARTIFLETTE_SDL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/sdl"
    TARTIFLETTE_MODULES = [
        '{{cookiecutter.project_slug}}.resolvers.query',
        '{{cookiecutter.project_slug}}.resolvers.mutation',
        '{{cookiecutter.project_slug}}.resolvers.subscription',
        '{{cookiecutter.project_slug}}.directives.rate_limiting',
        '{{cookiecutter.project_slug}}.directives.non_introspectable',
    ]