from decimal import Decimal

from ArmaWeapon import ArmaWeapon
from ArmaMagazine import ArmaMagazine


class ArmaLoadedWeapon:
    def __init__(self, weapon_class_name: str, weapon_class_path: str,
                 magazine_class_name: str, magazine_class_path: str):
        """
        Class to inherit for Loaded weapon types.

        Parameters:
            weapon_class_name (str): The class name of the weapon
            weapon_class_path (str): The absolute file path to the weapon dict
            magazine_class_name (str): The class name of the magazine
            magazine_class_path (str): The absolute file path to the magazine dict
        """
        #
        self.weapon = ArmaWeapon(weapon_class_name, weapon_class_path)
        self.magazine = ArmaMagazine(magazine_class_name, magazine_class_path)

        # Player weapon if scope_arsenal != 0 (should be None/2/1)
