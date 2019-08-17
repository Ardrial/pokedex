import argparse
import sys
import json
import random
from flask import Flask, render_template
app = Flask(__name__)


with open("pokemon_by_id.json", "r") as f:
    pokemon_by_id = json.load(f)
with open("pokemon_by_name.json", "r") as f:
    pokemon_by_name = json.load(f)


class Pokemon:
    def __init__(self, name, pokedex, weakness, type, evolution):
        self.name = name
        self.pokedex = pokedex
        self.weakness = weakness
        self.type = type
        self.evolution = evolution


def search_type(input, name_search=False):
    if name_search:
        try:
            if input.lower() == "random":
                return pokemon_by_id[str(random.randint(1, 151))]
            else:
                return pokemon_by_name[input.lower()]
        except KeyError:
            print("Pokemon not found!")
            sys.exit(1)
    else:
        try:
            if input == '0':
                input = str(random.randint(1, 151))
            return pokemon_by_id[input.lower()]
        except KeyError:
            print("Pokemon not found!")
            sys.exit(1)

@app.route('/result')
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="search input")
    parser.add_argument("--name", help="search by name instead of ID", action="store_true")
    parser.add_argument("--weakness", help="list the pokemon's weakness", action="store_true")
    parser.add_argument("--pokedex", help="list the pokemon's Pokedex Number", action="store_true")
    parser.add_argument("--type", help="list the pokemon's Typing", action="store_true")
    parser.add_argument("--evolution", help="list the pokemon's stage of evolution", action="store_true")

    args = parser.parse_args()  # Parse arguments
    pkmn = search_type(args.input, args.name)  # Determine if search by name or pokedex number

    # Create objects of Pokemon class
    pokemon_choice = Pokemon(pkmn['name'].title(), pkmn['pokedex'], ', '.join(pkmn['weakness']).title(),
                             ', '.join(pkmn['type']).title(), ((str(pkmn['evolution']).title()).strip('{')).strip('}'))

    # Create printable dictionary based on arguments passed
    pokemon_dict = {'Name': pokemon_choice.name}
    all_args = not any([args.weakness, args.type, args.evolution, args.pokedex])
    if args.pokedex or all_args:
        pokemon_dict['Pokedex #'] = pokemon_choice.pokedex
    if args.weakness or all_args:
        pokemon_dict['Weakness'] = pokemon_choice.weakness
    if args.type or all_args:
        pokemon_dict['Type'] = pokemon_choice.type
    if args.evolution or all_args:
        pokemon_dict['Evolution'] = pokemon_choice.evolution
    return render_template('pokemon.html', result=pokemon_dict)


if __name__ == '__main__':
    app.run(debug=True)