# -*- coding: utf-8 -*-
import csv
import importlib.util
import math
import os
import sys
from json import dumps


MOD = "RHS"

for root, dirs, magazines in os.walk((os.getcwd()) + "/" + MOD + "/Magazines", topdown = False):
    for magazine in magazines:
        if (magazine[-6:] != "pyc.py") and (magazine[-3:]!="pyc"):
            # Import magazine dict
            spec = importlib.util.spec_from_file_location(magazine, (os.getcwd())+"/"+MOD+"/Magazines/"+magazine)
            magazineModule = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(magazineModule)
    
            magazineList=[magazine[:-3],magazineModule.d["displaynameshort"]]
            if magazineList[1] == "":
                print(magazineList)