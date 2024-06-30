import sys

sys.path.append('..')
import unittest
import mock_module
from unittest.mock import MagicMock
from Arma import Arma


class TestArma(unittest.TestCase):
    def test_load_properties(self):
        # Create an instance of Arma
        arma_instance = Arma("mock_module", "mock_module.py")

        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.display_name, "Test Display Name")
        self.assertEqual(arma_instance.model, "Test Model")
        self.assertEqual(arma_instance.scope, "Test Scope")
        self.assertEqual(arma_instance.eventhandlers, {})
        #self.assertEqual(arma_instance.item_info_type, "Test Type")
        #self.assertEqual(arma_instance.item_info_mass, 100)
        #self.assertIsNone(arma_instance.item_info_hitpoints_protection_info)
        #self.assertEqual(arma_instance.item_info_allowed_slots, ["slot1", "slot2"])
        #self.assertEqual(arma_instance.item_info_general_macro, "Test Macro")
        #self.assertEqual(arma_instance.item_info_model_sides, ["side1", "side2"])



if __name__ == '__main__':
    unittest.main()
