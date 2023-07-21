# -*- coding: utf-8 -*-
import importlib.util
import os


MOD = "RHS"
MagazineDict = {}


#TODO Add folder open dialog from Uwuify-war-thunder
for root, dirs, weapons in os.walk((os.getcwd()) + "/" + MOD + "/Weapons", topdown = False):
    for weapon in weapons:
        try:
            if (weapon[-6:] != "pyc.py") and (weapon[-3:]!="pyc"):
                # Import weapon dict
                spec = importlib.util.spec_from_file_location(weapon, (os.getcwd())+"/"+MOD+"/Weapons/"+weapon)
                weaponModule = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(weaponModule)
                # Fetch magazines compatible with the weapon
                weaponMagazines = weaponModule.d["magazines"]
                # Append the current CfgWeapon to CfgMagazine index in MagazineDict

                for magazine in weaponMagazines:
                    if magazine in MagazineDict:
                        MagazineDict[magazine] += [weapon]
                    else:
                        #Create dict entry
                        MagazineDict[magazine]=[weapon]
        except (KeyError, AttributeError): #Not a CfgWeapon we need to use
            continue
with open ("list-compat-weapons.txt","w") as f:
    f.write(str(MagazineDict))