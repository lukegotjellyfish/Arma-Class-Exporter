import unittest
import sys

sys.path.append('..')
from ArmaLoadedWeapon import ArmaLoadedWeapon


class TestArma(unittest.TestCase):
    def test_ArmaLoadedWeapon(self):
        # Create an instance of ArmaMagazine
        arma_instance = ArmaLoadedWeapon("example_weapon_class", "example_weapon_class.py",
                                         "example_magazine_class", "example_magazine_class.py")
        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.weapon.init_speed, 730, "init_speed should be 730")
        self.assertEqual(arma_instance.weapon.can_lock, 0, "can_lock should be 0")
        self.assertEqual(arma_instance.magazine.ammo_class_name, "example_ammo_class", "ammo_class_name should be example_ammo_class")
        self.assertEqual(arma_instance.get_hit(0), 11.0, "get_hit should return 11.0")
        self.assertEqual(arma_instance.get_hit(100), 9.373581678628325, "get_hit should return 9.373581678628325")
        self.assertEqual(arma_instance.get_hit(1000), 2.2208616979412095, "get_hit should return 2.2208616979412095")

        arma_instance.set_magazine()

if __name__ == '__main__':
    unittest.main()
