# -*- coding: utf-8 -*-
import re
import os
import csv
import CombinedRHS
import math
from decimal import Decimal


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
def rhsusaf(array, depth):
    if depth == 2:
        return Combinedrhs.rhsusaf[array[0]][array[1]]
    if depth == 3:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]]
    if depth == 4:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]]
    if depth == 5:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]][array[4]]
    if depth == 6:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]]
    if depth == 7:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]]
    if depth == 8:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]]
    if depth == 9:
        return Combinedrhs.rhsusaf[array[0]][array[1]][array[2]][array[3]][array[4]][array[5]][array[6]][array[7]][array[8]]

def fetchSide(array):
    return rhsusaf(array, len(array))
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


#I should learn how to use classes
def getModeDependant(side, weapon, fireModes, wepProperty):
    thing = []
    for mode in fireModes:
        try:
            thing.append(fetchSide([side, weapon, mode, wepProperty]))
            print(side)
            print(weapon)
            print(mode)
            print(wepProperty)
            print(fetchSide([side, weapon, mode, wepProperty]))
            return thing
        except KeyError:
            continue

    try:
        thing.append(fetchSide([side, weapon, wepProperty]))
    except KeyError:
        pass

    return thing

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

def filterRifleFireModes(fireModes, rpm, dispersion):
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
    modeStats = [singleRPMdispersion, fullautoRPMdispersion]

    #stringModeStats = ""
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
                    #stringModeStats += fireType[0].title() + ": RPM[" + str(fireType[1]) + "] | Dispersion[" + str(fireType[2]) + "]\n"
                    rpm        += '{:.2f}'.format(round(60/fireType[1],2)).zfill(6)
                    dispersion += '{:.7f}'.format(fireType[2])
                    prevSets.append([fireType[1],fireType[2]])

    return [fireModes, rpm, dispersion]

def filterVehicleFireModes(fireModes, rpm, dispersion):
    fireModesX = []
    rpmX = []
    dispersionX = []
    x = 0
    for mode in fireModes:
        #If not a useless firemode (close-far are for AI and this is for smoke/missile launchers)
        if mode not in ["close","short","medium","far","far_ai","this"]:
            if fireModes[x] not in fireModesX:
                fireModesX.append(fireModes[x])
                rpmX.append(rpm[x])
                dispersionX.append(dispersion[x])
        x += 1
    return [fireModesX, rpmX, dispersionX]

def getDisplayName(side, category, _class):
    return fetchSide([side + category, _class, "displayname"])

def getMagazineCapacity(side, category, _class):
    return fetchSide([side + category, _class, "count"])

def getHit(side, category, _class, sub=""):
    if sub == "":
        return fetchSide([side + category, _class, "ammo", "hit"])
    else:
        return fetchSide([side + category, _class, "ammo", sub, "hit"])

def getIndirectHit(side, category, _class, sub=""):
    if sub == "":
        return fetchSide([side + category, _class, "ammo", "indirecthit"])
    else:
        return fetchSide([side + category, _class, "ammo", sub, "indirecthit"])

def getIndirectRange(side, category, _class, sub=""):
    if sub == "":
        return fetchSide([side + category, _class, "ammo", "indirecthitrange"])
    else:
        return fetchSide([side + category, _class, "ammo", sub, "indirecthitrange"])

def getSubmunition(side, category, _class):
    try:
        submunitionAmmo = fetchSide([side + category, _class, "ammo", "submunitionammo"])
        if submunitionAmmo != "":
            return "submunitionammo"
    except KeyError:  #No submunitionammo so must be submunitionammox OR no submunitionammo
        try:
            submunitionAmmo = []
            x = 1
            while True:
                subName = "submunitionammo" + str(x)
                fetchSide([side + category, _class, "ammo", subName])
                submunitionAmmo.append("submunitionammo" + str(x))
                x += 1
        except KeyError:
            if (x >= 3):
                print("SubmunitionAmmo: " + str(submunitionAmmo))
                return submunitionAmmo
    return 0

def getDisplayNameShort(side, category, _class):
    return fetchSide([side + category, _class, "displaynameshort"])

def getCartridge(side, category, _class):
    return fetchSide([side + category, _class, "ammo", "cartridge"]).replace("RHS_Cartridge_","").replace("FxCartridge_","").replace("762", "7.62")

