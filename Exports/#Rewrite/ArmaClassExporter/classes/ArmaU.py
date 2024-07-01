from Arma import Arma

class ArmaU(Arma):
    def __init__(self, _dict_name, _dict_path):
        """
        Class to get values of classes that are interactable with the user. probably.

        Parameters:
            _dict_name (str): The name of the dict
            _dict_path (str): The absolute file path to the dict
        """
        # Send the module details to the super class
        super().__init__(_dict_name, _dict_path)

        # Necessary Values
        self.scope_arsenal = self.arma_module.get("scopearsenal", 2)
        self.display_name = self.arma_module.get("displayname")
        self.display_name_short = self.arma_module.get("displaynameshort")
        self.show_to_player = self.arma_module.get("showtoplayer")