import unittest

from pokemon import Pokemon
from moves import Moves

class testPokemon(unittest.TestCase):
    def test_init(self):
        pokemon = Pokemon()
        self.assertEqual(1, pokemon._init_ok)

class testMoves(unittest.TestCase):
    def test_init(self):
        moves = Moves()
        self.assertEqual(1, moves._init_ok)
