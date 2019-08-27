import argparse
import random
from flask import Flask, render_template
import db
import type_and_weakness_search


app = Flask(__name__)


class Pokemon:
    def __init__(self, name, pokedex, weakness, type, evolution):
        self.name = name
        self.pokedex = pokedex
        self.weakness = weakness
        self.type = type
        self.evolution = evolution


def create_dict(pkmn, weakness, pokedex, type, evolution):
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
    parser.add_argument("--typesearch", help="searches all pokemon and returns a random pokemon that has that type", action="store_true")
    parser.add_argument("--weaknesssearch", help="searches all pokemon and returns a random pokemon that has that weakness", action="store_true")
    args = parser.parse_args()  # Parse arguments

    try:
        if args.input.lower() == "random":
            pkmn = db.get_one(str(random.randint(1, 151)))
        elif args.input.lower() == "0":
            pkmn = db.get_one(str(random.randint(1, 151)))
        elif args.typesearch:
            pkmn = type_and_weakness_search.search_by_type(args.input)
        elif args.weaknesssearch:
            pkmn = type_and_weakness_search.search_by_weakness(args.input)
        else:
            pkmn = db.get_one(args.input.lower())
    except db.PokemonNotFoundError:
        return "No result found!"

    pokemon_dict = create_dict(pkmn, args.weakness, args.pokedex, args.type, args.evolution)
    return render_template('pokemon.html', result=pokemon_dict)
    

if __name__ == '__main__':
    app.run(debug=True)

