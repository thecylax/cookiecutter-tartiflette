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

    TARTIFLETTE_CONFIG = {
        'subscription_ws_endpoint': '/ws',
        'executor_http_endpoint': '/graphql',
        'executor_http_methods': ['POST'],
        'graphiql_enabled': True,
        'graphiql_options': {
            'endpoint': '/graphiql',
            'default_query': '# {}\n\n'.format('{{cookiecutter.project_short_description}}'),
        }
    }
