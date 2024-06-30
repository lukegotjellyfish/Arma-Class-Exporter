# -*- coding: utf-8 -*-
import csv
import importlib.util
import math
import os
import sys
import json
from json import dumps


MOD = "RHS"
SEARCH_DIR = f"F:/Software/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/{MOD}/Weapons/"
type_list = {}

for root, dirs, CfgWeapons in os.walk(SEARCH_DIR, topdown = False):
    for CfgWeapon in CfgWeapons:
        try:
            if (CfgWeapon[-6:] != "pyc.py") and (CfgWeapon[-3:]!="pyc"):
                # Import CfgWeapon dict
                spec = importlib.util.spec_from_file_location(CfgWeapon, (f"{SEARCH_DIR}{CfgWeapon}"))
                magazineModule = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(magazineModule)
        
                #typeList.append([CfgWeapon[:-3],magazineModule.d["iteminfo"]["type"]])
                type_list[CfgWeapon[:-3]] = magazineModule.d["iteminfo"]["type"]
        except KeyError:
            pass

with open("uniforms.json", "w") as f:
    f.write(json.dumps(type_list, indent=4, sort_keys=True))