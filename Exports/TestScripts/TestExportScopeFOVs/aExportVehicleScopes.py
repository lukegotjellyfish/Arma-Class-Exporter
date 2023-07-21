import os
import ast
import sys


def opticsFuckery(_turret, andoptic):
    optics = [_vehicle["turrets"][_turret][andoptic]]
    try:
        optics.append(_vehicle["turrets"][_turret][andoptic]["visionmode"])
    except KeyError:
        optics.append("n/a")
    optics.append(_simpleTurrets.append((_turret+"_"+andoptic)))

    return optics


RHS_VERSION = "RHS"
cwd = os.getcwd()
with open(cwd + "/" + RHS_VERSION + "/Vehicles/" + "rhsgref_brdm2_atgm_vdv.py", "r", encoding="utf-8") as _dict:
    _vehicle = eval("".join(["{\n"] + _dict.readlines()[1:]))
    try:
        _simpleTurrets = []
        _simpleTurretOpticsIn = []
        for _turret in _vehicle["turrets"]:
            print("_turret="+_turret)

            _simpleTurrets.append(opticsFuckery(_turret,"viewoptics"))

            _OpticsIn = [opticsFuckery(_turret, "opticsin")]
            for optic in _OpticsIn:
                _simpleTurretOpticsIn.append(_vehicle["turrets"][_turret]["opticsin"][optic[0]], _turret+"_opticsin_"+optic)


        print(_vehicle["displayname"] + str(_simpleTurrets))
        print(_vehicle["displayname"] + str(_simpleTurretOpticsIn))
        
    except KeyError:
        print("KeyError:", sys.exc_info())
    except:
        print("Unexpected error:", sys.exc_info())

input("Press ENTER to exit...")
