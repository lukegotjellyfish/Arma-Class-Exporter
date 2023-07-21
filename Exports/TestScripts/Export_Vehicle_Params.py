# -*- coding: utf-8 -*-
import importlib.util
import os


MOD = "RHS"
vehicle_params = ""


param_one = ["displayname","Display Name", ""]
param_two = ["terraincoef", "Terrain Coef", ""]
param_three = ["enginepower", "Engine Power", ""]
# crewcrashprotection
# 

for root, dirs, vehicles in os.walk("C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/" + MOD + "/Vehicles", topdown = False):
    for vehicle in vehicles:
        try:
            if (vehicle[-3:]!="pyc") and ("item" not in vehicle) and ("weapon" not in vehicle):
                # Import vehicle dict
                spec = importlib.util.spec_from_file_location(vehicle, "C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/SQF-Class-Exports/"+MOD+"/vehicles/"+vehicle)
                vehicleModule = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(vehicleModule)
                param_one[2] = vehicleModule.d[param_one[0]]
                param_two[2] = vehicleModule.d[param_two[0]]
                param_three[2] = vehicleModule.d[param_three[0]]
                vehicle_params += f"{param_one[2]};{param_two[2]};{param_three[2]};{vehicle[:-3]}\n"
                #print(f"{vehicle[:-3]},{param}\n")
        except (KeyError, AttributeError):
            print(f"{vehicle[:-3]}")
            continue

with open("C:/Users/Lukeg/Desktop/GitHub/MyRepos/Arma-Class-Exporter/Exports/TestScripts/terraincoef_export.csv", "w") as f:
    f.write(f"{param_one[1]};{param_two[1]};{param_three[1]};Class\n")
    f.write(vehicle_params)
    print("wrote to file")