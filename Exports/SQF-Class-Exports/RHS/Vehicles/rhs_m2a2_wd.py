d = {
    "_generalmacro": "APC_Tracked_03_base_F",
    "accelaidforcecoef": 2,
    "accelaidforcespd": 4.23,
    "accelaidforceyoffset": -4,
    "access": 0,
    "accuracy": 0.3,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left"
        ],
        [
            "Right"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationlist": [
        "showBags",
        0,
        "showBags2",
        0,
        "showCamonetHull",
        0,
        "showCamonetTurret",
        0,
        "showTools",
        0,
        "showSLATHull",
        0,
        "showSLATTurret",
        0
    ],
    "animationsourcehatch": "",
    "animationsources": {
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "cargolights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "hatchc": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchd": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchg": {
            "animperiod": 2.1,
            "source": "door"
        },
        "iff_panels_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide IFF Panels",
            "initphase": 0,
            "mass": -20,
            "source": "user"
        },
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_weap_M242BC"
        },
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m240_bradley_coax"
        },
        "ramp": {
            "animperiod": 3.285,
            "initphase": 0,
            "sound": "rhs_ramp",
            "soundposition": "ramp_axis",
            "source": "door"
        },
        "rear_hatch": {
            "animperiod": 0.8,
            "initphase": 0,
            "source": "door"
        },
        "recoil_source": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        "select_stinger": {
            "animperiod": 1e-07,
            "author": "Red Hammer Studios",
            "displayname": "add TOW launcher",
            "forceanimate": [
                "Select_TOW",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 1,
            "onphasechanged": "_this call rhs_fnc_m2_handleWeaponVG",
            "source": "user"
        },
        "select_tow": {
            "animperiod": 1e-07,
            "author": "Red Hammer Studios",
            "displayname": "add Stinger launcher",
            "forceanimate": [
                "Select_Stinger",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "source": "user"
        },
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257_8"
        }
    },
    "antirollbarforcecoef": 15,
    "antirollbarforcelimit": 12,
    "antirollbarspeedmax": 55,
    "antirollbarspeedmin": 30,
    "armor": 290,
    "armorcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "armorcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "armorcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "armorcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
        1,
        200
    ],
    "armorcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "armorcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ],
    "armorlights": 0.1,
    "armorstructural": 280,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "TankAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "openramp": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open rear ramp",
            "expression": "_this animateDoor ['ramp', _value,true];_this setVariable ['ramp_handler',_value,true]",
            "property": "OpenRamp"
        },
        "rhs_hideiffpanel": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Hide IFF Panel",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "property": "rhs_hideIFFPanel"
        }
    },
    "audible": 18,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 1.78,
    "buildcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "buildcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "buildcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "buildcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
        1,
        200
    ],
    "buildcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "buildcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ],
    "bushcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_01",
        0.630957,
        1,
        100
    ],
    "bushcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_02",
        0.630957,
        1,
        100
    ],
    "bushcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_03",
        0.630957,
        1,
        100
    ],
    "cabinclosesound": [
        "",
        1,
        1
    ],
    "cabinclosesoundinternal": [
        "",
        1,
        1
    ],
    "cabinopensound": [
        "",
        1,
        1
    ],
    "cabinopensoundinternal": [
        "",
        1,
        1
    ],
    "camerasmoothspeed": 5,
    "camouflage": 8,
    "camshake": {
        "distance": 20,
        "frequency": 20,
        "minspeed": 5,
        "power": 5
    },
    "camshakecoef": 0,
    "camshakedamage": {
        "attenuation": 0.5,
        "distance": -1,
        "duration": 3,
        "frequency": 60,
        "minspeed": 1,
        "power": 0.5
    },
    "camshakegforce": {
        "distance": 0,
        "duration": 3,
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo02"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [
        "ramp"
    ],
    "cargogetinaction": [
        "GetInLow"
    ],
    "cargogetoutaction": [
        "GetOutLow"
    ],
    "cargoiscodriver": [
        0
    ],
    "cargolight": {
        "ambient": [
            0.6,
            0,
            0.15,
            1
        ],
        "brightness": 0.007,
        "color": [
            0,
            0,
            0,
            0
        ]
    },
    "cargoprecisegetinout": [
        0
    ],
    "cargoproxyindexes": [
        1,
        2,
        3,
        4,
        5,
        6
    ],
    "cargospec": {
        "cargo1": {
            "showheadphones": 0
        }
    },
    "cargoturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 0,
        "disablesoundattenuation": 1,
        "dontcreateai": 1,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "gunend": "konec hlavne",
        "gunfire": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletgrowup": 0.2,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletFire",
            "cloudletsize": 1,
            "deltat": -3000,
            "initt": 4500,
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        0.82,
                        0.95,
                        0.93,
                        0
                    ],
                    "maxt": 0
                },
                "t1": {
                    "color": [
                        0.75,
                        0.77,
                        0.9,
                        0
                    ],
                    "maxt": 200
                },
                "t10": {
                    "color": [
                        0.62,
                        0.29,
                        0.03,
                        0
                    ],
                    "maxt": 2600
                },
                "t11": {
                    "color": [
                        0.59,
                        0.35,
                        0.05,
                        0
                    ],
                    "maxt": 2650
                },
                "t12": {
                    "color": [
                        0.75,
                        0.37,
                        0.03,
                        0
                    ],
                    "maxt": 2700
                },
                "t13": {
                    "color": [
                        0.88,
                        0.34,
                        0.03,
                        0
                    ],
                    "maxt": 2750
                },
                "t14": {
                    "color": [
                        0.91,
                        0.5,
                        0.17,
                        0
                    ],
                    "maxt": 2800
                },
                "t15": {
                    "color": [
                        1,
                        0.6,
                        0.2,
                        0
                    ],
                    "maxt": 2850
                },
                "t16": {
                    "color": [
                        1,
                        0.71,
                        0.3,
                        0
                    ],
                    "maxt": 2900
                },
                "t17": {
                    "color": [
                        0.98,
                        0.83,
                        0.41,
                        0
                    ],
                    "maxt": 2950
                },
                "t18": {
                    "color": [
                        0.98,
                        0.91,
                        0.54,
                        0
                    ],
                    "maxt": 3000
                },
                "t19": {
                    "color": [
                        0.98,
                        0.99,
                        0.6,
                        0
                    ],
                    "maxt": 3100
                },
                "t2": {
                    "color": [
                        0.56,
                        0.62,
                        0.67,
                        0
                    ],
                    "maxt": 400
                },
                "t20": {
                    "color": [
                        0.96,
                        0.99,
                        0.72,
                        0
                    ],
                    "maxt": 3300
                },
                "t21": {
                    "color": [
                        1,
                        0.98,
                        0.91,
                        0
                    ],
                    "maxt": 3600
                },
                "t22": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 4200
                },
                "t3": {
                    "color": [
                        0.39,
                        0.46,
                        0.47,
                        0
                    ],
                    "maxt": 600
                },
                "t4": {
                    "color": [
                        0.24,
                        0.31,
                        0.31,
                        0
                    ],
                    "maxt": 800
                },
                "t5": {
                    "color": [
                        0.23,
                        0.31,
                        0.29,
                        0
                    ],
                    "maxt": 1000
                },
                "t6": {
                    "color": [
                        0.21,
                        0.29,
                        0.27,
                        0
                    ],
                    "maxt": 1500
                },
                "t7": {
                    "color": [
                        0.19,
                        0.23,
                        0.21,
                        0
                    ],
                    "maxt": 2000
                },
                "t8": {
                    "color": [
                        0.22,
                        0.19,
                        0.1,
                        0
                    ],
                    "maxt": 2300
                },
                "t9": {
                    "color": [
                        0.35,
                        0.2,
                        0.02,
                        0
                    ],
                    "maxt": 2500
                }
            },
            "timetolive": 0
        },
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "cargo",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 0,
        "hitpoints": {},
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "ispersonturret": 1,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 45,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 95,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 0.3,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletgrowup": 0.05,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "mincamelev": -90,
        "minelev": -45,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -95,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 1,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 0,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPCargo",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showascargo": 1,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 0,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 1,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "category": "Armored",
    "changegearomegaratios": [
        1,
        0.384615,
        0.384615,
        0,
        0.923077,
        0.384615,
        0.961538,
        0.538462,
        0.961538,
        0.576923,
        1,
        0.692308
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 35,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "commanderoptics": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "obsTurret",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "obsGun",
        "animationsourcehatch": "hatchCommander",
        "armorlights": 0.4,
        "body": "obsTurret",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 2,
        "disablesoundattenuation": 0,
        "dontcreateai": 0,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "obsGun",
        "gunbeg": "",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "gunend": "",
        "gunfire": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletgrowup": 0.2,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletFire",
            "cloudletsize": 1,
            "deltat": -3000,
            "initt": 4500,
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        0.82,
                        0.95,
                        0.93,
                        0
                    ],
                    "maxt": 0
                },
                "t1": {
                    "color": [
                        0.75,
                        0.77,
                        0.9,
                        0
                    ],
                    "maxt": 200
                },
                "t10": {
                    "color": [
                        0.62,
                        0.29,
                        0.03,
                        0
                    ],
                    "maxt": 2600
                },
                "t11": {
                    "color": [
                        0.59,
                        0.35,
                        0.05,
                        0
                    ],
                    "maxt": 2650
                },
                "t12": {
                    "color": [
                        0.75,
                        0.37,
                        0.03,
                        0
                    ],
                    "maxt": 2700
                },
                "t13": {
                    "color": [
                        0.88,
                        0.34,
                        0.03,
                        0
                    ],
                    "maxt": 2750
                },
                "t14": {
                    "color": [
                        0.91,
                        0.5,
                        0.17,
                        0
                    ],
                    "maxt": 2800
                },
                "t15": {
                    "color": [
                        1,
                        0.6,
                        0.2,
                        0
                    ],
                    "maxt": 2850
                },
                "t16": {
                    "color": [
                        1,
                        0.71,
                        0.3,
                        0
                    ],
                    "maxt": 2900
                },
                "t17": {
                    "color": [
                        0.98,
                        0.83,
                        0.41,
                        0
                    ],
                    "maxt": 2950
                },
                "t18": {
                    "color": [
                        0.98,
                        0.91,
                        0.54,
                        0
                    ],
                    "maxt": 3000
                },
                "t19": {
                    "color": [
                        0.98,
                        0.99,
                        0.6,
                        0
                    ],
                    "maxt": 3100
                },
                "t2": {
                    "color": [
                        0.56,
                        0.62,
                        0.67,
                        0
                    ],
                    "maxt": 400
                },
                "t20": {
                    "color": [
                        0.96,
                        0.99,
                        0.72,
                        0
                    ],
                    "maxt": 3300
                },
                "t21": {
                    "color": [
                        1,
                        0.98,
                        0.91,
                        0
                    ],
                    "maxt": 3600
                },
                "t22": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 4200
                },
                "t3": {
                    "color": [
                        0.39,
                        0.46,
                        0.47,
                        0
                    ],
                    "maxt": 600
                },
                "t4": {
                    "color": [
                        0.24,
                        0.31,
                        0.31,
                        0
                    ],
                    "maxt": 800
                },
                "t5": {
                    "color": [
                        0.23,
                        0.31,
                        0.29,
                        0
                    ],
                    "maxt": 1000
                },
                "t6": {
                    "color": [
                        0.21,
                        0.29,
                        0.27,
                        0
                    ],
                    "maxt": 1500
                },
                "t7": {
                    "color": [
                        0.19,
                        0.23,
                        0.21,
                        0
                    ],
                    "maxt": 2000
                },
                "t8": {
                    "color": [
                        0.22,
                        0.19,
                        0.1,
                        0
                    ],
                    "maxt": 2300
                },
                "t9": {
                    "color": [
                        0.35,
                        0.2,
                        0.02,
                        0
                    ],
                    "maxt": 2500
                }
            },
            "timetolive": 0
        },
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "GetInHigh",
        "gunnergetoutaction": "GetOutHigh",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "Commander",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "A3/weapons_f/reticle/Optics_Commander_02_F",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 1,
        "hitpoints": {
            "hitgun": {
                "armor": 0.6,
                "explosionshielding": 1,
                "material": 52,
                "name": "gun",
                "passthrough": 1,
                "visual": "gun"
            },
            "hitturret": {
                "armor": 0.8,
                "explosionshielding": 1,
                "material": 51,
                "name": "turret",
                "passthrough": 1,
                "visual": "turret"
            }
        },
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 20,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 360,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "gun_muzzle",
        "memorypointgunneroptics": "commanderview",
        "memorypointgunneroutoptics": "commander_weapon_view",
        "memorypointsgetingunner": "pos commander",
        "memorypointsgetingunnerdir": "pos commander dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 0.3,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletgrowup": 0.05,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "mincamelev": -90,
        "minelev": -4,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -360,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 1,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 0,
        "primaryobserver": 1,
        "proxyindex": 1,
        "proxytype": "CPCommander",
        "reflectors": {},
        "selectionfireanim": "zasleh_1",
        "showalltargets": 0,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "A3/sounds_f/dummysound",
            0.01,
            1,
            10
        ],
        "stabilizedinaxes": 0,
        "startengine": 1,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "compartmentslights": {
        "comp1": {
            "light1": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    22,
                    16
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.3,
                "point": "light_interior1",
                "size": 0,
                "useflare": 0
            },
            "light2": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    22,
                    16
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.6,
                "point": "light_interior2",
                "size": 0,
                "useflare": 0
            },
            "light3": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    22,
                    16
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.6,
                "point": "light_interior3",
                "size": 0,
                "useflare": 0
            },
            "light4": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    25,
                    25
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior4",
                "size": 0,
                "useflare": 0
            },
            "light5": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    25,
                    25
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior5",
                "size": 0,
                "useflare": 0
            },
            "light6": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    25,
                    25,
                    25
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 10,
                "point": "light_interior6",
                "size": 0,
                "useflare": 0
            }
        }
    },
    "complexgearbox": {
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -2.2,
            "N",
            0,
            "D1",
            4.2,
            "D2",
            2.23,
            "D3",
            1.22,
            "D4",
            0.839
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            14.75
        ]
    },
    "components": {
        "aitanksteeringcomponent": {
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "allowovertaking": 1,
            "allowturnaroundinpoint": 1,
            "commandturnfactor": 2,
            "convoypidweights": [
                1,
                0,
                0
            ],
            "differenceanglecoef": 1,
            "dopredictforward": 1,
            "doremapspeed": 0,
            "forwardanglecoef": 0.7,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.01,
            "predictforwardmaxspeed": 15,
            "predictforwardrange": [
                1,
                20
            ],
            "remapspeedrange": [
                30,
                70
            ],
            "remapspeedscalar": [
                1,
                0.35
            ],
            "speedpidweights": [
                0.7,
                0.2,
                0
            ],
            "speedpredictionmethod": 3,
            "steeraheadsaturation": [
                0.01,
                0.4
            ],
            "steeringanglecoef": 1,
            "steeringpidweights": [
                2.9,
                0.1,
                0.2
            ],
            "stuckmaxtime": 3,
            "wheelanglecoef": 0.7
        },
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "left": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        "vehiclesystemsdisplaymanagercomponentright": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 1000000.0,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_army_ucp_crewman",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV1.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV1_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV1_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2_ERAon.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2_ERAon_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/brad_UV2_ERAon_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/M2_tracks.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/M2_tracks_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/data/M2_tracks_destruct.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.01189,
    "damagetexdelay": 0,
    "dampersbumpcoef": 4.5,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "dampingratezerothrottleclutchengaged": 3,
    "delaybetweenejects": 0.5,
    "destrtype": "DestructDefault",
    "destructioneffects": {
        "firebig1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionFire1"
        },
        "firebig2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionFire2"
        },
        "firesparksbig1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "FireSparks"
        },
        "lightbig1": {
            "enabled": "distToWater",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "light",
            "type": "ObjectDestructionLight"
        },
        "refract1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionRefract"
        },
        "smokebig1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke"
        },
        "smokebig1_2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2"
        },
        "smokebig2": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2"
        },
        "sound": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "position": "destructionEffect1",
            "simulation": "sound",
            "type": "Fire"
        },
        "sparksbig1": {
            "intensity": 0,
            "interval": 1,
            "lifetime": 0,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSparks"
        }
    },
    "detectskill": 20,
    "displayname": "M2A2ODS",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "slide",
        "trackL",
        "trackR"
    ],
    "driveraction": "RHS_M2A2_DriverOut",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "hatchD",
    "driverforceoptics": 0,
    "driverinaction": "RHS_M2A2_Driver",
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "yoke",
    "driverleftleganimname": "pedal_brake",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsin": {
        "wide": {
            "hitpoint": "Hit_Optics_Dvr_Peri",
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.7,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.7,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.7,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "opticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_vision_block",
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0,
            "visionmode": [
                "Normal",
                "NVG"
            ]
        }
    },
    "driveropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_vision_block",
    "driverrighthandanimname": "yoke",
    "driverrightleganimname": "pedal_thrust",
    "dustbackleftpos": "wheel_1_7_bound",
    "dustbackrightpos": "wheel_2_7_bound",
    "dusteffects": {
        "both": {},
        "left": {
            "default": [
                "LDustEffects"
            ],
            "dirtrunway": [
                "LDustEffects"
            ],
            "gdtasphalt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtbeach": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtcliff": [
                "LDustEffects"
            ],
            "gdtconcrete": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtdead": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtdesert": [
                "LDustEffects",
                "LDirtEffectsBig",
                "LStonesEffects"
            ],
            "gdtdesert1": [
                "LDustEffects",
                "LDirtEffectsBig",
                "LStonesEffectsBig"
            ],
            "gdtdesert2": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtdirt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtfield": [
                "LDustEffects"
            ],
            "gdtforest": [
                "LDustEffects"
            ],
            "gdtgrassdry": [
                "LDustEffects",
                "LGrassEffectsDryBig",
                "LDirtEffectsBig"
            ],
            "gdtgrassgreen": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtgrassshort": [
                "LDustEffects",
                "LGrassEffectsBig"
            ],
            "gdtgrasstall": [
                "LDustEffects",
                "LGrassEffectsBig"
            ],
            "gdtgrasswild": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtkldirt": [
                "LDustEffects"
            ],
            "gdtklforestcon": [
                "LDustEffects"
            ],
            "gdtklforestdec": [
                "LDustEffects"
            ],
            "gdtklgrass1": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtklgrass2": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtklmud": [
                "LDustEffects"
            ],
            "gdtklsoil": [
                "LDustEffects"
            ],
            "gdtklstones": [
                "LStonesEffects"
            ],
            "gdtklstubble": [
                "LDustEffects"
            ],
            "gdtkltarmac": [
                "LDustEffects"
            ],
            "gdtreddirt": [
                "LDustEffectsRed"
            ],
            "gdtrock": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtrubble": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtseabed": [
                "LDustEffects"
            ],
            "gdtseabeddeep": [
                "LDustEffects"
            ],
            "gdtsoil": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstony": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstonygreen": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstonythistle": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisbeach": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtstratisconcrete": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstratisdirt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstratisdrygrass": [
                "LDustEffects",
                "LGrassEffectsDryBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisgreengrass": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisrocky": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisseabed": [
                "LDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffects"
            ],
            "gdtstratisthistles": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtthorn": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtvolcano": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtvolcanobeach": [
                "LDustEffects"
            ],
            "gdtweed1": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtweed2": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtwildfield": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "surfintconcrete": [
                "LDustEffects"
            ],
            "surfintmetal": [
                "LDustEffects"
            ],
            "surfinttiles": [
                "LDustEffects"
            ],
            "surfintwood": [
                "LDustEffects"
            ],
            "surfmetal": [
                "LDustEffects"
            ],
            "surfroadconcrete": [
                "LDustEffects"
            ],
            "surfroadconcrete_exp": [
                "LDustEffects"
            ],
            "surfroaddirt": [
                "LDustEffects"
            ],
            "surfroaddirt_enoch": [
                "LDustEffects"
            ],
            "surfroaddirt_exp": [
                "LDustEffectsRed"
            ],
            "surfroadtarmac": [
                "LDustEffects"
            ],
            "surfroadtarmac1_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac2_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac3_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac_exp": [
                "LDustEffects"
            ],
            "surfrooftiles": [
                "LDustEffects"
            ],
            "surfrooftin": [
                "LDustEffects"
            ],
            "surftraildirt_enoch": [
                "LDustEffects"
            ],
            "surfwood": [
                "LDustEffects"
            ]
        },
        "right": {
            "default": [
                "RDustEffects"
            ],
            "dirtrunway": [
                "RDustEffects"
            ],
            "gdtasphalt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtbeach": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtcliff": [
                "RDustEffects"
            ],
            "gdtconcrete": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtdead": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtdesert": [
                "RDustEffects",
                "RDirtEffectsBig",
                "RStonesEffects"
            ],
            "gdtdesert1": [
                "RDustEffects",
                "RDirtEffectsBig",
                "RStonesEffectsBig"
            ],
            "gdtdesert2": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtdirt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtfield": [
                "RDustEffects"
            ],
            "gdtforest": [
                "RDustEffects"
            ],
            "gdtgrassdry": [
                "RDustEffects",
                "RGrassEffectsDryBig",
                "RDirtEffectsBig"
            ],
            "gdtgrassgreen": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtgrassshort": [
                "RDustEffects",
                "RGrassEffectsBig"
            ],
            "gdtgrasstall": [
                "RDustEffects",
                "RGrassEffectsBig"
            ],
            "gdtgrasswild": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtkldirt": [
                "RDustEffects"
            ],
            "gdtklforestcon": [
                "RDustEffects"
            ],
            "gdtklforestdec": [
                "RDustEffects"
            ],
            "gdtklgrass1": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtklgrass2": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtklmud": [
                "RDustEffects"
            ],
            "gdtklsoil": [
                "RDustEffects"
            ],
            "gdtklstones": [
                "RStonesEffects"
            ],
            "gdtklstubble": [
                "RDustEffects"
            ],
            "gdtkltarmac": [
                "RDustEffects"
            ],
            "gdtreddirt": [
                "RDustEffectsRed"
            ],
            "gdtrock": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtrubble": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtseabed": [
                "RDustEffects"
            ],
            "gdtseabeddeep": [
                "RDustEffects"
            ],
            "gdtsoil": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstony": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstonygreen": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstonythistle": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisbeach": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtstratisconcrete": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstratisdirt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstratisdrygrass": [
                "RDustEffects",
                "RGrassEffectsDryBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisgreengrass": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisrocky": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisseabed": [
                "RDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffects"
            ],
            "gdtstratisthistles": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtthorn": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtvolcano": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtvolcanobeach": [
                "RDustEffects"
            ],
            "gdtweed1": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtweed2": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtwildfield": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "surfintconcrete": [
                "RDustEffects"
            ],
            "surfintmetal": [
                "RDustEffects"
            ],
            "surfinttiles": [
                "RDustEffects"
            ],
            "surfintwood": [
                "RDustEffects"
            ],
            "surfmetal": [
                "RDustEffects"
            ],
            "surfroadconcrete": [
                "RDustEffects"
            ],
            "surfroadconcrete_exp": [
                "RDustEffects"
            ],
            "surfroaddirt": [
                "RDustEffects"
            ],
            "surfroaddirt_enoch": [
                "RDustEffects"
            ],
            "surfroaddirt_exp": [
                "RDustEffectsRed"
            ],
            "surfroadtarmac": [
                "RDustEffects"
            ],
            "surfroadtarmac1_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac2_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac3_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac_exp": [
                "RDustEffects"
            ],
            "surfrooftiles": [
                "RDustEffects"
            ],
            "surfrooftin": [
                "RDustEffects"
            ],
            "surftraildirt_enoch": [
                "RDustEffects"
            ],
            "surfwood": [
                "RDustEffects"
            ]
        }
    },
    "dustfrontleftpos": "wheel_1_4_bound",
    "dustfrontrightpos": "wheel_2_4_bound",
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/RHS_M2A2_wd.paa",
    "editorsubcategory": "rhs_EdSubcat_ifv",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablewatch": 0,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 5,
    "enginepower": 447,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhsusf_eventhandlers": {
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_engineCheckDamage",
            "getin": "_this call rhs_fnc_m2_doors",
            "getout": "_this call rhs_fnc_m2_doors",
            "postinit": "_this call rhs_fnc_reapplyTextures"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectTankSide",
            "position": "vyfuk start"
        }
    },
    "explosioneffect": "FuelExplosionBig",
    "explosionshielding": 15,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        3,
        -10
    ],
    "faction": "rhs_faction_usarmy_wd",
    "features": "Randomization: No\t\t\t\t\t\t<br />Camo selections: 2 - turret, hull\t\t\t\t\t\t<br />Script door sources: None\t\t\t\t\t\t<br />Script animations: HideTurret\t\t\t\t\t\t<br />Executed scripts: None\t\t\t\t\t\t<br />Firing from vehicles: No\t\t\t\t\t\t<br />Slingload: No\t\t\t\t\t\t<br />Cargo proxy indexes: 1 to 7",
    "featuretype": 0,
    "firedusteffect": "FDustEffects",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 24.15,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "gearbox": [
        -7,
        0,
        11,
        8,
        5.7,
        4.2
    ],
    "getinaction": "GetInHigh",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1,
        2,
        3,
        4,
        5,
        6
    ],
    "getinradius": 3.5,
    "getoutaction": "GetOutHigh",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunclouds": {
        "access": 0,
        "cloudletaccy": 0.4,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.3,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletgrowup": 1,
        "cloudletmaxyspeed": 0.8,
        "cloudletminyspeed": 0.2,
        "cloudletshape": "cloudletClouds",
        "cloudletsize": 1,
        "deltat": 0,
        "initt": 0,
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
        "table": {
            "t0": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 0
            }
        },
        "timetolive": 0
    },
    "gunfire": {
        "access": 0,
        "cloudletaccy": 0,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletgrowup": 0.2,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletFire",
        "cloudletsize": 1,
        "deltat": -3000,
        "initt": 4500,
        "interval": 0.01,
        "size": 3,
        "sourcesize": 0.5,
        "table": {
            "t0": {
                "color": [
                    0.82,
                    0.95,
                    0.93,
                    0
                ],
                "maxt": 0
            },
            "t1": {
                "color": [
                    0.75,
                    0.77,
                    0.9,
                    0
                ],
                "maxt": 200
            },
            "t10": {
                "color": [
                    0.62,
                    0.29,
                    0.03,
                    0
                ],
                "maxt": 2600
            },
            "t11": {
                "color": [
                    0.59,
                    0.35,
                    0.05,
                    0
                ],
                "maxt": 2650
            },
            "t12": {
                "color": [
                    0.75,
                    0.37,
                    0.03,
                    0
                ],
                "maxt": 2700
            },
            "t13": {
                "color": [
                    0.88,
                    0.34,
                    0.03,
                    0
                ],
                "maxt": 2750
            },
            "t14": {
                "color": [
                    0.91,
                    0.5,
                    0.17,
                    0
                ],
                "maxt": 2800
            },
            "t15": {
                "color": [
                    1,
                    0.6,
                    0.2,
                    0
                ],
                "maxt": 2850
            },
            "t16": {
                "color": [
                    1,
                    0.71,
                    0.3,
                    0
                ],
                "maxt": 2900
            },
            "t17": {
                "color": [
                    0.98,
                    0.83,
                    0.41,
                    0
                ],
                "maxt": 2950
            },
            "t18": {
                "color": [
                    0.98,
                    0.91,
                    0.54,
                    0
                ],
                "maxt": 3000
            },
            "t19": {
                "color": [
                    0.98,
                    0.99,
                    0.6,
                    0
                ],
                "maxt": 3100
            },
            "t2": {
                "color": [
                    0.56,
                    0.62,
                    0.67,
                    0
                ],
                "maxt": 400
            },
            "t20": {
                "color": [
                    0.96,
                    0.99,
                    0.72,
                    0
                ],
                "maxt": 3300
            },
            "t21": {
                "color": [
                    1,
                    0.98,
                    0.91,
                    0
                ],
                "maxt": 3600
            },
            "t22": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 4200
            },
            "t3": {
                "color": [
                    0.39,
                    0.46,
                    0.47,
                    0
                ],
                "maxt": 600
            },
            "t4": {
                "color": [
                    0.24,
                    0.31,
                    0.31,
                    0
                ],
                "maxt": 800
            },
            "t5": {
                "color": [
                    0.23,
                    0.31,
                    0.29,
                    0
                ],
                "maxt": 1000
            },
            "t6": {
                "color": [
                    0.21,
                    0.29,
                    0.27,
                    0
                ],
                "maxt": 1500
            },
            "t7": {
                "color": [
                    0.19,
                    0.23,
                    0.21,
                    0
                ],
                "maxt": 2000
            },
            "t8": {
                "color": [
                    0.22,
                    0.19,
                    0.1,
                    0
                ],
                "maxt": 2300
            },
            "t9": {
                "color": [
                    0.35,
                    0.2,
                    0.02,
                    0
                ],
                "maxt": 2500
            }
        },
        "timetolive": 0
    },
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "gunnerhasflares": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.015,
        0.011,
        0.015
    ],
    "headlimits": {
        "initanglex": 5,
        "initangley": 0,
        "maxanglex": 40,
        "maxangley": 90,
        "maxanglez": 45,
        "minanglex": -30,
        "minangley": -90,
        "minanglez": -45,
        "rotzradius": 0.2
    },
    "hiddenselections": [
        "camo1",
        "camo2",
        "camo3",
        "selection_stinger",
        "selection_tow"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa",
        "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/a3_co.paa",
        "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/ultralp_co.paa",
        "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa",
        "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hit_lightl": {
            "armor": -10,
            "explosionshielding": 1,
            "minimalhit": -0.1,
            "name": "l svetlo",
            "passthrough": 0,
            "radius": 0,
            "visual": "-"
        },
        "hit_lightr": {
            "armor": -10,
            "explosionshielding": 1,
            "minimalhit": -0.1,
            "name": "p svetlo",
            "passthrough": 0,
            "radius": 0,
            "visual": "-"
        },
        "hit_optics_dvr_peri": {
            "armor": -40,
            "armorcomponent": "Hit_Optics_Dvr_Peri",
            "explosionshielding": 0,
            "name": "",
            "passthrough": 0,
            "visual": "vis_optics_Dvr_Peri"
        },
        "hitengine": {
            "armor": -100,
            "armorcomponent": "Hit_Engine",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_engine_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallFireFPlace"
                },
                "rhs_engine_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_engine_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke3",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_engine_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "RHS_FireSparks"
                }
            },
            "explosionshielding": 0.009,
            "material": -1,
            "minimalhit": 0.14,
            "name": "Hit_Engine",
            "passthrough": 0,
            "radius": 0.17,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 0.5,
            "armorcomponent": "hit_fuel",
            "explosionshielding": 0.6,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_fuel_point",
            "passthrough": 0.3,
            "radius": 0.3,
            "visual": "-"
        },
        "hithull": {
            "armor": -110,
            "armorcomponent": "Hit_Hull",
            "depends": "HitHull_Structural",
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": -0.15,
            "name": "Hit_Hull",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "zbytek"
        },
        "hithull_structural": {
            "armor": -600,
            "explosionshielding": 0,
            "minimalhit": -0.22,
            "name": "Hit_Engine",
            "passthrough": 0,
            "radius": 0,
            "visual": "-"
        },
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "Hit_TrackL",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_L"
        },
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "Hit_TrackR",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_P"
        },
        "hitslat_back": {
            "armor": -200,
            "armorcomponent": "cage_back_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_back_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_front": {
            "armor": -200,
            "armorcomponent": "cage_front_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_front_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_1": {
            "armor": -200,
            "armorcomponent": "cage_left_1_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_1_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_2": {
            "armor": -200,
            "armorcomponent": "cage_left_2_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_2_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_3": {
            "armor": -200,
            "armorcomponent": "cage_left_3_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_3_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_1": {
            "armor": -200,
            "armorcomponent": "cage_right_1_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_1_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_2": {
            "armor": -200,
            "armorcomponent": "cage_right_2_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_2_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_3": {
            "armor": -200,
            "armorcomponent": "cage_right_3_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_3_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_top_back": {
            "armor": -200,
            "armorcomponent": "cage_top_back_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_top_back_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_top_left": {
            "armor": -200,
            "armorcomponent": "cage_top_left_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_top_left_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_top_right": {
            "armor": -200,
            "armorcomponent": "cage_top_right_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_top_right_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsusf/addons/rhsusf_a2port_armor/Data/UI/Icon_m2a2_CA.paa",
    "idlerpm": 800,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.9,
    "irscanground": 0,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "latency": 1,
    "leftdusteffect": "LDustEffects",
    "leftdusteffects": [
        [
            "GdtKLDirt",
            "LDustEffects"
        ],
        [
            "GdtKLGrass1",
            "LDustEffects"
        ],
        [
            "GdtKLGrass1",
            "LGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "LDustEffects"
        ],
        [
            "GdtKLGrass2",
            "LGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "LDustEffects"
        ],
        [
            "GdtKLForestDec",
            "LDustEffects"
        ],
        [
            "GdtKlMud",
            "LDustEffects"
        ],
        [
            "GdtKlSoil",
            "LDustEffects"
        ],
        [
            "GdtKlTarmac",
            "LDustEffects"
        ],
        [
            "GdtKlStubble",
            "LDustEffects"
        ],
        [
            "GdtKlStones",
            "LStonesEffects"
        ],
        [
            "SurfRoadDirt_Enoch",
            "LDustEffects"
        ],
        [
            "SurfTrailDirt_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "LDustEffects"
        ],
        [
            "GdtGrassShort",
            "LDustEffects"
        ],
        [
            "GdtGrassShort",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassTall",
            "LDustEffects"
        ],
        [
            "GdtGrassTall",
            "LGrassEffectsBig"
        ],
        [
            "GdtRedDirt",
            "LDustEffectsRed"
        ],
        [
            "GdtField",
            "LDustEffects"
        ],
        [
            "GdtForest",
            "LDustEffects"
        ],
        [
            "GdtVolcano",
            "LDustEffects"
        ],
        [
            "GdtVolcano",
            "LStonesEffectsBig"
        ],
        [
            "GdtCliff",
            "LDustEffects"
        ],
        [
            "GdtVolcanoBeach",
            "LDustEffects"
        ],
        [
            "SurfRoadDirt_exp",
            "LDustEffectsRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac_exp",
            "LDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "LDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisBeach",
            "LDustEffects"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffectsBig"
        ],
        [
            "GdtStratisDirt",
            "LDustEffects"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisSeabedCluttered",
            "LDustEffects"
        ],
        [
            "GdtStratisSeabed",
            "LDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LGrassEffectsDryBig"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "LDustEffects"
        ],
        [
            "GdtStratisRocky",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "LDustEffects"
        ],
        [
            "GdtStratisThistles",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "LDirtEffectsBig"
        ],
        [
            "GdtConcrete",
            "LDustEffects"
        ],
        [
            "GdtConcrete",
            "LDirtEffectsBig"
        ],
        [
            "GdtAsphalt",
            "LDustEffects"
        ],
        [
            "GdtAsphalt",
            "LDirtEffectsBig"
        ],
        [
            "GdtRubble",
            "LDustEffects"
        ],
        [
            "GdtRubble",
            "LDirtEffectsBig"
        ],
        [
            "GdtSoil",
            "LDustEffects"
        ],
        [
            "GdtSoil",
            "LDirtEffectsBig"
        ],
        [
            "GdtBeach",
            "LDustEffects"
        ],
        [
            "GdtBeach",
            "LStonesEffectsBig"
        ],
        [
            "GdtRock",
            "LDustEffects"
        ],
        [
            "GdtRock",
            "LDirtEffectsBig"
        ],
        [
            "GdtDead",
            "LDustEffects"
        ],
        [
            "GdtDead",
            "LDirtEffectsBig"
        ],
        [
            "Default",
            "LDustEffects"
        ],
        [
            "GdtDesert",
            "LDustEffects"
        ],
        [
            "GdtDesert",
            "LDirtEffectsBig"
        ],
        [
            "GdtDesert",
            "LStonesEffects"
        ],
        [
            "GdtDesert1",
            "LDustEffects"
        ],
        [
            "GdtDesert1",
            "LDirtEffectsBig"
        ],
        [
            "GdtDesert1",
            "LStonesEffectsBig"
        ],
        [
            "GdtDesert2",
            "LDustEffects"
        ],
        [
            "GdtDesert2",
            "LGrassEffectsBig"
        ],
        [
            "GdtDesert2",
            "LDirtEffectsBig"
        ],
        [
            "GdtDirt",
            "LDustEffects"
        ],
        [
            "GdtDirt",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "LDustEffects"
        ],
        [
            "GdtGrassGreen",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassDry",
            "LDustEffects"
        ],
        [
            "GdtGrassDry",
            "LGrassEffectsDryBig"
        ],
        [
            "GdtGrassDry",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassWild",
            "LDustEffects"
        ],
        [
            "GdtGrassWild",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassWild",
            "LDirtEffectsBig"
        ],
        [
            "GdtWildField",
            "LDustEffects"
        ],
        [
            "GdtWildField",
            "LGrassEffectsBig"
        ],
        [
            "GdtWildField",
            "LDirtEffectsBig"
        ],
        [
            "GdtWeed1",
            "LDustEffects"
        ],
        [
            "GdtWeed1",
            "LGrassEffectsBig"
        ],
        [
            "GdtWeed1",
            "LDirtEffectsBig"
        ],
        [
            "GdtWeed2",
            "LDustEffects"
        ],
        [
            "GdtWeed2",
            "LGrassEffectsBig"
        ],
        [
            "GdtWeed2",
            "LDirtEffectsBig"
        ],
        [
            "GdtThorn",
            "LDustEffects"
        ],
        [
            "GdtThorn",
            "LGrassEffectsBig"
        ],
        [
            "GdtThorn",
            "LDirtEffectsBig"
        ],
        [
            "GdtStony",
            "LDustEffects"
        ],
        [
            "GdtStony",
            "LGrassEffectsBig"
        ],
        [
            "GdtStony",
            "LDirtEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "LDustEffects"
        ],
        [
            "GdtStonyGreen",
            "LGrassEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "LDirtEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "LDustEffects"
        ],
        [
            "GdtStonyThistle",
            "LGrassEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "LDirtEffectsBig"
        ],
        [
            "GdtSeabedDeep",
            "LDustEffects"
        ],
        [
            "GdtSeabed",
            "LDustEffects"
        ],
        [
            "SurfRoadDirt",
            "LDustEffects"
        ],
        [
            "SurfRoadConcrete",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac",
            "LDustEffects"
        ],
        [
            "SurfWood",
            "LDustEffects"
        ],
        [
            "SurfMetal",
            "LDustEffects"
        ],
        [
            "SurfRoofTin",
            "LDustEffects"
        ],
        [
            "SurfRoofTiles",
            "LDustEffects"
        ],
        [
            "SurfIntWood",
            "LDustEffects"
        ],
        [
            "SurfIntConcrete",
            "LDustEffects"
        ],
        [
            "SurfIntTiles",
            "LDustEffects"
        ],
        [
            "SurfIntMetal",
            "LDustEffects"
        ],
        [
            "dirtrunway",
            "RDustEffects"
        ]
    ],
    "leftfastwatereffect": "LWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "library": {
        "libtextdesc": "The M2 Bradley IFV (Infantry Fighting Vehicle) is an US infantry fighting vehicle. It is designed to transport infantry with armor protection while providing covering fire to suppressing enemy troops and armored vehicles.<br/>The A2 variant features improvements based on lessons learned during Gulf War in 1991."
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "loddriveropticsin": 0,
    "loddriverturnedin": 1100,
    "loddriverturnedout": 0,
    "magazines": [
        "rhs_mag_smokegen"
    ],
    "mapsize": 7,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0,
    "maxgforce": 2,
    "maximumload": 6000,
    "maxomega": 272.27,
    "maxspeed": 66,
    "memorypointcargolight": "cargo light",
    "memorypointdriveroptics": "driverview",
    "memorypointmissile": [
        "spice rakety",
        "usti hlavne"
    ],
    "memorypointmissiledir": [
        "konec rakety",
        "konec hlavne"
    ],
    "memorypointsgetincargo": [
        "pos cargo",
        "pos cargo 1",
        "pos cargo 2",
        "pos cargo 3"
    ],
    "memorypointsgetincargodir": [
        "pos cargo dir",
        "pos cargo 1 dir",
        "pos cargo dir",
        "pos cargo 2 dir",
        "pos cargo 3 dir"
    ],
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
    "mfact": 1,
    "mfd": {
        "mfd_commander_display": {
            "alpha": 0.5,
            "bones": {
                "fuelscale": {
                    "max": 1,
                    "maxpos": [
                        -0.09,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        0
                    ],
                    "source": "fuel",
                    "sourceindex": 1,
                    "sourcescale": 1,
                    "type": "linear"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "azimuth": {
                    "align": "center",
                    "down": [
                        [
                            0.605,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.605,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.63,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "GUN AZIM",
                    "type": "text"
                },
                "azimuth_number": {
                    "align": "center",
                    "down": [
                        [
                            0.61,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.61,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.635,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "coax": {
                    "align": "center",
                    "down": [
                        [
                            0.498,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.498,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.523,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "COAX",
                    "type": "text"
                },
                "coax_ammo_count": {
                    "align": "center",
                    "down": [
                        [
                            0.493,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.493,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.518,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "fuel": {
                    "align": "center",
                    "down": [
                        [
                            0.83,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.83,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.855,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "FUEL",
                    "type": "text"
                },
                "fuel_background_green": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.787,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.9
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.787,
                                        0.9
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0,
                        0.7,
                        0
                    ],
                    "condition": "fuel>=0.5"
                },
                "fuel_background_red": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.787,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.9
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.787,
                                        0.9
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0.7,
                        0,
                        0
                    ],
                    "condition": "fuel<0.3"
                },
                "fuel_background_white": {
                    "alpha": 0.1,
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.787,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.877,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.877,
                                        0.9
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.787,
                                        0.9
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0.2,
                        0.2,
                        0.2
                    ],
                    "condition": "1"
                },
                "fuel_background_yellow": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.787,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.7
                                    ],
                                    1
                                ],
                                [
                                    "FuelScale",
                                    [
                                        0.877,
                                        0.9
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.787,
                                        0.9
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0.9,
                        0.7,
                        0
                    ],
                    "condition": "fuel<0.5"
                },
                "fuel_number": {
                    "align": "left",
                    "down": [
                        [
                            0.835,
                            0.66
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.835,
                            0.4
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.86,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "fuel",
                    "sourcelength": 1,
                    "sourcescale": 100,
                    "type": "text"
                },
                "fuel_percent_sign": {
                    "align": "right",
                    "down": [
                        [
                            0.845,
                            0.66
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.845,
                            0.4
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.87,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "%",
                    "type": "text"
                },
                "main_gun": {
                    "align": "center",
                    "down": [
                        [
                            0.273,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.273,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.298,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "MAIN GUN",
                    "type": "text"
                },
                "main_gun_ammo_count": {
                    "align": "center",
                    "down": [
                        [
                            0.273,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.273,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.298,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_gun_ammo_type": {
                    "align": "center",
                    "down": [
                        [
                            0.385,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.385,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.41,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_gun_ammo_type_text": {
                    "align": "center",
                    "down": [
                        [
                            0.385,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.385,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.41,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "TYPE",
                    "type": "text"
                },
                "smoke": {
                    "align": "center",
                    "down": [
                        [
                            0.717,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.717,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.742,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "SMOKE",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_display_damage": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "damage_engine": {
                    "align": "center",
                    "down": [
                        [
                            0.11,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.11,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.135,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "ENG",
                    "type": "text"
                },
                "damage_fuel": {
                    "align": "center",
                    "down": [
                        [
                            0.178,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.178,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.203,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "FUEL",
                    "type": "text"
                },
                "damage_gun": {
                    "align": "center",
                    "down": [
                        [
                            0.11,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.11,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.135,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "GUN",
                    "type": "text"
                },
                "damage_hull": {
                    "align": "center",
                    "down": [
                        [
                            0.04,
                            0.44
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.04,
                            0.18
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.065,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "HULL",
                    "type": "text"
                },
                "damage_turret": {
                    "align": "center",
                    "down": [
                        [
                            0.178,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.178,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.203,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "TRT",
                    "type": "text"
                },
                "damage_wheels": {
                    "align": "center",
                    "down": [
                        [
                            0.04,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.04,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.065,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "TRK",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_display_mainturret": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "smoke_ammo": {
                    "align": "center",
                    "down": [
                        [
                            0.72,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.72,
                            0.55
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.745,
                            0.55
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_heading": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_dir_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.61,
                    0.62,
                    0
                ],
                "condition": "on",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_dir_TL",
            "topright": "mfd_com_dir_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_onscreen": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "PIP_COM_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "azimuth_number": {
                    "align": "center",
                    "down": [
                        [
                            0.22,
                            0.472
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.22,
                            0.435
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.245,
                            0.435
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "elevation_number": {
                    "align": "center",
                    "down": [
                        [
                            0.23,
                            0.317
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.23,
                            0.28
                        ],
                        1
                    ],
                    "refreshrate": 0,
                    "right": [
                        [
                            0.255,
                            0.28
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "[y]turretworld",
                    "sourcelength": 4,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "type": "text"
                },
                "elevation_text": {
                    "align": "center",
                    "down": [
                        [
                            0.2,
                            0.317
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.2,
                            0.28
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.225,
                            0.28
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "E: ",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.75,
                            0.317
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.75,
                            0.28
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.775,
                            0.28
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "visionmode_string": {
                    "align": "center",
                    "down": [
                        [
                            0.825,
                            0.687
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.825,
                            0.65
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.85,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "visionMode",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "visionmode_text": {
                    "align": "center",
                    "down": [
                        [
                            0.75,
                            0.687
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.75,
                            0.65
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.775,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "WFOV",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "PIP_COM_TL",
            "topright": "PIP_COM_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_driver_heading": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_1_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.61,
                    0.62,
                    0
                ],
                "condition": "on",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR"
        },
        "mfd_driver_heading_second": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_Driver_2_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.95,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_Driver_2_TL",
            "topright": "MFD_Driver_2_TR"
        },
        "mfd_driver_heading_text": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_Driver_1_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.87
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0.02
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.7,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "AZIMUTH",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_Driver_1_TL",
            "topright": "MFD_Driver_1_TR"
        },
        "mfd_gunner_ammoindicator_main_armament": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            0.375,
                            0.143
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.375,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.435,
                            0.065
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_2": {
                    "align": "left",
                    "down": [
                        [
                            0.375,
                            0.203
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.375,
                            0.125
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.435,
                            0.125
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_armament_ammo_type_1": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.143
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.065
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "MP-T",
                    "type": "text"
                },
                "main_armament_ammo_type_2": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.203
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.125
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.06,
                            0.125
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "APFSDS-T",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospacePro",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_ammotype": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_4_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.455,
                            0.7
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.455,
                            0.2
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.655,
                            0.2
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "topleft": "MFD_4_TL",
            "topright": "MFD_4_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_coax_ammo": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            0.36,
                            0.388
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.36,
                            0.31
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.42,
                            0.31
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_display": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "azimut": {
                    "align": "right",
                    "down": [
                        [
                            0.025,
                            0.993
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.025,
                            0.915
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.085,
                            0.915
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "AZIMUTH",
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "damage": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.468
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.39
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.39
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "DAMAGE",
                    "type": "text"
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.34,
                            0.993
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.34,
                            0.915
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.4,
                            0.915
                        ],
                        1
                    ],
                    "scale": 0.2,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_distance_elevation": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.918
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.84
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.84
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "LASED DST",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.335,
                            0.918
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.335,
                            0.84
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.395,
                            0.84
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "machinegun": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.388
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.31
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.31
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "COAX",
                    "type": "text"
                },
                "main_armament": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.075
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            -0.003
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            -0.003
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "MAIN ARMAMENT",
                    "type": "text"
                },
                "main_armament_ammo_type": {
                    "align": "center",
                    "down": [
                        [
                            0.545,
                            0.075
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.545,
                            -0.003
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.605,
                            -0.003
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "AMMO TYPE",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_heading": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_Gunner_heading_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.7,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "topleft": "MFD_Gunner_heading_TL",
            "topright": "MFD_Gunner_heading_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_main_armament_ammo_type": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.56,
                            0.168
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.56,
                            0.09
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.62,
                            0.09
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_range": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_5_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_range": {
                    "align": "center",
                    "down": [
                        [
                            0.48,
                            1
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.48,
                            -0.1
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.88,
                            -0.1
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_ready_to_fire": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_cli_BL",
            "color": [
                0,
                0,
                0
            ],
            "draw": {
                "alpha": 1,
                "bottom_text": {
                    "align": "center",
                    "down": [
                        [
                            0.465,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.465,
                            0.45
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.685,
                            0.45
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "FIRE",
                    "type": "text"
                },
                "color": [
                    0,
                    0,
                    0
                ],
                "condition": "1",
                "top_text": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.55
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0.05
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.67,
                            0.05
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "READY TO",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_cli_TL",
            "topright": "mfd_gun_cli_TR"
        }
    },
    "mfmax": 80,
    "mgunclouds": {
        "access": 0,
        "cloudletaccy": 0,
        "cloudletalpha": 0.3,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletgrowup": 0.05,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletClouds",
        "cloudletsize": 1,
        "deltat": 0,
        "initt": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "table": {
            "t0": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 0
            }
        },
        "timetolive": 0
    },
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minomega": 84,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/M2A2",
    "namesound": "veh_vehicle_APC_s",
    "newturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "mainTurret",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "mainTurret",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 1,
        "disablesoundattenuation": 0,
        "dontcreateai": 0,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "mainGun",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "gunend": "konec hlavne",
        "gunfire": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletgrowup": 0.2,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletFire",
            "cloudletsize": 1,
            "deltat": -3000,
            "initt": 4500,
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        0.82,
                        0.95,
                        0.93,
                        0
                    ],
                    "maxt": 0
                },
                "t1": {
                    "color": [
                        0.75,
                        0.77,
                        0.9,
                        0
                    ],
                    "maxt": 200
                },
                "t10": {
                    "color": [
                        0.62,
                        0.29,
                        0.03,
                        0
                    ],
                    "maxt": 2600
                },
                "t11": {
                    "color": [
                        0.59,
                        0.35,
                        0.05,
                        0
                    ],
                    "maxt": 2650
                },
                "t12": {
                    "color": [
                        0.75,
                        0.37,
                        0.03,
                        0
                    ],
                    "maxt": 2700
                },
                "t13": {
                    "color": [
                        0.88,
                        0.34,
                        0.03,
                        0
                    ],
                    "maxt": 2750
                },
                "t14": {
                    "color": [
                        0.91,
                        0.5,
                        0.17,
                        0
                    ],
                    "maxt": 2800
                },
                "t15": {
                    "color": [
                        1,
                        0.6,
                        0.2,
                        0
                    ],
                    "maxt": 2850
                },
                "t16": {
                    "color": [
                        1,
                        0.71,
                        0.3,
                        0
                    ],
                    "maxt": 2900
                },
                "t17": {
                    "color": [
                        0.98,
                        0.83,
                        0.41,
                        0
                    ],
                    "maxt": 2950
                },
                "t18": {
                    "color": [
                        0.98,
                        0.91,
                        0.54,
                        0
                    ],
                    "maxt": 3000
                },
                "t19": {
                    "color": [
                        0.98,
                        0.99,
                        0.6,
                        0
                    ],
                    "maxt": 3100
                },
                "t2": {
                    "color": [
                        0.56,
                        0.62,
                        0.67,
                        0
                    ],
                    "maxt": 400
                },
                "t20": {
                    "color": [
                        0.96,
                        0.99,
                        0.72,
                        0
                    ],
                    "maxt": 3300
                },
                "t21": {
                    "color": [
                        1,
                        0.98,
                        0.91,
                        0
                    ],
                    "maxt": 3600
                },
                "t22": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 4200
                },
                "t3": {
                    "color": [
                        0.39,
                        0.46,
                        0.47,
                        0
                    ],
                    "maxt": 600
                },
                "t4": {
                    "color": [
                        0.24,
                        0.31,
                        0.31,
                        0
                    ],
                    "maxt": 800
                },
                "t5": {
                    "color": [
                        0.23,
                        0.31,
                        0.29,
                        0
                    ],
                    "maxt": 1000
                },
                "t6": {
                    "color": [
                        0.21,
                        0.29,
                        0.27,
                        0
                    ],
                    "maxt": 1500
                },
                "t7": {
                    "color": [
                        0.19,
                        0.23,
                        0.21,
                        0
                    ],
                    "maxt": 2000
                },
                "t8": {
                    "color": [
                        0.22,
                        0.19,
                        0.1,
                        0
                    ],
                    "maxt": 2300
                },
                "t9": {
                    "color": [
                        0.35,
                        0.2,
                        0.02,
                        0
                    ],
                    "maxt": 2500
                }
            },
            "timetolive": 0
        },
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "Gunner",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 1,
        "hitpoints": {
            "hitgun": {
                "armor": 0.6,
                "explosionshielding": 1,
                "material": 52,
                "name": "gun",
                "passthrough": 1,
                "visual": "gun"
            },
            "hitturret": {
                "armor": 0.8,
                "explosionshielding": 1,
                "material": 51,
                "name": "turret",
                "passthrough": 1,
                "visual": "turret"
            }
        },
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 20,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 360,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 0.3,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletgrowup": 0.05,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "mincamelev": -90,
        "minelev": -4,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -360,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 0,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 1,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPGunner",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 1,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "continuous": 0,
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "nightvision": 0,
    "normalspeedforwardcoef": 0.6,
    "numberphysicalwheels": 16,
    "nvgmarker": {
        "ambient": [
            1,
            1,
            1,
            1
        ],
        "blinking": 0,
        "brightness": 1,
        "diffuse": [
            1,
            1,
            1,
            1
        ],
        "onlyinnvg": 0
    },
    "nvgmarkers": {
        "nvgmarker01": {
            "ambient": [
                0.003,
                0.0003,
                0.0003,
                1
            ],
            "blinking": 1,
            "brightness": 0.001,
            "color": [
                0.03,
                0.003,
                0.003,
                1
            ],
            "name": "nvg_marker"
        }
    },
    "nvscanner": 0,
    "nvtarget": 0,
    "obstructsoundlfratio": 0,
    "obstructsoundswhenin": 0,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0,
    "outsidesoundfilter": 1,
    "peaktorque": 1660,
    "picture": "rhsusf/addons/rhsusf_a2port_armor/pictures/rhs_m2a2_pic_ca.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 10,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.2,
    "radartype": 1,
    "redrpm": 2600,
    "reflectors": {
        "left": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 60,
                "hardlimitstart": 30,
                "linear": 0,
                "quadratic": 0.25,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec l svetla",
            "flaresize": 1,
            "hitpointclass": "Hit_LightL",
            "innerangle": 30,
            "intensity": 1,
            "outerangle": 100,
            "position": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 60,
                "hardlimitstart": 30,
                "linear": 0,
                "quadratic": 0.25,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec p svetla",
            "flaresize": 1,
            "hitpointclass": "Hit_LightR",
            "innerangle": 30,
            "intensity": 1,
            "outerangle": 100,
            "position": "p svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reportownposition": 1,
    "reversed": 1,
    "rhs_fuelcapacity": 462,
    "rhs_hassmokecap": 1,
    "rightdusteffect": "RDustEffects",
    "rightdusteffects": [
        [
            "GdtKLDirt",
            "RDustEffects"
        ],
        [
            "GdtKLGrass1",
            "RDustEffects"
        ],
        [
            "GdtKLGrass1",
            "RGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "RDustEffects"
        ],
        [
            "GdtKLGrass2",
            "RGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "RDustEffects"
        ],
        [
            "GdtKLForestDec",
            "RDustEffects"
        ],
        [
            "GdtKlMud",
            "RDustEffects"
        ],
        [
            "GdtKlSoil",
            "RDustEffects"
        ],
        [
            "GdtKlTarmac",
            "RDustEffects"
        ],
        [
            "GdtKlStubble",
            "RDustEffects"
        ],
        [
            "GdtKlStones",
            "RStonesEffects"
        ],
        [
            "SurfRoadDirt_Enoch",
            "RDustEffects"
        ],
        [
            "SurfTrailDirt_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "RDustEffects"
        ],
        [
            "GdtGrassShort",
            "RDustEffects"
        ],
        [
            "GdtGrassShort",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassTall",
            "RDustEffects"
        ],
        [
            "GdtGrassTall",
            "RGrassEffectsBig"
        ],
        [
            "GdtRedDirt",
            "RDustEffectsRed"
        ],
        [
            "GdtField",
            "RDustEffects"
        ],
        [
            "GdtForest",
            "RDustEffects"
        ],
        [
            "GdtVolcano",
            "RDustEffects"
        ],
        [
            "GdtVolcano",
            "RStonesEffectsBig"
        ],
        [
            "GdtCliff",
            "RDustEffects"
        ],
        [
            "GdtVolcanoBeach",
            "RDustEffects"
        ],
        [
            "SurfRoadDirt_exp",
            "RDustEffectsRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac_exp",
            "RDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "RDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisBeach",
            "RDustEffects"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffectsBig"
        ],
        [
            "GdtStratisDirt",
            "RDustEffects"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisSeabedCluttered",
            "RDustEffects"
        ],
        [
            "GdtStratisSeabed",
            "RDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RGrassEffectsDryBig"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "RDustEffects"
        ],
        [
            "GdtStratisRocky",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "RDustEffects"
        ],
        [
            "GdtStratisThistles",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "RDirtEffectsBig"
        ],
        [
            "GdtConcrete",
            "RDustEffects"
        ],
        [
            "GdtConcrete",
            "RDirtEffectsBig"
        ],
        [
            "GdtAsphalt",
            "RDustEffects"
        ],
        [
            "GdtAsphalt",
            "RDirtEffectsBig"
        ],
        [
            "GdtRubble",
            "RDustEffects"
        ],
        [
            "GdtRubble",
            "RDirtEffectsBig"
        ],
        [
            "GdtSoil",
            "RDustEffects"
        ],
        [
            "GdtSoil",
            "RDirtEffectsBig"
        ],
        [
            "GdtBeach",
            "RDustEffects"
        ],
        [
            "GdtBeach",
            "RStonesEffectsBig"
        ],
        [
            "GdtRock",
            "RDustEffects"
        ],
        [
            "GdtRock",
            "RDirtEffectsBig"
        ],
        [
            "GdtDead",
            "RDustEffects"
        ],
        [
            "GdtDead",
            "RDirtEffectsBig"
        ],
        [
            "Default",
            "RDustEffects"
        ],
        [
            "GdtDesert",
            "RDustEffects"
        ],
        [
            "GdtDesert",
            "RDirtEffectsBig"
        ],
        [
            "GdtDesert",
            "RStonesEffects"
        ],
        [
            "GdtDesert1",
            "RDustEffects"
        ],
        [
            "GdtDesert1",
            "RDirtEffectsBig"
        ],
        [
            "GdtDesert1",
            "RStonesEffectsBig"
        ],
        [
            "GdtDesert2",
            "RDustEffects"
        ],
        [
            "GdtDesert2",
            "RGrassEffectsBig"
        ],
        [
            "GdtDesert2",
            "RDirtEffectsBig"
        ],
        [
            "GdtDirt",
            "RDustEffects"
        ],
        [
            "GdtDirt",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "RDustEffects"
        ],
        [
            "GdtGrassGreen",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassDry",
            "RDustEffects"
        ],
        [
            "GdtGrassDry",
            "RGrassEffectsDryBig"
        ],
        [
            "GdtGrassDry",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassWild",
            "RDustEffects"
        ],
        [
            "GdtGrassWild",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassWild",
            "RDirtEffectsBig"
        ],
        [
            "GdtWildField",
            "RDustEffects"
        ],
        [
            "GdtWildField",
            "RGrassEffectsBig"
        ],
        [
            "GdtWildField",
            "RDirtEffectsBig"
        ],
        [
            "GdtWeed1",
            "RDustEffects"
        ],
        [
            "GdtWeed1",
            "RGrassEffectsBig"
        ],
        [
            "GdtWeed1",
            "RDirtEffectsBig"
        ],
        [
            "GdtWeed2",
            "RDustEffects"
        ],
        [
            "GdtWeed2",
            "RGrassEffectsBig"
        ],
        [
            "GdtWeed2",
            "RDirtEffectsBig"
        ],
        [
            "GdtThorn",
            "RDustEffects"
        ],
        [
            "GdtThorn",
            "RGrassEffectsBig"
        ],
        [
            "GdtThorn",
            "RDirtEffectsBig"
        ],
        [
            "GdtStony",
            "RDustEffects"
        ],
        [
            "GdtStony",
            "RGrassEffectsBig"
        ],
        [
            "GdtStony",
            "RDirtEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "RDustEffects"
        ],
        [
            "GdtStonyGreen",
            "RGrassEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "RDirtEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "RDustEffects"
        ],
        [
            "GdtStonyThistle",
            "RGrassEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "RDirtEffectsBig"
        ],
        [
            "GdtSeabedDeep",
            "RDustEffects"
        ],
        [
            "GdtSeabed",
            "RDustEffects"
        ],
        [
            "SurfRoadDirt",
            "RDustEffects"
        ],
        [
            "SurfRoadConcrete",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac",
            "RDustEffects"
        ],
        [
            "SurfWood",
            "RDustEffects"
        ],
        [
            "SurfMetal",
            "RDustEffects"
        ],
        [
            "SurfRoofTin",
            "RDustEffects"
        ],
        [
            "SurfRoofTiles",
            "RDustEffects"
        ],
        [
            "SurfIntWood",
            "RDustEffects"
        ],
        [
            "SurfIntConcrete",
            "RDustEffects"
        ],
        [
            "SurfIntTiles",
            "RDustEffects"
        ],
        [
            "SurfIntMetal",
            "RDustEffects"
        ],
        [
            "dirtrunway",
            "RDustEffects"
        ]
    ],
    "rightfastwatereffect": "RWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionbrakelights": "brzdove svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 2.5,
    "sensitivityear": "0.0075 /3",
    "sensorposition": "gunnerView",
    "shadow": 1,
    "showalltargets": 0,
    "showcrewaim": 0,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        0
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 1,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.45,
    "smokelauncherangle": 120,
    "smokelaunchergrenadecount": 10,
    "smokelauncheronturret": 1,
    "smokelaunchervelocity": 14,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.25,
        "ArmorCrash1",
        0.25,
        "ArmorCrash2",
        0.25,
        "ArmorCrash3",
        0.25
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "buildCrash0",
        0.25,
        "buildCrash1",
        0.25,
        "buildCrash2",
        0.25,
        "buildCrash3",
        0.25
    ],
    "soundburning": {},
    "soundbushcrash": [
        "BushCrash1",
        0.33,
        "BushCrash2",
        0.33,
        "BushCrash3",
        0.33
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "soundCrash",
        1
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "",
        0.562341,
        1
    ],
    "sounddrown": {},
    "sounddrowning": {},
    "soundelevation": [
        "",
        0.00316228,
        0.5
    ],
    "soundengine": [
        "",
        1,
        1
    ],
    "soundengineoffext": [
        "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_stop",
        1,
        1,
        200
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_stop",
        0.630957,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_start",
        1,
        1,
        200
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_start",
        0.630957,
        1
    ],
    "soundenviron": [
        "",
        1,
        1
    ],
    "soundenvironext": {},
    "soundequipment": {},
    "soundevents": {},
    "soundflapsdown": [
        "",
        1,
        1
    ],
    "soundflapsup": [
        "",
        1,
        1
    ],
    "soundgear": [
        "",
        0.000316228,
        1
    ],
    "soundgeardown": [
        "",
        1,
        1
    ],
    "soundgearup": [
        "",
        1,
        1
    ],
    "soundgetin": [
        "A3/sounds_f/vehicles/armor/noises/get_in_out",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/sounds_f/vehicles/armor/noises/get_in_out",
        0.562341,
        1,
        20
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_2",
        0.316228,
        1
    ],
    "soundinjured": {},
    "soundlandcrash": [
        "",
        1,
        1
    ],
    "soundlandcrashes": [
        "soundLandCrash",
        1
    ],
    "soundlocked": [
        "/A3/Sounds_F/weapons/Rockets/locked_1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "engine": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(600/\t2600),(1100/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_2",
                0.794328,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t2600) factor[(550/\t2600),(700/\t2600)])\t*\t((rpm/\t2600) factor[(1100/\t2600),(760/\t2600)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(770/\t2600),(1400/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_3",
                0.891251,
                1,
                260
            ],
            "volume": "engineOn*camPos*(((rpm/\t2600) factor[(720/\t2600),(1060/\t2600)])\t*\t((rpm/\t2600) factor[(1400/\t2600),(1180/\t2600)]))"
        },
        "engine1_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(770/\t2600),(1400/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_3",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2600) factor[(720/\t2600),(1060/\t2600)])\t*\t((rpm/\t2600) factor[(1400/\t2600),(1180/\t2600)]))"
        },
        "engine1_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(770/\t2600),(1400/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_3",
                1.25893,
                1,
                300
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(720/\t2600),(1060/\t2600)])\t*\t((rpm/\t2600) factor[(1400/\t2600),(1180/\t2600)]))"
        },
        "engine1_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(770/\t2600),(1400/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_3",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(720/\t2600),(1060/\t2600)])\t*\t((rpm/\t2600) factor[(1400/\t2600),(1180/\t2600)]))"
        },
        "engine2_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1150/\t2600),(1700/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_4",
                1,
                1,
                280
            ],
            "volume": "engineOn*camPos*(((rpm/\t2600) factor[(1130/\t2600),(1370/\t2600)])\t*\t((rpm/\t2600) factor[(1700/\t2600),(1500/\t2600)]))"
        },
        "engine2_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1150/\t2600),(1700/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_4",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2600) factor[(1130/\t2600),(1370/\t2600)])\t*\t((rpm/\t2600) factor[(1700/\t2600),(1500/\t2600)]))"
        },
        "engine2_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1150/\t2600),(1700/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_4",
                1.41254,
                1,
                340
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(1130/\t2600),(1370/\t2600)])\t*\t((rpm/\t2600) factor[(1700/\t2600),(1500/\t2600)]))"
        },
        "engine2_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1150/\t2600),(1700/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_4",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(1130/\t2600),(1370/\t2600)])\t*\t((rpm/\t2600) factor[(1700/\t2600),(1500/\t2600)]))"
        },
        "engine3_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1500/\t2600),(2100/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_5",
                1.12202,
                1,
                300
            ],
            "volume": "engineOn*camPos*(((rpm/\t2600) factor[(1460/\t2600),(1670/\t2600)])\t*\t((rpm/\t2600) factor[(2100/\t2600),(1800/\t2600)]))"
        },
        "engine3_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1500/\t2600),(2100/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_5",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2600) factor[(1460/\t2600),(1670/\t2600)])\t*\t((rpm/\t2600) factor[(2100/\t2600),(1800/\t2600)]))"
        },
        "engine3_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1500/\t2600),(2100/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_5",
                1.77828,
                1,
                360
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(1460/\t2600),(1670/\t2600)])\t*\t((rpm/\t2600) factor[(2100/\t2600),(1800/\t2600)]))"
        },
        "engine3_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1500/\t2600),(2100/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_5",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(1460/\t2600),(1670/\t2600)])\t*\t((rpm/\t2600) factor[(2100/\t2600),(1800/\t2600)]))"
        },
        "engine4_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1800/\t2600),(2600/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_6",
                1.25893,
                1,
                320
            ],
            "volume": "engineOn*camPos*((rpm/\t2600) factor[(1750/\t2600),(2050/\t2600)])"
        },
        "engine4_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1800/\t2600),(2600/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_6",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*((rpm/\t2600) factor[(1750/\t2600),(2050/\t2600)])"
        },
        "engine4_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1800/\t2600),(2600/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_6",
                1.99526,
                1,
                380
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t2600) factor[(1750/\t2600),(2050/\t2600)])"
        },
        "engine4_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(1800/\t2600),(2600/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_6",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t2600) factor[(1750/\t2600),(2050/\t2600)])"
        },
        "engine_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(600/\t2600),(1100/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_2",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2600) factor[(550/\t2600),(700/\t2600)])\t*\t((rpm/\t2600) factor[(1100/\t2600),(760/\t2600)]))"
        },
        "enginethrust": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(600/\t2600),(1100/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_2",
                1.12202,
                1,
                280
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(550/\t2600),(700/\t2600)])\t*\t((rpm/\t2600) factor[(1100/\t2600),(760/\t2600)]))"
        },
        "enginethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(600/\t2600),(1100/\t2600)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_2",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(550/\t2600),(700/\t2600)])\t*\t((rpm/\t2600) factor[(1100/\t2600),(760/\t2600)]))"
        },
        "idle_ext": {
            "frequency": "0.3\t+\t((rpm/\t2600) factor[(100/\t2600),(250/\t2600)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_engine_1",
                0.562341,
                1,
                160
            ],
            "volume": "engineOn*camPos*(((rpm/\t2600) factor[(100/\t2600),(400/\t2600)])\t*\t((rpm/\t2600) factor[(730/\t2600),(610/\t2600)]))"
        },
        "idle_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(500/\t2600),(650/\t2600)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_engine_1",
                0.316228,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2600) factor[(100/\t2600),(400/\t2600)])\t*\t((rpm/\t2600) factor[(730/\t2600),(610/\t2600)]))"
        },
        "idlethrust": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(500/\t2600),(650/\t2600)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/ext_exhaust_1",
                1,
                1,
                250
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(100/\t2600),(400/\t2600)])\t*\t((rpm/\t2600) factor[(730/\t2600),(610/\t2600)]))"
        },
        "idlethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2600) factor[(500/\t2600),(650/\t2600)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/APC/APC3/int_exhaust_1",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2600) factor[(100/\t2600),(400/\t2600)])\t*\t((rpm/\t2600) factor[(730/\t2600),(610/\t2600)]))"
        },
        "noiseext": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/noises/noise_tank_ext_1",
                3.16228,
                1,
                250
            ],
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        "noiseint": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/noises/noise_tank_int_1",
                3.16228,
                1
            ],
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        "threadsinh0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_01",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-0) max 0)/\t95),(((-10) max 10)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-25) max 25)/\t95),(((-15) max 15)/\t95)]))"
        },
        "threadsinh1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_02",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-20) max 20)/\t95),(((-35) max 35)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-55) max 55)/\t95),(((-40) max 40)/\t95)]))"
        },
        "threadsinh2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_03",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-45) max 45)/\t95),(((-55) max 55)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-70) max 70)/\t95),(((-60) max 60)/\t95)]))"
        },
        "threadsinh3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_04",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-65) max 65)/\t95),(((-70) max 70)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-85) max 85)/\t95),(((-80) max 80)/\t95)]))"
        },
        "threadsinh4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_05",
                0.707946,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/\t95) factor[(((-80) max 80)/\t95),(((-90) max 90)/\t95)])"
        },
        "threadsins0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_01",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-0) max 0)/\t95),(((-10) max 10)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-25) max 25)/\t95),(((-15) max 15)/\t95)]))"
        },
        "threadsins1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_02",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-20) max 20)/\t95),(((-35) max 35)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-55) max 55)/\t95),(((-40) max 40)/\t95)]))"
        },
        "threadsins2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_03",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-45) max 45)/\t95),(((-55) max 55)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-70) max 70)/\t95),(((-60) max 60)/\t95)]))"
        },
        "threadsins3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_04",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-65) max 65)/\t95),(((-70) max 70)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-85) max 85)/\t95),(((-80) max 80)/\t95)]))"
        },
        "threadsins4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_05",
                0.707946,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/\t95) factor[(((-80) max 80)/\t95),(((-90) max 90)/\t95)])"
        },
        "threadsouth0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_01",
                0.398107,
                1,
                140
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-0) max 0)/\t95),(((-10) max 10)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-25) max 25)/\t95),(((-15) max 15)/\t95)]))"
        },
        "threadsouth1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_02",
                0.446684,
                1,
                160
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-20) max 20)/\t95),(((-35) max 35)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-55) max 55)/\t95),(((-40) max 40)/\t95)]))"
        },
        "threadsouth2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_03",
                0.501187,
                1,
                180
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-45) max 45)/\t95),(((-55) max 55)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-70) max 70)/\t95),(((-60) max 60)/\t95)]))"
        },
        "threadsouth3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_04",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-65) max 65)/\t95),(((-70) max 70)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-85) max 85)/\t95),(((-80) max 80)/\t95)]))"
        },
        "threadsouth4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_05",
                0.562341,
                1,
                220
            ],
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/\t95) factor[(((-80) max 80)/\t95),(((-90) max 90)/\t95)])"
        },
        "threadsouts0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_01",
                0.316228,
                1,
                120
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-0) max 0)/\t95),(((-10) max 10)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-25) max 25)/\t95),(((-15) max 15)/\t95)]))"
        },
        "threadsouts1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_02",
                0.354813,
                1,
                140
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-20) max 20)/\t95),(((-35) max 35)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-55) max 55)/\t95),(((-40) max 40)/\t95)]))"
        },
        "threadsouts2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_03",
                0.398107,
                1,
                160
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-45) max 45)/\t95),(((-55) max 55)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-70) max 70)/\t95),(((-60) max 60)/\t95)]))"
        },
        "threadsouts3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_04",
                0.446684,
                1,
                180
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t95) factor[(((-65) max 65)/\t95),(((-70) max 70)/\t95)])\t*\t((((-speed*3.6) max speed*3.6)/\t95) factor[(((-85) max 85)/\t95),(((-80) max 80)/\t95)]))"
        },
        "threadsouts4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_05",
                0.501187,
                1,
                200
            ],
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/\t95) factor[(((-80) max 80)/\t95),(((-90) max 90)/\t95)])"
        }
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundturnin": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnininternal": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnout": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnoutinternal": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundwatercrash": [
        "",
        0.177828,
        1
    ],
    "soundwatercrashes": [
        "soundWaterCrash",
        1
    ],
    "soundwoodcrash": [
        "woodCrash0",
        0.166,
        "woodCrash1",
        0.166,
        "woodCrash2",
        0.166,
        "woodCrash3",
        0.166,
        "woodCrash4",
        0.166,
        "woodCrash5",
        0.166
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_vehicle_APC_p"
            ],
            "speechsingular": [
                "veh_vehicle_APC_s"
            ]
        }
    },
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "squadtitles": {
        "color": [
            0,
            0,
            0,
            0.75
        ],
        "name": "clan_sign"
    },
    "steeraheadplan": 0.4,
    "steeraheadsimul": 0.3,
    "supplyradius": -1,
    "switchtime": 0.1,
    "tankturnforce": 450000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.87,
    "tbody": 250,
    "textplural": "IFVs",
    "textsingular": "IFV",
    "texturelist": [],
    "texturesources": {
        "desert": {
            "author": "Red Hammer Studios",
            "displayname": "Desert",
            "factions": [
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/a3_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/ultralp_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/base_co.paa"
            ]
        },
        "olive": {
            "author": "Red Hammer Studios",
            "displayname": "Olive",
            "factions": [
                "rhs_faction_usarmy_wd"
            ],
            "textures": [
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/m6_base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/m6_a3_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/ultralp_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/m6_base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/m6_base_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Woodland",
            "factions": [
                "rhs_faction_usarmy_wd"
            ],
            "textures": [
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/a3_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/ultralp_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa",
                "/rhsusf/addons/rhsusf_a2port_armor/m2a2_bradley/data/woodland/base_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "threat": [
        0.9,
        0.9,
        0.4
    ],
    "thrustdelay": 0.3,
    "torquecurve": [
        [
            0.307692,
            0.518072
        ],
        [
            0.384615,
            0.855422
        ],
        [
            0.538462,
            1
        ],
        [
            0.576923,
            0.945783
        ],
        [
            0.653846,
            0.909639
        ],
        [
            0.769231,
            0.873494
        ],
        [
            0.903846,
            0.843373
        ],
        [
            1.02962,
            0
        ]
    ],
    "tracksspeed": 10,
    "transmissionlosses": 15,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 8
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 10,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 2,
            "name": "Medikit"
        },
        "_xx_toolkit": {
            "count": 1,
            "name": "Toolkit"
        }
    },
    "transportmagazines": {
        "_xx_rhs_fgm148_magazine_at": {
            "count": 4,
            "magazine": "rhs_fgm148_magazine_AT"
        },
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 75,
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag"
        },
        "_xx_rhs_mag_an_m8hc": {
            "count": 10,
            "magazine": "rhs_mag_an_m8hc"
        },
        "_xx_rhs_mag_m18_green": {
            "count": 4,
            "magazine": "rhs_mag_m18_green"
        },
        "_xx_rhs_mag_m18_red": {
            "count": 4,
            "magazine": "rhs_mag_m18_red"
        },
        "_xx_rhs_mag_m441_he": {
            "count": 20,
            "magazine": "rhs_mag_M441_HE"
        },
        "_xx_rhs_mag_m662_red": {
            "count": 4,
            "magazine": "rhs_mag_M662_red"
        },
        "_xx_rhs_mag_m67": {
            "count": 10,
            "magazine": "rhs_mag_m67"
        },
        "_xx_rhs_mag_m714_white": {
            "count": 8,
            "magazine": "rhs_mag_M714_white"
        },
        "_xx_rhsusf_100rnd_556x45_soft_pouch": {
            "count": 11,
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch"
        },
        "_xx_rhsusf_100rnd_762x51": {
            "count": 11,
            "magazine": "rhsusf_100Rnd_762x51"
        }
    },
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 6,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_fgm148": {
            "count": 2,
            "weapon": "rhs_weap_fgm148"
        },
        "_xx_rhs_weap_m4_carryhandle_pmag": {
            "count": 4,
            "weapon": "rhs_weap_m4_carryhandle_pmag"
        }
    },
    "turncoef": 5,
    "turrets": {
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "armorlights": 0.4,
            "body": "mainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "EmptyDisplay",
                    "left": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                "vehiclesystemsdisplaymanagercomponentright": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "EmptyDisplay",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "discretedistance": [
                0,
                200,
                400,
                600,
                800,
                1000,
                1200,
                1400,
                1600,
                1800,
                2000,
                2200,
                2400,
                2600,
                2800,
                3000
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mainGun",
            "gunbeg": "Usti hlavne",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "gunend": "Konec hlavne",
            "gunfire": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletgrowup": 0.2,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletFire",
                "cloudletsize": 1,
                "deltat": -3000,
                "initt": 4500,
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            0.82,
                            0.95,
                            0.93,
                            0
                        ],
                        "maxt": 0
                    },
                    "t1": {
                        "color": [
                            0.75,
                            0.77,
                            0.9,
                            0
                        ],
                        "maxt": 200
                    },
                    "t10": {
                        "color": [
                            0.62,
                            0.29,
                            0.03,
                            0
                        ],
                        "maxt": 2600
                    },
                    "t11": {
                        "color": [
                            0.59,
                            0.35,
                            0.05,
                            0
                        ],
                        "maxt": 2650
                    },
                    "t12": {
                        "color": [
                            0.75,
                            0.37,
                            0.03,
                            0
                        ],
                        "maxt": 2700
                    },
                    "t13": {
                        "color": [
                            0.88,
                            0.34,
                            0.03,
                            0
                        ],
                        "maxt": 2750
                    },
                    "t14": {
                        "color": [
                            0.91,
                            0.5,
                            0.17,
                            0
                        ],
                        "maxt": 2800
                    },
                    "t15": {
                        "color": [
                            1,
                            0.6,
                            0.2,
                            0
                        ],
                        "maxt": 2850
                    },
                    "t16": {
                        "color": [
                            1,
                            0.71,
                            0.3,
                            0
                        ],
                        "maxt": 2900
                    },
                    "t17": {
                        "color": [
                            0.98,
                            0.83,
                            0.41,
                            0
                        ],
                        "maxt": 2950
                    },
                    "t18": {
                        "color": [
                            0.98,
                            0.91,
                            0.54,
                            0
                        ],
                        "maxt": 3000
                    },
                    "t19": {
                        "color": [
                            0.98,
                            0.99,
                            0.6,
                            0
                        ],
                        "maxt": 3100
                    },
                    "t2": {
                        "color": [
                            0.56,
                            0.62,
                            0.67,
                            0
                        ],
                        "maxt": 400
                    },
                    "t20": {
                        "color": [
                            0.96,
                            0.99,
                            0.72,
                            0
                        ],
                        "maxt": 3300
                    },
                    "t21": {
                        "color": [
                            1,
                            0.98,
                            0.91,
                            0
                        ],
                        "maxt": 3600
                    },
                    "t22": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 4200
                    },
                    "t3": {
                        "color": [
                            0.39,
                            0.46,
                            0.47,
                            0
                        ],
                        "maxt": 600
                    },
                    "t4": {
                        "color": [
                            0.24,
                            0.31,
                            0.31,
                            0
                        ],
                        "maxt": 800
                    },
                    "t5": {
                        "color": [
                            0.23,
                            0.31,
                            0.29,
                            0
                        ],
                        "maxt": 1000
                    },
                    "t6": {
                        "color": [
                            0.21,
                            0.29,
                            0.27,
                            0
                        ],
                        "maxt": 1500
                    },
                    "t7": {
                        "color": [
                            0.19,
                            0.23,
                            0.21,
                            0
                        ],
                        "maxt": 2000
                    },
                    "t8": {
                        "color": [
                            0.22,
                            0.19,
                            0.1,
                            0
                        ],
                        "maxt": 2300
                    },
                    "t9": {
                        "color": [
                            0.35,
                            0.2,
                            0.02,
                            0
                        ],
                        "maxt": 2500
                    }
                },
                "timetolive": 0
            },
            "gunneraction": "RHS_M2A2_GunnerOut",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchG",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerhasflares": 0,
            "gunnerinaction": "RHS_M2A2_Gunner",
            "gunnerlefthandanimname": "turret_control",
            "gunnerleftleganimname": "",
            "gunnername": "Gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerrighthandanimname": "",
            "gunnerrightleganimname": "",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hit_optics_gnr": {
                    "armor": -40,
                    "armorcomponent": "Hit_Optics_Gnr",
                    "explosionshielding": 0,
                    "name": "",
                    "passthrough": 0,
                    "visual": "vis_optics_Gnr"
                },
                "hitgun": {
                    "armor": -60,
                    "armorcomponent": "Hit_Gun",
                    "explosionshielding": 0.001,
                    "isgun": 1,
                    "minimalhit": -0.3,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.1,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": -60,
                    "armorcomponent": "Hit_Turret",
                    "explosionshielding": 0.001,
                    "isturret": 1,
                    "minimalhit": -0.3,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.08,
                    "visual": "vez"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "lockwhendriverout": 1,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 0,
            "lodturnedin": 1000,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_1100Rnd_762x51_M240",
                "rhs_mag_1100Rnd_762x51_M240",
                "rhs_mag_230Rnd_25mm_M242_HEI",
                "rhs_mag_230Rnd_25mm_M242_HEI",
                "rhs_mag_230Rnd_25mm_M242_HEI",
                "rhs_mag_70Rnd_25mm_M242_APFSDS",
                "rhs_mag_70Rnd_25mm_M242_APFSDS",
                "rhs_mag_70Rnd_25mm_M242_APFSDS",
                "rhs_mag_2Rnd_TOW2A",
                "rhs_mag_2Rnd_TOW2A",
                "rhs_mag_2Rnd_TOW2A",
                "rhs_mag_2Rnd_TOW2BB",
                "rhs_laserfcsmag"
            ],
            "maxcamelev": 90,
            "maxelev": 57,
            "maxhorizontalrotspeed": 1.04,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 1.04,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 0.3,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletgrowup": 0.05,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "mincamelev": -90,
            "minelev": -9,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "narrow": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_ISU",
                    "hitpoint": "Hit_Optics_Gnr",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.0583333,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.0583333,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.0583333,
                    "opticsdisplayname": "NARROW",
                    "thermalmode": [
                        4
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "wide": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_ISU",
                    "hitpoint": "Hit_Optics_Gnr",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.175,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.175,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.175,
                    "opticsdisplayname": "WIDE",
                    "thermalmode": [
                        4
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                }
            },
            "outgunnermayfire": 0,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh2",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_gunner",
                0.562341,
                1,
                30
            ],
            "soundservovertical": [
                "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_gunner_vertical",
                0.562341,
                1,
                30
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscODS_ISU",
            "turrets": {
                "commanderoptics": {
                    "aggregatereflectors": [],
                    "allowlauncherin": 0,
                    "allowlauncherout": 0,
                    "allowtablock": 0,
                    "animationsourcebody": "obsTurret",
                    "animationsourcecamelev": "camElev",
                    "animationsourcegun": "obsGun",
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "armorlights": 0.4,
                    "body": "obsTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 1,
                    "castgunnershadow": 0,
                    "commanding": 2,
                    "components": {
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            "components": {
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                },
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "defaultdisplay": "EmptyDisplay",
                            "left": 1,
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        "vehiclesystemsdisplaymanagercomponentright": {
                            "components": {
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                },
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "defaultdisplay": "EmptyDisplay",
                            "right": 1,
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "disablesoundattenuation": 0,
                    "dontcreateai": 0,
                    "ejectdeadgunner": 0,
                    "forcehidegunner": 0,
                    "forcenvg": 0,
                    "gun": "obsGun",
                    "gunbeg": "",
                    "gunclouds": {
                        "access": 0,
                        "cloudletaccy": 0.4,
                        "cloudletalpha": 1,
                        "cloudletanimperiod": 1,
                        "cloudletcolor": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "cloudletduration": 0.3,
                        "cloudletfadein": 0.01,
                        "cloudletfadeout": 1,
                        "cloudletgrowup": 1,
                        "cloudletmaxyspeed": 0.8,
                        "cloudletminyspeed": 0.2,
                        "cloudletshape": "cloudletClouds",
                        "cloudletsize": 1,
                        "deltat": 0,
                        "initt": 0,
                        "interval": 0.05,
                        "size": 3,
                        "sourcesize": 0.5,
                        "table": {
                            "t0": {
                                "color": [
                                    1,
                                    1,
                                    1,
                                    0
                                ],
                                "maxt": 0
                            }
                        },
                        "timetolive": 0
                    },
                    "gunend": "",
                    "gunfire": {
                        "access": 0,
                        "cloudletaccy": 0,
                        "cloudletalpha": 1,
                        "cloudletanimperiod": 1,
                        "cloudletcolor": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "cloudletduration": 0.2,
                        "cloudletfadein": 0.01,
                        "cloudletfadeout": 0.5,
                        "cloudletgrowup": 0.2,
                        "cloudletmaxyspeed": 100,
                        "cloudletminyspeed": -100,
                        "cloudletshape": "cloudletFire",
                        "cloudletsize": 1,
                        "deltat": -3000,
                        "initt": 4500,
                        "interval": 0.01,
                        "size": 3,
                        "sourcesize": 0.5,
                        "table": {
                            "t0": {
                                "color": [
                                    0.82,
                                    0.95,
                                    0.93,
                                    0
                                ],
                                "maxt": 0
                            },
                            "t1": {
                                "color": [
                                    0.75,
                                    0.77,
                                    0.9,
                                    0
                                ],
                                "maxt": 200
                            },
                            "t10": {
                                "color": [
                                    0.62,
                                    0.29,
                                    0.03,
                                    0
                                ],
                                "maxt": 2600
                            },
                            "t11": {
                                "color": [
                                    0.59,
                                    0.35,
                                    0.05,
                                    0
                                ],
                                "maxt": 2650
                            },
                            "t12": {
                                "color": [
                                    0.75,
                                    0.37,
                                    0.03,
                                    0
                                ],
                                "maxt": 2700
                            },
                            "t13": {
                                "color": [
                                    0.88,
                                    0.34,
                                    0.03,
                                    0
                                ],
                                "maxt": 2750
                            },
                            "t14": {
                                "color": [
                                    0.91,
                                    0.5,
                                    0.17,
                                    0
                                ],
                                "maxt": 2800
                            },
                            "t15": {
                                "color": [
                                    1,
                                    0.6,
                                    0.2,
                                    0
                                ],
                                "maxt": 2850
                            },
                            "t16": {
                                "color": [
                                    1,
                                    0.71,
                                    0.3,
                                    0
                                ],
                                "maxt": 2900
                            },
                            "t17": {
                                "color": [
                                    0.98,
                                    0.83,
                                    0.41,
                                    0
                                ],
                                "maxt": 2950
                            },
                            "t18": {
                                "color": [
                                    0.98,
                                    0.91,
                                    0.54,
                                    0
                                ],
                                "maxt": 3000
                            },
                            "t19": {
                                "color": [
                                    0.98,
                                    0.99,
                                    0.6,
                                    0
                                ],
                                "maxt": 3100
                            },
                            "t2": {
                                "color": [
                                    0.56,
                                    0.62,
                                    0.67,
                                    0
                                ],
                                "maxt": 400
                            },
                            "t20": {
                                "color": [
                                    0.96,
                                    0.99,
                                    0.72,
                                    0
                                ],
                                "maxt": 3300
                            },
                            "t21": {
                                "color": [
                                    1,
                                    0.98,
                                    0.91,
                                    0
                                ],
                                "maxt": 3600
                            },
                            "t22": {
                                "color": [
                                    1,
                                    1,
                                    1,
                                    0
                                ],
                                "maxt": 4200
                            },
                            "t3": {
                                "color": [
                                    0.39,
                                    0.46,
                                    0.47,
                                    0
                                ],
                                "maxt": 600
                            },
                            "t4": {
                                "color": [
                                    0.24,
                                    0.31,
                                    0.31,
                                    0
                                ],
                                "maxt": 800
                            },
                            "t5": {
                                "color": [
                                    0.23,
                                    0.31,
                                    0.29,
                                    0
                                ],
                                "maxt": 1000
                            },
                            "t6": {
                                "color": [
                                    0.21,
                                    0.29,
                                    0.27,
                                    0
                                ],
                                "maxt": 1500
                            },
                            "t7": {
                                "color": [
                                    0.19,
                                    0.23,
                                    0.21,
                                    0
                                ],
                                "maxt": 2000
                            },
                            "t8": {
                                "color": [
                                    0.22,
                                    0.19,
                                    0.1,
                                    0
                                ],
                                "maxt": 2300
                            },
                            "t9": {
                                "color": [
                                    0.35,
                                    0.2,
                                    0.02,
                                    0
                                ],
                                "maxt": 2500
                            }
                        },
                        "timetolive": 0
                    },
                    "gunneraction": "RHS_M2A2_CommanderOut",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "hatchC",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 1,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "RHS_M2A2_Commander",
                    "gunnerlefthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnername": "Commander",
                    "gunneropticscolor": [
                        0,
                        0,
                        0,
                        1
                    ],
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_a2port_armor/M2A2_Bradley/gunnerOptics_M2A2_2",
                    "gunneropticsshowcursor": 0,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunneroutforceoptics": 0,
                    "gunneroutopticscolor": [
                        0,
                        0,
                        0,
                        1
                    ],
                    "gunneroutopticseffect": [],
                    "gunneroutopticsmodel": "",
                    "gunneroutopticsshowcursor": 0,
                    "gunnerrighthandanimname": "com_turret_control",
                    "gunnerrightleganimname": "",
                    "gunnertype": "",
                    "gunnerusespilotview": 0,
                    "hasgunner": 1,
                    "hideweaponsgunner": 1,
                    "hitpoints": {
                        "hit_optics_cdr_peri": {
                            "armor": -40,
                            "armorcomponent": "Hit_Optics_Cdr_Peri",
                            "explosionshielding": 0,
                            "name": "",
                            "passthrough": 0,
                            "visual": "vis_optics_Cdr_Peri"
                        },
                        "hitguncom": {
                            "armor": 0.3,
                            "explosionshielding": 0.001,
                            "isgun": 1,
                            "material": -1,
                            "minimalhit": 0.03,
                            "name": "zbranVelitele",
                            "passthrough": 0,
                            "radius": 0.25,
                            "visual": "zbranVelitele"
                        },
                        "hitturretcom": {
                            "armor": 0.3,
                            "explosionshielding": 0.001,
                            "isturret": 1,
                            "material": -1,
                            "minimalhit": 0.03,
                            "name": "vezVelitele",
                            "passthrough": 0,
                            "radius": 0.25,
                            "visual": "vezVelitele"
                        }
                    },
                    "ingunnermayfire": 1,
                    "initcamelev": 0,
                    "initelev": 0,
                    "initoutelev": 0,
                    "initoutturn": 0,
                    "initturn": 0,
                    "iscopilot": 0,
                    "ispersonturret": 1,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "lodopticsin": 0,
                    "lodturnedin": 1000,
                    "lodturnedout": -1,
                    "magazines": [
                        "rhsusf_mag_L8A3_8"
                    ],
                    "maxcamelev": 90,
                    "maxelev": 5,
                    "maxhorizontalrotspeed": 1.8,
                    "maxoutelev": 15,
                    "maxoutturn": 90,
                    "maxturn": 360,
                    "maxverticalrotspeed": 1.8,
                    "memorypointgun": "gun_muzzle",
                    "memorypointgunneroptics": "commanderview",
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "memorypointsgetingunnerprecise": "",
                    "mgunclouds": {
                        "access": 0,
                        "cloudletaccy": 0,
                        "cloudletalpha": 0.3,
                        "cloudletanimperiod": 1,
                        "cloudletcolor": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "cloudletduration": 0.05,
                        "cloudletfadein": 0,
                        "cloudletfadeout": 0.1,
                        "cloudletgrowup": 0.05,
                        "cloudletmaxyspeed": 100,
                        "cloudletminyspeed": -100,
                        "cloudletshape": "cloudletClouds",
                        "cloudletsize": 1,
                        "deltat": 0,
                        "initt": 0,
                        "interval": 0.02,
                        "size": 0.3,
                        "sourcesize": 0.02,
                        "table": {
                            "t0": {
                                "color": [
                                    1,
                                    1,
                                    1,
                                    0
                                ],
                                "maxt": 0
                            }
                        },
                        "timetolive": 0
                    },
                    "mincamelev": -90,
                    "minelev": -5,
                    "minoutelev": -10,
                    "minoutturn": -45,
                    "minturn": -360,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "narrow": {
                            "campos": "gunnerview",
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_ISU",
                            "hitpoint": "Hit_Optics_Gnr",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.0583333,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.0583333,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.0583333,
                            "opticsdisplayname": "NARROW",
                            "thermalmode": [
                                4
                            ],
                            "visionmode": [
                                "Normal",
                                "Ti"
                            ]
                        },
                        "visionblock": {
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_vision_block",
                            "hitpoint": "Hit_Optics_Cdr_Peri",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.7,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.7,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.7,
                            "opticsdisplayname": "periscope",
                            "visionmode": [
                                "Normal",
                                "NVG"
                            ]
                        },
                        "wide": {
                            "campos": "gunnerview",
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhsusf_ISU",
                            "hitpoint": "Hit_Optics_Gnr",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.175,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.175,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.175,
                            "opticsdisplayname": "WIDE",
                            "thermalmode": [
                                4
                            ],
                            "visionmode": [
                                "Normal",
                                "Ti"
                            ]
                        }
                    },
                    "outgunnermayfire": 1,
                    "personturretaction": "vehicle_turnout_1",
                    "playerposition": 0,
                    "precisegetinout": 0,
                    "primary": 1,
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "proxyindex": 1,
                    "proxytype": "CPCommander",
                    "reflectors": {
                        "cabin": {
                            "ambient": [
                                5,
                                5,
                                5
                            ],
                            "attenuation": {
                                "constant": 0,
                                "hardlimitend": 1.5,
                                "hardlimitstart": 1,
                                "linear": 1,
                                "quadratic": 50,
                                "start": 0
                            },
                            "blinking": 0,
                            "color": [
                                800,
                                900,
                                650
                            ],
                            "conefadecoef": 1,
                            "daylight": 1,
                            "direction": "cabin_light_dir",
                            "flaremaxdistance": 5,
                            "flaresize": 1,
                            "hitpoint": "cabin_light",
                            "innerangle": 90,
                            "intensity": 0.3,
                            "outerangle": 165,
                            "position": "cabin_light",
                            "selection": "cabin_light",
                            "size": 1,
                            "useflare": 1
                        },
                        "cargo_light_1": {
                            "ambient": [
                                5,
                                5,
                                5
                            ],
                            "attenuation": {
                                "constant": 0,
                                "hardlimitend": 2,
                                "hardlimitstart": 1.4,
                                "linear": 1,
                                "quadratic": 70,
                                "start": 0
                            },
                            "blinking": 0,
                            "color": [
                                800,
                                900,
                                650
                            ],
                            "conefadecoef": 0.1,
                            "daylight": 1,
                            "direction": "cargo_light_1_dir",
                            "flaremaxdistance": 5,
                            "flaresize": 1,
                            "hitpoint": "cargo_light_1",
                            "innerangle": 140,
                            "intensity": 3,
                            "outerangle": 175,
                            "position": "cargo_light_1",
                            "selection": "cargo_light_1",
                            "size": 1,
                            "useflare": 0
                        }
                    },
                    "selectionfireanim": "zasleh_1",
                    "showalltargets": 0,
                    "showcrewaim": 0,
                    "showhmd": 0,
                    "slingloadoperator": 0,
                    "soundelevation": [
                        "",
                        0.00316228,
                        1
                    ],
                    "soundservo": [
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        0.562341,
                        1,
                        30
                    ],
                    "soundservovertical": [
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        0.562341,
                        1,
                        30
                    ],
                    "stabilizedinaxes": 3,
                    "startengine": 0,
                    "turnin": {
                        "turnoffset": 0
                    },
                    "turnout": {
                        "turnoffset": 0
                    },
                    "turretcansee": 0,
                    "turretfollowfreelook": 2,
                    "turretinfotype": "RHS_RscODS_ISU",
                    "turrets": {},
                    "turretspec": {
                        "showheadphones": 0
                    },
                    "usepip": 2,
                    "viewgunner": {
                        "initanglex": -5,
                        "initangley": 0,
                        "initfov": 0.9,
                        "maxanglex": 85,
                        "maxangley": 150,
                        "maxfov": 1.25,
                        "maxmovex": 0.075,
                        "maxmovey": 0.075,
                        "maxmovez": 0.1,
                        "minanglex": -65,
                        "minangley": -150,
                        "minfov": 0.25,
                        "minmovex": -0.075,
                        "minmovey": -0.075,
                        "minmovez": -0.075,
                        "speedzoommaxfov": 0,
                        "speedzoommaxspeed": 10000000000.0
                    },
                    "viewgunnerinexternal": 1,
                    "viewgunnershadow": 1,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "viewoptics": {
                        "initanglex": 0,
                        "initangley": 0,
                        "initfov": 0.155,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.155,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.067
                    },
                    "weapons": [
                        "rhsusf_weap_M257_8"
                    ]
                }
            },
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 2,
            "viewgunner": {
                "continuous": 0,
                "initanglex": -5,
                "initangley": 0,
                "initfov": 0.9,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0.075,
                "maxmovey": 0.075,
                "maxmovez": 0.1,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": -0.075,
                "minmovey": -0.075,
                "minmovez": -0.075,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 1,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "RHS_weap_M242BC",
                "rhs_weap_m240_bradley_coax",
                "Rhs_weap_TOW_Launcher",
                "rhs_weap_fcs_ammo"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RHSUSF_RscUnitInfoWestTank",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "closecargodoor": {
            "condition": "this doorPhase 'ramp' > 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "displayname": "Close ramp",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 15,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateDoor ['ramp', 0];this setVariable ['ramp_handler',0,true]"
        },
        "opencargodoor": {
            "condition": "this doorPhase 'ramp' == 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "displayname": "Open ramp",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 15,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateDoor ['ramp', 1];this setVariable ['ramp_handler',1,true]"
        },
        "togglelight": {
            "condition": "player in this;",
            "displayname": "Toggle interior light",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "statement": "[this,'cargolights_hide',[0,0]] call rhs_fnc_toggleIntLight"
        }
    },
    "vehicleclass": "rhs_vehclass_ifv",
    "viewcargo": {
        "initanglex": 5,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -75,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewcargoshadow": 1,
    "viewcargoshadowamb": 0.5,
    "viewcargoshadowdiff": 0.05,
    "viewdriverinexternal": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.7,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.7,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0,
        "visionmode": [
            "Normal",
            "NVG"
        ]
    },
    "viewpilot": {
        "initanglex": 7,
        "initangley": 0,
        "initfov": 0.9,
        "maxanglex": 25,
        "maxangley": 90,
        "maxfov": 1.25,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -15,
        "minangley": -90,
        "minfov": 0.25,
        "minmovex": -0.075,
        "minmovey": -0.075,
        "minmovez": -0.075,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 0,
    "waterresistancecoef": 0.5,
    "weapons": [
        "rhs_weap_smokegen"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1.95,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l7": {
            "bonename": "wheel_podkolol6",
            "boundary": "wheel_1_7_bound",
            "center": "wheel_1_7_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.0392,
            "side": "left",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r7": {
            "bonename": "wheel_podkolop6",
            "boundary": "wheel_2_7_bound",
            "center": "wheel_2_7_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1088,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.32,
                    1
                ],
                [
                    0.6,
                    0.86
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 130,
            "maxbraketorque": 6520,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.0392,
            "side": "right",
            "springdamperrate": 14811,
            "springstrength": 256250,
            "sprungmass": 2500,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.4
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "woodcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "woodcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "woodcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
        1,
        200
    ],
    "woodcrash4": [
        "A3/sounds_f/Vehicles/crashes/crash_01",
        1,
        1,
        200
    ],
    "woodcrash5": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ]
}