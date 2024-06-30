import sys
from Arma import Arma
from decimal import Decimal
import importlib.util
import os

sys.path.append('..')
from decimal import Decimal


class ArmaAmmo(Arma):
    def __init__(self, ammo_mod_folder, ammo_class_name):
        cwd = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

        # Construct path to magazine dict
        ammo_module_path = os.path.join(cwd, "SQF-Class-Exports", ammo_mod_folder, "Magazines", f"{ammo_class_name}.py")

        # Send the module details to the super class
        super().__init__(ammo_class_name, ammo_module_path)

        properties_mapping = {
            "cartridge": "displaynameshort",  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#cartridge
            "hit": "hit",  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#hit
            "explosive": "explosive",  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#explosive
        }
        self.load_properties(properties_mapping)

        #Assign Properties