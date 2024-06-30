from Arma import Arma
from decimal import Decimal
import importlib.util
import os
import sys
sys.path.append('..')
import eval_param_value as epv


class ArmaWeapon(Arma):
    def __init__(self, weapon_mod_folder, weapon_class_name):

        cwd = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

        # Construct path to weapon dict
        weapon_module_path = os.path.join(cwd, "SQF-Class-Exports", weapon_mod_folder, "Weapons", f"{weapon_class_name}.py")

        # Send the module details to the super class
        super().__init__(weapon_class_name, weapon_module_path)

        properties_mapping = {
            "init_speed": "initspeed", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#initSpeed.3D0
            "can_lock": "canlock", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#canLock=2
            "firemodes": "modes", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#modes[]=_{%22this%22}
        }
        self.load_properties(properties_mapping)