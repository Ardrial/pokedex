import json

with open("pokemon_by_id.json", "r") as f:
    pokemon_by_id = json.load(f)
with open("pokemon_by_id.json", "r") as f:
    pokemon_by_name = json.load(f)


if __name__ == '__main__':
    for pkmn_id, pkmn in pokemon_by_id.items():
        for x,y in pkmn.items():
            if x.lower() == "evolution":
                try:
                    if y == "second evolution" and pokemon_by_id[str(int(pkmn_id) + 1)][x.lower()] == "third evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": pokemon_by_id[str(int(pkmn_id) + 1)]["name"], "pokedex": pokemon_by_id[str(int(pkmn_id) + 1)]["pokedex"]}
                    elif y == "first evolution" and pokemon_by_id[str(int(pkmn_id)+1)][x.lower()] == "second evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": pokemon_by_id[str(int(pkmn_id)+1)]["name"], "pokedex": pokemon_by_id[str(int(pkmn_id)+1)]["pokedex"]}
                    elif y == "third evolution" and pokemon_by_id[str(int(pkmn_id) + 1)][x.lower()] != "fourth evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": "", "pokedex": "none"}
                    elif y == "second evolution" and pokemon_by_id[str(int(pkmn_id)+1)][x.lower()] != "third evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": "", "pokedex": "none"}
                    elif y == "first evolution" and pokemon_by_id[str(int(pkmn_id)+1)][x.lower()] != "second evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": "", "pokedex": "none"}
                    elif y == "none":
                        pokemon_by_id[pkmn_id][x] = {"name": "", "pokedex": "none"}
                    elif y == "no evolution":
                        pokemon_by_id[pkmn_id][x] = {"name": "", "pokedex": "none"}
                except KeyError:
                        print("End of Dictionary! ")
    new_pokemon_by_name = {}
    for pkmn_name, pkmn in pokemon_by_name.items():
        pkmn_name = pkmn["name"]
        new_pokemon_by_name.update({pkmn_name: pkmn})

with open("pokemon_by_id.json", "w+") as f:
    json.dump(pokemon_by_id, f)
with open("pokemon_by_name.json", "w+") as f:
    json.dump(new_pokemon_by_name, f)