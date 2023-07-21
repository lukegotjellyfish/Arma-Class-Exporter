import os
import ast
import sys

RHS_VERSION = "RHS"

cwd = os.getcwd()
for root, dirs, files in os.walk(cwd + "/" + RHS_VERSION + "/Vehicles", topdown = False):
	for file in files:
		if ("vest_" not in file) or ("_magazine_" not in file) or ("item_" not in file) or ("_weapon_" not in file):
			try:
				with open(cwd + "/" + RHS_VERSION + "/Vehicles/" + file, "r", encoding="utf-8") as _dict:
					_vehicle = eval("".join(["{\n"] + _dict.readlines()[1:]))
					try:
						_simpleTurrets = []
						_simpleTurretOpticsIn = []
						for _turret in _vehicle["turrets"]:
							print("_turret="+_turret)
							_simpleTurrets.append([_vehicle["turrets"][_turret]["viewoptics"],_vehicle["turrets"][_turret]["viewoptics"]["visionmode"], _turret+"_viewoptics"])

							_OpticsIn = [[_vehicle["turrets"][_turret]["opticsin"]],_vehicle["turrets"][_turret]["viewoptics"]["visionmode"], _turret+"_opticsin"]
							for optic in _OpticsIn:
								_simpleTurretOpticsIn.append(_vehicle["turrets"][_turret]["opticsin"][optic[0]], _turret+"_opticsin_"+optic)


						print(_vehicle["displayname"] + str(_simpleTurrets))
						print(_vehicle["displayname"] + str(_simpleTurretOpticsIn))
						
					except KeyError:
						continue
					except:
						#print("Unexpected error:", sys.exc_info()[0])
						raise
			except:
				#print("Unexpected error:", sys.exc_info()[0])
				raise

input("Press ENTER to exit...")
