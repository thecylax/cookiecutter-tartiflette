import os
from aiohttp import web

from tartiflette import Engine
from tartiflette_aiohttp import register_graphql_handlers

from {{cookiecutter.project_slug}}.settings import Settings

settings = Settings()
engine = Engine(
    sdl=settings.TARTIFLETTE_SDL_PATH,
    modules=settings.TARTIFLETTE_MODULES,
)


def run():
    app = web.Application()

    web.run_app(
        register_graphql_handlers(
            app=app,
            engine=engine,
            subscription_ws_endpoint="/ws",
            executor_http_endpoint='/graphql',
            executor_http_methods=['POST'],
            graphiql_enabled=True
        )
    )
