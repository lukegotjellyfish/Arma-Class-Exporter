# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedBluFor
import CombinedOpFor


#\33[m

os.system("")
cred     = '\33[31m'
cgreen   = '\33[32m'
cyellow  = '\33[33m'
cviolet  = '\33[35m'
ccyan    = '\33[36m'

cgrey    = '\33[90m'
cred2    = '\33[91m'
cgreen2  = '\33[92m'
cyellow2 = '\33[93m'
cblue2   = '\33[94m'
cviolet2 = '\33[95m'
ccyan2   = '\33[96m'
cwhite   = '\33[96m'


cbold    = '\33[1m'

cend     = '\33[0m'

SEPERATOR = cgreen + cbold + "======================================================================================================================" + cend

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

def getModeDependant(side, weapon, fireModes, wepProperty):
    thing = []
    try:
        thing.append(fetchSide([side,weapon,wepProperty]))
    except KeyError:
        pass

    for mode in fireModes:
        try:
            thing.append(fetchSide([side,weapon,mode,wepProperty]))
        except KeyError:
            continue
    return thing


#I should learn how to use classes
def filterModes(mode, array, rpm, dispersion, x):
    #If there is already a firemode
    if len(array) > 0:
        #Go through firemodes
        for single in array:
            #If this firemode matches another in rpm and dispersion, ignore it
            if ((single[1] == rpm[x]) and (single[2] == dispersion[x])):
                continue
            else:
                array.append([mode,rpm[x],dispersion[x]])
            x += 1
    else:
        array.append([mode,rpm[x],dispersion[x]])
    return array

def filterFireModes(fireModes, rpm, dispersion):
    if (len(fireModes) > len(rpm)) and (len(fireModes) > len(dispersion)):
        x = 1
    else:
        x = 0
    singleRPMdispersion = []
    fullautoRPMdispersion = []
    for mode in fireModes:
        #If mode is a firemode
        if mode.count("single") > 0:
            singleRPMdispersion = filterModes(mode, singleRPMdispersion, rpm, dispersion, x)
        elif mode.count("auto") > 0 or mode.count("manual") > 0:
            fullautoRPMdispersion = filterModes(mode, fullautoRPMdispersion, rpm, dispersion, x)
    return [singleRPMdispersion, fullautoRPMdispersion]


def getWeaponStats(weapon, magazine, side):
    name          = fetchSide([side + "Weapons",weapon,"displayname"])
    cartridge     = fetchSide([side + "Magazines",magazine,"displaynameshort"])
    if (len(cartridge) == 0):
        cartridge = fetchSide([side + "Magazines",magazine,"ammo","cartridge"]).replace("RHS_Cartridge_","")
    magCapacity   = fetchSide([side + "Magazines",magazine,"count"])
    damage        = fetchSide([side + "Magazines",magazine,"ammo","hit"])
    fireModes     = [x.lower() for x in fetchSide([side + "Weapons",weapon,"modes"])]
    rpm           = getModeDependant(side + "Weapons",weapon,fireModes,"reloadtime")
    wepClass      = weapon
    magClass      = magazine + " = " + fetchSide([side + "Magazines",magazine,"displayname"])
    dispersion    = getModeDependant(side + "Weapons",weapon,fireModes,"dispersion")
    initialSpeed  = fetchSide([side + "Magazines",magazine,"initspeed"])
    typicalSpeed  = fetchSide([side + "Magazines",magazine,"ammo","typicalspeed"])
    airResistance = fetchSide([side + "Magazines",magazine,"ammo","airfriction"])
    caliber       = fetchSide([side + "Magazines",magazine,"ammo","caliber"])
    penetration   = ('{:.2f}'.format(round((initialSpeed * caliber * 0.015)/10,2)).zfill(4) + "|" +
                     '{:.2f}'.format(round((initialSpeed * caliber * 0.080)/10,2)).zfill(5) + "|" +
                     '{:.2f}'.format(round((initialSpeed * caliber * 0.250)/10,2)).zfill(5))
    modeStats     = filterFireModes(fireModes, rpm, dispersion)

    return ["X", "X", name, cartridge, magCapacity, damage, modeStats, wepClass, magClass,
            initialSpeed, typicalSpeed, airResistance, caliber, penetration, "X"]


