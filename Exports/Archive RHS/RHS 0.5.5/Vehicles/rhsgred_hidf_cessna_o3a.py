rhsgred_hidf_cessna_o3a = {
    "author": "Red Hammer Studios",
    "scope": 2,
    "scopecurator": 2,
    "side": 1,
    "faction": "rhsgref_faction_hidf",
    "displayname": "O-3A",
    "vehicleclass": "Air",
    "crew": "rhsgref_hidf_helipilot",
    "typicalcargo": ["rhsgref_hidf_helipilot"],
    "hiddenselectionsmaterials": ["rhsgref|addons|rhsgref_vehicles_ret|data|hidf|cessna|rhs_cessna_ttx_ext_01.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|hidf|cessna|rhs_cessna_ttx_ext_02.rvmat","a3|air_f_exp|plane_civil_01|data|btt_int_01.rvmat","a3|air_f_exp|plane_civil_01|data|btt_int_02.rvmat"],
    "hiddenselectionstextures": ["rhsgref|addons|rhsgref_vehicles_ret|data|hidf|cessna|rhs_cessna_ttx_ext_01_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|hidf|cessna|rhs_cessna_ttx_ext_02_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_co.paa"],
    # Class: CfgVehicles|rhsgred_hidf_cessna_o3a|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "init": "this setVariable ['BIS_enableRandomization',false];"
    },
    "texturelist": [],
    # Class: CfgVehicles|C_Plane_Civil_01_F|SimpleObject [Indent level: 1],
    "simpleobject": {
        "eden": 1,
        "animate": [["mfd_on",0],["avionics_damage",0],["mfd_horizon_virtual_base_rotate",0],["mfd_horizon_virtual_base_dive",-0.01],["mfd_horizon_virtual_pip_1_damagehide",0],["mfd_horizon_virtual_pip_2_damagehide",0],["mfd_compass_pilot_rotate",0],["mfd_roll_indicator_pilot_rotate",0],["mfd_compass_copilot_rotate",0],["mfd_roll_indicator_copilot_rotate",0],["mfd_center_flaps_up_0",0],["mfd_center_flaps_landing_1",0],["mfd_center_flaps_landing_1_2",0],["mfd_center_flaps_takeoff",0],["mfd_center_needle_fuel_l",1],["mfd_center_needle_fuel_r",1],["mfd_center_needle_oil_psi",0],["mfd_center_needle_oil_temp",6.61],["mfd_center_needle_rpm",0],["mfd_center_needle_rpm_throttle",0],["cabin_throttle_move",0],["cabin_console_top_compass_rotate",0],["cabin_console_top_compass_backlit_rotate",0],["wheel_front",0],["wheel_left",0],["wheel_right",0],["gear_1_damper_move",0],["gear_2_damper_move",0],["gear_3_damper_move",0],["flap_l",0],["flap_r",0],["aileron_r",0],["aileron_r_brake",0],["aileron_l",0],["aileron_l_brake",0],["elevator_l",0],["elevator_r",0],["rudder",0],["propeler",0],["door_r_open",0],["door_l_open",0],["door_l_hydraulic_1",0],["door_l_hydraulic_2",0],["door_r_hydraulic_1",0],["door_r_hydraulic_2",0],["cabin_stick_pilot_bank",0],["cabin_stick_pilot_dive",0],["cabin_stick_copilot_bank",0],["cabin_stick_copilot_dive",0],["cabin_pedals_pilot_l",0],["cabin_pedals_pilot_r",0],["cabin_pedals_copilot_l",0],["cabin_pedals_copilot_r",0],["wing_left_light_volumetric_hide",6.61],["wing_right_light_volumetric_hide",6.61],["hull_lights_coll_on",0],["hull_lights_coll_on_white_1_blinking",0],["hull_lights_coll_on_white_2_blinking",0],["glass1_damagehide",0],["glass2_damagehide",0],["glass3_damagehide",0],["glass4_damagehide",0],["glass5_damagehide",0]],
        "hide": ["zasleh","wing_left_light","wing_right_light","zadni svetlo","clan","podsvit pristroju","poskozeni"],
        "verticaloffset": 1.548,
        "verticaloffsetworld": -0.059,
        "init": "''"
    },
    "editorpreview": "A3|EditorPreviews_F_Exp|Data|CfgVehicles|C_Plane_Civil_01_F.jpg",
    "_generalmacro": "C_Plane_Civil_01_F",
    "dlc": "Expansion",
    "accuracy": 1000,
    "mapsize": 11.18,
    "overviewpicture": "A3|Data_F_Exp|Images|VehicleCaesar_ca.paa",
    "hasdriver": 1,
    "hasgunner": 1,
    "transportsoldier": 2,
    "precisegetinout": 1,
    "driveraction": "Pilot_Plane_Civil_01",
    "getinaction": "Pilot_Plane_Civil_01_Enter",
    "getoutaction": "Pilot_Plane_Civil_01_Exit",
    "cargoaction": ["Passenger_Plane_Civil_01_R","Passenger_Plane_Civil_01_L"],
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "drivercaneject": 1,
    "cargocaneject": 1,
    "ejectspeed": [0,0,3],
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "useprecisegetinaction": 1,
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincargo": ["pos cargo r","pos cargo l"],
    "memorypointsgetincargodir": ["pos cargo r dir","pos cargo l dir"],
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo r","pos cargo r"],
    "driverlefthandanimname": "cabin_stick_pilot",
    "driverrighthandanimname": "",
    "driverleftleganimname": "cabin_pedals_pilot_l",
    "driverrightleganimname": "cabin_pedals_pilot_r",
    # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Damper_1_source [Indent level: 2]
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|AnimationSources|Hit_Avionics [Indent level: 2],
        "hit_avionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        }
    },
    "editorsubcategory": "EdSubcat_Planes",
    "icon": "A3|Air_F_Exp|Plane_Civil_01|Data|UI|Map_Plane_Civil_01_CA.paa",
    "picture": "A3|Air_F_Exp|Plane_Civil_01|Data|UI|Plane_Civil_01_CA.paa",
    "unitinfotype": "RscUnitInfoAirPlaneNoWeapon",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "simulation": "airplaneX",
    "model": "A3|Air_F_Exp|Plane_Civil_01|Plane_Civil_01_basic_F.p3d",
    "animated": 1,
    "hiddenselections": ["camo1","camo2","camo3","camo4"],
    "extcameraposition": [0,1.5,-15],
    "availableforsupporttypes": [],
    "weapons": [],
    "magazines": [],
    "driveoncomponent": [],
    "cabinopening": 1,
    "gearretracting": 0,
    "lightongear": 0,
    "memorypointsupply": "Supply_pos",
    "supplyradius": 4,
    "armor": 35,
    "armorstructural": 1,
    "damageresistance": 0.0001,
    "fuelconsumptionrate": 0.0255,
    "destrtype": "DestructWreck",
    "damageeffect": "AirDestructionEffects",
    "epeimpulsedamagecoef": 50,
    "waterleakiness": 1.5,
    # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 1.5,
            "explosionshielding": 1,
            "name": "HitHull",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "Hit_Hull",
            "depends": "Total",
            "minimalhit": 0,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "name": "HitGlass1",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "glass1",
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "name": "HitGlass2",
            "radius": 0.1,
            "visual": "glass2",
            "passthrough": 0,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "name": "HitGlass3",
            "radius": 0.1,
            "visual": "glass3",
            "passthrough": 0,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "name": "HitGlass4",
            "radius": 0.08,
            "visual": "glass4",
            "passthrough": 0,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "name": "HitGlass5",
            "radius": 0.08,
            "visual": "glass5",
            "passthrough": 0,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitRotor [Indent level: 2],
        "hitrotor": {
            "armor": 0.25,
            "explosionshielding": 1,
            "name": "HitRotor",
            "passthrough": 0.2,
            "radius": 0.13,
            "visual": "",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.25,
            "explosionshielding": 1,
            "name": "HitEngine",
            "passthrough": 0.2,
            "radius": 0.4,
            "visual": "Hit_Engine",
            "depends": "HitRotor",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.1,
            "explosionshielding": 3,
            "name": "HitAvionics",
            "passthrough": 0.2,
            "radius": 0.2,
            "visual": "MFD_off_dmg",
            "depends": "0",
            "minimalhit": 0.05,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.5,
            "explosionshielding": 2,
            "name": "HitFuel",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "Hit_AileronL",
            "depends": "0",
            "minimalhit": 0,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 1.5,
            "explosionshielding": 2,
            "name": "HitFuel2",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "Hit_AileronR",
            "depends": "0",
            "minimalhit": 0,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitLAileron",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "Hit_AileronL",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitRAileron",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "Hit_AileronR",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitLCRudder",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "Hit_RudderC",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitLCElevator",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "Hit_ElevatorL",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|HitPoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitRElevator",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "Hit_ElevatorR",
            "depends": "0",
            "minimalhit": 0.1,
            "material": -1
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|Damage [Indent level: 1],
    "damage": {
        "tex": ["A3|Air_F_Exp|Plane_Civil_01|Data|MFD|digital_mfd_background_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|MFD|digital_mfd_background_damage_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|MFD|digital_mfd_background_damage_co.paa"],
        "mat": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_damage.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_destruct.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_damage.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_destruct.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_ext.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_ext_damage.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_ext_damage.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_int.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_int_damage.rvmat","A3|Air_F_Exp|Plane_Civil_01|Data|btt_glass_int_damage.rvmat"]
    },
    "radartargetsize": 0.7,
    "visualtargetsize": 0.8,
    "irtargetsize": 0.8,
    "lockdetectionsystem": 0,
    "incomingmissiledetectionsystem": 0,
    "laserscanner": 0,
    "artilleryscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "irscanrangemin": 0,
    "irscanrangemax": 0,
    "irscantoeyefactor": 1,
    "threat": [0,0,0],
    "maxspeed": 450,
    "landingaoa": "10*3.1415/180",
    "landingspeed": 130,
    "stallspeed": 110,
    "stallwarningtreshold": 0.1,
    "wheelsteeringsensitivity": 1,
    "airbrake": 1,
    "flaps": 1,
    "flapsfrictioncoef": 0.4,
    "angleofindicence": "4*3.1415/180",
    "envelope": [0,0.01,0.4,1.6,3.2,3.4,3.5,3.6,3.6,3.7,3.7,3.6,1],
    "altnoforce": 7500,
    "altfullforce": 6000,
    "thrustcoef": [1.26,1.25,1.23,1.21,1.18,1.14,1.09,1.03,0.96,0.87,0.48,0.12,0,0,0,0],
    "aileronsensitivity": 0.7,
    "aileroncoef": [0,0.4,0.9,1.1,1.2,1.3,1.3],
    "elevatorsensitivity": 0.9,
    "elevatorcoef": [0,0.1,0.28,0.35,0.4,0.45,0.49,0.53,0.57,0.58,0.56],
    "rudderinfluence": 0.6946,
    "ruddercoef": [0,0.89,1.5,2.1,2.5,3,3.6,3.9,4,3.6,1.8],
    "aileroncontrolssensitivitycoef": 3.6,
    "elevatorcontrolssensitivitycoef": 2,
    "ruddercontrolssensitivitycoef": 3,
    "draconicforcexcoef": 12,
    "draconicforceycoef": 1,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [14,12,11.2,10.6,9.9,9.6,9.7,10.5,11,11.5,12],
    "draconictorqueycoef": [4.5,4.1,3.7,3.3,3,2.7,2.5,2.3,2.1,1.9,1.8],
    "vtolyawinfluence": 7,
    "vtolpitchinfluence": 3,
    "vtolrollinfluence": 9,
    # Class: CfgVehicles|Plane_Civil_01_base_F|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Wheels|Wheel_1 [Indent level: 2]
        "wheel_1": {
            "bonename": "Wheel_1",
            "steering": 0,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 20,
            "moi": 1,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 1500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "sprungmass": 144,
            "springstrength": 14366,
            "springdamperrate": 3448,
            "longitudinalstiffnessperunitgravity": 50,
            "latstiffx": 1,
            "latstiffy": 10,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "bonename": "Wheel_2",
            "steering": 0,
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "width": 0.28,
            "springdamperrate": 3062,
            "sprungmass": 128,
            "springstrength": 12757,
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "susptraveldirection": [0,-1,0],
            "side": "left",
            "mass": 20,
            "moi": 1,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 1500,
            "maxhandbraketorque": 0,
            "longitudinalstiffnessperunitgravity": 50,
            "latstiffx": 1,
            "latstiffy": 10,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "bonename": "Wheel_3",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "springdamperrate": 3062,
            "sprungmass": 128,
            "springstrength": 12757,
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "susptraveldirection": [0,-1,0],
            "mass": 20,
            "moi": 1,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 1500,
            "maxhandbraketorque": 0,
            "longitudinalstiffnessperunitgravity": 50,
            "latstiffx": 1,
            "latstiffy": 10,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1 [Indent level: 2]
        "btt_pilot_mfd_1": {
            "enableparallax": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Pos10Vector [Indent level: 3],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.5],
                "pos10": [1.225,1.1]
            },
            "topleft": "HUD LH pilot",
            "topright": "HUD PH pilot",
            "bottomleft": "HUD LD pilot",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.43]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Speed_number_anchor [Indent level: 4],
                "speed_number_anchor": {
                    "type": "fixed",
                    "pos": [0.07,0.37]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Alt_number_anchor [Indent level: 4],
                "alt_number_anchor": {
                    "type": "fixed",
                    "pos": [0.93,0.37]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Heading_number_anchor [Indent level: 4],
                "heading_number_anchor": {
                    "type": "fixed",
                    "pos": [0.5,0.465]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "refreshrate": 0.12,
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.43],
                    "pos10": [1.395,1.13]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Velocity2 [Indent level: 4],
                "velocity2": {
                    "refreshrate": 0.06,
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.43],
                    "pos10": [1.395,1.13]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|TerrainBone [Indent level: 4],
                "terrainbone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 200,
                    "minpos": [0.895,0.15],
                    "maxpos": [0.895,0.36]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP55 [Indent level: 4],
                "levelp55": {
                    "angle": 55,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM55 [Indent level: 4],
                "levelm55": {
                    "angle": -55,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP65 [Indent level: 4],
                "levelp65": {
                    "angle": 65,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM65 [Indent level: 4],
                "levelm65": {
                    "angle": -65,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP75 [Indent level: 4],
                "levelp75": {
                    "angle": 75,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM75 [Indent level: 4],
                "levelm75": {
                    "angle": -75,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP85 [Indent level: 4],
                "levelp85": {
                    "angle": 85,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM85 [Indent level: 4],
                "levelm85": {
                    "angle": -85,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.65,
                "width": 5,
                "color": [1,1,1],
                "condition": "on",
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity1Group [Indent level: 4],
                "velocity1group": {
                    "condition": "speed <= 8",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity1Group|TrueVelocityVector [Indent level: 5],
                    "truevelocityvector": {
                        "type": "line",
                        "width": 5,
                        "points": [["Velocity",[0,-0.02],1],["Velocity",[0.01,-0.01732],1],["Velocity",[0.01732,-0.01],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.01],1],["Velocity",[0.01,0.01732],1],["Velocity",[0,0.02],1],["Velocity",[-0.01,0.01732],1],["Velocity",[-0.01732,0.01],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.01],1],["Velocity",[-0.01,-0.01732],1],["Velocity",[0,-0.02],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.04],1],["Velocity",[0,-0.02],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity2Group [Indent level: 4],
                "velocity2group": {
                    "condition": "speed >= 8",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity2Group|TrueVelocityVector [Indent level: 5],
                    "truevelocityvector": {
                        "type": "line",
                        "width": 5,
                        "points": [["Velocity2",[0,-0.02],1],["Velocity2",[0.01,-0.01732],1],["Velocity2",[0.01732,-0.01],1],["Velocity2",[0.02,0],1],["Velocity2",[0.01732,0.01],1],["Velocity2",[0.01,0.01732],1],["Velocity2",[0,0.02],1],["Velocity2",[-0.01,0.01732],1],["Velocity2",[-0.01732,0.01],1],["Velocity2",[-0.02,0],1],["Velocity2",[-0.01732,-0.01],1],["Velocity2",[-0.01,-0.01732],1],["Velocity2",[0,-0.02],1],[],["Velocity2",[0.04,0],1],["Velocity2",[0.02,0],1],[],["Velocity2",[-0.04,0],1],["Velocity2",[-0.02,0],1],[],["Velocity2",[0,-0.04],1],["Velocity2",[0,-0.02],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Speed_number_anchor",[0,0],1],
                    "right": ["Speed_number_anchor",[0.075,0],1],
                    "down": ["Speed_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedScale_top [Indent level: 4],
                "speedscale_top": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.37,
                    "center": 0.235,
                    "bottom": 0.1,
                    "linexleft": 0.125,
                    "lineyright": 0.158,
                    "linexleftmajor": 0.09,
                    "lineyrightmajor": 0.158,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "right",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedScale_bottom [Indent level: 4],
                "speedscale_bottom": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.7,
                    "center": 0.59,
                    "bottom": 0.48,
                    "linexleft": 0.125,
                    "lineyright": 0.158,
                    "linexleftmajor": 0.09,
                    "lineyrightmajor": 0.158,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "right",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltScale_top [Indent level: 4],
                "altscale_top": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "altitudeASL",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.1,
                    "center": 0.235,
                    "bottom": 0.37,
                    "linexleft": 0.82,
                    "lineyright": 0.853,
                    "linexleftmajor": 0.888,
                    "lineyrightmajor": 0.82,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "left",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltScale_bottom [Indent level: 4],
                "altscale_bottom": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "altitudeASL",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.48,
                    "center": 0.59,
                    "bottom": 0.7,
                    "linexleft": 0.82,
                    "lineyright": 0.853,
                    "linexleftmajor": 0.888,
                    "lineyrightmajor": 0.82,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "left",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltitudeNumber [Indent level: 4],
                "altitudenumber": {
                    "type": "text",
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Alt_number_anchor",[0,0],1],
                    "right": ["Alt_number_anchor",[0.075,0],1],
                    "down": ["Alt_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|HeadingNumber [Indent level: 4],
                "headingnumber": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Heading_number_anchor",[0,0],1],
                    "right": ["Heading_number_anchor",[0.075,0],1],
                    "down": ["Heading_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup [Indent level: 4],
                "terraingroup": {
                    "type": "group",
                    "cliptl": [0,0],
                    "clipbr": [1,0.361],
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainLine [Indent level: 5],
                    "terrainline": {
                        "type": "line",
                        "width": 6,
                        "points": [["TerrainBone",[0,0],1],["TerrainBone",[0.45,0],1]]
                    },
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainText [Indent level: 5],
                    "terraintext": {
                        "type": "text",
                        "source": "static",
                        "text": "AGL",
                        "align": "right",
                        "scale": 1,
                        "pos": ["TerrainBone",[0,0.002],1],
                        "right": ["TerrainBone",[0.045,0.002],1],
                        "down": ["TerrainBone",[0,0.062],1]
                    },
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainNumber [Indent level: 5],
                    "terrainnumber": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": ["TerrainBone",[0,-0.08],1],
                        "right": ["TerrainBone",[0.06,-0.08],1],
                        "down": ["TerrainBone",[0,0],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|StallGroup [Indent level: 4],
                "stallgroup": {
                    "type": "group",
                    "condition": "stall",
                    "color": [1,0,0],
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|StallGroup|StallText [Indent level: 5],
                    "stalltext": {
                        "type": "text",
                        "source": "static",
                        "text": "STALL",
                        "align": "center",
                        "scale": 1,
                        "pos": ["PlaneW",[0,-0.2],1],
                        "right": ["PlaneW",[0.075,-0.2],1],
                        "down": ["PlaneW",[0,-0.1],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|FlapsGroup [Indent level: 4],
                "flapsgroup": {
                    "type": "group",
                    "condition": "flaps",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|FlapsGroup|FlapsText [Indent level: 5],
                    "flapstext": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 1,
                        "pos": ["Alt_number_anchor",[-0.1,0.36],1],
                        "right": ["Alt_number_anchor",[-0.04,0.36],1],
                        "down": ["Alt_number_anchor",[-0.1,0.44],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|LightsGroup [Indent level: 4],
                "lightsgroup": {
                    "type": "group",
                    "condition": "lights",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|LightsGroup|LightsText [Indent level: 5],
                    "lightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "LLS",
                        "align": "left",
                        "scale": 1,
                        "pos": ["Speed_number_anchor",[0.1,0.36],1],
                        "right": ["Speed_number_anchor",[0.16,0.36],1],
                        "down": ["Speed_number_anchor",[0.1,0.44],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|CollisionLightsGroup [Indent level: 4],
                "collisionlightsgroup": {
                    "type": "group",
                    "condition": "collisionlights",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|CollisionLightsGroup|CollisionLightsText [Indent level: 5],
                    "collisionlightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "COLL",
                        "align": "left",
                        "scale": 1,
                        "pos": ["Speed_number_anchor",[0.1,0.42],1],
                        "right": ["Speed_number_anchor",[0.16,0.42],1],
                        "down": ["Speed_number_anchor",[0.1,0.5],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.2,0.18],
                    "clipbr": [0.8,0.7],
                    "width": 6,
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|Level0_extensions [Indent level: 6],
                        "level0_extensions": {
                            "type": "line",
                            "points": [["Level0",[-0.32,0.03],1],["Level0",[-0.32,0],1],["Level0",[-0.2,0],1],[],["Level0",[0.2,0],1],["Level0",[0.32,0],1],["Level0",[0.32,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM55 [Indent level: 6],
                        "levelm55": {
                            "type": "line",
                            "points": [["LevelM55",[-0.2,-0.03],1],["LevelM55",[-0.2,0],1],["LevelM55",[-0.15,0],1],[],["LevelM55",[-0.1,0],1],["LevelM55",[-0.05,0],1],[],["LevelM55",[0.05,0],1],["LevelM55",[0.1,0],1],[],["LevelM55",[0.15,0],1],["LevelM55",[0.2,0],1],["LevelM55",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP55 [Indent level: 6],
                        "levelp55": {
                            "type": "line",
                            "points": [["LevelP55",[-0.2,0.03],1],["LevelP55",[-0.2,0],1],["LevelP55",[-0.05,0],1],[],["LevelP55",[0.05,0],1],["LevelP55",[0.2,0],1],["LevelP55",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM60 [Indent level: 6],
                        "levelm60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.2,-0.03],1],["LevelM60",[-0.2,0],1],["LevelM60",[-0.15,0],1],[],["LevelM60",[-0.1,0],1],["LevelM60",[-0.05,0],1],[],["LevelM60",[0.05,0],1],["LevelM60",[0.1,0],1],[],["LevelM60",[0.15,0],1],["LevelM60",[0.2,0],1],["LevelM60",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP60 [Indent level: 6],
                        "levelp60": {
                            "type": "line",
                            "points": [["LevelP60",[-0.2,0.03],1],["LevelP60",[-0.2,0],1],["LevelP60",[-0.05,0],1],[],["LevelP60",[0.05,0],1],["LevelP60",[0.2,0],1],["LevelP60",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM65 [Indent level: 6],
                        "levelm65": {
                            "type": "line",
                            "points": [["LevelM65",[-0.2,-0.03],1],["LevelM65",[-0.2,0],1],["LevelM65",[-0.15,0],1],[],["LevelM65",[-0.1,0],1],["LevelM65",[-0.05,0],1],[],["LevelM65",[0.05,0],1],["LevelM65",[0.1,0],1],[],["LevelM65",[0.15,0],1],["LevelM65",[0.2,0],1],["LevelM65",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP65 [Indent level: 6],
                        "levelp65": {
                            "type": "line",
                            "points": [["LevelP65",[-0.2,0.03],1],["LevelP65",[-0.2,0],1],["LevelP65",[-0.05,0],1],[],["LevelP65",[0.05,0],1],["LevelP65",[0.2,0],1],["LevelP65",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM70 [Indent level: 6],
                        "levelm70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.2,-0.03],1],["LevelM70",[-0.2,0],1],["LevelM70",[-0.15,0],1],[],["LevelM70",[-0.1,0],1],["LevelM70",[-0.05,0],1],[],["LevelM70",[0.05,0],1],["LevelM70",[0.1,0],1],[],["LevelM70",[0.15,0],1],["LevelM70",[0.2,0],1],["LevelM70",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP70 [Indent level: 6],
                        "levelp70": {
                            "type": "line",
                            "points": [["LevelP70",[-0.2,0.03],1],["LevelP70",[-0.2,0],1],["LevelP70",[-0.05,0],1],[],["LevelP70",[0.05,0],1],["LevelP70",[0.2,0],1],["LevelP70",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM75 [Indent level: 6],
                        "levelm75": {
                            "type": "line",
                            "points": [["LevelM75",[-0.2,-0.03],1],["LevelM75",[-0.2,0],1],["LevelM75",[-0.15,0],1],[],["LevelM75",[-0.1,0],1],["LevelM75",[-0.05,0],1],[],["LevelM75",[0.05,0],1],["LevelM75",[0.1,0],1],[],["LevelM75",[0.15,0],1],["LevelM75",[0.2,0],1],["LevelM75",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP75 [Indent level: 6],
                        "levelp75": {
                            "type": "line",
                            "points": [["LevelP75",[-0.2,0.03],1],["LevelP75",[-0.2,0],1],["LevelP75",[-0.05,0],1],[],["LevelP75",[0.05,0],1],["LevelP75",[0.2,0],1],["LevelP75",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM80 [Indent level: 6],
                        "levelm80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.2,-0.03],1],["LevelM80",[-0.2,0],1],["LevelM80",[-0.15,0],1],[],["LevelM80",[-0.1,0],1],["LevelM80",[-0.05,0],1],[],["LevelM80",[0.05,0],1],["LevelM80",[0.1,0],1],[],["LevelM80",[0.15,0],1],["LevelM80",[0.2,0],1],["LevelM80",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP80 [Indent level: 6],
                        "levelp80": {
                            "type": "line",
                            "points": [["LevelP80",[-0.2,0.03],1],["LevelP80",[-0.2,0],1],["LevelP80",[-0.05,0],1],[],["LevelP80",[0.05,0],1],["LevelP80",[0.2,0],1],["LevelP80",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM85 [Indent level: 6],
                        "levelm85": {
                            "type": "line",
                            "points": [["LevelM85",[-0.2,-0.03],1],["LevelM85",[-0.2,0],1],["LevelM85",[-0.15,0],1],[],["LevelM85",[-0.1,0],1],["LevelM85",[-0.05,0],1],[],["LevelM85",[0.05,0],1],["LevelM85",[0.1,0],1],[],["LevelM85",[0.15,0],1],["LevelM85",[0.2,0],1],["LevelM85",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP85 [Indent level: 6],
                        "levelp85": {
                            "type": "line",
                            "points": [["LevelP85",[-0.2,0.03],1],["LevelP85",[-0.2,0],1],["LevelP85",[-0.05,0],1],[],["LevelP85",[0.05,0],1],["LevelP85",[0.2,0],1],["LevelP85",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM90 [Indent level: 6],
                        "levelm90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.2,-0.03],1],["LevelM90",[-0.2,0],1],["LevelM90",[-0.15,0],1],[],["LevelM90",[-0.1,0],1],["LevelM90",[-0.05,0],1],[],["LevelM90",[0.05,0],1],["LevelM90",[0.1,0],1],[],["LevelM90",[0.15,0],1],["LevelM90",[0.2,0],1],["LevelM90",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP90 [Indent level: 6],
                        "levelp90": {
                            "type": "line",
                            "points": [["LevelP90",[-0.2,0.03],1],["LevelP90",[-0.2,0],1],["LevelP90",[-0.05,0],1],[],["LevelP90",[0.05,0],1],["LevelP90",[0.2,0],1],["LevelP90",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "valm_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": "",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.165,-0.025],1],
                            "down": ["Level0",[-0.23,0.05],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "valm_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.285,-0.025],1],
                            "down": ["Level0",[0.22,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.165,0.035],1],
                            "down": ["LevelP5",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "valp_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.285,0.035],1],
                            "down": ["LevelP5",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.165,0.035],1],
                            "down": ["LevelP10",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "valp_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.285,0.035],1],
                            "down": ["LevelP10",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.165,0.035],1],
                            "down": ["LevelP15",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "valp_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.285,0.035],1],
                            "down": ["LevelP15",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.165,0.035],1],
                            "down": ["LevelP20",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "valp_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.285,0.035],1],
                            "down": ["LevelP20",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.165,0.035],1],
                            "down": ["LevelP25",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "valp_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.285,0.035],1],
                            "down": ["LevelP25",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.165,0.035],1],
                            "down": ["LevelP30",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "valp_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.285,0.035],1],
                            "down": ["LevelP30",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.165,0.035],1],
                            "down": ["LevelP35",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "valp_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.285,0.035],1],
                            "down": ["LevelP35",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.165,0.035],1],
                            "down": ["LevelP40",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "valp_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.285,0.035],1],
                            "down": ["LevelP40",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.165,0.035],1],
                            "down": ["LevelP45",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "valp_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.285,0.035],1],
                            "down": ["LevelP45",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.165,0.035],1],
                            "down": ["LevelP50",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "valp_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.285,0.035],1],
                            "down": ["LevelP50",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_55 [Indent level: 6],
                        "valp_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP55",[-0.23,0.035],1],
                            "right": ["LevelP55",[-0.165,0.035],1],
                            "down": ["LevelP55",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_55 [Indent level: 6],
                        "valp_2_55": {
                            "align": "right",
                            "pos": ["LevelP55",[0.22,0.035],1],
                            "right": ["LevelP55",[0.285,0.035],1],
                            "down": ["LevelP55",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_60 [Indent level: 6],
                        "valp_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP60",[-0.23,0.035],1],
                            "right": ["LevelP60",[-0.165,0.035],1],
                            "down": ["LevelP60",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_60 [Indent level: 6],
                        "valp_2_60": {
                            "align": "right",
                            "pos": ["LevelP60",[0.22,0.035],1],
                            "right": ["LevelP60",[0.285,0.035],1],
                            "down": ["LevelP60",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_65 [Indent level: 6],
                        "valp_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP65",[-0.23,0.035],1],
                            "right": ["LevelP65",[-0.165,0.035],1],
                            "down": ["LevelP65",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_65 [Indent level: 6],
                        "valp_2_65": {
                            "align": "right",
                            "pos": ["LevelP65",[0.22,0.035],1],
                            "right": ["LevelP65",[0.285,0.035],1],
                            "down": ["LevelP65",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_70 [Indent level: 6],
                        "valp_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP70",[-0.23,0.035],1],
                            "right": ["LevelP70",[-0.165,0.035],1],
                            "down": ["LevelP70",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_70 [Indent level: 6],
                        "valp_2_70": {
                            "align": "right",
                            "pos": ["LevelP70",[0.22,0.035],1],
                            "right": ["LevelP70",[0.285,0.035],1],
                            "down": ["LevelP70",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_75 [Indent level: 6],
                        "valp_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP75",[-0.23,0.035],1],
                            "right": ["LevelP75",[-0.165,0.035],1],
                            "down": ["LevelP75",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_75 [Indent level: 6],
                        "valp_2_75": {
                            "align": "right",
                            "pos": ["LevelP75",[0.22,0.035],1],
                            "right": ["LevelP75",[0.285,0.035],1],
                            "down": ["LevelP75",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_80 [Indent level: 6],
                        "valp_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP80",[-0.23,0.035],1],
                            "right": ["LevelP80",[-0.165,0.035],1],
                            "down": ["LevelP80",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_80 [Indent level: 6],
                        "valp_2_80": {
                            "align": "right",
                            "pos": ["LevelP80",[0.22,0.035],1],
                            "right": ["LevelP80",[0.285,0.035],1],
                            "down": ["LevelP80",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_85 [Indent level: 6],
                        "valp_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP85",[-0.23,0.035],1],
                            "right": ["LevelP85",[-0.165,0.035],1],
                            "down": ["LevelP85",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_85 [Indent level: 6],
                        "valp_2_85": {
                            "align": "right",
                            "pos": ["LevelP85",[0.22,0.035],1],
                            "right": ["LevelP85",[0.285,0.035],1],
                            "down": ["LevelP85",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_90 [Indent level: 6],
                        "valp_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP90",[-0.23,0.035],1],
                            "right": ["LevelP90",[-0.165,0.035],1],
                            "down": ["LevelP90",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_90 [Indent level: 6],
                        "valp_2_90": {
                            "align": "right",
                            "pos": ["LevelP90",[0.22,0.035],1],
                            "right": ["LevelP90",[0.285,0.035],1],
                            "down": ["LevelP90",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.165,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "valm_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.285,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.165,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "valm_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.285,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.165,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "valm_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.285,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.165,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "valm_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.285,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.165,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "valm_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.285,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.165,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "valm_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.285,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.165,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "valm_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.285,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.165,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "valm_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.285,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.165,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "valm_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.285,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.165,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "valm_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.285,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_55 [Indent level: 6],
                        "valm_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM55",[-0.23,-0.085],1],
                            "right": ["LevelM55",[-0.165,-0.085],1],
                            "down": ["LevelM55",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_55 [Indent level: 6],
                        "valm_2_55": {
                            "align": "right",
                            "pos": ["LevelM55",[0.22,-0.085],1],
                            "right": ["LevelM55",[0.285,-0.085],1],
                            "down": ["LevelM55",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_60 [Indent level: 6],
                        "valm_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM60",[-0.23,-0.085],1],
                            "right": ["LevelM60",[-0.165,-0.085],1],
                            "down": ["LevelM60",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_60 [Indent level: 6],
                        "valm_2_60": {
                            "align": "right",
                            "pos": ["LevelM60",[0.22,-0.085],1],
                            "right": ["LevelM60",[0.285,-0.085],1],
                            "down": ["LevelM60",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_65 [Indent level: 6],
                        "valm_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM65",[-0.23,-0.085],1],
                            "right": ["LevelM65",[-0.165,-0.085],1],
                            "down": ["LevelM65",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_65 [Indent level: 6],
                        "valm_2_65": {
                            "align": "right",
                            "pos": ["LevelM65",[0.22,-0.085],1],
                            "right": ["LevelM65",[0.285,-0.085],1],
                            "down": ["LevelM65",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_70 [Indent level: 6],
                        "valm_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM70",[-0.23,-0.085],1],
                            "right": ["LevelM70",[-0.165,-0.085],1],
                            "down": ["LevelM70",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_70 [Indent level: 6],
                        "valm_2_70": {
                            "align": "right",
                            "pos": ["LevelM70",[0.22,-0.085],1],
                            "right": ["LevelM70",[0.285,-0.085],1],
                            "down": ["LevelM70",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_75 [Indent level: 6],
                        "valm_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM75",[-0.23,-0.085],1],
                            "right": ["LevelM75",[-0.165,-0.085],1],
                            "down": ["LevelM75",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_75 [Indent level: 6],
                        "valm_2_75": {
                            "align": "right",
                            "pos": ["LevelM75",[0.22,-0.085],1],
                            "right": ["LevelM75",[0.285,-0.085],1],
                            "down": ["LevelM75",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_80 [Indent level: 6],
                        "valm_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM80",[-0.23,-0.085],1],
                            "right": ["LevelM80",[-0.165,-0.085],1],
                            "down": ["LevelM80",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_80 [Indent level: 6],
                        "valm_2_80": {
                            "align": "right",
                            "pos": ["LevelM80",[0.22,-0.085],1],
                            "right": ["LevelM80",[0.285,-0.085],1],
                            "down": ["LevelM80",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_85 [Indent level: 6],
                        "valm_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM85",[-0.23,-0.085],1],
                            "right": ["LevelM85",[-0.165,-0.085],1],
                            "down": ["LevelM85",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_85 [Indent level: 6],
                        "valm_2_85": {
                            "align": "right",
                            "pos": ["LevelM85",[0.22,-0.085],1],
                            "right": ["LevelM85",[0.285,-0.085],1],
                            "down": ["LevelM85",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_90 [Indent level: 6],
                        "valm_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM90",[-0.23,-0.085],1],
                            "right": ["LevelM90",[-0.165,-0.085],1],
                            "down": ["LevelM90",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_90 [Indent level: 6],
                        "valm_2_90": {
                            "align": "right",
                            "pos": ["LevelM90",[0.22,-0.085],1],
                            "right": ["LevelM90",[0.285,-0.085],1],
                            "down": ["LevelM90",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_2 [Indent level: 2],
        "btt_pilot_mfd_2": {
            "topleft": "HUD LH pilot 2",
            "topright": "HUD PH pilot 2",
            "bottomleft": "HUD LD pilot 2",
            "enableparallax": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Pos10Vector [Indent level: 3],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.5],
                "pos10": [1.225,1.1]
            },
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.43]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Speed_number_anchor [Indent level: 4],
                "speed_number_anchor": {
                    "type": "fixed",
                    "pos": [0.07,0.37]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Alt_number_anchor [Indent level: 4],
                "alt_number_anchor": {
                    "type": "fixed",
                    "pos": [0.93,0.37]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Heading_number_anchor [Indent level: 4],
                "heading_number_anchor": {
                    "type": "fixed",
                    "pos": [0.5,0.465]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "refreshrate": 0.12,
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.43],
                    "pos10": [1.395,1.13]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Velocity2 [Indent level: 4],
                "velocity2": {
                    "refreshrate": 0.06,
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.43],
                    "pos10": [1.395,1.13]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|TerrainBone [Indent level: 4],
                "terrainbone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 200,
                    "minpos": [0.895,0.15],
                    "maxpos": [0.895,0.36]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP55 [Indent level: 4],
                "levelp55": {
                    "angle": 55,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM55 [Indent level: 4],
                "levelm55": {
                    "angle": -55,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP65 [Indent level: 4],
                "levelp65": {
                    "angle": 65,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM65 [Indent level: 4],
                "levelm65": {
                    "angle": -65,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP75 [Indent level: 4],
                "levelp75": {
                    "angle": 75,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM75 [Indent level: 4],
                "levelm75": {
                    "angle": -75,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP85 [Indent level: 4],
                "levelp85": {
                    "angle": 85,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM85 [Indent level: 4],
                "levelm85": {
                    "angle": -85,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "pos0": [0.5,0.43],
                    "pos10": [1.4,1.13],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.65,
                "width": 5,
                "color": [1,1,1],
                "condition": "on",
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity1Group [Indent level: 4],
                "velocity1group": {
                    "condition": "speed <= 8",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity1Group|TrueVelocityVector [Indent level: 5],
                    "truevelocityvector": {
                        "type": "line",
                        "width": 5,
                        "points": [["Velocity",[0,-0.02],1],["Velocity",[0.01,-0.01732],1],["Velocity",[0.01732,-0.01],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.01],1],["Velocity",[0.01,0.01732],1],["Velocity",[0,0.02],1],["Velocity",[-0.01,0.01732],1],["Velocity",[-0.01732,0.01],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.01],1],["Velocity",[-0.01,-0.01732],1],["Velocity",[0,-0.02],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.04],1],["Velocity",[0,-0.02],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity2Group [Indent level: 4],
                "velocity2group": {
                    "condition": "speed >= 8",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Velocity2Group|TrueVelocityVector [Indent level: 5],
                    "truevelocityvector": {
                        "type": "line",
                        "width": 5,
                        "points": [["Velocity2",[0,-0.02],1],["Velocity2",[0.01,-0.01732],1],["Velocity2",[0.01732,-0.01],1],["Velocity2",[0.02,0],1],["Velocity2",[0.01732,0.01],1],["Velocity2",[0.01,0.01732],1],["Velocity2",[0,0.02],1],["Velocity2",[-0.01,0.01732],1],["Velocity2",[-0.01732,0.01],1],["Velocity2",[-0.02,0],1],["Velocity2",[-0.01732,-0.01],1],["Velocity2",[-0.01,-0.01732],1],["Velocity2",[0,-0.02],1],[],["Velocity2",[0.04,0],1],["Velocity2",[0.02,0],1],[],["Velocity2",[-0.04,0],1],["Velocity2",[-0.02,0],1],[],["Velocity2",[0,-0.04],1],["Velocity2",[0,-0.02],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Speed_number_anchor",[0,0],1],
                    "right": ["Speed_number_anchor",[0.075,0],1],
                    "down": ["Speed_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedScale_top [Indent level: 4],
                "speedscale_top": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.37,
                    "center": 0.235,
                    "bottom": 0.1,
                    "linexleft": 0.125,
                    "lineyright": 0.158,
                    "linexleftmajor": 0.09,
                    "lineyrightmajor": 0.158,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "right",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|SpeedScale_bottom [Indent level: 4],
                "speedscale_bottom": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.7,
                    "center": 0.59,
                    "bottom": 0.48,
                    "linexleft": 0.125,
                    "lineyright": 0.158,
                    "linexleftmajor": 0.09,
                    "lineyrightmajor": 0.158,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "right",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltScale_top [Indent level: 4],
                "altscale_top": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "altitudeASL",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.1,
                    "center": 0.235,
                    "bottom": 0.37,
                    "linexleft": 0.82,
                    "lineyright": 0.853,
                    "linexleftmajor": 0.888,
                    "lineyrightmajor": 0.82,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "left",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltScale_bottom [Indent level: 4],
                "altscale_bottom": {
                    "type": "scale",
                    "horizontal": 0,
                    "source": "altitudeASL",
                    "sourcescale": 3.6,
                    "width": 6,
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "top": 0.48,
                    "center": 0.59,
                    "bottom": 0.7,
                    "linexleft": 0.82,
                    "lineyright": 0.853,
                    "linexleftmajor": 0.888,
                    "lineyrightmajor": 0.82,
                    "majorlineeach": 5,
                    "numbereach": 1000,
                    "step": 5,
                    "stepsize": 0.057,
                    "align": "left",
                    "scale": 1,
                    "pos": [0,0],
                    "right": [0,0],
                    "down": [0,0]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|AltitudeNumber [Indent level: 4],
                "altitudenumber": {
                    "type": "text",
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Alt_number_anchor",[0,0],1],
                    "right": ["Alt_number_anchor",[0.075,0],1],
                    "down": ["Alt_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|HeadingNumber [Indent level: 4],
                "headingnumber": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": ["Heading_number_anchor",[0,0],1],
                    "right": ["Heading_number_anchor",[0.075,0],1],
                    "down": ["Heading_number_anchor",[0,0.1],1]
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup [Indent level: 4],
                "terraingroup": {
                    "type": "group",
                    "cliptl": [0,0],
                    "clipbr": [1,0.361],
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainLine [Indent level: 5],
                    "terrainline": {
                        "type": "line",
                        "width": 6,
                        "points": [["TerrainBone",[0,0],1],["TerrainBone",[0.45,0],1]]
                    },
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainText [Indent level: 5],
                    "terraintext": {
                        "type": "text",
                        "source": "static",
                        "text": "AGL",
                        "align": "right",
                        "scale": 1,
                        "pos": ["TerrainBone",[0,0.002],1],
                        "right": ["TerrainBone",[0.045,0.002],1],
                        "down": ["TerrainBone",[0,0.062],1]
                    },
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|TerrainGroup|TerrainNumber [Indent level: 5],
                    "terrainnumber": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": ["TerrainBone",[0,-0.08],1],
                        "right": ["TerrainBone",[0.06,-0.08],1],
                        "down": ["TerrainBone",[0,0],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|StallGroup [Indent level: 4],
                "stallgroup": {
                    "type": "group",
                    "condition": "stall",
                    "color": [1,0,0],
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|StallGroup|StallText [Indent level: 5],
                    "stalltext": {
                        "type": "text",
                        "source": "static",
                        "text": "STALL",
                        "align": "center",
                        "scale": 1,
                        "pos": ["PlaneW",[0,-0.2],1],
                        "right": ["PlaneW",[0.075,-0.2],1],
                        "down": ["PlaneW",[0,-0.1],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|FlapsGroup [Indent level: 4],
                "flapsgroup": {
                    "type": "group",
                    "condition": "flaps",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|FlapsGroup|FlapsText [Indent level: 5],
                    "flapstext": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 1,
                        "pos": ["Alt_number_anchor",[-0.1,0.36],1],
                        "right": ["Alt_number_anchor",[-0.04,0.36],1],
                        "down": ["Alt_number_anchor",[-0.1,0.44],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|LightsGroup [Indent level: 4],
                "lightsgroup": {
                    "type": "group",
                    "condition": "lights",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|LightsGroup|LightsText [Indent level: 5],
                    "lightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "LLS",
                        "align": "left",
                        "scale": 1,
                        "pos": ["Speed_number_anchor",[0.1,0.36],1],
                        "right": ["Speed_number_anchor",[0.16,0.36],1],
                        "down": ["Speed_number_anchor",[0.1,0.44],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|CollisionLightsGroup [Indent level: 4],
                "collisionlightsgroup": {
                    "type": "group",
                    "condition": "collisionlights",
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|CollisionLightsGroup|CollisionLightsText [Indent level: 5],
                    "collisionlightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "COLL",
                        "align": "left",
                        "scale": 1,
                        "pos": ["Speed_number_anchor",[0.1,0.42],1],
                        "right": ["Speed_number_anchor",[0.16,0.42],1],
                        "down": ["Speed_number_anchor",[0.1,0.5],1]
                    }
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.2,0.18],
                    "clipbr": [0.8,0.7],
                    "width": 6,
                    # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|Level0_extensions [Indent level: 6],
                        "level0_extensions": {
                            "type": "line",
                            "points": [["Level0",[-0.32,0.03],1],["Level0",[-0.32,0],1],["Level0",[-0.2,0],1],[],["Level0",[0.2,0],1],["Level0",[0.32,0],1],["Level0",[0.32,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM55 [Indent level: 6],
                        "levelm55": {
                            "type": "line",
                            "points": [["LevelM55",[-0.2,-0.03],1],["LevelM55",[-0.2,0],1],["LevelM55",[-0.15,0],1],[],["LevelM55",[-0.1,0],1],["LevelM55",[-0.05,0],1],[],["LevelM55",[0.05,0],1],["LevelM55",[0.1,0],1],[],["LevelM55",[0.15,0],1],["LevelM55",[0.2,0],1],["LevelM55",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP55 [Indent level: 6],
                        "levelp55": {
                            "type": "line",
                            "points": [["LevelP55",[-0.2,0.03],1],["LevelP55",[-0.2,0],1],["LevelP55",[-0.05,0],1],[],["LevelP55",[0.05,0],1],["LevelP55",[0.2,0],1],["LevelP55",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM60 [Indent level: 6],
                        "levelm60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.2,-0.03],1],["LevelM60",[-0.2,0],1],["LevelM60",[-0.15,0],1],[],["LevelM60",[-0.1,0],1],["LevelM60",[-0.05,0],1],[],["LevelM60",[0.05,0],1],["LevelM60",[0.1,0],1],[],["LevelM60",[0.15,0],1],["LevelM60",[0.2,0],1],["LevelM60",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP60 [Indent level: 6],
                        "levelp60": {
                            "type": "line",
                            "points": [["LevelP60",[-0.2,0.03],1],["LevelP60",[-0.2,0],1],["LevelP60",[-0.05,0],1],[],["LevelP60",[0.05,0],1],["LevelP60",[0.2,0],1],["LevelP60",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM65 [Indent level: 6],
                        "levelm65": {
                            "type": "line",
                            "points": [["LevelM65",[-0.2,-0.03],1],["LevelM65",[-0.2,0],1],["LevelM65",[-0.15,0],1],[],["LevelM65",[-0.1,0],1],["LevelM65",[-0.05,0],1],[],["LevelM65",[0.05,0],1],["LevelM65",[0.1,0],1],[],["LevelM65",[0.15,0],1],["LevelM65",[0.2,0],1],["LevelM65",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP65 [Indent level: 6],
                        "levelp65": {
                            "type": "line",
                            "points": [["LevelP65",[-0.2,0.03],1],["LevelP65",[-0.2,0],1],["LevelP65",[-0.05,0],1],[],["LevelP65",[0.05,0],1],["LevelP65",[0.2,0],1],["LevelP65",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM70 [Indent level: 6],
                        "levelm70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.2,-0.03],1],["LevelM70",[-0.2,0],1],["LevelM70",[-0.15,0],1],[],["LevelM70",[-0.1,0],1],["LevelM70",[-0.05,0],1],[],["LevelM70",[0.05,0],1],["LevelM70",[0.1,0],1],[],["LevelM70",[0.15,0],1],["LevelM70",[0.2,0],1],["LevelM70",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP70 [Indent level: 6],
                        "levelp70": {
                            "type": "line",
                            "points": [["LevelP70",[-0.2,0.03],1],["LevelP70",[-0.2,0],1],["LevelP70",[-0.05,0],1],[],["LevelP70",[0.05,0],1],["LevelP70",[0.2,0],1],["LevelP70",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM75 [Indent level: 6],
                        "levelm75": {
                            "type": "line",
                            "points": [["LevelM75",[-0.2,-0.03],1],["LevelM75",[-0.2,0],1],["LevelM75",[-0.15,0],1],[],["LevelM75",[-0.1,0],1],["LevelM75",[-0.05,0],1],[],["LevelM75",[0.05,0],1],["LevelM75",[0.1,0],1],[],["LevelM75",[0.15,0],1],["LevelM75",[0.2,0],1],["LevelM75",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP75 [Indent level: 6],
                        "levelp75": {
                            "type": "line",
                            "points": [["LevelP75",[-0.2,0.03],1],["LevelP75",[-0.2,0],1],["LevelP75",[-0.05,0],1],[],["LevelP75",[0.05,0],1],["LevelP75",[0.2,0],1],["LevelP75",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM80 [Indent level: 6],
                        "levelm80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.2,-0.03],1],["LevelM80",[-0.2,0],1],["LevelM80",[-0.15,0],1],[],["LevelM80",[-0.1,0],1],["LevelM80",[-0.05,0],1],[],["LevelM80",[0.05,0],1],["LevelM80",[0.1,0],1],[],["LevelM80",[0.15,0],1],["LevelM80",[0.2,0],1],["LevelM80",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP80 [Indent level: 6],
                        "levelp80": {
                            "type": "line",
                            "points": [["LevelP80",[-0.2,0.03],1],["LevelP80",[-0.2,0],1],["LevelP80",[-0.05,0],1],[],["LevelP80",[0.05,0],1],["LevelP80",[0.2,0],1],["LevelP80",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM85 [Indent level: 6],
                        "levelm85": {
                            "type": "line",
                            "points": [["LevelM85",[-0.2,-0.03],1],["LevelM85",[-0.2,0],1],["LevelM85",[-0.15,0],1],[],["LevelM85",[-0.1,0],1],["LevelM85",[-0.05,0],1],[],["LevelM85",[0.05,0],1],["LevelM85",[0.1,0],1],[],["LevelM85",[0.15,0],1],["LevelM85",[0.2,0],1],["LevelM85",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP85 [Indent level: 6],
                        "levelp85": {
                            "type": "line",
                            "points": [["LevelP85",[-0.2,0.03],1],["LevelP85",[-0.2,0],1],["LevelP85",[-0.05,0],1],[],["LevelP85",[0.05,0],1],["LevelP85",[0.2,0],1],["LevelP85",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelM90 [Indent level: 6],
                        "levelm90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.2,-0.03],1],["LevelM90",[-0.2,0],1],["LevelM90",[-0.15,0],1],[],["LevelM90",[-0.1,0],1],["LevelM90",[-0.05,0],1],[],["LevelM90",[0.05,0],1],["LevelM90",[0.1,0],1],[],["LevelM90",[0.15,0],1],["LevelM90",[0.2,0],1],["LevelM90",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|LevelP90 [Indent level: 6],
                        "levelp90": {
                            "type": "line",
                            "points": [["LevelP90",[-0.2,0.03],1],["LevelP90",[-0.2,0],1],["LevelP90",[-0.05,0],1],[],["LevelP90",[0.05,0],1],["LevelP90",[0.2,0],1],["LevelP90",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "valm_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": "",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.165,-0.025],1],
                            "down": ["Level0",[-0.23,0.05],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "valm_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.285,-0.025],1],
                            "down": ["Level0",[0.22,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.165,0.035],1],
                            "down": ["LevelP5",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "valp_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.285,0.035],1],
                            "down": ["LevelP5",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.165,0.035],1],
                            "down": ["LevelP10",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "valp_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.285,0.035],1],
                            "down": ["LevelP10",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.165,0.035],1],
                            "down": ["LevelP15",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "valp_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.285,0.035],1],
                            "down": ["LevelP15",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.165,0.035],1],
                            "down": ["LevelP20",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "valp_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.285,0.035],1],
                            "down": ["LevelP20",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.165,0.035],1],
                            "down": ["LevelP25",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "valp_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.285,0.035],1],
                            "down": ["LevelP25",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.165,0.035],1],
                            "down": ["LevelP30",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "valp_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.285,0.035],1],
                            "down": ["LevelP30",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.165,0.035],1],
                            "down": ["LevelP35",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "valp_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.285,0.035],1],
                            "down": ["LevelP35",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.165,0.035],1],
                            "down": ["LevelP40",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "valp_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.285,0.035],1],
                            "down": ["LevelP40",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.165,0.035],1],
                            "down": ["LevelP45",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "valp_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.285,0.035],1],
                            "down": ["LevelP45",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.165,0.035],1],
                            "down": ["LevelP50",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "valp_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.285,0.035],1],
                            "down": ["LevelP50",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_55 [Indent level: 6],
                        "valp_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP55",[-0.23,0.035],1],
                            "right": ["LevelP55",[-0.165,0.035],1],
                            "down": ["LevelP55",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_55 [Indent level: 6],
                        "valp_2_55": {
                            "align": "right",
                            "pos": ["LevelP55",[0.22,0.035],1],
                            "right": ["LevelP55",[0.285,0.035],1],
                            "down": ["LevelP55",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_60 [Indent level: 6],
                        "valp_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP60",[-0.23,0.035],1],
                            "right": ["LevelP60",[-0.165,0.035],1],
                            "down": ["LevelP60",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_60 [Indent level: 6],
                        "valp_2_60": {
                            "align": "right",
                            "pos": ["LevelP60",[0.22,0.035],1],
                            "right": ["LevelP60",[0.285,0.035],1],
                            "down": ["LevelP60",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_65 [Indent level: 6],
                        "valp_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP65",[-0.23,0.035],1],
                            "right": ["LevelP65",[-0.165,0.035],1],
                            "down": ["LevelP65",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_65 [Indent level: 6],
                        "valp_2_65": {
                            "align": "right",
                            "pos": ["LevelP65",[0.22,0.035],1],
                            "right": ["LevelP65",[0.285,0.035],1],
                            "down": ["LevelP65",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_70 [Indent level: 6],
                        "valp_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP70",[-0.23,0.035],1],
                            "right": ["LevelP70",[-0.165,0.035],1],
                            "down": ["LevelP70",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_70 [Indent level: 6],
                        "valp_2_70": {
                            "align": "right",
                            "pos": ["LevelP70",[0.22,0.035],1],
                            "right": ["LevelP70",[0.285,0.035],1],
                            "down": ["LevelP70",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_75 [Indent level: 6],
                        "valp_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP75",[-0.23,0.035],1],
                            "right": ["LevelP75",[-0.165,0.035],1],
                            "down": ["LevelP75",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_75 [Indent level: 6],
                        "valp_2_75": {
                            "align": "right",
                            "pos": ["LevelP75",[0.22,0.035],1],
                            "right": ["LevelP75",[0.285,0.035],1],
                            "down": ["LevelP75",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_80 [Indent level: 6],
                        "valp_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP80",[-0.23,0.035],1],
                            "right": ["LevelP80",[-0.165,0.035],1],
                            "down": ["LevelP80",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_80 [Indent level: 6],
                        "valp_2_80": {
                            "align": "right",
                            "pos": ["LevelP80",[0.22,0.035],1],
                            "right": ["LevelP80",[0.285,0.035],1],
                            "down": ["LevelP80",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_85 [Indent level: 6],
                        "valp_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP85",[-0.23,0.035],1],
                            "right": ["LevelP85",[-0.165,0.035],1],
                            "down": ["LevelP85",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_85 [Indent level: 6],
                        "valp_2_85": {
                            "align": "right",
                            "pos": ["LevelP85",[0.22,0.035],1],
                            "right": ["LevelP85",[0.285,0.035],1],
                            "down": ["LevelP85",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_1_90 [Indent level: 6],
                        "valp_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP90",[-0.23,0.035],1],
                            "right": ["LevelP90",[-0.165,0.035],1],
                            "down": ["LevelP90",[-0.23,0.11],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALP_2_90 [Indent level: 6],
                        "valp_2_90": {
                            "align": "right",
                            "pos": ["LevelP90",[0.22,0.035],1],
                            "right": ["LevelP90",[0.285,0.035],1],
                            "down": ["LevelP90",[0.22,0.11],1],
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.165,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "valm_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.285,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.165,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "valm_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.285,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.165,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "valm_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.285,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.165,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "valm_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.285,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.165,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "valm_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.285,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.165,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "valm_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.285,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.165,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "valm_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.285,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.165,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "valm_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.285,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.165,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "valm_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.285,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.165,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "valm_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.285,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_55 [Indent level: 6],
                        "valm_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM55",[-0.23,-0.085],1],
                            "right": ["LevelM55",[-0.165,-0.085],1],
                            "down": ["LevelM55",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_55 [Indent level: 6],
                        "valm_2_55": {
                            "align": "right",
                            "pos": ["LevelM55",[0.22,-0.085],1],
                            "right": ["LevelM55",[0.285,-0.085],1],
                            "down": ["LevelM55",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_60 [Indent level: 6],
                        "valm_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM60",[-0.23,-0.085],1],
                            "right": ["LevelM60",[-0.165,-0.085],1],
                            "down": ["LevelM60",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_60 [Indent level: 6],
                        "valm_2_60": {
                            "align": "right",
                            "pos": ["LevelM60",[0.22,-0.085],1],
                            "right": ["LevelM60",[0.285,-0.085],1],
                            "down": ["LevelM60",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_65 [Indent level: 6],
                        "valm_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM65",[-0.23,-0.085],1],
                            "right": ["LevelM65",[-0.165,-0.085],1],
                            "down": ["LevelM65",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_65 [Indent level: 6],
                        "valm_2_65": {
                            "align": "right",
                            "pos": ["LevelM65",[0.22,-0.085],1],
                            "right": ["LevelM65",[0.285,-0.085],1],
                            "down": ["LevelM65",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_70 [Indent level: 6],
                        "valm_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM70",[-0.23,-0.085],1],
                            "right": ["LevelM70",[-0.165,-0.085],1],
                            "down": ["LevelM70",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_70 [Indent level: 6],
                        "valm_2_70": {
                            "align": "right",
                            "pos": ["LevelM70",[0.22,-0.085],1],
                            "right": ["LevelM70",[0.285,-0.085],1],
                            "down": ["LevelM70",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_75 [Indent level: 6],
                        "valm_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM75",[-0.23,-0.085],1],
                            "right": ["LevelM75",[-0.165,-0.085],1],
                            "down": ["LevelM75",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_75 [Indent level: 6],
                        "valm_2_75": {
                            "align": "right",
                            "pos": ["LevelM75",[0.22,-0.085],1],
                            "right": ["LevelM75",[0.285,-0.085],1],
                            "down": ["LevelM75",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_80 [Indent level: 6],
                        "valm_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM80",[-0.23,-0.085],1],
                            "right": ["LevelM80",[-0.165,-0.085],1],
                            "down": ["LevelM80",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_80 [Indent level: 6],
                        "valm_2_80": {
                            "align": "right",
                            "pos": ["LevelM80",[0.22,-0.085],1],
                            "right": ["LevelM80",[0.285,-0.085],1],
                            "down": ["LevelM80",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_85 [Indent level: 6],
                        "valm_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM85",[-0.23,-0.085],1],
                            "right": ["LevelM85",[-0.165,-0.085],1],
                            "down": ["LevelM85",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_85 [Indent level: 6],
                        "valm_2_85": {
                            "align": "right",
                            "pos": ["LevelM85",[0.22,-0.085],1],
                            "right": ["LevelM85",[0.285,-0.085],1],
                            "down": ["LevelM85",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_1_90 [Indent level: 6],
                        "valm_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM90",[-0.23,-0.085],1],
                            "right": ["LevelM90",[-0.165,-0.085],1],
                            "down": ["LevelM90",[-0.23,-0.01],1]
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|MFD|BTT_pilot_MFD_1|Draw|Horizont|Dimmed|VALM_2_90 [Indent level: 6],
                        "valm_2_90": {
                            "align": "right",
                            "pos": ["LevelM90",[0.22,-0.085],1],
                            "right": ["LevelM90",[0.285,-0.085],1],
                            "down": ["LevelM90",[0.22,-0.01],1],
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                }
            }
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|RenderTargets|MFD_virtual_horizon [Indent level: 2]
        "mfd_virtual_horizon": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|Plane_Civil_01_base_F|RenderTargets|MFD_virtual_horizon|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "pos_MFD_virtual_camera",
                "pointdirection": "pos_MFD_virtual_camera_dir",
                "renderquality": 2,
                "rendervisionmode": 0,
                "fov": 0.25
            }
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|TransportBackpacks|_xx_B_Parachute [Indent level: 2]
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 4
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -5,
        "initfov": 0.75,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initangley": 0,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "iscopilot": 1,
            "gunnername": "Copilot",
            "primarygunner": 0,
            "ejectspeed": [0,0,3],
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "weapons": [],
            "magazines": [],
            "gunneraction": "Copilot_Plane_Civil_01",
            "gunnerinaction": "Copilot_Plane_Civil_01",
            "gunnergetinaction": "Copilot_Plane_Civil_01_Enter",
            "gunnergetoutaction": "Copilot_Plane_Civil_01_Exit",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "memorypointsgetingunnerprecise": "pos gunner",
            "precisegetinout": 1,
            "caneject": 1,
            "startengine": 0,
            "gunnerforceoptics": 0,
            "soundservo": ["",0.01,1],
            "outgunnermayfire": 0,
            "ingunnermayfire": 0,
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -130,
            "maxturn": 130,
            "initturn": 0,
            "maxhorizontalrotspeed": 3,
            "maxverticalrotspeed": 3,
            # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -5,
                "initfov": 0.75,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initangley": 0,
                "minanglex": -65,
                "maxanglex": 85,
                "minangley": -150,
                "maxangley": 150,
                "minmovex": -0.2,
                "maxmovex": 0.2,
                "minmovey": -0.1,
                "maxmovey": 0.1,
                "minmovez": -0.1,
                "maxmovez": 0.2,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|Plane_Civil_01_base_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "commanding": -1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "cabin_stick_copilot",
            "gunnerleftleganimname": "cabin_pedals_copilot_l",
            "gunnerrightleganimname": "cabin_pedals_copilot_r",
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnertype": "",
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsmodel": "",
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "lodturnedin": -1,
            "lodturnedout": -1,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
            "hitpoints": {
                # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
                "hitturret": {
                    "armor": 0.8,
                    "material": 51,
                    "name": "turret",
                    "visual": "turret",
                    "passthrough": 1,
                    "explosionshielding": 1
                },
                # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
                "hitgun": {
                    "armor": 0.6,
                    "material": 52,
                    "name": "gun",
                    "visual": "gun",
                    "passthrough": 1,
                    "explosionshielding": 1
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.3,
                "minfov": 0.07,
                "maxfov": 0.35,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "forcenvg": 0,
            "gunnerdoor": "",
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "disablesoundattenuation": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|Plane_Civil_01_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "memorypointldust": "WheelDust_left_pos",
    "memorypointrdust": "WheelDust_right_pos",
    # Class: CfgVehicles|Plane_Civil_01_base_F|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Exhausts|Exhaust_left [Indent level: 2]
        "exhaust_left": {
            "position": "pos_Exhausts_start_left",
            "direction": "pos_Exhausts_end_left",
            "effect": "ExhaustsEffectPlaneSmallHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Exhausts|Exhaust_right [Indent level: 2],
        "exhaust_right": {
            "position": "pos_Exhausts_start_right",
            "direction": "pos_Exhausts_end_right",
            "effect": "ExhaustsEffectPlaneSmallHP",
            "engineindex": 0
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|WingVortices|BodyLeft [Indent level: 2]
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "pos_Vapour_body_left"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "pos_Vapour_body_right"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|WingVortices|WingTipLeft [Indent level: 2],
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "pos_Vapour_wintip_left"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "pos_Vapour_wintip_right"
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red [Indent level: 2]
        "markerlight_wingtip_red": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "name": "marker_light_wingtip_l",
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_green [Indent level: 2],
        "markerlight_wingtip_green": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "marker_light_wingtip_r",
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|Collision_Light_tail_White [Indent level: 2],
        "collision_light_tail_white": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "marker_light_tail_white",
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingstartson": 1,
            "blinkingpatternguarantee": 1,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|Collision_Light_hull_White [Indent level: 2],
        "collision_light_hull_white": {
            "name": "marker_light_hull_white",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingstartson": 1,
            "blinkingpatternguarantee": 1,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|Collision_Light_wingtip_r_White [Indent level: 2],
        "collision_light_wingtip_r_white": {
            "name": "marker_light_wingtip_r_w",
            "blinking": 1,
            "blinkingpattern": [0.2,0.8],
            "blinkingstartson": 0,
            "blinkingpatternguarantee": 1,
            "drawlightsize": 0.1,
            "drawlightcentersize": 0.02,
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|Collision_Light_wingtip_l_White [Indent level: 2],
        "collision_light_wingtip_l_white": {
            "name": "marker_light_wingtip_l_w",
            "blinking": 1,
            "blinkingpattern": [0.2,0.8],
            "blinkingstartson": 0,
            "blinkingpatternguarantee": 1,
            "drawlightsize": 0.1,
            "drawlightcentersize": 0.02,
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Plane_Civil_01_base_F|MarkerLights|MarkerLight_wingtip_red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_1 [Indent level: 2]
        "wing_left_light_1": {
            "position": "pos_wing_left_light",
            "direction": "pos_wing_left_light_dir",
            "hitpoint": "wing_left_light",
            "selection": "wing_left_light",
            "color": [1900,1800,1700],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 20,
            "outerangle": 90,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 60,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_right_light_1 [Indent level: 2],
        "wing_right_light_1": {
            "position": "pos_wing_right_light",
            "direction": "pos_wing_right_light_dir",
            "hitpoint": "wing_right_light",
            "selection": "wing_right_light",
            "color": [1900,1800,1700],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 20,
            "outerangle": 90,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 60,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_right_light_2 [Indent level: 2],
        "wing_right_light_2": {
            "position": "pos_wing_right_light",
            "useflare": 1,
            "direction": "pos_wing_right_light_dir",
            "hitpoint": "wing_right_light",
            "selection": "wing_right_light",
            "color": [1900,1800,1700],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 20,
            "outerangle": 90,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 60,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_2 [Indent level: 2],
        "wing_left_light_2": {
            "position": "pos_wing_left_light",
            "useflare": 1,
            "direction": "pos_wing_left_light_dir",
            "hitpoint": "wing_left_light",
            "selection": "wing_left_light",
            "color": [1900,1800,1700],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 20,
            "outerangle": 90,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|Plane_Civil_01_base_F|Reflectors|Wing_left_light_1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 60,
                "hardlimitend": 120
            }
        }
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|Library [Indent level: 1],
    "library": {
        "libenable": 1,
        "libtextdesc": "Caesar BTT is a single-engine, fixed-gear, low-wing general aviation aircraft built from composite materials. The Caesar BTT is one of the fastest fixed-gear, single-engined piston aircraft, reaching a speed of 235 knots (435 km/h) true air speed at 25,000 feet (7,600 m). It is used by civilians and smaller shipping companies all around the world."
    },
    # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Racer_1 [Indent level: 2]
        "racer_1": {
            "displayname": "Racing (Tan Interior)",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Racer_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Racer_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_tan_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_tan_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Racer_2 [Indent level: 2],
        "racer_2": {
            "displayname": "Racing",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Racer_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Racer_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|RedLine_1 [Indent level: 2],
        "redline_1": {
            "displayname": "Red Line (Tan Interior)",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_RedLine_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_RedLine_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_tan_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_tan_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|RedLine_2 [Indent level: 2],
        "redline_2": {
            "displayname": "Red Line",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_RedLine_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_RedLine_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Wave_1 [Indent level: 2],
        "wave_1": {
            "displayname": "Blue Wave (Tan Interior)",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Wave_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Wave_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_tan_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_tan_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Wave_2 [Indent level: 2],
        "wave_2": {
            "displayname": "Blue Wave",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Wave_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Wave_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_co.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Tribal_1 [Indent level: 2],
        "tribal_1": {
            "displayname": "Tribal (Tan Interior)",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Tribal_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Tribal_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_tan_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_tan_co.paa"],
            "factions": ["CIV_F","IND_C_F"]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|TextureSources|Tribal_2 [Indent level: 2],
        "tribal_2": {
            "displayname": "Tribal",
            "author": "Bohemia Interactive",
            "textures": ["A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_01_Tribal_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_ext_02_Tribal_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_01_co.paa","A3|Air_F_Exp|Plane_Civil_01|Data|btt_int_02_co.paa"],
            "factions": ["CIV_F","IND_C_F"]
        }
    },
    "animationlist": [],
    "attenuationeffecttype": "PlaneAttenuation",
    "sounddammage": ["",0.562341,1],
    "soundlocked": ["",0.562341,1],
    "soundincommingmissile": ["",0.562341,1],
    "soundgearup": ["A3|Sounds_F_EPC|CAS_01|gear_up",0.794328,1,150],
    "soundgeardown": ["A3|Sounds_F_EPC|CAS_01|gear_down",0.794328,1,150],
    "soundflapsup": ["A3|Sounds_F_EPC|CAS_01|Flaps_Up",0.630957,1,100],
    "soundflapsdown": ["A3|Sounds_F_EPC|CAS_01|Flaps_Down",0.630957,1,100],
    "cabinopensound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|Plane_Civil_CabinOpen",3.16228,1,40],
    "cabinclosesound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|Plane_Civil_CabinClose",3.16228,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|Plane_Civil_CabinOpen",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|Plane_Civil_CabinClose",10,1,40],
    "soundgetin": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|Plane_Civil_GetIn",0.316228,1],
    "soundgetout": ["",0.316228,1,40],
    "buildcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",3.16228,1,900],
    "buildcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",3.16228,1,900],
    "buildcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",3.16228,1,900],
    "buildcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",3.16228,1,900],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "woodcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "woodcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "woodcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundwoodcrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorcrash0": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_ext_1",3.16228,1,900],
    "armorcrash1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_ext_2",3.16228,1,900],
    "armorcrash2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_ext_3",3.16228,1,900],
    "soundarmorcrash": ["ArmorCrash0",0.33,"ArmorCrash1",0.33,"ArmorCrash2",0.34],
    "crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",3.16228,1,900],
    "crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",3.16228,1,900],
    "crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",3.16228,1,900],
    "crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",3.16228,1,900],
    "soundcrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "soundengineonint": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_start_int",1,1],
    "soundengineonext": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_start_ext",1,1,600],
    "soundengineoffint": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_stop_int",1,1],
    "soundengineoffext": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_stop_ext",1,1,600],
    # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|EngineMidhExt [Indent level: 2]
        "enginemidhext": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_mid_ext",1.77828,1,1100],
            "frequency": "1.1 + rpm/3 + (thrust - 0.5)/6",
            "volume": "camPos*(rpm factor[0.15, 0.3])*(rpm factor[1.0, 0.5])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|EngineHighExt [Indent level: 2],
        "enginehighext": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_high_ext",1.77828,1,1100],
            "frequency": "1.2 + rpm/4 +(thrust - 0.5)/5",
            "volume": "camPos*(rpm factor[0.5, 0.9])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|ForsageExt [Indent level: 2],
        "forsageext": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_prop_ext",1.41254,1.2,1100],
            "frequency": "1 + (thrust - 0.5)/4",
            "volume": "camPos*(thrust factor[0, 1.0])*(rpm factor[0.7,1])",
            "cone": [1.14,3.92,2.5,0.4]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|EngineMidhInt [Indent level: 2],
        "enginemidhint": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_mid_int",1.77828,1,1100],
            "frequency": "1 + rpm/3 + (thrust - 0.5)/6",
            "volume": "(1-camPos)*(rpm factor[0.15, 0.3])*(rpm factor[1.0, 0.8])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|EngineHighInt [Indent level: 2],
        "enginehighint": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_engine_high_int",1.77828,1,1100],
            "frequency": "0.6 + rpm/5 +(thrust - 0.5)/5",
            "volume": "(1-camPos)*(rpm factor[0.4, 0.9])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|ForsageInt [Indent level: 2],
        "forsageint": {
            "sound": ["A3|Sounds_F_Exp|vehicles|air|Plane_Civil_01|BTT_prop_int",1.41254,1.2,1100],
            "frequency": "1 + (thrust - 0.5)/4",
            "volume": "(1-campos)*(thrust factor[0, 1.0])*(rpm factor[0.7,1])",
            "cone": [1.14,3.92,2.5,0.4]
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1.77828,1,100],
            "frequency": 1,
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|Waternoise_ext [Indent level: 2],
        "waternoise_ext": {
            "sound": ["A3|Sounds_F|vehicles|noises|air_driving_in_water",0.707946,1,300],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        # Class: CfgVehicles|Plane_Civil_01_base_F|Sounds|Waternoise_int [Indent level: 2],
        "waternoise_int": {
            "sound": ["A3|Sounds_F|vehicles|noises|soft_driving_in_water_int",0.562341,1,100],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    # Class: CfgVehicles|Plane_Base_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1
    },
    "mingforce": 0.3,
    "maxgforce": 3,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|Plane_Base_F|NewTurret [Indent level: 1],
    "newturret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationsourcebody": "mainTurret",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxytype": "CPGunner",
        "proxyindex": 1,
        "gunnername": "Gunner",
        "gunnertype": "",
        "primarygunner": 1,
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "minelev": -4,
        "maxelev": 20,
        "initelev": 0,
        "minturn": -360,
        "maxturn": 360,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "commanding": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "continuous": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "hideweaponsgunner": 1,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "outgunnermayfire": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "viewgunnerinexternal": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "startengine": 1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "hitpoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
            "hitturret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passthrough": 1,
                "explosionshielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "hitgun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passthrough": 1,
                "explosionshielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "iscopilot": 0,
        "caneject": 1,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "turretfollowfreelook": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "dontcreateai": 0,
        "disablesoundattenuation": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    "formationx": 200,
    "formationz": 300,
    "precision": 200,
    "brakedistance": 500,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "gearuptime": 3.33,
    "geardowntime": 2,
    "ejectdamagelimit": 0.45,
    "minfiretime": 60,
    "cost": 2e+006,
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "gunaimdown": 0,
    # Class: CfgVehicles|Plane|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": 0,
        "maxanglex": 0,
        "initangley": 0,
        "minangley": 0,
        "maxangley": 0,
        "initfov": 0.5,
        "minfov": 0.5,
        "maxfov": 0.5,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "selectionrotorstill": "vrtule staticka",
    "selectionrotormove": "vrtule blur",
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    # Class: CfgVehicles|Plane|GunFire [Indent level: 1],
    "gunfire": {
        "access": 0,
        "cloudletduration": 0.2,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.01,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 4500,
        "deltat": -3000,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|GunClouds [Indent level: 1],
    "gunclouds": {
        "access": 0,
        "cloudletduration": 0.3,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 1,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletaccy": 0.4,
        "cloudletminyspeed": 0.2,
        "cloudletmaxyspeed": 0.8,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunFire [Indent level: 1],
    "mgunfire": {
        "cloudletduration": 0,
        "cloudletgrowup": 0.06,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
        "initt": 3200,
        "deltat": -4000,
        "access": 0,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunClouds [Indent level: 1],
    "mgunclouds": {
        "access": 0,
        "cloudletgrowup": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletduration": 0.05,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 0.3,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsMGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "numberphysicalwheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_plane_s"],
            "speechplural": ["veh_air_plane_p"]
        }
    },
    "textsingular": "fast mover",
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "type": 2,
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "getinradius": 1.2,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
    "camshakecoef": 0,
    "headgforceleaningfactor": [0.005,0.001,0.025],
    "explosionshielding": 2,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "drivercompartments": 0,
    "cargocompartments": [0],
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    # Class: CfgVehicles|Air|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsAir|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsAir|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffectsAir"],
            "gdtstratisconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtstratisdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisseabedcluttered": ["LDustEffectsAir"],
            "gdtstratisseabed": ["LDustEffectsAir"],
            "gdtstratisdrygrass": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtstratisgreengrass": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisrocky": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisthistles": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtasphalt": ["LDustEffectsAir","LDirtEffects"],
            "gdtrubble": ["LDustEffectsAir","LDirtEffects"],
            "gdtsoil": ["LDustEffectsAir","LDirtEffects"],
            "gdtbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtrock": ["LDustEffectsAir","LDirtEffects"],
            "gdtdead": ["LDustEffectsAir","LDirtEffects"],
            "gdtdesert1": ["LDustEffectsAir","LSandEffects","LDirtEffects","LStonesEffects"],
            "gdtdesert2": ["LDustEffectsAir","LSandEffects","LGrassEffects","LDirtEffects"],
            "gdtdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtgrassgreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtgrassdry": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtgrasswild": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffectsAir"],
            "gdtseabed": ["LDustEffectsAir"],
            "surfroaddirt": ["LDustEffectsAir"],
            "surfroadconcrete": ["LDustEffectsAir"],
            "surfroadtarmac": ["LDustEffectsAir"],
            "surfwood": ["LDustEffectsAir"],
            "surfmetal": ["LDustEffectsAir"],
            "surfrooftin": ["LDustEffectsAir"],
            "surfrooftiles": ["LDustEffectsAir"],
            "surfintwood": ["LDustEffectsAir"],
            "surfintconcrete": ["LDustEffectsAir"],
            "surfinttiles": ["LDustEffectsAir"],
            "surfintmetal": ["LDustEffectsAir"],
            "gdtgrassshort": ["LDustEffectsAir","LGrassEffects"],
            "gdtgrasstall": ["LDustEffectsAir","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsAirRed"],
            "gdtfield": ["LDustEffectsAir"],
            "gdtforest": ["LDustEffectsAir"],
            "gdtvolcano": ["LDustEffectsAir","LStonesEffects"],
            "gdtcliff": ["LDustEffectsAir"],
            "gdtvolcanobeach": ["LDustEffectsAir"],
            "surfroaddirt_exp": ["LDustEffectsAirRed"],
            "surfroadconcrete_exp": ["LDustEffectsAir"],
            "surfroadtarmac_exp": ["LDustEffectsAir"],
            "gdtkldirt": ["LDustEffectsAir"],
            "gdtklgrass1": ["LDustEffectsAir","LGrassEffects"],
            "gdtklgrass2": ["LDustEffectsAir","LGrassEffects"],
            "gdtklforestcon": ["LDustEffectsAir"],
            "gdtklforestdec": ["LDustEffectsAir"],
            "gdtklmud": ["LDustEffectsAir"],
            "gdtklsoil": ["LDustEffectsAir"],
            "gdtkltarmac": ["LDustEffectsAir"],
            "gdtklstubble": ["LDustEffectsAir"],
            "gdtklstones": ["LDustEffectsAir"],
            "surfroaddirt_enoch": ["LDustEffectsAir"],
            "surftraildirt_enoch": ["LDustEffectsAir"],
            "surfroadtarmac1_enoch": ["LDustEffectsAir"],
            "surfroadtarmac2_enoch": ["LDustEffectsAir"],
            "surfroadtarmac3_enoch": ["LDustEffectsAir"]
        },
        # Class: CfgDustEffectsAir|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffectsAir"],
            "gdtstratisconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtstratisdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisseabedcluttered": ["RDustEffectsAir"],
            "gdtstratisseabed": ["RDustEffectsAir"],
            "gdtstratisdrygrass": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtstratisgreengrass": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisrocky": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisthistles": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtasphalt": ["RDustEffectsAir","RDirtEffects"],
            "gdtrubble": ["RDustEffectsAir","RDirtEffects"],
            "gdtsoil": ["RDustEffectsAir","RDirtEffects"],
            "gdtbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtrock": ["RDustEffectsAir","RDirtEffects"],
            "gdtdead": ["RDustEffectsAir","RDirtEffects"],
            "gdtdesert1": ["RDustEffectsAir","RSandEffects","RDirtEffects","RStonesEffects"],
            "gdtdesert2": ["RDustEffectsAir","RSandEffects","RGrassEffects","RDirtEffects"],
            "gdtdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtgrassgreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtgrassdry": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtgrasswild": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffectsAir"],
            "gdtseabed": ["RDustEffectsAir"],
            "surfroaddirt": ["RDustEffectsAir"],
            "surfroadconcrete": ["RDustEffectsAir"],
            "surfroadtarmac": ["RDustEffectsAir"],
            "surfwood": ["RDustEffectsAir"],
            "surfmetal": ["RDustEffectsAir"],
            "surfrooftin": ["RDustEffectsAir"],
            "surfrooftiles": ["RDustEffectsAir"],
            "surfintwood": ["RDustEffectsAir"],
            "surfintconcrete": ["RDustEffectsAir"],
            "surfinttiles": ["RDustEffectsAir"],
            "surfintmetal": ["RDustEffectsAir"],
            "gdtgrassshort": ["RDustEffectsAir","RGrassEffects"],
            "gdtgrasstall": ["RDustEffectsAir","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsAirRed"],
            "gdtfield": ["RDustEffectsAir"],
            "gdtforest": ["RDustEffectsAir"],
            "gdtvolcano": ["RDustEffectsAir","RStonesEffects"],
            "gdtcliff": ["RDustEffectsAir"],
            "gdtvolcanobeach": ["RDustEffectsAir"],
            "surfroaddirt_exp": ["RDustEffectsAirRed"],
            "surfroadconcrete_exp": ["RDustEffectsAir"],
            "surfroadtarmac_exp": ["RDustEffectsAir"],
            "gdtkldirt": ["RDustEffectsAir"],
            "gdtklgrass1": ["RDustEffectsAir","RGrassEffects"],
            "gdtklgrass2": ["RDustEffectsAir","RGrassEffects"],
            "gdtklforestcon": ["RDustEffectsAir"],
            "gdtklforestdec": ["RDustEffectsAir"],
            "gdtklmud": ["RDustEffectsAir"],
            "gdtklsoil": ["RDustEffectsAir"],
            "gdtkltarmac": ["RDustEffectsAir"],
            "gdtklstubble": ["RDustEffectsAir"],
            "gdtklstones": ["RDustEffectsAir"],
            "surfroaddirt_enoch": ["RDustEffectsAir"],
            "surftraildirt_enoch": ["RDustEffectsAir"],
            "surfroadtarmac1_enoch": ["RDustEffectsAir"],
            "surfroadtarmac2_enoch": ["RDustEffectsAir"],
            "surfroadtarmac3_enoch": ["RDustEffectsAir"]
        }
    },
    "maxfordingdepth": 0.001,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radartype": 4,
    "radartarget": 1,
    "visualtarget": 1,
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryexplosion": -1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointdriveroptics": ["driverview","pilot"],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
    "selectionshowdamage": "poskozeni",
    "selectionbacklights": "zadni svetlo",
    # Class: CfgVehicles|AllVehicles|ViewCargo [Indent level: 1],
    "viewcargo": {
        "initanglex": 5,
        "minanglex": -75,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -150,
        "maxangley": 150,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initfov": 0.75,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "pilotspec": {
        "showheadphones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "cargoprecisegetinout": [0],
    "waterppinvehicle": 1,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0.2,
    "tbody": 150,
    "impacteffectspeedlimit": 8,
    "showcrewaim": 0,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "cargoturret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2]
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|CargoTurret|Hitpoints [Indent level: 2],
        "hitpoints": {
        },
        "animationsourcebody": "",
        "animationsourcegun": "",
        "body": "",
        "caneject": 1,
        "commanding": 0,
        "dontcreateai": 1,
        "gun": "",
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnername": "cargo",
        "hideweaponsgunner": 0,
        "iscopilot": 0,
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "primarygunner": 0,
        "proxytype": "CPCargo",
        "startengine": 0,
        "turretfollowfreelook": 0,
        "viewgunnerinexternal": 1,
        "disablesoundattenuation": 1,
        "outgunnermayfire": 1,
        "ispersonturret": 1,
        "showascargo": 1,
        "maxelev": 45,
        "minelev": -45,
        "maxturn": 95,
        "minturn": -95,
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxyindex": 1,
        "gunnertype": "",
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "initelev": 0,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "shadow": 1,
    "featuretype": 0,
    "speechsingular": [],
    "speechplural": [],
    "maxdetectrange": 20,
    "detectskill": 20,
    "minealerticonrange": 200,
    "killfriendlyexpcoef": 1,
    "weaponslots": 0,
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "crewvulnerable": 1,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
    "camerasmoothspeed": 5,
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "alwaystarget": 0,
    "irtarget": 1,
    "irscanground": 1,
    "lasertarget": 0,
    "artillerytarget": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "driverforceoptics": 0,
    "enablewatch": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    "hulldamagecauseexplosion": 0,
    # Class: CfgVehicles|All|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
    },
    # Class: CfgVehicles|All|NVGMarker [Indent level: 1],
    "nvgmarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyinnvg": 0
    },
    # Class: CfgVehicles|All|HeadLimits [Indent level: 1],
    "headlimits": {
        "initanglex": 5,
        "minanglex": -30,
        "maxanglex": 40,
        "initangley": 0,
        "minangley": -90,
        "maxangley": 90,
        "minanglez": -45,
        "maxanglez": 45,
        "rotzradius": 0.2
    },
    "transportammo": 0,
    "isbackpack": 0,
    "transportfuel": 0,
    "transportrepair": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavhacker": 0,
    "soundengine": ["",1,1],
    "soundenviron": ["",1,1],
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "soundenvironext": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "soundequipment": {
    },
    # Class: CfgVehicles|All|SoundGear [Indent level: 1],
    "soundgear": {
    },
    # Class: CfgVehicles|All|SoundBreath [Indent level: 1],
    "soundbreath": {
    },
    # Class: CfgVehicles|All|SoundBreathSwimming [Indent level: 1],
    "soundbreathswimming": {
    },
    # Class: CfgVehicles|All|SoundBreathInjured [Indent level: 1],
    "soundbreathinjured": {
    },
    # Class: CfgVehicles|All|SoundHitScream [Indent level: 1],
    "soundhitscream": {
    },
    # Class: CfgVehicles|All|SoundInjured [Indent level: 1],
    "soundinjured": {
    },
    # Class: CfgVehicles|All|SoundBreathAutomatic [Indent level: 1],
    "soundbreathautomatic": {
    },
    # Class: CfgVehicles|All|SoundDrown [Indent level: 1],
    "sounddrown": {
    },
    # Class: CfgVehicles|All|SoundChoke [Indent level: 1],
    "soundchoke": {
    },
    # Class: CfgVehicles|All|SoundRecovered [Indent level: 1],
    "soundrecovered": {
    },
    # Class: CfgVehicles|All|SoundBurning [Indent level: 1],
    "soundburning": {
    },
    # Class: CfgVehicles|All|PulsationSound [Indent level: 1],
    "pulsationsound": {
    },
    # Class: CfgVehicles|All|SoundDrowning [Indent level: 1],
    "sounddrowning": {
    },
    "soundcrash": ["",0.316228,1],
    "soundlandcrash": ["",1,1],
    "soundwatercrash": ["",0.177828,1],
    "soundservo": ["",0.00316228,0.5],
    "soundelevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundlandcrashes": ["soundLandCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
    "aggregatereflectors": [],
    "driverinaction": "",
    "cargoiscodriver": [0],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "fxexplo": {
        "access": 1
    },
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "fireresistance": 10,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}