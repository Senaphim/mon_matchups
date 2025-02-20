import json

from pokemon import Pokemon
from moves import Moves
from pTypes import get_mon_resists, get_move_coverage, combine_types, count_types
from prettyPrint import defensive_table_str

def main():
    pokemon_df = Pokemon()
    move_df = Moves()
    team = import_team()
    mon_resists, combined_resists, count_resists = defensive_coverage(team, pokemon_df)
    mon_coverage, combined_coverage = offensive_coverage(team, move_df)
    defensive_table_str(team, mon_resists, combined_resists, count_resists)

def import_team():
    with open("./team.json", mode="r", encoding="utf-8") as team_file:
        team = json.load(team_file)
    return team

def defensive_coverage(team, pokemon_df):
    mon_resists = []
    for mon in team.keys():
        types = pokemon_df.types(team[mon]["name"], team[mon]["form"])
        mon_resists.append(get_mon_resists(types))
    mon_resists = [x for x in mon_resists if x is not None]
    combined_resists = combine_types(mon_resists, atk=False)
    count_resists = count_types(mon_resists, atk=False)
    return mon_resists, combined_resists, count_resists

def offensive_coverage(team, move_df):
    mon_coverage = []
    for mon in team.keys():
        move_coverage = []
        move_dict = team[mon]["moves"]
        for move in move_dict.keys():
            mv_type = move_df.move_type(move_dict[move]["name"], move_dict[move]["type"])
            move_coverage.append(get_move_coverage(mv_type))
        move_coverage = [x for x in move_coverage if x is not None]
        if len(move_coverage) == 0:
            combined_mv_coverage = None
        else:
            combined_mv_coverage = combine_types(move_coverage)
        mon_coverage.append(combined_mv_coverage)
    mon_coverage = [x for x in mon_coverage if x is not None]
    combined_coverage = combine_types(mon_coverage)
    return mon_coverage, combined_coverage

if __name__ == "__main__":
    main()

