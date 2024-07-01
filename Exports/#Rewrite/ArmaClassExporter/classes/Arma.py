from ExportProperties import ExportProperties

class Arma(ExportProperties):
    def __init__(self, _dict_name, _dict_path):
        """
        Top level class to get universal class values

        Parameters:
            _dict_name (str): The name of the dict
            _dict_path (str): The absolute file path to the dict
        """
        # Send the module details to the super class
        super().__init__(_dict_name, _dict_path)

        # Necessary values
        self.scope = self.arma_module.get("scope")