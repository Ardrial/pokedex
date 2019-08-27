import redis
import json


db = redis.StrictRedis()


class PokemonNotFoundError(Exception):
    pass


def get():
    i = 1
    pkmn = {}
    while i <= 151:
        pkmn[str(i)] = get_one(str(i))
        i += 1
    return pkmn


def get_one(key):
    choice = db.get(key)
    if choice is not None:
        return json.loads(db.get(key))
    else:
        raise PokemonNotFoundError("Error! Pokemon not found!")


if __name__ == '__main__':
    with open("pokemon_by_id.json", "r") as f:
        pokemon_by_id = json.load(f)
    with open("pokemon_by_name.json", "r") as f:
        pokemon_by_name = json.load(f)
    for x,y in pokemon_by_id.items():
        db.set(x, json.dumps(y))
    for x,y in pokemon_by_name.items():
        db.set(x, json.dumps(y))