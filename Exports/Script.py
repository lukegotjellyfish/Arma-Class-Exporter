# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedBluFor
import CombinedOpFor
import math


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

#There must be a better way of doing this, it hurts my eyes and looks wrong
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
    if (len(fireModes) < len(rpm)) and (len(fireModes) < len(dispersion)):
        x = 1
    else:
        x = 0
    singleRPMdispersion = []
    fullautoRPMdispersion = []
    for mode in fireModes:
        #If mode is a firemode
        if mode.count("single") > 0:
            singleRPMdispersion = filterModes(mode, singleRPMdispersion, rpm, dispersion, x)
        elif mode.count("auto") > 0 or mode.count("manual") > 0 or mode.count("burst") > 0:
            fullautoRPMdispersion = filterModes(mode, fullautoRPMdispersion, rpm, dispersion, x)
    return [singleRPMdispersion, fullautoRPMdispersion]


def getDisplayName(side, category, _class):
    return fetchSide([side + category, _class, "displayname"])

def getMagazineCapacity(side, category, _class):
    return fetchSide([side + category, _class, "count"])

def getAmmoHit(side, category, _class):
    return fetchSide([side + category, _class, "ammo", "hit"])


def getWeaponStats(weapon, magazine, side):
    name          = getDisplayName(side, "CfgWeapons", weapon)
    cartridge     = fetchSide([side + "Magazines", magazine, "displaynameshort"])
    if (len(cartridge) == 0):
        cartridge = fetchSide([side + "Magazines",magazine,"ammo","cartridge"]).replace("RHS_Cartridge_","").replace("FxCartridge_","").replace("762", "7.62")

    # Easier to do it manually :p
    if cartridge == "Buckshot":
        shot = []
        for shotDistance in range(100, 600, 100):
            estSpeed = 331.8 * (1/math.exp(abs(-0.00634) * shotDistance))
            shotDamage = 3.91 * (estSpeed/403.86)
            shot.append('{:.3f}'.format(round(shotDamage,3)))
        return ["X", "X", name, "Buckshot","1","35.19 (9*3.91)","Single","120", "0.945","331.8","403.86","-0.00634",
                "0.15|00.78|02.42", shot[0], shot[1], shot[2], shot[3], shot[4], "X", "rhs_weap_Izh18","rhsgref_1Rnd_00Buck = 1Rnd 00 Buckshot", "0.24"]

    magCapacity   = getMagazineCapacity(side, "Magazines", magazine)
    damage        = getAmmoHit(side, "Magazines", magazine)
    fireModes     = [x.lower().replace("manual","Fullauto") for x in fetchSide([side + "Weapons",weapon,"modes"])]
    rpm           = getModeDependant(side + "Weapons",weapon,fireModes,"reloadtime")
    wepClass      = weapon
    magClass      = magazine + " = " + fetchSide([side + "Magazines",magazine,"displayname"])
    dispersion    = getModeDependant(side + "Weapons",weapon,fireModes,"dispersion")
    initialSpeed  = fetchSide([side + "Magazines",magazine,"initspeed"])
    typicalSpeed  = fetchSide([side + "Magazines",magazine,"ammo","typicalspeed"])
    airResistance = fetchSide([side + "Magazines",magazine,"ammo","airfriction"])
    caliber       = fetchSide([side + "Magazines",magazine,"ammo","caliber"])
    penetration   = ('{:.2f}'.format(round((typicalSpeed * caliber * 0.015)/10,2)).zfill(4) + "|" +
                     '{:.2f}'.format(round((typicalSpeed * caliber * 0.080)/10,2)).zfill(5) + "|" +
                     '{:.2f}'.format(round((typicalSpeed * caliber * 0.250)/10,2)).zfill(5))
    thrust        = fetchSide([side + "Magazines",magazine,"ammo","thrust"])
    thrustTime    = fetchSide([side + "Magazines",magazine,"ammo","thrusttime"])


    #FireMode filtering, likely more useful for vehicle weapons
    modeStats     = filterFireModes(fireModes, rpm, dispersion)
    stringModeStats = ""
    prevSets = []
    fireModes = ""
    rpm = ""
    dispersion = ""
    for fireGroup in modeStats:
        for fireType in fireGroup:
            if fireType[0] != "":
                fireModes += fireType[0].title() + "\\"
                #If matching values not already an added set
                if ([fireType[1],fireType[2]] not in prevSets):
                    stringModeStats += fireType[0].title() + ": RPM[" + str(fireType[1]) + "] | Dispersion[" + str(fireType[2]) + "]\n"
                    rpm        += '{:.2f}'.format(round(60/fireType[1],2)).zfill(6)
                    dispersion += '{:.7f}'.format(fireType[2])
                    prevSets.append([fireType[1],fireType[2]])

    # hit = hit * (speed / typicalSpeed)
    hitValues = []
    for distance in range(100, 600, 100):
        estSpeed = initialSpeed * (1/math.exp(abs(airResistance) * distance))
        # str(distance).zfill(4) + ": " + '{:.2f}'.format(round(estSpeed, 2)).zfill(6) + " - Hit: " + '{:.3f}'.format(round(damage * (estSpeed/typicalSpeed),3)) + "\n"
        hitValues.append('{:.3f}'.format(round(damage * (estSpeed/typicalSpeed),3)))


    # Now that we're finished with damage, round up to 3dp
    # hit = hit * (speed / typicalSpeed)
    # Some bullets have a highter typicalSpeed than initial - they will always do less damage than their Hit value
    damage = '{:.3f}'.format(round(damage * (initialSpeed / typicalSpeed), 3))
    return ["X", "X", name, cartridge, magCapacity, damage, fireModes[:-1], rpm, dispersion,
            initialSpeed, typicalSpeed, airResistance, penetration,
            hitValues[0], hitValues[1], hitValues[2], hitValues[3], hitValues[4], "X", wepClass, magClass, caliber]


