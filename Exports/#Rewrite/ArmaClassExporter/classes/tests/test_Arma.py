import sys

sys.path.append('..')
import unittest
from Arma import Arma


class TestArma(unittest.TestCase):
    def test_arma(self):
        # Create an instance of Arma
        arma_instance = Arma("example_weapon_class", "example_weapon_class.py")

        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.display_name, "AK-12 7.62 mm")
        self.assertEqual(arma_instance.model, "A3/Weapons_F_Exp/Rifles/AK12/AK12_F.p3d")
        self.assertEqual(arma_instance.scope, 2)
        self.assertEqual(arma_instance.eventhandlers, {})
        #self.assertEqual(arma_instance.item_info_type, "Test Type")
        #self.assertEqual(arma_instance.item_info_mass, 100)
        #self.assertIsNone(arma_instance.item_info_hitpoints_protection_info)
        #self.assertEqual(arma_instance.item_info_allowed_slots, ["slot1", "slot2"])
        #self.assertEqual(arma_instance.item_info_general_macro, "Test Macro")
        #self.assertEqual(arma_instance.item_info_model_sides, ["side1", "side2"])



if __name__ == '__main__':
    unittest.main()
