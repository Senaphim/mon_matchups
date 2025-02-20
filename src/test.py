import unittest

from pokemon import Pokemon
from moves import Moves
from pTypes import (P_Types, str_type_to_enum, get_type_resists,
    get_mon_resists, get_move_coverage, combine_types)

class testPokemon(unittest.TestCase):
    def test_init(self):
        pokemon = Pokemon()
        self.assertEqual(1, pokemon._init_ok)

    def test_type_mono(self):
        pokemon = Pokemon()
        types = [P_Types.GRASS, None]
        self.assertEqual(types, pokemon.types("Chikorita", ""))

    def test_type_dual(self):
        pokemon = Pokemon()
        types = [P_Types.FIRE, P_Types.FLYING]
        self.assertEqual(types, pokemon.types("Charizard", ""))

class testMoves(unittest.TestCase):
    def test_init(self):
        moves = Moves()
        self.assertEqual(1, moves._init_ok)

    def test_move_type(self):
        moves = Moves()
        move = "Flamethrower"
        self.assertEqual(P_Types.FIRE, moves.move_type(move))

    def test_move_type_forced(self):
        moves = Moves()
        move = "Hyper Voice"
        mv_type = "Fairy"
        self.assertEqual(P_Types.FAIRY, moves.move_type(move, mv_type))

    def test_move_type_status(self):
        moves = Moves()
        move = "Poison Powder"
        self.assertEqual(None, moves.move_type(move))

class testTypes(unittest.TestCase):
    def test_str_to_enum(self):
        ptype = P_Types.GRASS
        self.assertEqual(ptype, str_type_to_enum("Grass"))

    def test_bad_str_to_enum(self):
        self.assertEqual(None, str_type_to_enum("Bad String"))

    def test_resist_list(self):
        resist_list = [1, 2, .5, .5, .5, 2, 1, 2, .5, 2, 1, 2, 1, 1, 1, 1, 1, 1]
        self.assertEqual(resist_list, get_type_resists(P_Types.GRASS))

    def test_mon_resists_mono(self):
        types = [P_Types.GRASS, None]
        resist_list = [1, 2, .5, .5, .5, 2, 1, 2, .5, 2, 1, 2, 1, 1, 1, 1, 1, 1]
        self.assertEqual(resist_list, get_mon_resists(types))
    
    def test_mon_resists_dual(self):
        types = [P_Types.FIRE, P_Types.WATER]
        resist_list = [1, .25, 1, 2, 1, .25, 1, 1, 2, 1, 1, .5, 2, 1, 1, 1, .25, .5]
        self.assertEqual(resist_list, get_mon_resists(types))

    def test_mon_resists_none(self):
        types = [None, None]
        self.assertEqual(None, get_mon_resists(types))

    def test_move_coverage(self):
        coverage_list = [1,  1,  1, .5,  2,  1,  2,  1,  1,  1,  1,  2, .5,  1,  1,  1, .5,  1]
        self.assertEqual(coverage_list, get_move_coverage(P_Types.FLYING))

    def test_move_coverage_none(self):
        self.assertEqual(None, get_move_coverage(None))

    def test_combine_types_atk(self):
        types_to_combine = [
            [1,  1,  1,  1,  2,  1,  1, .5, .5,  1,  1,  1, .5, .5,  1,  1,  0,  2], 
            [1,  2,  1,  2, .5,  1,  1,  2,  1,  0,  1, .5,  2,  1,  1,  1,  2,  1]
        ]
        combined = [1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2]
        self.assertEqual(combined, combine_types(types_to_combine))

    def test_combine_types_def(self):
        types_to_combine = [
            [1,  1,  1,  1,  2,  1,  1, .5, .5,  1,  1,  1, .5, .5,  1,  1,  0,  2], 
            [1,  2,  1,  2, .5,  1,  1,  2,  1,  0,  1, .5,  2,  1,  1,  1,  2,  1]
        ]
        combined = [1, 1, 1, 1, .5, 1, 1, .5, .5, 0, 1, .5, .5, .5, 1, 1, 0, 1]
        self.assertEqual(combined, combine_types(types_to_combine, atk=False))