def writeWeaponStats(weapon, side, csvwriter):
    weaponStats = getWeaponStats(weapon[0], weapon[1], side)
    print(SEPERATOR)
    print(ccyan + "           Name: " + cend + cgreen  + str(weaponStats[2])  + cend + "\n" +
          ccyan + "      Cartridge: " + cend + cgreen  + str(weaponStats[3])  + cend + "\n" +
          cred  + "       Capacity: " + cend + cviolet + str(weaponStats[4])  + cend + "\n" +
          cred  + "         Damage: " + cend + cviolet + str(weaponStats[5])  + cend + "\n" +
          ccyan + "     Fire Modes: " + cend + cyellow + str(weaponStats[6])  + cend + "\n" +
          ccyan + "            RPM: " + cend + cyellow + str(weaponStats[7])  + cend + "\n" +
          ccyan + "     Dispersion: " + cend + cyellow + str(weaponStats[8]) + cend + "\n" +
          cred  + "  Initial Speed: " + cend + cviolet + str(weaponStats[9]) + cend + "\n" +
          cred  + "  Typical Speed: " + cend + cviolet + str(weaponStats[10]) + cend + "\n" +
          cred  + " Air Resistance: " + cend + cviolet + str(weaponStats[11]) + cend + "\n" +
          cred  + "    Penetration: " + cend + cgreen  + str(weaponStats[12]) + cend + "\n" +
          cred  + "     Ballistics: " + cend + cgreen  + "\n       " + str(weaponStats[13] + "\n" +
                                                                           weaponStats[14] + "\n" +
                                                                           weaponStats[15] + "\n" +
                                                                           weaponStats[16] + "\n" +
                                                                           weaponStats[17]).replace("\n","\n       ") + cend + "\n" +

          ccyan + "   Weapon Class: " + cend + cgreen  + str(weaponStats[19])  + cend + "\n" +
          cred  + " Magazine Class: " + cend + cgreen  + str(weaponStats[20])  + cend + "\n" +
          cred  + "        Caliber: " + cend + cviolet + str(weaponStats[21]) + cend)
    #Force excel to parse as string
    weaponStats[5]  = "=\"" + str(weaponStats[5])  + "\""
    weaponStats[7]  = "=\"" + str(weaponStats[7])  + "\""
    weaponStats[8]  = "=\"" + str(weaponStats[8])  + "\""
    weaponStats[9]  = "=\"" + str(weaponStats[9])  + "\""
    weaponStats[10] = "=\"" + str(weaponStats[10]) + "\""
    weaponStats[11] = "=\"" + str(weaponStats[11]) + "\""
    weaponStats[12] = "=\"" + str(weaponStats[12]) + "\""
    weaponStats[13] = "=\"" + str(weaponStats[13]) + "\""
    weaponStats[14] = "=\"" + str(weaponStats[14]) + "\""
    weaponStats[15] = "=\"" + str(weaponStats[15]) + "\""
    weaponStats[16] = "=\"" + str(weaponStats[16]) + "\""
    weaponStats[17] = "=\"" + str(weaponStats[17]) + "\""
    csvwriter.writerow(weaponStats)
    print(SEPERATOR + "\n\n")


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
    ["rhs_weap_m4a1_blockII"  ,"rhs_mag_30Rnd_556x45_Mk262_Stanag"    ],
    ["rhs_weap_m4a1"          ,"rhs_mag_30Rnd_556x45_M855_Stanag"     ],
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
    ["rhs_weap_6p53"         ,"rhs_18rnd_9x21mm_7N29"        ] ,
    ["rhs_weap_pb_6p9"       ,"rhs_mag_9x18_8_57N181S"       ] ,
    ["rhs_weap_pya"          ,"rhs_mag_9x19_17"              ] ,
    ["rhs_weap_makarov_pm"   ,"rhs_mag_9x18_8_57N181S"       ] ,
    ["rhs_weap_pp2000_folded","rhs_mag_9x19mm_7n21_20"       ] ,
    ["rhs_weap_tt33"         ,"rhs_mag_762x25_8"             ] ,
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

weaponArray = ["x","x","Name","Cartridge","Capacity","Damage","Fire Modes", "RPM", "Dispersion", "Initial Speed", "Typical Speed",
               "Air Resistance", "Penetration", "Damage at 100m", "Damage at 200m", "Damage at 300m", "Damage at 400m", "Damage at 500m", "Unlock Level"
               "Weapon Class", "Magazine Class", "Caliber"]

with open("BluForExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(weaponArray)
    for weapon in bluForWeapons:
        writeWeaponStats(weapon, "BluFor", csvwriter)

with open("OpForExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(weaponArray)
    for weapon in opForWeapons:
        writeWeaponStats(weapon, "OpFor", csvwriter)




# print('{:.2f}'.format(round((403.86 * 0.24 * 0.015)/10,2)).zfill(4) + "|" +
#                      '{:.2f}'.format(round((403.86 * 0.24 * 0.080)/10,2)).zfill(5) + "|" +
#                      '{:.2f}'.format(round((403.86 * 0.24 * 0.250)/10,2)).zfill(5))