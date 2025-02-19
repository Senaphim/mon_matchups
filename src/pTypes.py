from enum import Enum 

#ATKv DEF>  Nor Fir Wat Ele Gra Ice Fig Poi Gro Fly Psy Bug Roc Gho Dra Dar Ste Fai
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
