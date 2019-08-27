import db
import random


class Pokemon:
    def __init__(self, name, pokedex, weakness, type, evolution):
        self.name = name
        self.pokedex = pokedex
        self.weakness = weakness
        self.type = type
        self.evolution = evolution


def search_by_type(input):
    i = 1
    pkmn = {}
    while i <= 151:
        if input in db.get_one(str(i))["type"]:
            pkmn[str(i)] = db.get_one(str(i))
        i += 1
    # return random.choice(list(pkmn.values()))
    return pkmn


def search_by_weakness(input):
    i = 1
    pkmn = {}
    while i <= 151:
        if input in db.get_one(str(i))["weakness"]:
            pkmn[str(i)] = db.get_one(str(i))
        i += 1
    # return random.choice(list(pkmn.values()))
    return pkmn


def create_dict_multiple(pkmn, weakness, pokedex, type, evolution):
    pokemon_choice = Pokemon(pkmn['name'].title(), pkmn['pokedex'], ', '.join(pkmn['weakness']).title(),
                             ', '.join(pkmn['type']).title(), ((str(pkmn['evolution']).title()).strip('{')).strip('}'))
    choice_dict = {'Name': pokemon_choice.name}
    all_args = not any([weakness, type, evolution, pokedex])
    if pokedex or all_args:
        choice_dict['Pokedex #'] = pokemon_choice.pokedex
    if type or all_args:
        choice_dict['Type'] = pokemon_choice.type
    if weakness or all_args:
        choice_dict['Weakness'] = pokemon_choice.weakness
    if evolution or all_args:
        choice_dict['Evolution'] = pokemon_choice.evolution
    return choice_dict