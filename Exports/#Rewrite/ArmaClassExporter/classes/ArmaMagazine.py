import contextlib

from Arma import Arma
from ArmaAmmo import ArmaAmmo
from decimal import Decimal
import importlib.util
import os
import sys
from Arma import Arma
sys.path.append('..')


class ArmaMagazine(Arma):
    def __init__(self, magazine_class_name, magazine_mod_folder):
        cwd = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

        # Construct path to magazine dict
        magazine_module_path = os.path.join(cwd, "SQF-Class-Exports", magazine_mod_folder, "Magazines", f"{magazine_class_name}.py")

        # Send the module details to the super class
        super().__init__(magazine_class_name, magazine_module_path)

        # Init variables
        self.ammo_class_name = None

        # Find Ammo name with magazine parameters
        properties_mapping = {
            "ammo_class_name": "ammo",
        }

        self.load_properties(properties_mapping)

        # If the magazine actually has an Ammo...
        if self.ammo_class_name:
            # Import CfgAmmo in the magazine
            ammo_module_path = os.path.join(cwd, "SQF-Class-Exports", magazine_mod_folder, "Ammo", f"{magazine_class_name}.cfg")

            # Import ammo dict
            spec = importlib.util.spec_from_file_location(ammo_class_name, ammo_module_path)
            self.magazine_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.magazine_module)
            self.magazine_module = self.magazine_module.d