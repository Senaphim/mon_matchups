import unittest

from pokemon import Pokemon
from moves import Moves
from pTypes import P_Types, str_type_to_enum

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

class testTypes(unittest.TestCase):
    def test_str_to_enum(self):
        ptype = P_Types.GRASS
        self.assertEqual(ptype, str_type_to_enum("Grass"))

    def test_bad_str_to_enum(self):
        self.assertEqual(None, str_type_to_enum("Bad String"))