def writeWeaponStats(weapon, side, csvwriter):
    weaponStats = getWeaponStats(weapon[0], weapon[1], side)
    csvwriter.writerow(weaponStats)
    print(SEPERATOR)
    print(ccyan + "           Name: " + cend + cgreen  + str(weaponStats[2])  + cend + "\n" +
          ccyan + "      Cartridge: " + cend + cgreen  + str(weaponStats[3]) + cend + "\n" +
          cred  + "       Capacity: " + cend + cviolet + str(weaponStats[4])  + cend + "\n" +
          cred  + "         Damage: " + cend + cviolet + str(weaponStats[5])  + cend + "\n" +
          ccyan + "     Fire Modes: " + cend + cyellow + str(weaponStats[6])  + cend + "\n" +
          ccyan + "   Weapon Class: " + cend + cgreen  + str(weaponStats[7])  + cend + "\n" +
          cred  + " Magazine Class: " + cend + cgreen  + str(weaponStats[8])  + cend + "\n" +
          cred  + "  Initial Speed: " + cend + cviolet + str(weaponStats[9])  + cend + "\n" +
          cred  + "  Typical Speed: " + cend + cviolet + str(weaponStats[10])  + cend + "\n" +
          cred  + " Air Resistance: " + cend + cviolet + str(weaponStats[11])  + cend + "\n" +
          cred  + "        Caliber: " + cend + cviolet + str(weaponStats[12]) + cend + "\n" +
          cred  + "    Penetration: " + cend + cgreen  + str(weaponStats[13]) + cend)
    print(SEPERATOR + "\n\n")

#[name, magCapacity, damage, fireModes, rpm, wepClass, magClass,
# dispersion, initialSpeed, airResistance, caliber, penetration]

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
    ["rhs_weap_ak103"        ,"rhs_30Rnd_762x39mm_polymer_89"],
    ["rhs_weap_ak74"         ,"rhs_30Rnd_545x39_7N6_AK"      ],
    ["rhs_weap_ak74m"        ,"rhs_30Rnd_545x39_7N10_AK"     ],
    ["rhs_weap_ak74mr"       ,"rhs_30Rnd_545x39_7N22_AK"     ],
    ["rhs_weap_akmn"         ,"rhs_30Rnd_762x39mm"           ],
    ["rhs_weap_aks74un"      ,"rhs_30Rnd_545x39_7N6M_AK"     ],
    ["rhs_weap_asval_npz"    ,"rhs_20rnd_9x39mm_SP6"         ],
    ["rhs_weap_asval"        ,"rhs_20rnd_9x39mm_SP6"         ],
    ["rhs_weap_dsr1"         ,"rhsusf_5Rnd_762x51_m62_Mag"   ],
    ["rhs_weap_Izh18"        ,"rhsgref_1Rnd_00Buck"          ],
    ["rhs_weap_Izh18"        ,"rhsgref_1Rnd_Slug"            ],
    ["rhs_weap_m38_rail"     ,"rhsgref_5Rnd_762x54_m38"      ],
    ["rhs_weap_m38"          ,"rhsgref_5Rnd_762x54_m38"      ],
    ["rhs_weap_m76"          ,"rhsgref_10Rnd_792x57_m76"     ],
    ["rhs_weap_m84"          ,"rhssaf_250Rnd_762x54R"        ],
    ["rhs_weap_pkm"          ,"rhs_100Rnd_762x54mmR"         ],
    ["rhs_weap_pkp"          ,"rhs_100Rnd_762x54mmR"         ],
    ["rhs_weap_savz58p_rail" ,"rhs_30Rnd_762x39mm"           ],
    ["rhs_weap_savz58v_fold" ,"rhs_30Rnd_762x39mm"           ],
    ["rhs_weap_svdp_npz"     ,"rhs_10Rnd_762x54mmR_7N14"     ],
    ["rhs_weap_svdp"         ,"rhs_10Rnd_762x54mmR_7N14"     ],
    ["rhs_weap_t5000"        ,"rhs_5Rnd_338lapua_t5000"      ],
    ["rhs_weap_vhsd2"        ,"rhsgref_30rnd_556x45_vhs2"    ],
    ["rhs_weap_vss_npz"      ,"rhs_10rnd_9x39mm_SP5"         ],
    ["rhs_weap_vss"          ,"rhs_10rnd_9x39mm_SP5"         ]
]

# [name, magazine count, damage, fire modes, RPM, weapon classname, magazine classnames, dispersion, initspeed, bullet friction, caliber, penetration]


with open("BluForExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)
    csvwriter = csv.writer(csvfile, delimiter=',')
    for weapon in bluForWeapons:
        writeWeaponStats(weapon, "BluFor", csvwriter)

with open("OpForExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)
    csvwriter = csv.writer(csvfile, delimiter=',')
    for weapon in opForWeapons:
        writeWeaponStats(weapon, "OpFor", csvwriter)

# for weapon in opForWeapons:
#     opForWeapon(weapon)



















# search = ["BluForWeapons","rhsusf_weap_glock17g4","reloadTime"]
# print(bluFor(search,len(search)))