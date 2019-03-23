import collections

from tartiflette import Resolver

from {{cookiecutter.project_slug}}.data import USERS


@Resolver("Query.users")
async def resolver_users(parent, args, ctx, info):
    return USERS


@Resolver("Query.user")
async def resolver_user(parent, args, ctx, info):
    user = [r for r in USERS if r["id"] == int(args["id"])]

    if not user:
        return None

    return user[0]

