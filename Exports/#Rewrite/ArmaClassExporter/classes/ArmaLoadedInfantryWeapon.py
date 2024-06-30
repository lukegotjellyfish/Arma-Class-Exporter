from decimal import Decimal

from ArmaInfantryWeapon import ArmaInfantryWeapon
from ArmaMagazine import ArmaMagazine
from ArmaLoadedWeapon import ArmaLoadedWeapon

class ArmaLoadedWeaponSharedProperties(ArmaLoadedWeapon):
    def __init__(self, weapon_class_name: str, weapon_mod_folder: str,
                 magazine_class_name: str, magazine_mod_folder: str):
        # Send the module details to the super class
        super().__init__(magazine_class_name, magazine_mod_folder)

        # Class Properties
        self.weapon = ArmaInfantryWeapon(weapon_mod_folder, weapon_class_name)