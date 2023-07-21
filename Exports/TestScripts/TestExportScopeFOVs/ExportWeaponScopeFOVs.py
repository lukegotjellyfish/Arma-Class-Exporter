import os
import ast
import sys

RHS_VERSION = "RHS"

cwd = os.getcwd()
for root, dirs, files in os.walk(cwd + "/" + RHS_VERSION + "/Weapons", topdown = False):
	for file in files:
		if file.count("_acc_") > 0:
			try:
				with open(cwd + "/" + RHS_VERSION + "/Weapons/" + file, "r", encoding="utf-8") as _dict:
					_scope = eval("".join(["{\n"] + _dict.readlines()[1:]))
					try:
						_opticsModes = list(_scope["iteminfo"]["opticsmodes"].keys())
						_zooms = []
						for mode in _opticsModes:
							_zooms.append([mode, _scope["iteminfo"]["opticsmodes"][mode]["opticszoommin"]])

						print(_scope["displayname"] + str(_zooms))
					except KeyError:
						continue
					except:
						print("Unexpected error:", sys.exc_info()[0])
						raise
			except:
				print("Unexpected error:", sys.exc_info()[0])
				raise

input("Press ENTER to exit...")
