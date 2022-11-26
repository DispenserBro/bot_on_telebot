from yaml import load, Loader

from starters.register_bot import BASE_DIR


with open(f'{BASE_DIR}/starters/commands.yaml', 'rb') as config:
    commands_dict = load(config, Loader)

commands_to_register = commands_dict['commands_register']
commands_descriptions = commands_dict['commands_menu']
