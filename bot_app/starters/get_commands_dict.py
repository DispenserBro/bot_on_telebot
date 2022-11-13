import tomllib


with open('./starters/commands.toml', 'rb') as config:
    commands_dict = tomllib.load(config)