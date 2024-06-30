# -*- coding: utf-8 -*-

import importlib.util
import json
import os
import concurrent.futures

# Get script directory for dict path
cwd = os.getcwd()

def format_dict(file_path):
    spec = importlib.util.spec_from_file_location("v", file_path)
    dict_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dict_module)

    formatted_dict = json.dumps(dict_module.d, indent=4, default=str, sort_keys=True)
    with open(file_path, "w") as outfile:
        outfile.write("d = " + formatted_dict)
    print(f"Formatted {file_path}")

# Collect all .py files except the script itself
file_paths = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py") and file != "Sort_And_Format_Dicts.py":
            end_path = os.path.join(root, file)
            full_path = cwd + end_path[1:]
            file_paths.append(full_path)

# Process files using multithreading
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(format_dict, file_paths)