def getFireModes(side, category, _class):
    return fetchSide([side + category, _class, "modes"])

def getInitialSpeed(side, category, _class):
    return fetchSide([side + category, _class, "initspeed"])

def getTypicalSpeed(side, category, _class, sub=""):
    if sub == "":
        return fetchSide([side + category, _class, "ammo","typicalspeed"])
    else:
        return fetchSide([side + category, _class, "ammo", sub, "typicalspeed"])

def getAirResistance(side, category, _class):
    return fetchSide([side + category, _class, "ammo","airfriction"])

def getCaliber(side, category, _class, sub=""):
    if sub == "":
        return fetchSide([side + category, _class, "ammo","caliber"])
    else:
        return fetchSide([side + category, _class, "ammo", sub, "caliber"])

def getThrust(side, category, _class):
    return fetchSide([side + category, _class, "ammo","thrust"])

def getThrustTime(side, category, _class):
    return fetchSide([side + category, _class, "ammo","thrusttime"])

def getMaxSpeed(side, category, _class):
    return fetchSide([side + category, _class, "ammo","maxspeed"])

def getSubmunitionValues(side, magazine, submunition):
    subDamage         = getHit(side, "VehicleMagazines", magazine, submunition)
    subIndirectDamage = getIndirectHit(side, "VehicleMagazines", magazine, submunition)
    subIndirectRange  = getIndirectRange(side, "VehicleMagazines", magazine, submunition)
    subInitialSpeed   = getInitialSpeed(side, "VehicleMagazines", magazine)
    subTypicalSpeed   = getTypicalSpeed(side, "VehicleMagazines", magazine, submunition)
    subCaliber        = getCaliber(side, "VehicleMagazines", magazine, submunition)
    subPenetration    = ('{:.2f}'.format(round((subTypicalSpeed * subCaliber * 0.015),2)).zfill(4) + "|" +
                            '{:.2f}'.format(round((subTypicalSpeed * subCaliber * 0.080),2)).zfill(5) + "|" +
                            '{:.2f}'.format(round((subTypicalSpeed * subCaliber * 0.250),2)).zfill(5))
    return [subDamage, subIndirectDamage, subIndirectRange, subInitialSpeed, subTypicalSpeed, subCaliber, subPenetration]

def getWeaponStats(weapon, magazine, side):
    name          = getDisplayName(side, "Weapons", weapon)
    cartridge     = getDisplayNameShort(side, "Magazines", magazine)
    if (len(cartridge) == 0):
        cartridge = getCartridge(side, "Magazines", magazine)

    # Easier to do it manually for now :p
    if cartridge == "Buckshot":
        shot = []
        for shotDistance in range(100, 600, 100):
            estSpeed = 331.8 * (1/math.exp(abs(-0.00634) * shotDistance))
            shotDamage = 3.91 * (estSpeed/403.86)
            shot.append('{:.3f}'.format(round(shotDamage,3)))
        return ["X", "X", name, "Buckshot","1","35.19 (9*3.91)","Single","120", "0.945","331.8","403.86","-0.00634",
                "0.15|00.78|02.42", shot[0], shot[1], shot[2], shot[3], shot[4], "X", "rhs_weap_Izh18","rhsgref_1Rnd_00Buck = 1Rnd 00 Buckshot", "0.24"]

    magCapacity   = getMagazineCapacity(side, "Magazines", magazine)
    damage        = getHit(side, "Magazines", magazine)
    fireModes     = [x.lower().replace("manual","Fullauto") for x in getFireModes(side, "Weapons", weapon)]
    rpm           = getModeDependant(side + "Weapons", weapon, fireModes, "reloadtime")
    wepClass      = weapon
    magClass      = magazine + " = " + fetchSide([side + "Magazines",magazine,"displayname"])
    dispersion    = getModeDependant(side + "Weapons", weapon, fireModes, "dispersion")
    initialSpeed  = getInitialSpeed(side, "Magazines", magazine)
    typicalSpeed  = getTypicalSpeed(side, "Magazines", magazine)
    airResistance = getAirResistance(side, "Magazines", magazine)
    caliber       = getCaliber(side, "Magazines", magazine)
    penetration   = ('{:.2f}'.format(round((typicalSpeed * caliber * 0.015)/10,2)).zfill(4) + "|" +
                     '{:.2f}'.format(round((typicalSpeed * caliber * 0.080)/10,2)).zfill(5) + "|" +
                     '{:.2f}'.format(round((typicalSpeed * caliber * 0.250)/10,2)).zfill(5))
    thrust        = getThrust(side, "Magazines", magazine)
    thrustTime    = getThrustTime(side, "Magazines", magazine)
    maxSpeed      = getMaxSpeed(side, "Magazines", magazine)

    #FireMode filtering, likely more useful for vehicle weapons
    modeStats     = filterRifleFireModes(fireModes, rpm, dispersion)
    fireModes     = modeStats[0]
    rpm           = modeStats[1]
    dispersion    = modeStats[2]


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

