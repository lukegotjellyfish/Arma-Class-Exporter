from Arma import Arma


class ArmaAmmo(Arma):
    def __init__(self, ammo_class_name, ammo_dict_path):
        """
        Class to get Ammo values, to be used by ArmaMagazine

        Parameters:
            ammo_class_name (str): The class name of the magazine
            ammo_mod_folder (str): The mod folder of the magazine
        """
        # Send the module details to the super class
        super().__init__(ammo_class_name, ammo_dict_path)

        # Necessary Values
        self.hit = self.arma_module.get("hit")
        self.indirect_hit = self.arma_module.get("indirecthit")
        self.explosive = self.arma_module.get("explosive")
        self.air_resistance = abs(self.arma_module.get("airfriction"))
        self.typical_speed = self.arma_module.get("typicalspeed")

        #Assign Properties