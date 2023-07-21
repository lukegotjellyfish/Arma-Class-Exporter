# -*- coding: utf-8 -*-
import importlib.util
import os
import gc


def get_weapons_magazines(weapons):
    weapons_loadout = {}
    for weapon in weapons:
        weapon += ".py"
        # Import weapon dict
        try:
            spec = importlib.util.spec_from_file_location(weapon, "C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/"+MOD+"/Weapons/"+weapon)
            weaponModule = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(weaponModule)
        except FileNotFoundError:
            try:
                spec = importlib.util.spec_from_file_location(weapon, "C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/Arma3/Weapons/"+weapon)
                weaponModule = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(weaponModule)
            except FileNotFoundError:
                weapons_loadout[weapon] = []
                continue

        weapons_loadout[weapon] = weaponModule.d["magazines"]
    return weapons_loadout


def addTurretLayout(addToDict,searchDict,turret):
    currentTurret = searchDict[turret]
    try:
        currentTurretWeapons = currentTurret["weapons"]
        # print(f"currentTurretWeapons: {currentTurretWeapons}")
        currentTurretWeapons = get_weapons_magazines(currentTurretWeapons)
        # print(f"currentTurretWeapons: {currentTurretWeapons}")
        if currentTurretWeapons:
            addToDict[turret] = {currentTurret["gunnername"]: currentTurretWeapons}
            # turretList.append(currentTurret)
    except KeyError:
        pass


def findTurretDict(_dict):
    turretList=[]
    turretLayout={}
    turretDict = _dict["turrets"]
    if turretDict:
        for turret in turretDict:
            addTurretLayout(turretLayout,turretDict,turret)
            try:
                currentTurret=turretDict[turret]["turrets"]
                for subTurret in currentTurret:
                    addTurretLayout(turretLayout,currentTurret,subTurret)
            except KeyError:
                pass
    return turretLayout


def findPylonDict(_dict):
    pylonLayout = {}
    pylonDict = _dict["components"]


with open("list-vehicles-that-have-weapon.txt","w") as f:
    f.truncate()

    MOD = "RHS"
    WeaponDict = {}

    for root, dirs, vehicles in os.walk("C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/" + MOD + "/Vehicles", topdown = False):
        for vehicle in vehicles:
            # try:
            if (vehicle[-6:] != "pyc.py") and (vehicle[-3:]!="pyc"):
                # Import vehicle dict
                spec = importlib.util.spec_from_file_location(vehicle, "C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/"+MOD+"/Vehicles/"+vehicle)
                vehicleModule = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(vehicleModule)

                if vehicleModule.d["category"] == "Air":
                    vehicleWeapons = findTurretDict(vehicleModule.d)
                    # Need to add compatible pylon weapons to sqf script
                    #vehicleWeapons = findPylonDict(vehicleModule.d)
                else:
                    vehicleWeapons = findTurretDict(vehicleModule.d)
                try:
                    driverWeapons = vehicleModule.d["weapons"]   # List
                    #driverWeapons = get_weapons_magazines(driverWeapons)
                    if driverWeapons:
                        vehicleWeapons["driver/man"] = driverWeapons
                except KeyError:
                    driverWeapons = []

                if vehicleWeapons:
                    WeaponDict[vehicle] = vehicleWeapons
                    print(f"Added {vehicle[:-3]}'s weapons")
                    print(vehicleWeapons)

                    with open("list-vehicles-that-have-weapon.txt","a") as f:
                        f.write(f"{vehicle[:-3]}: {vehicleWeapons}\n")

        # except (KeyError, AttributeError): #Not a CfgWeapon we need to use
        #     pass