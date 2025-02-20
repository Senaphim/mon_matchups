TABLE_HEADER = "  Nor |  Fir |  Wat |  Ele |  Gra |  Ice |  Fig |  Poi |  Gro |  Fly |  Psy |  Bug |  Roc |  Gho |  Dra |  Dar |  Ste |  Fai | Pokemon\n"
TABLE_BREAK = "------|"*18 + "---------\n"
TABLE_TOP = "-"*len(TABLE_HEADER) + "\n"

def defensive_table_str(team, mon_rows, combined_rows, count_rows):
    mon_list = []
    for mon in team.keys():
        mon_list.append(team[mon]["name"])
    row_strings = []
    for i in range(len(mon_rows)):
        row_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in mon_rows[i]])
        row_string += "| " + mon_list[i]
        row_strings.append(row_string)
    combined_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in combined_rows])
    combined_string += "| Best"
    count_string = "|".join([" "*(5-len(str(x))) + str(x) + " " for x in count_rows])
    count_string += "| Count"
    table = TABLE_TOP + TABLE_HEADER + TABLE_BREAK
    table_body = "\n".join(row_strings)
    table += table_body + "\n"
    table += TABLE_BREAK
    table += combined_string + "\n"
    table += TABLE_BREAK
    table += count_string + "\n"
    table += TABLE_TOP
    return table
