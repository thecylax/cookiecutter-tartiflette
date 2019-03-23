import collections

from tartiflette import Resolver

from {{cookiecutter.project_slug}}.data import USERS


@Resolver('Mutation.updateUser')
async def resolver_recipe(parent, args, ctx, info):
    user_input = args['input']

    for index, user in enumerate(USERS):
        if user['id'] == user_input['id']:
            if 'name' in user_input:
                USERS[index]['name'] = user_input['name']

            if 'email' in user_input:
                USERS[index]['email'] = user_input['email']

            return USERS[index]

    raise Exception('The user specified is not found.')