def getVehicleWeaponStats(weapon, magazine, side):
    name              = getDisplayName(side, "VehicleWeapons", weapon)
    print(name)
    cartridge         = getDisplayNameShort(side, "VehicleMagazines", magazine)
    capacity          = getMagazineCapacity(side, "VehicleMagazines", magazine)
    damage            = getHit(side, "VehicleMagazines", magazine)
    indirectDamage    = getIndirectHit(side, "VehicleMagazines", magazine)
    indirectRange     = getIndirectRange(side, "VehicleMagazines", magazine)
    submunition       = getSubmunition(side, "VehicleMagazines", magazine)
    subDamage         = []
    subIndirectDamage = []
    subIndirectRange  = []
    subInitialSpeed   = []
    subTypicalSpeed   = []
    subCaliber        = []
    subPenetration    = []
    subArray          = []

    if (submunition != 0):
        if isinstance(submunition, list):
            submunitionCount = len(submunition)
            for i in range(0, submunitionCount, 1):
                subArray = (getSubmunitionValues(side, magazine, submunition[i]))
                subDamage.append(subArray[0])
                subIndirectDamage.append(subArray[1])
                subIndirectRange.append(subArray[2])
                subInitialSpeed.append(subArray[3])
                subTypicalSpeed.append(subArray[4])
                subCaliber.append(subArray[5])
                subPenetration.append(subArray[6])
        else:
            subArray = (getSubmunitionValues(side, magazine, submunition))
            subDamage.append(subArray[0])
            subIndirectDamage.append(subArray[1])
            subIndirectRange.append(subArray[2])
            subInitialSpeed.append(subArray[3])
            subTypicalSpeed.append(subArray[4])
            subCaliber.append(subArray[5])
            subPenetration.append(subArray[6])



    caliber           = getCaliber(side, "VehicleMagazines", magazine)
    fireModes         = [x.lower().replace("manual","Fullauto") for x in getFireModes(side, "VehicleWeapons", weapon)]
    rpm               = getModeDependant(side + "VehicleWeapons", weapon, fireModes, "reloadtime")
    dispersion        = getModeDependant(side + "VehicleWeapons", weapon, fireModes, "dispersion")
    initialSpeed      = getInitialSpeed(side, "VehicleMagazines", magazine)
    typicalSpeed      = getTypicalSpeed(side, "VehicleMagazines", magazine)
    airResistance     = getAirResistance(side, "VehicleMagazines", magazine)
    if str(airResistance).count("E") == 1:
        airResistance = "{:.8f}".format(float(airResistance))
    penetration       = ('{:.2f}'.format(round((typicalSpeed * caliber * 0.015),2)).zfill(4) + "|" +
                         '{:.2f}'.format(round((typicalSpeed * caliber * 0.080),2)).zfill(5) + "|" +
                         '{:.2f}'.format(round((typicalSpeed * caliber * 0.250),2)).zfill(5))



    # hit = hit * (speed / typicalSpeed)
    hitValues = []
    for distance in [100,500,1000,2000,3000]:
        try:
            estSpeed = initialSpeed * (1/math.exp(abs(airResistance) * distance))
        except OverflowError:
            estSpeed = float(initialSpeed * (1/Decimal(abs(airResistance)).exp() * distance))
        # str(distance).zfill(4) + ": " + '{:.2f}'.format(round(estSpeed, 2)).zfill(6) + " - Hit: " + '{:.3f}'.format(round(damage * (estSpeed/typicalSpeed),3)) + "\n"
        hitValues.append('{:.3f}'.format(round(damage * (estSpeed/typicalSpeed),3)))
        if hitValues[0] == 0:
            hitValues = ["","","","",""]

    thrust            = getThrust(side, "VehicleMagazines", magazine)
    thrustTime        = getThrustTime(side, "VehicleMagazines", magazine)
    maxSpeed          = getMaxSpeed(side, "VehicleMagazines", magazine)


    if len(rpm) > len(fireModes):
        del rpm[0]

    #FireMode filtering, likely more useful for vehicle weapons
    modeStats     = filterVehicleFireModes(fireModes, rpm, dispersion)
    fireModes     = modeStats[0]
    rpm           = modeStats[1]
    dispersion    = modeStats[2]

    if subDamage         == []: subDamage = ""
    if subIndirectDamage == []: subIndirectDamage = ""
    if subIndirectRange  == []: subIndirectRange = ""
    if subInitialSpeed   == []: subInitialSpeed = ""
    if subTypicalSpeed   == []: subTypicalSpeed = ""
    if subCaliber        == []: subCaliber = ""
    if subPenetration    == []: subPenetration = ""
    if subArray          == []: subArray = ""
    if fireModes         == []: fireModes = ""
    if rpm               == []: rpm = ""
    if dispersion        == []: dispersion = ""

    return [name, cartridge, capacity, damage, indirectDamage, indirectRange, subDamage, subIndirectDamage, subIndirectRange,
            fireModes, rpm, dispersion, initialSpeed, typicalSpeed, airResistance, penetration, subPenetration,
            hitValues[0], hitValues[1], hitValues[2], hitValues[3], hitValues[4],
            thrust, thrustTime, maxSpeed, weapon, magazine, caliber, subCaliber]

