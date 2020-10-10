# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedBluFor
import CombinedOpFor


#There must be a better way of doing this
def bluFor(array, depth):
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

def opFor(array, depth):
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

def fetchSide(array):
    if array[0][:2] == "Op":
        return opFor(array, len(array))
    else:
        return bluFor(array, len(array))
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

def getRPM(side, weapon, fireModes):
    rpm = []
    try:
        rpm.append(fetchSide([side,weapon,"reloadtime"]))
    except KeyError:
        pass

    for mode in fireModes:
        try:
            rpm.append(fetchSide([side,weapon,mode,"reloadtime"]))
        except KeyError:
            continue
    return rpm


def getWeaponStats(weapon, magazine):
    name          = fetchSide(["BluForWeapons",weapon,"displayname"])
    magCapacity   = fetchSide(["BluForMagazines",magazine,"count"])
    damage        = fetchSide(["BluForMagazines",magazine,"ammo","hit"])
    fireModes     = [x.lower() for x in fetchSide(["BluForWeapons",weapon,"modes"])]
    rpm           = getRPM("BluForWeapons",weapon,fireModes)
    wepClass      = weapon
    magClass      = magazine
    dispersion    = fetchSide(["BluForWeapons",weapon,"dispersion"])
    initialSpeed  = fetchSide(["BluForMagazines",magazine,"initspeed"])
    airResistance = fetchSide(["BluForMagazines",magazine,"ammo","airfriction"])
    caliber       = fetchSide(["BluForMagazines",magazine,"ammo","caliber"])
    penetration   = str((initialSpeed * (caliber/1000) * 15)) + "mm"  #RHA
    return [name, magCapacity, damage, fireModes, rpm, wepClass, magClass,
            dispersion, initialSpeed, airResistance, caliber, penetration]


bluForWeapons = [
    ["rhs_weap_g36kv"         ,"rhssaf_30rnd_556x45_EPR_G36"          ],
    ["rhs_weap_hk416d145"     ,"rhs_mag_30Rnd_556x45_Mk318_Stanag"    ],
    ["rhs_weap_kar98k"        ,"rhsgref_5Rnd_792x57_kar98k"           ],
    ["rhs_weap_l1a1_base"     ,"rhs_mag_20Rnd_762x51_m80_fnfal"       ],
    ["rhs_weap_M107"          ,"rhsusf_mag_10Rnd_STD_50BMG_M33"       ],
    ["rhs_weap_m14ebrri"      ,"rhsusf_20Rnd_762x51_m118_special_Mag" ],
    ["rhs_weap_m16a4"         ,"rhs_mag_30Rnd_556x45_M855_Stanag"     ],
    ["rhs_weap_m1garand_sa43" ,"rhsgref_8Rnd_762x63_M2B_M1rifle"      ],
    ["rhs_weap_m21a"          ,"rhsgref_30rnd_556x45_m21"             ],
    ["rhs_weap_m240G"         ,"Rhsusf_100Rnd_762x51"                 ],
    ["rhs_weap_m249_pip"      ,"rhs_200rnd_556x45_B_SAW"              ],
    ["rhs_weap_m249"          ,"rhs_200rnd_556x45_B_SAW"              ],
    ["rhs_weap_m24sws"        ,"rhsusf_5Rnd_762x51_m993_Mag"          ],
    ["rhs_weap_m27iar"        ,"rhs_mag_30Rnd_556x45_Mk318_Stanag"    ],
    ["rhs_weap_m3a1_specops"  ,"rhsgref_30rnd_1143x23_M1911B_SMG"     ],
    ["rhs_weap_m40a5"         ,"rhsusf_10Rnd_762x51_m993_Mag"         ],
    ["rhs_weap_m4a1_blockII"  ,"rhs_mag_30Rnd_556x45_M855_Stanag"     ],
    ["rhs_weap_m4a1"          ,"rhs_mag_30Rnd_556x45_Mk262_Stanag"    ],
    ["rhs_weap_M590_5RD"      ,"rhsusf_5Rnd_00Buck"                   ],
    ["rhs_weap_M590_5RD"      ,"rhsusf_5Rnd_Slug"                     ],
    ["rhs_weap_mg42"          ,"rhsgref_50Rnd_792x57_SmE_drum"        ],
    ["rhs_weap_mk18"          ,"rhs_mag_30Rnd_556x45_Mk262_Stanag"    ],
    ["rhs_weap_mosin_sbr"     ,"rhsgref_5Rnd_762x54_m38"              ],
    ["rhs_weap_MP44"          ,"rhsgref_30Rnd_792x33_SmE_StG"         ],
    ["rhs_weap_savz61"        ,"rhsgref_20rnd_765x17_vz61"            ],
    ["rhs_weap_SCARH_STD"     ,"rhs_mag_20Rnd_SCAR_762x51_m80_ball"   ],
    ["rhs_weap_sr25"          ,"rhsusf_20Rnd_762x51_m118_special_Mag" ],
    ["rhs_weap_type94_new"    ,"rhs_mag_6x8mm_mhp"                    ],
    ["rhs_weap_XM2010"        ,"rhsusf_5Rnd_300winmag_xm2010"         ],
    ["rhsusf_weap_glock17g4"  ,"rhsusf_mag_17Rnd_9x19_JHP"            ],
    ["rhsusf_weap_m1911a1"    ,"rhsusf_mag_7x45acp_MHP"               ],
    ["rhsusf_weap_m9"         ,"rhsusf_mag_15Rnd_9x19_JHP"            ],
    ["rhsusf_weap_MP7A2"      ,"rhsusf_mag_40Rnd_46x30_JHP"           ]
]
opForWeapons = [
    ["rhs_weap_ak103"        ,""],
    ["rhs_weap_ak74"         ,""],
    ["rhs_weap_ak74m"        ,""],
    ["rhs_weap_ak74mr"       ,""],
    ["rhs_weap_akmn"         ,""],
    ["rhs_weap_aks74un"      ,""],
    ["rhs_weap_asval_npz"    ,""],
    ["rhs_weap_asval"        ,""],
    ["rhs_weap_dsr1"         ,""],
    ["rhs_weap_Izh18"        ,""],
    ["rhs_weap_m38_rail"     ,""],
    ["rhs_weap_m38"          ,""],
    ["rhs_weap_m76"          ,""],
    ["rhs_weap_m84"          ,""],
    ["rhs_weap_pkm"          ,""],
    ["rhs_weap_pkp"          ,""],
    ["rhs_weap_savz58p_rail" ,""],
    ["rhs_weap_savz58v_fold" ,""],
    ["rhs_weap_svdp_npz"     ,""],
    ["rhs_weap_svdp"         ,""],
    ["rhs_weap_t5000"        ,""],
    ["rhs_weap_vhsd2"        ,""],
    ["rhs_weap_vss_npz"      ,""],
    ["rhs_weap_vss"          ,""]
]

# [name, magazine count, damage, fire modes, RPM, weapon classname, magazine classnames, dispersion, initspeed, bullet friction, caliber, penetration]


with open("BluForExport.csv", "w", newline='\n') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for weapon in bluForWeapons:
            weaponStats = getWeaponStats(weapon[0], weapon[1])
            csvwriter.writerow(weaponStats)
            print("Weapon: " + weapon[0])
            print("stats: " + str(weaponStats))

# for weapon in opForWeapons:
#     opForWeapon(weapon)



















# search = ["BluForWeapons","rhsusf_weap_glock17g4","reloadTime"]
# print(bluFor(search,len(search)))