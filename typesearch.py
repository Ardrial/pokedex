import argparse
import db
import random


def search_by_type(input):
    i = 1
    pkmn = {}
    while i <= 151:
        if input in db.get_one(str(i))["type"]:
            pkmn[str(i)] = db.get_one(str(i))
        i += 1
    return random.choice(list(pkmn.values()))

