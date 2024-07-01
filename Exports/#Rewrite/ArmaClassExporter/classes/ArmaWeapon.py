from ArmaU import ArmaU


class ArmaWeapon(ArmaU):
    def __init__(self, weapon_class_name, weapon_class_path):
        # Send the module details to the super class
        super().__init__(weapon_class_name, weapon_class_path)

        properties_mapping = {
            "magazines": "magazines",
            "init_speed": "initspeed", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#initSpeed.3D0
            "can_lock": "canlock", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#canLock=2
            "firemodes": "modes", # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#modes[]=_{%22this%22}

            # Infantry weapon parameters
            "slots_info": "weaponslotsinfo",
            "slot": ["weaponslotsinfo","allowedslots"],
            "mass": ["weaponslotsinfo","mass"],
            "comptabile_optics": ["weaponslotsinfo","cowsslot","compatibleitems"],
            "compatible_muzzles": ["weaponslotsinfo","muzzleslot","compatibleitems"],
            "compatible_pointers": ["weaponslotsinfo","pointerslot","compatibleitems"],
            "compatible_underbarrel_attachments": ["weaponslotsinfo","underbarrelslot","compatibleitems"],
        }
        self.load_properties(properties_mapping)