# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedBluFor
import CombinedOpFor


def getAttribBluFor(array, depth):
    return CombinedBluFor.BluFor["BluForWeapons"]["rhsusf_weap_glock17g4"]["magazines"]

def getAttribOpFor(array, depth):
    return array

"""
<Side>LauncherMagazines
<Side>Launchers
<Side>Magazines
<Side>VehicleMagazines
<Side>Vehicles
<Side>VehicleWeapons
<Side>Weapons
<Side>Uniforms
<Side>Backpacks
<Side>Glasses
"""



print(CombinedBluFor)
print(CombinedOpFor)
search = ["BluForWeapons","rhsusf_weap_glock17g4","magazines"]
print(getAttribBluFor(search,len(search)))
#print(getAttrib("rhs_200rnd_556x45_B_SAW", "author"))