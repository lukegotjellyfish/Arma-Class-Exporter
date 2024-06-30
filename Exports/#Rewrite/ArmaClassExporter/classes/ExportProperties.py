import importlib.util


class ExportProperties:
    def __init__(self, _module_name: str, _module_path: str, _backup_paths: list[str] | None = None):
        """
        Loads the Arma class dict and assigns properties
        Backup paths are used to search for the dict if the target export does not (if a full export was not done)
         \ contain the dict.

        
        Parameters:
            _module_name (str): The name of the dict
            _module_path (str): The absolute file path to the dict
            _backup_paths (list[str]|None): An optional list of backup paths to search for the dict
        """
        # Load module
        spec = importlib.util.spec_from_file_location(_module_name, _module_path)
        self.arma_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.arma_module)
        self.arma_module = self.arma_module.d
        # CSV Export text
        self.csv_export = []

    def load_properties(self, properties_mapping: dict):
        """
        Assigns properties to the class

        Parameters:
            properties_mapping (dict): The properties to assign
        """
        for attr, key in properties_mapping.items():
            nested_keys = key if isinstance(key, list) else [key]
            value = self.arma_module
            try:
                for nested_key in nested_keys:
                    value = value.get(nested_key, {})
            except AttributeError:
                value = None

            setattr(self, attr, value)
