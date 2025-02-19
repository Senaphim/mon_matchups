import json

from pokemon import Pokemon
from moves import Moves

def main():
    pokemon = Pokemon()
    team = import_team()
    defensive_coverage(team, pokemon)

def import_team():
    with open("./team.json", mode="r", encoding="utf-8") as team_file:
        team = json.load(team_file)
    return team

def defensive_coverage(team, pokemon):
    for mon in team.keys():
        types = pokemon.types(team[mon]["name"], team[mon]["form"])
        resists = type_resist_coverage(types)

if __name__ == "__main__":
    main()

