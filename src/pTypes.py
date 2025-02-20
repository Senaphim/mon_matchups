from enum import Enum 

# ATKv DEF> Nor Fir Wat Ele Gra Ice Fig Poi Gro Fly Psy Bug Roc Gho Dra Dar Ste Fai
MATCHUPS = [
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, .5,  0,  1,  1, .5,  1], # Nor
            [1, .5, .5,  1,  2,  2,  1,  1,  1,  1,  1,  2, .5,  1, .5,  1,  2,  1], # Fir
            [1,  2, .5,  1, .5,  1,  1,  1,  2,  1,  1,  1,  2,  1, .5,  1,  1,  1], # Wat
            [1,  1,  2, .5, .5,  1,  1,  1,  0,  2,  1,  1,  1,  1, .5,  1,  1,  1], # Ele
            [1, .5,  2,  1, .5,  1,  1, .5,  2, .5,  1, .5,  2,  1, .5,  1, .5,  1], # Gra
            [1, .5, .5,  1,  2, .5,  1,  1,  2,  2,  1,  1,  1,  1,  2,  1, .5,  1], # Ice
            [2,  1,  1,  1,  1,  2,  1, .5,  1, .5, .5, .5,  2,  0,  1,  2,  2, .5], # Fig
            [1,  1,  1,  1,  2,  1,  1, .5, .5,  1,  1,  1, .5, .5,  1,  1,  0,  2], # Poi
            [1,  2,  1,  2, .5,  1,  1,  2,  1,  0,  1, .5,  2,  1,  1,  1,  2,  1], # Gro
            [1,  1,  1, .5,  2,  1,  2,  1,  1,  1,  1,  2, .5,  1,  1,  1, .5,  1], # Fly
            [1,  1,  1,  1,  1,  1,  2,  2,  1,  1, .5,  1,  1,  1,  1,  0, .5,  1], # Psy
            [1, .5,  1,  1,  2,  1, .5, .5,  1, .5,  2,  1,  1, .5,  1,  2, .5, .5], # Bug
            [1,  2,  1,  1,  1,  2, .5,  1, .5,  2,  1,  2,  1,  1,  1,  1, .5,  1], # Roc
            [0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  2,  1, .5,  1,  1], # Gho
            [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1, .5,  0], # Drg
            [1,  1,  1,  1,  1,  1, .5,  1,  1,  1,  2,  1,  1,  2,  1, .5,  1, .5], # Dar
            [1, .5, .5, .5,  1,  2,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1, .5,  2], # Ste
            [1, .5,  1,  1,  1,  1,  2, .5,  1,  1,  1,  1,  1,  1,  2,  2, .5,  1]  # Fai
           ]

class P_Types(Enum):
    NORMAL = 0 
    FIRE = 1 
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

def str_type_to_enum(str_type):
    match str_type:
        case "Normal":
            return P_Types.NORMAL
        case "Fire":
            return P_Types.FIRE
        case "Water":
            return P_Types.WATER
        case "Electric":
            return P_Types.ELECTRIC
        case "Grass":
            return P_Types.GRASS
        case "Ice":
            return P_Types.ICE
        case "Fighting":
            return P_Types.FIGHTING
        case "Poison":
            return P_Types.POISON
        case "Ground":
            return P_Types.GROUND
        case "Flying":
            return P_Types.FLYING
        case "Psychic":
            return P_Types.PSYCHIC
        case "Bug":
            return P_Types.BUG
        case "Rock":
            return P_Types.ROCK
        case "Ghost":
            return P_Types.GHOST
        case "Dragon":
            return P_Types.DRAGON
        case "Dark":
            return P_Types.DARK
        case "Steel":
            return P_Types.STEEL
        case "Fairy":
            return P_Types.FAIRY
        case _:
            return None

def get_type_resists(p_type):
    resist_list = []
    for atk_list in MATCHUPS:
        resist_list.append(atk_list[p_type.value])
    return resist_list

def get_mon_resists(type_list):
    all_resists = []
    for p_type in type_list:
        if p_type is not None:
            all_resists.append(get_type_resists(p_type))
    combined_resists = []
    if len(all_resists) == 0:
        return None
    elif len(all_resists) == 2:
        for i in range(len(all_resists[0])):
            combined_resists.append(all_resists[0][i] * all_resists[1][i])
    else:
        combined_resists = all_resists[0]
    return combined_resists

def get_move_coverage(mv_type):
    if mv_type is None:
        return None
    return MATCHUPS[mv_type.value]

def combine_types(type_lists, atk=True):
    combined_type = []
    for i in range(len(type_lists[0])):
        each_type = []
        for type_list in type_lists:
            each_type.append(type_list[i])
        if atk:
            combined_type.append(max(each_type))
        else:
            combined_type.append(min(each_type))
    return combined_type

