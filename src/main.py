import json

from pokemon import Pokemon
from moves import Moves
from pTypes import get_mon_resists

def main():
    pokemon = Pokemon()
    team = import_team()
    mon_resists, combined_resists = defensive_coverage(team, pokemon)

def import_team():
    with open("./team.json", mode="r", encoding="utf-8") as team_file:
        team = json.load(team_file)
    return team

def defensive_coverage(team, pokemon):
    mon_resists = []
    for mon in team.keys():
        types = pokemon.types(team[mon]["name"], team[mon]["form"])
        mon_resists.append(get_mon_resists(types))
    mon_resists = [x for x in mon_resists if x is not None]
    combined_resists = []
    for i in range(len(mon_resists[0])):
        type_resist = []
        for res_list in mon_resists:
            type_resist.append(res_list[i])
        combined_resists.append(min(type_resist))
    return mon_resists, combined_resists

if __name__ == "__main__":
    main()

