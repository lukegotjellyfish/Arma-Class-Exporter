# -*- coding: utf-8 -*-

import importlib
import json
import os


# Get script directory for dict path
cwd = os.getcwd()

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py") and file != "Sort_And_Format_Dicts.py":
            end_path = os.path.join(root, file)
            full_path = cwd + end_path[1:]

            spec = importlib.util.spec_from_file_location("v", f"{full_path}")
            dict_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(dict_module)

            formatted_dict = json.dumps(dict_module.d, indent=4, default=str, sort_keys=True)
            with open(full_path, "w") as outfile:
                outfile.write("d = " + formatted_dict)
            print(f"Formatted {file}")
