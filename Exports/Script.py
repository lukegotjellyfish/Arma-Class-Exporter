# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedBluFor
import CombinedOpFor


#There must be a better way of doing this
def getAttribBluFor(array, depth):
    if depth == 2:
        return CombinedBluFor.BluFor[array[0]][array[1]]
    if depth == 3:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]]
    if depth == 4:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]]
    if depth == 5:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]][array[4]]
    if depth == 6:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]]
    if depth == 7:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]]
    if depth == 8:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]]
    if depth == 9:
        return CombinedBluFor.BluFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]][array[8]]

def getAttribOpFor(array, depth):
    if depth == 2:
        return CombinedOpFor.OpFor[array[0]][array[1]]
    if depth == 3:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]]
    if depth == 4:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]]
    if depth == 5:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]][array[4]]
    if depth == 6:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]]
    if depth == 7:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]]
    if depth == 8:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]]
    if depth == 9:
        return CombinedOpFor.OpFor[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]][array[8]]


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


#Test for errors:
# print(CombinedBluFor)
# print(CombinedOpFor)

search = ["BluForWeapons","rhsusf_weap_glock17g4","magazines"]
print(getAttribBluFor(search,len(search)))
#print(getAttrib("rhs_200rnd_556x45_B_SAW", "author"))