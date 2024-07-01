from ArmaU import ArmaU


class ArmaWeapon(ArmaU):
    def __init__(self, weapon_class_name, weapon_class_path):
        # Send the module details to the super class
        super().__init__(weapon_class_name, weapon_class_path)

        # Necessary Values
        self.magazines = self.arma_module.get("magazines")
        self.init_speed = self.arma_module.get("initspeed")
        self.can_lock = self.arma_module.get("canlock")
        self.firemodes = self.arma_module.get("modes")
        # Infantry weapons
        if self.scope_arsenal != 0:
            self.slots_info = self.arma_module.get("weaponslotsinfo")
            if self.slots_info is not None:
                self.slot = self.slots_info.get("allowedslots")
                self.mass = self.slots_info.get("mass")
                self.compatible_mobile_optics = self.slots_info.get("cowsslot").get("compatibleitems")
                self.compatible_muzzles = self.slots_info.get("muzzleslot").get("compatibleitems")
                self.compatible_pointers = self.slots_info.get("pointerslot").get("compatibleitems")
                self.compatible_underbarrel_attachments = self.slots_info.get("underbarrelslot").get("compatibleitems")