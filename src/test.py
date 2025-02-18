import unittest

from pokemon import Pokemon
from moves import Moves

class testPokemon(unittest.TestCase):
    def test_init(self):
        pokemon = Pokemon()
        self.assertEqual(1, pokemon._init_ok)

    def test_type_mono(self):
        pokemon = Pokemon()
        types = ["Grass", ""]
        self.assertEqual(types, pokemon.types("Chikorita", ""))

    def test_type_dual(self):
        pokemon = Pokemon()
        types = ["Fire", "Flying"]
        self.assertEqual(types, pokemon.types("Charizard", ""))

class testMoves(unittest.TestCase):
    def test_init(self):
        moves = Moves()
        self.assertEqual(1, moves._init_ok)
