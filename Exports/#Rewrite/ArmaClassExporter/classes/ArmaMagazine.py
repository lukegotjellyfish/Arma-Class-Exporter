import sys
from ArmaU import ArmaU
from ArmaAmmo import ArmaAmmo


class ArmaMagazine(ArmaU):
    def __init__(self, magazine_class_name: str, magazine_dict_path: str):
        """
        Class to get Magazine values

        Parameters:
            magazine_class_name (str): The class name of the magazine
            magazine_dict_path (str): The absolute file path to the dict
        """
        # Send the module details to the super class
        super().__init__(magazine_class_name, magazine_dict_path)

        # Necessary Values
        self.ammo_class_name = self.arma_module.get("ammo")
        self.init_speed = self.arma_module.get("initspeed")

        # If the magazine actually has an Ammo...
        if self.ammo_class_name:
            # Create a new instance of ArmaAmmo
            # TODO: Add backup folders to check (or default check other export folders)?
            ammo_dict_path = magazine_dict_path.replace(magazine_class_name + ".py", self.ammo_class_name + ".py")
            self.ammo = ArmaAmmo(self.ammo_class_name, ammo_dict_path)