# Armour
# -*- coding: utf-8 -*-

from ExportList import ExportList
from timeit import default_timer
import os
import logging
import importlib.util

MOD_FOLDER = "RHS"  # Folder name of RHS Export
BACKUP_FOLDERS = ["Arma3"]  # List of other SQF script exports, Arma3 folder for basegame classes
DISABLE_PRINT = False  # Bool pass to enable/disable printing class stats to console
LOG_FILE = 'armour.log'
SQF_CLASS_EXPORTS = 'SQF-Class-Exports'
WEAPONS_FOLDER = 'Weapons'


# Taken from:
# @RHSAFRF/rhs_main/config.cpp
# cfgammo >> warheadname = "AP_Level_2" etc
#test this ingame to see what the fuck is going on
class RHS_Gost:
    class Default:
        hit = [0.1, 3]
        speed = [0.1, 1]
    class HE:
        hit = [0.1, 1]
        speed = [1]
    class AP_Level_1(Default):
        hit = [0.5, 3]
    class AP_Level_2(Default):
        hit = [0.69999999, 3]
    class AP_Level_3(Default):
        hit = [0.94999999, 3]

class RHS_Gost_1(RHS_Gost):
    pass

class RHS_Gost_2(RHS_Gost):
    class AP_Level_1(RHS_Gost.Default):
        hit = [0.5, 3]
    class AP_Level_2(RHS_Gost.Default):
        hit = [0.69999999, 3]
    class AP_Level_3(RHS_Gost.Default):
        hit = [0.80000001, 3]

class RHS_Gost_3(RHS_Gost):
    class AP_Level_1(RHS_Gost.Default):
        hit = [0.5, 3]
    class AP_Level_2(RHS_Gost.Default):
        hit = [0.60000002, 3]
    class AP_Level_3(RHS_Gost.Default):
        hit = [0.69999999, 3]

class RHS_Gost_4(RHS_Gost):
    class AP_Level_1(RHS_Gost.Default):
        hit = [0.40000001, 3]
    class AP_Level_2(RHS_Gost.Default):
        hit = [0.5, 3]
    class AP_Level_3(RHS_Gost.Default):
        hit = [0.60000002, 3]

class RHS_Gost_5(RHS_Gost):
    class AP_Level_1(RHS_Gost.Default):
        hit = [0.2, 3]
    class AP_Level_2(RHS_Gost.Default):
        hit = [0.40000001, 3]
    class AP_Level_3(RHS_Gost.Default):
        hit = [0.5, 3]

class RHS_Gost_6(RHS_Gost):
    class AP_Level_1(RHS_Gost.Default):
        hit = [0.1, 3]
    class AP_Level_2(RHS_Gost.Default):
        hit = [0.30000001, 3]
    class AP_Level_3(RHS_Gost.Default):
        hit = [0.40000001, 3]


script_start = default_timer()  # Start timer to get total execution time
current_working_dir = os.getcwd()  # Save current folder path


def print_and_log(text):
    # Configure the logging module
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')
    # Print the text
    if not DISABLE_PRINT:
        print(text)
    # Log the text
    logging.info(text)


def get_armour_list(cwd, mod, backup_folders, append_list):
    # cwd            = /path/to/this/script
    # mod            = "cwd/FolderToSearchForClasses"
    # backup_folders = ["other mods to search", "for classes"]
    # append_list    = list to append weapon+magazine loadout combinations to
    for folder in [mod, *backup_folders]:
        weapons_folder_path = os.path.join(cwd, SQF_CLASS_EXPORTS, folder, WEAPONS_FOLDER)
        print(f"Folder: {weapons_folder_path}")
        if not os.path.exists(weapons_folder_path):
            continue

        for weapon in [file for file in os.listdir(weapons_folder_path) if file.endswith(".py")]:
            spec = importlib.util.spec_from_file_location(weapon, os.path.join(weapons_folder_path, weapon))
            weapon_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(weapon_module)
            try:
                if "hitpointsprotectioninfo" in weapon_module.d["iteminfo"]:
                    weapon = weapon[:-3]  # Remove .py file extension
                    print_and_log(f"{weapon}")
                    append_list.append(weapon)
                else:
                    continue
            except KeyError:
                # No Type
                continue


start_time = default_timer()  # Start timer
all_armours = []
get_armour_list(current_working_dir, MOD_FOLDER, BACKUP_FOLDERS, all_armours)
elapsed_time = round((default_timer() - start_time), 3)
print(f"Getting an armour list took {elapsed_time}s | Armour Count: {len(all_armours)}")  # Print time taken

start = default_timer()  # Start timer
csv_path = "#CSV_Exports/RHS_ARMA3/"
os.makedirs(csv_path, exist_ok=True)
with open(f"{csv_path}/ArmourExport.csv", "w", newline='\n', encoding="utf-8") as csvFile:
    opForArmourExport = ExportList(MOD_FOLDER, all_armours, current_working_dir, csvFile,
                                   BACKUP_FOLDERS)  # Create new ExportList obj
    opForArmourExport.disable_print = DISABLE_PRINT  # Set new ExportList disablePrint value
    opForArmourExport.export_list("Armour", 1)  # Set off the main script, exporting each loadout to the given CSV file
print(f"Armour Export took {round((default_timer() - start), 3)}s")  # Print time taken
