# -*- coding: utf-8 -*-

from ExportList import ExportList
from timeit import default_timer
import os
import importlib.util

mod = "RHS"  # Folder name of RHS Export
backup_folders = ["Arma3"]  # List of other SQF script exports, Arma3 folder for basegame classes
disable_print = True  # Bool pass to enable/disable printing class stats to console
scriptStart = default_timer()  # Start timer to get total execution time
cwd = os.getcwd()  # Save current folder path


def export_all_loadouts(cwd, weapon, mod, backup_folders, appendList, dupe_list):
    # cwd           = /path/to/this/script
    # loadout       = ["passed weapon", "passed magazine"]
    # mod           = "cwd/FolderToSearchForClasses"
    # backupFolders = ["other mods to seach", "for classes"]
    # appendList    = list to append weapon+magazine loadout combinations to
    spec = importlib.util.spec_from_file_location(weapon, f"{cwd}/SQF-Class-Exports/{mod}/Weapons/{weapon}.py")
    weapon_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(weapon_module)
    magazines = weapon_module.d["magazines"]
    for magazine in magazines:
        # Append magazines with the weapon as a loadout
        # .lower() is applied to make sure path name matches magazine name
        #  as all exports from SQF script are in lower case
        appendList.append([weapon, magazine.lower()])


def export_weapons(path, loadout_list, export_class, export_to_csv=True, hit_ranges=[0, 100, 200, 500, 1000]):
    with open(path, "w", newline='\n', encoding="utf-8") as csv_export_file:
        exportList = ExportList(mod, loadout_list, cwd, csv_export_file, backup_folders)  # Create new ExportList obj
        exportList.hit_ranges = hit_ranges  # Set hit_ranges var to given list
        exportList.disable_print = disable_print  # Set new ExportList disablePrint value
        exportList.export_list(export_class, export_to_csv)  # Set off the main script, exporting each loadout to the given CSV file


# Regex to copy loadouts from CSV export:
#    FIND: (.*)	(.*)
# REPLACE:     ["$1","$2"],

scopes = []
for root, dirs, files in os.walk(cwd + "/" + mod + "/Weapons", topdown=False):
    for file in files:
        if file[-2:] == "py":
            if file.count("_acc_") > 0:
                scopes.append(file[:-3])

# for root, dirs, files in os.walk(cwd + "/" + mod + "/Vehicles", topdown=False):
#     for file in files:
#         if file[-2:] == "py":
#             if file.count()

# Scope
start = default_timer()  # Start timer
with open(f"#CSV_Exports/{mod}/scopeExport.csv", "w", newline='\n', encoding="utf-8") as csvFile:
    modScopes = ExportList(mod, scopes, cwd, csvFile, backup_folders)  # Create new ExportList obj
    modScopes.set_fov(0.75, 5)  # Basegame default FOV | round to 3 digits
    modScopes.disable_print = disable_print  # Set new ExportList disablePrint value
    modScopes.export_list("Scope", 1)  # Set off the main script, exporting each loadout to the given CSV file
print(f"            scopeExport took {round((default_timer() - start), 3)}s")  # Print time taken


print(f"\nRHSExportScript took {round((default_timer() - scriptStart), 3)}s")  # Print time taken for the entire script
