import sys

sys.path.append('..')
import unittest
import example_weapon_class
from unittest.mock import MagicMock
from ArmaAmmo import ArmaAmmo


class TestArma(unittest.TestCase):
    def test_ArmaAmmo(self):
        # Create an instance of Arma
        arma_instance = ArmaAmmo("example_ammo_class", "example_ammo_class.py")

        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.hit, 11)
        self.assertEqual(arma_instance.explosive, 0)
        self.assertEqual(arma_instance.eventhandlers, {})


if __name__ == '__main__':
    unittest.main()
