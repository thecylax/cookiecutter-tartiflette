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
app = web.Application()
registered_handlers = register_graphql_handlers(
    app=app, engine=engine, **settings.TARTIFLETTE_CONFIG
)

def run():
    web.run_app(registered_handlers)

# For liveroload only
async def create_app():
    return registered_handlers