def writeVehicleWeaponStats(weapon, side, csvwriter):
    weaponStats = getVehicleWeaponStats(weapon[0], weapon[1], side)
    print(SEPERATOR)
    print(ccyan + "Name: " + cend + cgreen  + str(weaponStats[0])  + cend)
    csvwriter.writerow(weaponStats)
    print(SEPERATOR + "\n\n")

weaponArray = ["x","x","Name","Cartridge","Capacity","Damage","Fire Modes", "RPM", "Dispersion", "Initial Speed", "Typical Speed",
               "Air Resistance", "Penetration", "Damage at 100m", "Damage at 200m", "Damage at 300m", "Damage at 400m", "Damage at 500m", "Unlock Level"
               "Weapon Class", "Magazine Class", "Caliber"]
rhsusafWeapons = [
    ["rhs_weap_g36kv"         ,"rhssaf_30rnd_556x45_epr_g36"          ],
    ["rhs_weap_hk416d145"     ,"rhs_mag_30rnd_556x45_mk318_stanag"    ],
    ["rhs_weap_kar98k"        ,"rhsgref_5rnd_792x57_kar98k"           ],
    ["rhs_weap_l1a1_base"     ,"rhs_mag_20rnd_762x51_m80_fnfal"       ],
    ["rhs_weap_m107"          ,"rhsusf_mag_10rnd_std_50bmg_m33"       ],
    ["rhs_weap_m107"          , "rhsusf_mag_10rnd_std_50bmg_mk211"    ],
    ["rhs_weap_m14ebrri"      ,"rhsusf_20rnd_762x51_m118_special_mag" ],
    ["rhs_weap_m16a4"         ,"rhs_mag_30rnd_556x45_m855_stanag"     ],
    ["rhs_weap_m1garand_sa43" ,"rhsgref_8rnd_762x63_m2b_m1rifle"      ],
    ["rhs_weap_m21a"          ,"rhsgref_30rnd_556x45_m21"             ],
    ["rhs_weap_m240g"         ,"rhsusf_100rnd_762x51"                 ],
    ["rhs_weap_m249_pip"      ,"rhs_200rnd_556x45_b_saw"              ],
    ["rhs_weap_m249"          ,"rhs_200rnd_556x45_b_saw"              ],
    ["rhs_weap_m24sws"        ,"rhsusf_5rnd_762x51_m993_mag"          ],
    ["rhs_weap_m27iar"        ,"rhs_mag_30rnd_556x45_mk318_stanag"    ],
    ["rhs_weap_m3a1_specops"  ,"rhsgref_30rnd_1143x23_m1911b_smg"     ],
    ["rhs_weap_m40a5"         ,"rhsusf_10rnd_762x51_m993_mag"         ],
    ["rhs_weap_m4a1_blockii"  ,"rhs_mag_30rnd_556x45_mk262_stanag"    ],
    ["rhs_weap_m4a1"          ,"rhs_mag_30rnd_556x45_m855_stanag"     ],
    ["rhs_weap_m590_5rd"      ,"rhsusf_5rnd_00buck"                   ],
    ["rhs_weap_m590_5rd"      ,"rhsusf_5rnd_slug"                     ],
    ["rhs_weap_mg42"          ,"rhsgref_50rnd_792x57_sme_drum"        ],
    ["rhs_weap_mk18"          ,"rhs_mag_30rnd_556x45_mk262_stanag"    ],
    ["rhs_weap_mosin_sbr"     ,"rhsgref_5rnd_762x54_m38"              ],
    ["rhs_weap_mp44"          ,"rhsgref_30rnd_792x33_sme_stg"         ],
    ["rhs_weap_savz61"        ,"rhsgref_20rnd_765x17_vz61"            ],
    ["rhs_weap_scarh_std"     ,"rhs_mag_20rnd_scar_762x51_m80_ball"   ],
    ["rhs_weap_sr25"          ,"rhsusf_20rnd_762x51_m118_special_mag" ],
    ["rhs_weap_type94_new"    ,"rhs_mag_6x8mm_mhp"                    ],
    ["rhs_weap_xm2010"        ,"rhsusf_5rnd_300winmag_xm2010"         ],
    ["rhsusf_weap_glock17g4"  ,"rhsusf_mag_17rnd_9x19_jhp"            ],
    ["rhsusf_weap_m1911a1"    ,"rhsusf_mag_7x45acp_mhp"               ],
    ["rhsusf_weap_m9"         ,"rhsusf_mag_15rnd_9x19_jhp"            ],
    ["rhsusf_weap_mp7a2"      ,"rhsusf_mag_40rnd_46x30_jhp"           ]
]
rhsafrfWeapons = [
    ["rhs_weap_ak103"        ,"rhs_30rnd_762x39mm_polymer_89"],
    ["rhs_weap_ak74"         ,"rhs_30rnd_545x39_7n6_ak"      ],
    ["rhs_weap_6p53"         ,"rhs_18rnd_9x21mm_7n29"        ],
    ["rhs_weap_pb_6p9"       ,"rhs_mag_9x18_8_57n181s"       ],
    ["rhs_weap_pya"          ,"rhs_mag_9x19_17"              ],
    ["rhs_weap_makarov_pm"   ,"rhs_mag_9x18_8_57n181s"       ],
    ["rhs_weap_pp2000_folded","rhs_mag_9x19mm_7n21_20"       ],
    ["rhs_weap_tt33"         ,"rhs_mag_762x25_8"             ],
    ["rhs_weap_ak74m"        ,"rhs_30rnd_545x39_7n10_ak"     ],
    ["rhs_weap_ak74mr"       ,"rhs_30rnd_545x39_7n22_ak"     ],
    ["rhs_weap_akmn"         ,"rhs_30rnd_762x39mm"           ],
    ["rhs_weap_aks74un"      ,"rhs_30rnd_545x39_7n6m_ak"     ],
    ["rhs_weap_asval_npz"    ,"rhs_20rnd_9x39mm_sp6"         ],
    ["rhs_weap_asval"        ,"rhs_20rnd_9x39mm_sp6"         ],
    ["rhs_weap_dsr1"         ,"rhsusf_5rnd_762x51_m62_mag"   ],
    ["rhs_weap_izh18"        ,"rhsgref_1rnd_00buck"          ],
    ["rhs_weap_izh18"        ,"rhsgref_1rnd_slug"            ],
    ["rhs_weap_m38_rail"     ,"rhsgref_5rnd_762x54_m38"      ],
    ["rhs_weap_m38"          ,"rhsgref_5rnd_762x54_m38"      ],
    ["rhs_weap_m76"          ,"rhsgref_10rnd_792x57_m76"     ],
    ["rhs_weap_m84"          ,"rhssaf_250rnd_762x54r"        ],
    ["rhs_weap_pkm"          ,"rhs_100rnd_762x54mmr"         ],
    ["rhs_weap_pkp"          ,"rhs_100rnd_762x54mmr"         ],
    ["rhs_weap_savz58p_rail" ,"rhs_30rnd_762x39mm"           ],
    ["rhs_weap_savz58v_fold" ,"rhs_30rnd_762x39mm"           ],
    ["rhs_weap_svdp_npz"     ,"rhs_10rnd_762x54mmr_7n14"     ],
    ["rhs_weap_svdp"         ,"rhs_10rnd_762x54mmr_7n14"     ],
    ["rhs_weap_t5000"        ,"rhs_5rnd_338lapua_t5000"      ],
    ["rhs_weap_vhsd2"        ,"rhsgref_30rnd_556x45_vhs2"    ],
    ["rhs_weap_vss_npz"      ,"rhs_10rnd_9x39mm_sp5"         ],
    ["rhs_weap_vss"          ,"rhs_10rnd_9x39mm_sp5"         ]
]


