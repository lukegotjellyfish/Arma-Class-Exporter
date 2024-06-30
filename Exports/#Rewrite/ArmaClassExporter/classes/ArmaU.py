from ExportProperties import ExportProperties
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

        properties_mapping = {
            "scope_arsenal": "scopearsenal",
            "display_name": "displayname",
            "display_name_short": "displaynameshort", # These two parameters probably need to be moved
            "showtoplayer": "showtoplayer",           #  but it's fine for now
        }
        self.load_properties(properties_mapping)