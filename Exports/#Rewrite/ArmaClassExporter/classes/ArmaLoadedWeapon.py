from decimal import Decimal

from ArmaWeapon import ArmaWeapon
from ArmaMagazine import ArmaMagazine


class ArmaLoadedWeapon:
    def __init__(self, magazine_class_name: str, magazine_mod_folder: str):
        """
        Class to inherit for Loaded weapon types.
        As weapon types differ in features, but magazines don't, this class is used to abstract them.

        Parameters:
            magazine_class_name (str): The class name of the magazine
            magazine_mod_folder (str): The mod folder of the magazine
        """
        self.magazine = ArmaMagazine(magazine_class_name, magazine_mod_folder)

