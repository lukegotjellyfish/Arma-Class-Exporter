import unittest
import sys

sys.path.append('..')
from ArmaLoadedWeapon import ArmaLoadedWeapon


class TestArma(unittest.TestCase):
    def test_ArmaLoadedWeapon(self):
        # Create an instance of ArmaMagazine
        arma_instance = ArmaLoadedWeapon("example_weapon_class", "example_weapon_class.py",
                                         "exampmle_magazine_class", "example_magazine_class.py")

        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.weapon.init_speed, 730)
        self.assertEqual(arma_instance.weapon.can_lock, 0)
        self.assertEqual(arma_instance.magazine.ammo_class_name, "B_762x39_Ball_Green_F")



if __name__ == '__main__':
    unittest.main()
