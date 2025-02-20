HEADER = "#################\n# TEAM ANALYSIS #\n#################\n\n"
TABLE_HEADER = "  Nor |  Fir |  Wat |  Ele |  Gra |  Ice |  Fig |  Poi |  Gro |  Fly |  Psy |  Bug |  Roc |  Gho |  Dra |  Dar |  Ste |  Fai | Pokemon\n"
TABLE_BREAK = "------|"*18 + "---------\n"
TABLE_TOP = "-"*len(TABLE_HEADER) + "\n"

def defensive_table_str(team, mon_resists, combined_resists, count_resists):
    mon_list = []
    for mon in team.keys():
        mon_list.append(team[mon]["name"])
    resist_strings = []
    for i in range(len(mon_resists)):
        resist_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in mon_resists[i]])
        resist_string += "| " + mon_list[i]
        resist_strings.append(resist_string)
    combined_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in combined_resists])
    combined_string += "| Best"
    count_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in count_resists])
    count_string += "| Count"
    table = "DEFENSIVE ANALYSIS\n\n"
    table += TABLE_TOP + TABLE_HEADER + TABLE_BREAK
    table_body = "\n".join(resist_strings)
    table += table_body + "\n"
    table += TABLE_BREAK
    table += combined_string + "\n"
    table += TABLE_BREAK
    table += count_string + "\n"
    table += TABLE_TOP
    print(table)