vehicleWeaponArray = ["Name","Cartridge","Capacity","Damage","Indirect Damage","Indirect Range", "Submunition Damage", "Submunition Indirect Damage",
                      "Submunition Indirect Range", "Fire Modes", "RPM", "Dispersion", "Initial Speed", "Typical Speed",
                      "Air Resistance", "Penetration", "Submunition Penetration", "Damage at 100m", "Damage at 500m", "Damage at 1000m", "Damage at 2000m", "Damage at 3000m",
                      "Thrust", "Thrust Time", "Max speed",
                      "Weapon Class", "Magazine Class", "Caliber", "Submunition Caliber"]
rhsusafVehicleWeapons = [
    ["rhs_weap_gau8"                ,"rhs_mag_1150rnd_30x173_mixed"             ],
    ["rhs_m2"                       , "rhs_mag_100rnd_127x99_mag_tracer_red"    ],
    ["rhs_mk19"                     ,"rhs_48rnd_40mm_mk19_m430a1"               ],
    ["rhs_mk19"                     ,"rhs_48rnd_40mm_mk19_m1001"                ],
    ["rhsusf_weap_m259"             ,"rhsusf_mag_l8a3_8"                        ],
    ["rhs_weap_tow_launcher_static" ,"rhs_mag_tow2a"                            ],
    ["rhs_weap_tow_launcher_static" ,"rhs_mag_tow2b"                            ],
    ["rhs_weap_tow_launcher_static" ,"rhs_mag_tow2bb"                           ],
    ["rhs_m2_m1117"                 ,"rhs_mag_200rnd_127x99_mag_tracer_red"     ],
    ["rhsusf_weap_m257_8"           ,"rhsusf_mag_l8a3_8"                        ],
    ["rhs_weap_2a14"                ,"rhs_mag_azp23_100"                        ],
    ["rhs_m2_crows_m153"            ,"rhs_mag_400rnd_127x99_mag_tracer_red"     ],
    ["rhs_weap_m242bc"              ,"rhs_mag_70rnd_25mm_m242_apfsds"           ],
    ["rhs_weap_m242bc"              ,"rhs_mag_230rnd_25mm_m242_hei"             ],
    ["rhs_weap_m240_bradley_coax"   ,"rhs_mag_1100rnd_762x51_m240"              ],
    ["rhs_weap_stinger_launcher"    ,"rhs_mag_4rnd_stinger"                     ],
	["rhs_weap_tow_launcher"        ,"rhs_mag_2rnd_tow2a"                       ],
	["rhs_weap_tow_launcher"        ,"rhs_mag_2rnd_tow2bb"                      ],
	["rhs_weap_m256"                ,"rhs_mag_m829a1"                           ],
	["rhs_weap_m256"                ,"rhs_mag_m830a1"                           ],
	["rhs_weap_m240_abrams_coax"    ,"rhs_mag_762x51_m240_1200"                 ],
	["rhs_m2_abrams_gunner"         ,"rhs_mag_200rnd_127x99_slap_mag_tracer_red"],
	["rhs_weap_tow_launcher"        ,"rhs_mag_2rnd_tow2b_aero"                  ],
	["rhs_weap_m134_pylon"          ,"rhs_mag_m134_pylon_3000"                  ],
	["rhs_weap_ffarlauncher"        ,"rhs_mag_m151_7_green"                     ],
	["rhs_weap_m134_minigun_1"      ,"rhs_mag_762x51_m80a1_4000"                ],
	["rhs_weap_gau19"               ,"rhs_mag_gau19_air_base"                   ],
	["rhs_weap_ffarlauncher"        ,"rhs_mag_m151_19_green"                    ],
	["rhs_weap_m197"                ,"rhs_mag_m197_750"                         ],
	["rhs_weap_m230"                ,"rhs_mag_30x113mm_m789_hedp_1200"          ],
	["rhs_weap_hellfirelauncher"    ,"rhs_mag_agm114l_4"                        ],
	["rhs_weap_hellfirelauncher"    ,"rhs_mag_agm114k_4"                        ],
	["rhs_weap_gbu12"               ,"rhs_mag_gbu12"                            ],
	["rhs_weap_zpl20"               ,"rhs_mag_zpl20_mixed"                      ],
	["rhs_weap_mk82"                ,"rhs_mag_mk82"                             ]
]
rhsafrfVehicleWeapons = [
    ["rhs_weap_dshkm"         ,"rhs_mag_127x108mm_50"       ],
    ["rhs_weap_ags30"         ,"rhs_mag_vog30_30"           ],
    ["rhs_weap_spg9"          ,"rhs_mag_og9v"               ],
    ["rhs_weap_spg9"          ,"rhs_mag_pg9v"               ],
    ["rhs_weap_kpvt"          ,"rhs_mag_145x115mm_50"       ],
    ["rhs_weap_pkt_btr"       ,"rhs_mag_762x54mm_250"       ],
    ["rhs_weap_9p148"         ,"rhs_mag_9m113_5"            ],
    ["rhs_weap_2a14"          ,"rhs_mag_azp23_100"          ],
    ["rhs_weap_s8"            ,"rhs_mag_s8_12"              ],
    ["rhs_weap_2a28"          ,"rhs_mag_pg15v_20"           ],
    ["rhs_weap_2a28"          ,"rhs_mag_og15v_20"           ],
    ["rhs_weap_pkt"           ,"rhs_mag_762x54mm_250"       ],
    ["rhs_weap_9k11"          ,"rhs_mag_9m14m"              ],
    ["rhs_weap_9m113"         ,"rhs_mag_9m113m"             ],
    ["rhs_weap_2a42"          ,"rhs_mag_3uof8_340"          ],
    ["rhs_weap_2a42"          ,"rhs_mag_3ubr8_160"          ],
    ["rhs_weap_azp23"         ,"rhs_mag_azp23_2000"         ],
    ["rhs_weap_2a75"          ,"rhs_mag_3bm46_10"           ],
    ["rhs_weap_2a75"          ,"rhs_mag_3bk29_8"            ],
    ["rhs_weap_2a75"          ,"rhs_mag_3of26_6"            ],
    ["rhs_weap_2a75"          ,"rhs_mag_9m119_6"            ],
    ["rhs_weap_2a42"          ,"rhs_mag_3uof8_180"          ],
    ["rhs_weap_2a42"          ,"rhs_mag_3ubr8_120"          ],
    ["rhs_weap_9k133"         ,"rhs_mag_9m133_2"            ],
    ["rhs_weap_2a70"          ,"rhs_mag_3uof17_22"          ],
    ["rhs_weap_2a70"          ,"rhs_mag_9m117_8"            ],
    ["rhs_weap_2a72"          ,"rhs_mag_3uof8_305"          ],
    ["rhs_weap_2a72"          ,"rhs_mag_3ubr6_195"          ],
    ["rhs_weap_pkt_bmd_coax"  ,"rhs_mag_762x54mm_2000"      ],
    ["rhs_weap_2a72_btr"      ,"rhs_mag_3uof8_150"          ],
    ["rhs_weap_2a72_btr"      ,"rhs_mag_3ubr11_150"         ],
    ["rhs_weap_pkt_btr80a"    ,"rhs_mag_762x54mm_2000"      ],
    ["rhs_weap_2a70"          ,"rhs_mag_9m117m_8"           ],
    ["rhs_weap_2a72"          ,"rhs_mag_3uof8_237"          ],
    ["rhs_weap_2a72"          ,"rhs_mag_3ubr11_227"         ],
    ["rhs_weap_2a46m"         ,"rhs_mag_3bm42_7"            ],
    ["rhs_weap_2a46m"         ,"rhs_mag_3bk18m_6"           ],
    ["rhs_weap_2a46m"         ,"rhs_mag_3of26_5"            ],
    ["rhs_weap_2a46m"         ,"rhs_mag_9m119_4"            ],
    ["rhs_weap_nsvt_t72"      ,"rhs_mag_127x108mm_50"       ],
    ["rhs_weap_2a46_2"        ,"rhs_mag_3bm22_14"           ],
    ["rhs_weap_2a46_2"        ,"rhs_mag_3bk18m_8"           ],
    ["rhs_weap_2a46_2"        ,"rhs_mag_3of26_6"            ],
    ["rhs_weap_2a46m_4"       ,"rhs_mag_3bm46_10"           ],
    ["rhs_weap_2a46m_4"       ,"rhs_mag_3bk31_8"            ],
    ["rhs_weap_2a46m_4"       ,"rhs_mag_3of26_6"            ],
    ["rhs_weap_2a46m_4"       ,"rhs_mag_9m119_4"            ],
    ["rhs_weap_2a46m_5"       ,"rhs_mag_3bm46_8"            ],
    ["rhs_weap_2a46m_5"       ,"rhs_mag_3bk31_3"            ],
    ["rhs_weap_2a46m_5"       ,"rhs_mag_3of26_7"            ],
    ["rhs_weap_2a46m_5"       ,"rhs_mag_9m119_4"            ],
    ["rhs_weap_yakb"          ,"rhs_mag_127x108mm_1slt_1470"],
    ["rhs_weap_gsh30"         ,"rhs_mag_gsh30_ofzt_750"     ],
    ["rhs_weap_s8"            ,"rhs_mag_b8m1_s8kom"         ],
    ["rhs_weap_fab250"        ,"rhs_mag_fab250"             ],
    ["rhs_weap_9m120_launcher","rhs_mag_9m120m_mi24_2x"     ],
    ["rhs_weap_s8df"          ,"rhs_mag_b8m1_s8df"          ],
    ["rhs_weap_gi2"           ,"rhs_mag_gi2_420_he"         ],
    ["rhs_weap_gi2"           ,"rhs_mag_gi2_420_ap"         ],
    ["rhs_weap_2a42"          ,"rhs_mag_3ubr11_125"         ],
    ["rhs_weap_2a42"          ,"rhs_mag_3uof8_125"          ],
    ["rhs_weap_9k121_launcher","rhs_mag_apu6_9m127m_ka52"   ],
    ["rhs_weap_s8"            ,"rhs_mag_b8v20a_ka52_s8kom"  ],
    ["rhs_weap_gsh23l"        ,"rhs_mag_upk23_mixed"        ],
    ["rhs_weap_gsh302"        ,"rhs_mag_gsh30_bt_250"       ],
    ["rhs_weap_s13"           ,"rhs_mag_b13l_s13b"          ],
    ["rhs_weap_9m120_launcher","rhs_mag_9m120m_mi28_8x"     ]
]

