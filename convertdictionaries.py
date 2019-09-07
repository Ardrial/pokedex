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
                    del pokemon_by_id[pkmn_id][x]['Type']
                    del pokemon_by_id[pkmn_id][x]['Weakness']
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