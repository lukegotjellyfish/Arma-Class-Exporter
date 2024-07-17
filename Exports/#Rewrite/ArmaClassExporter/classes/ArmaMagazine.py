import os
import sys
from ArmaU import ArmaU
from ArmaAmmo import ArmaAmmo


@staticmethod
def check_file_exists(self, name, _type):
    for folder in [*[self.mod], *self.backup_folders]:
        # If weapon dict file exists
        for configType in _type:
            if os.path.isfile(f"{self.cwd}/SQF-Class-Exports/{folder}/{configType}/{name}.py"):
                return [folder, configType]
    print(
        f"\33[31m{name} could not be found in {[*[self.mod], *self.backup_folders]} with configType(s) {_type}\33[0m")
    return False

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
            #try: something i cant remember
            ammo_dict_path = magazine_dict_path.replace(magazine_class_name + ".py", self.ammo_class_name + ".py")

            """
             NOTE: The file should probably not be looked for outside of this export
                    since different exports may give wildly different results. Other
                    mods that are loaded can affect the values of classes directly or
                    though inheritance of modified parent classes.
                    
            """
            self.ammo = ArmaAmmo(self.ammo_class_name, ammo_dict_path)