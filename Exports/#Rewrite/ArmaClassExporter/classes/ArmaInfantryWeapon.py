import contextlib
from ArmaWeapon import ArmaWeapon
import sys
sys.path.append('..')
import eval_param_value as epv


# Vehicle weapons and launchers
class ArmaInfantryWeapon(ArmaWeapon):
    def __init__(self, weapon_mod_folder, weapon_class_name):
        super().__init__(weapon_mod_folder, weapon_class_name)
        self.slots_info = None
        properties_mapping = {
            "slots_info": "weaponslotsinfo",
            "slot": ["weaponslotsinfo","allowedslots"],
            "mass": ["weaponslotsinfo","mass"],
            "comptabile_optics": ["weaponslotsinfo","cowsslot","compatibleitems"],
            "compatible_muzzles": ["weaponslotsinfo","muzzleslot","compatibleitems"],
            "compatible_pointers": ["weaponslotsinfo","pointerslot","compatibleitems"],
            "compatible_underbarrel_attachments": ["weaponslotsinfo","underbarrelslot","compatibleitems"],
        }
        self.load_properties(properties_mapping)