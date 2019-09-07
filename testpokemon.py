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
    pokemon_choice = Pokemon(**pkmn)
    choice_dict = {'Name': pokemon_choice.name.title()}
    all_args = not any([weakness, type, evolution, pokedex])
    if pokedex or all_args:
        choice_dict['Pokedex #'] = pokemon_choice.pokedex
    if type or all_args:
        choice_dict['Type'] = ', '.join(pokemon_choice.type).title()
    if weakness or all_args:
        choice_dict['Weakness'] = ', '.join(pokemon_choice.weakness).title()
    if evolution or all_args:
        choice_dict['Evolution'] = ((str(pokemon_choice.evolution).title()).strip('{')).strip('}')
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
            pokemon_dict = create_dict(pkmn, args.weakness, args.pokedex, args.type, args.evolution)
            return render_template('pokemon.html', result=pokemon_dict)
        elif args.input.lower() == "0":
            pkmn = db.get_one(str(random.randint(1, 151)))
            pokemon_dict = create_dict(pkmn, args.weakness, args.pokedex, args.type, args.evolution)
            return render_template('pokemon.html', result=pokemon_dict)
        elif args.typesearch:
            pkmn_multiple = type_and_weakness_search.search_by_type(args.input)
            return type_and_weakness_search.create_dict_multiple(pkmn_multiple, args.weakness, args.pokedex, args.type, args.evolution)
            #return render_template('pokemon_multiple.html', result=pokemon_dict_multiple)
        elif args.weaknesssearch:
            return type_and_weakness_search.search_by_weakness(args.input)
            # return type_and_weakness_search.create_dict_multiple(pkmn_multiple, args.weakness, args.pokedex, args.type, args.evolution)
            #return render_template('pokemon_multiple.html', result=pokemon_dict_multiple)
        else:
            pkmn = db.get_one(args.input.lower())
            pokemon_dict = create_dict(pkmn, args.weakness, args.pokedex, args.type, args.evolution)
            return render_template('pokemon.html', result=pokemon_dict)
    except db.PokemonNotFoundError:
        return "No result found!"


if __name__ == '__main__':
    app.run(debug=True)

