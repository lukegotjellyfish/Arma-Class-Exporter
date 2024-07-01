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

        properties_mapping = {
            "hit": "hit",  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#hit
            "explosive": "explosive",  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#explosive
        }
        self.load_properties(properties_mapping)

        #Assign Properties