#Normal infantry weapons
with open("rhsusafWeaponExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(weaponArray)
    for weapon in rhsusafWeapons:
        writeWeaponStats(weapon, "rhsusaf", csvwriter)
with open("rhsafrfWeaponExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(weaponArray)
    for weapon in rhsafrfWeapons:
        writeWeaponStats(weapon, "rhsafrf", csvwriter)

#Vehicle weapons
with open("rhsusafVehicleWeaponExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(vehicleWeaponArray)
    for weapon in rhsusafVehicleWeapons:
        writeVehicleWeaponStats(weapon, "rhsusaf", csvwriter)
with open("rhsafrfVehicleWeaponExport.csv", "w", newline='\n') as csvfile:
    csvfile.truncate(0)  #Clear file
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(vehicleWeaponArray)
    for weapon in rhsafrfVehicleWeapons:
        writeVehicleWeaponStats(weapon, "rhsafrf", csvwriter)

# print('{:.2f}'.format(round((403.86 * 0.24 * 0.015)/10,2)).zfill(4) + "|" +
#                      '{:.2f}'.format(round((403.86 * 0.24 * 0.080)/10,2)).zfill(5) + "|" +
#                      '{:.2f}'.format(round((403.86 * 0.24 * 0.250)/10,2)).zfill(5))