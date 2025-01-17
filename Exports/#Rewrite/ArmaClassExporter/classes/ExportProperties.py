import importlib.util
import os

class ExportProperties:
    def __init__(self, _dict_name: str, _dict_path: str, _backup_paths: list[str] | None = None):
        """
        Loads the Arma class dict and assigns properties
        Backup paths are used to search for the dict if the target export does not (if a full export was not done)
         > contain the dict.

        
        Parameters:
            _dict_name (str): The name of the dict
            _dict_path (str): The absolute file path to the dict
            _backup_paths (list[str]|None): An optional list of backup paths to search for the dict
        """
        # Load module
        spec = importlib.util.spec_from_file_location(_dict_name, _dict_path)
        self.arma_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.arma_module)
        self.arma_module = self.arma_module.d
        # CSV Export text
        self.csv_export = []

        # Meta vars
        # Figure out splitting paths to get parent folder consistently with \ /
        # tbh just if \ in x then split by \ else / then [-3] for 2nd last (export parent folder)
        self.target_folder = _dict_path
        # os.path.
        # inputos.path.split(_dict_path)[:1]
        # TODO add backup_folders feature for non-full ClassExports
        # self.backup_folders = []