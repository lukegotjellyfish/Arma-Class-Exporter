# Construct path to magazine dict
import os
import importlib.util
import cProfile
from decimal import Decimal

cwd = os.path.abspath(os.path.dirname(__file__))

ammo_module_path = os.path.join(cwd, "Ammo", "b_127x108_apds.py")

# Import magazine dict
spec = importlib.util.spec_from_file_location("a", ammo_module_path)
ammo_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ammo_module)


def get_typical_speed(ammo_mod):
    ammo_mod["typicalspeed"]
    _ = Decimal(ammo_mod["typicalspeed"])
def get_typical_speedd(ammo_mod):
    _ = Decimal(ammo_mod.d["typicalspeed"])


def profile_code_a():
    for _ in range(10000000):
        get_typical_speed(ammo_module.d)

cProfile.run('profile_code_a()')

def profile_code_b():
    for _ in range(10000000):
        get_typical_speedd(ammo_module)

cProfile.run('profile_code_b()')



#test_byref

def change_typicalspeed(dict_a):
    dict_a["typicalspeed"] = 999

dict_a = {"typicalspeed": 500}
print(dict_a["typicalspeed"])
change_typicalspeed(dict_a)
print(dict_a["typicalspeed"])


