import argparse
import sys
import json
import random
from flask import Flask, render_template
import db


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


def create_dict(pkmn, weakness, pokedex, type, evolution):

    # Create objects of Pokemon class
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


@app.route('/result')
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="search input")
    parser.add_argument("--weakness", help="list the pokemon's weakness", action="store_true")
    parser.add_argument("--pokedex", help="list the pokemon's Pokedex Number", action="store_true")
    parser.add_argument("--type", help="list the pokemon's Typing", action="store_true")
    parser.add_argument("--evolution", help="list the pokemon's stage of evolution", action="store_true")

    args = parser.parse_args()  # Parse arguments

    try:
        if args.input.lower() == "random":
            pkmn = db.get_one(str(random.randint(1, 151)))
        elif args.input.lower() == "0":
            pkmn = db.get_one(str(random.randint(1, 151)))
        else:
            pkmn = db.get_one(args.input.lower())
    except db.PokemonNotFoundError:
        return "Pokemon not found!"

    # Create printable dictionary based on arguments passed
    pokemon_dict = create_dict(pkmn, args.weakness, args.pokedex, args.type, args.evolution)
    # Return result to table template
    return render_template('pokemon.html', result=pokemon_dict)


if __name__ == '__main__':
    app.run(debug=True)
