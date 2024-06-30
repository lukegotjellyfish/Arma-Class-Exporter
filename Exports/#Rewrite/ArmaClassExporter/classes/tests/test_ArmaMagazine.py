import sys

sys.path.append('..')
import unittest
from ArmaMagazine import ArmaMagazine


class TestArma(unittest.TestCase):
    def test_ArmaMagazine(self):
        # Create an instance of ArmaMagazine
        arma_instance = ArmaMagazine("exampmle_magazine_class", "example_magazine_class.py")

        # Check that each attribute has been correctly set
        self.assertEqual(arma_instance.ammo_class_name, "B_762x39_Ball_Green_F")



if __name__ == '__main__':
    unittest.main()
