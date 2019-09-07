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