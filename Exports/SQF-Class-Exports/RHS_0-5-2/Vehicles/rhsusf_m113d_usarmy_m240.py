d = {
    "_generalmacro": "APC_Tracked_02_base_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 3.23,
    "accelaidforceyoffset": -3.3,
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
        "hatchd": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchgunner": {
            "animperiod": 1e-05,
            "displayname": "close commander hatch",
            "initphase": 0,
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
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m240_m113"
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
        "reloadanim": {
            "source": "reload",
            "weapon": "rhs_weap_m240_m113"
        },
        "reloadmagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_m240_m113"
        },
        "revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_m240_m113"
        },
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M259"
        }
    },
    "antirollbarforcecoef": 20,
    "antirollbarforcelimit": 10,
    "antirollbarspeedmax": 55,
    "antirollbarspeedmin": 10,
    "armor": 200,
    "armorcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "armorcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "armorcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "armorcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
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
    "armorstructural": 350,
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
        "rhs_hideiffpanel": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Hide IFF Panel",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "property": "rhs_hideIFFPanel"
        },
        "rhs_openramp": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open rear ramp",
            "expression": "_this animateDoor ['ramp',_value,true]",
            "property": "rhs_openRamp"
        }
    },
    "audible": 18,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 0.1,
    "buildcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "buildcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "buildcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "buildcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
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
    "canfloat": 1,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_M113_Cargo01",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo02",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo01",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo03",
        "RHS_M113_Cargo01"
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
        4,
        5,
        6,
        8,
        9,
        10,
        11
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
        0.4,
        0.4,
        0,
        0.84,
        0.56,
        0.94,
        0.56,
        0.96,
        0.56,
        1,
        0.6
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 15,
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
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 1,
                "point": "light_interior1",
                "size": 0,
                "useflare": 0
            },
            "light10": {
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
                    20,
                    20,
                    20
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior10",
                "size": 0,
                "useflare": 0
            },
            "light11": {
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
                    20,
                    20,
                    20
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior11",
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
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.3,
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
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.4,
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
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.5,
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
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.3,
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
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior6",
                "size": 0,
                "useflare": 0
            },
            "light7": {
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
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior7",
                "size": 0,
                "useflare": 0
            },
            "light8": {
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
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior8",
                "size": 0,
                "useflare": 0
            },
            "light9": {
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
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior9",
                "size": 0,
                "useflare": 0
            }
        }
    },
    "complexgearbox": {
        "amphibiousratios": [
            "R1",
            -10,
            "N",
            0,
            "D1",
            10
        ],
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -6.62,
            "N",
            0,
            "D1",
            4.16,
            "D2",
            2.14,
            "D3",
            1.46,
            "D4",
            1.02
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.6,
        "transmissionratios": [
            "High",
            12.3
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
    "cost": 1500000.0,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_army_ocp_crewman",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.999,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_01.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_02.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_03.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int01.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int01_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int01_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int02.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int02_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int02_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/M23_pintle.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/M23_pintle_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_t.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_t_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_t_destr.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_shield.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_shield_dam.rvmat",
            "rhsusf/addons/rhsusf_m113/data_new/m113a3_shield_destr.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "dampersbumpcoef": 4.5,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "dampingratezerothrottleclutchengaged": 3,
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
    "displayname": "M113A3 (M240)",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "Track_L",
        "Track_R",
        "Slide"
    ],
    "driveraction": "RHS_M113_DriverOut",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "hatchD",
    "driverforceoptics": 0,
    "driverinaction": "RHS_M113_Driver",
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "driverstick_left",
    "driverleftleganimname": "pedal_brake",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhs_periscope_BISType",
    "driverrighthandanimname": "driverstick_right",
    "driverrightleganimname": "pedal_thrust",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/rhsusf_m113d_usarmy_M240.paa",
    "editorsubcategory": "EdSubcat_APCs",
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
    "engineeffectspeed": 5,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 10,
    "enginepower": 205,
    "engineshifty": 0.6,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "postinit": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhsusf_eventhandlers": {
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay",
            "getin": "_this call rhs_fnc_m2_doors",
            "getout": "_this call rhs_fnc_m2_doors",
            "hitpart": "_this call rhsusf_fnc_hitSpall",
            "turnin": "([0] + _this)  call rhsusf_fnc_turretAction;",
            "turnout": "([1] + _this) call rhsusf_fnc_turretAction;"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustsEffectBig",
            "position": "vyfuk start"
        }
    },
    "explosioneffect": "FuelExplosionBig",
    "explosionshielding": 70,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2,
        -11
    ],
    "faction": "rhs_faction_usarmy_d",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "emptyEffect",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 24,
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
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11
    ],
    "getinradius": 3.5,
    "getoutaction": "GetOutLow",
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
    "hascommander": 0,
    "hasdriver": 1,
    "hasgunner": 1,
    "hasterminal": 0,
    "headaimdown": 19,
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
        "camo4",
        "camo5",
        "camo6"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_d_l_co.paa",
        "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_d_l_co.paa",
        "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_d_co.paa",
        "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_d_co.paa",
        "rhsusf/addons/rhsusf_m113/data_new/m23_pintle_d_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 0.45,
            "armorcomponent": "hit_engine",
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
            "minimalhit": 0.039,
            "name": "motor",
            "passthrough": 0,
            "radius": 0.27,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 0.25,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.7,
            "name": "palivo",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": ""
        },
        "hithull": {
            "armor": 5.9,
            "armorcomponent": "hit_hull",
            "explosionshielding": 0.005,
            "material": -1,
            "minimalhit": 0.14,
            "name": "telo",
            "passthrough": 0,
            "radius": 0.01,
            "visual": "zbytek"
        },
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "hit_trackL",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "pas_L",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_L"
        },
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "hit_trackR",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "pas_P",
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
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsusf/addons/rhsusf_m113/data/icom113_ca",
    "idlerpm": 550,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.8,
    "irscanground": 2,
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
    "latency": 0.1,
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
        "libtextdesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "loddriveropticsin": 1202,
    "loddriverturnedin": 1100,
    "loddriverturnedout": 0,
    "magazines": [
        "rhs_mag_smokegen"
    ],
    "mapsize": 4.8,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.1,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 261.8,
    "maxspeed": 72,
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
        "mfd_commander_ammoindicator_main_armament": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
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
                            0.39,
                            0.28
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.13
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.13
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
                "gunner_text_2": {
                    "align": "left",
                    "down": [
                        [
                            0.39,
                            0.38
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.23
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.23
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
                "gunner_text_3": {
                    "align": "left",
                    "down": [
                        [
                            0.39,
                            0.48
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.33
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.33
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 2,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_armament_ammo_type_1": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.28
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.13
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.13
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0411\u0420",
                    "type": "text"
                },
                "main_armament_ammo_type_2": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.38
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.23
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.23
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0424",
                    "type": "text"
                },
                "main_armament_ammo_type_3": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.48
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.33
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.33
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0420",
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
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_coax_ammo": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_ammo_count_BL",
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
                            1.32,
                            1
                        ],
                        1
                    ],
                    "pos": [
                        [
                            1.32,
                            0.2
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.97,
                            0.2
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
            "topleft": "mfd_com_ammo_count_TL",
            "topright": "mfd_com_ammo_count_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_coax_magazines": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_mag_count_BL",
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
                            0.1,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.11
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.85,
                            0.11
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
            "topleft": "mfd_com_mag_count_TL",
            "topright": "mfd_com_mag_count_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_display": {
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
                "azimut": {
                    "align": "center",
                    "down": [
                        [
                            0.71,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.71,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.77,
                            0.8
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "commander_armament": {
                    "align": "center",
                    "down": [
                        [
                            0.795,
                            0.125
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.795,
                            0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.845,
                            0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0420\u0423\u0414\u0418\u0415 \u041a\u041e\u041c\u0410\u041d\u0414\u0418\u0420\u0410",
                    "type": "text"
                },
                "commander_armament_magazines": {
                    "align": "center",
                    "down": [
                        [
                            0.47,
                            0.55
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.47,
                            0.4
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.53,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041c\u0410\u0413.",
                    "type": "text"
                },
                "commander_machinegun": {
                    "align": "center",
                    "down": [
                        [
                            0.81,
                            0.34
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.81,
                            0.19
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.87,
                            0.19
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "----",
                    "type": "text"
                },
                "condition": "1",
                "damage": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.82
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.82
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u041e\u0412\u0420\u0415\u0416\u0414\u0415\u041d\u0418\u042f",
                    "type": "text"
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.925,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.925,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.985,
                            0.8
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
                    "align": "center",
                    "down": [
                        [
                            0.73,
                            0.75
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.73,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.785,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0414\u0410\u041b\u042c\u041d\u041e\u0421\u0422\u042c",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.925,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.925,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.985,
                            0.61
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
                    "align": "center",
                    "down": [
                        [
                            0.51,
                            0.145
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.51,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.57,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u0423\u041b\u0415\u041c\u0415\u0422",
                    "type": "text"
                },
                "main_armament": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.145
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0413\u041b\u0410\u0412\u041d\u041e\u0415 \u041e\u0420\u0423\u0414\u0418\u0415",
                    "type": "text"
                },
                "main_armament_ammo_type": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0422\u0418\u041f \u0410\u041c\u0423\u041d\u0418\u0426\u0418\u0418",
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
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_main_armament_ammo_type": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
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
                            0.36,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.36,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.42,
                            0.61
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
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_ready_to_fire": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_cli_BL",
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
                            0.5,
                            0.92
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.41
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.7,
                            0.41
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0413\u041e\u0422\u041e\u0412",
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
                            0.48,
                            0.56
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.48,
                            0.05
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.68,
                            0.05
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u041a \u0421\u0422\u0420\u0415\u041b\u042c\u0411\u0415",
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
            "topleft": "mfd_com_cli_TL",
            "topright": "mfd_com_cli_TR"
        },
        "mfd_commander_second_display": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_7_BL",
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
                "crosshair": {
                    "points": [
                        [
                            [
                                0.5,
                                0.423413
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.346429
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.5,
                                0.577381
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.654365
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.55,
                                0.500397
                            ],
                            1
                        ],
                        [
                            [
                                0.6,
                                0.500397
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4,
                                0.500397
                            ],
                            1
                        ],
                        [
                            [
                                0.45,
                                0.500397
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.346429
                            ],
                            1
                        ],
                        [
                            [
                                0.3,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.269444
                            ],
                            1
                        ],
                        [
                            [
                                0.35,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.7,
                                0.346429
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.65,
                                0.269444
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.7,
                                0.654365
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.65,
                                0.731349
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.654365
                            ],
                            1
                        ],
                        [
                            [
                                0.3,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.731349
                            ],
                            1
                        ],
                        [
                            [
                                0.35,
                                0.731349
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line",
                    "width": 3
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.83,
                            0.33
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.83,
                            0.25
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.88,
                            0.25
                        ],
                        1
                    ],
                    "scale": 0.2,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.494,
                            0.88
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.494,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.544,
                            0.8
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_range_background": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.43,
                                        0.81
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.57,
                                        0.81
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.57,
                                        0.87
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.43,
                                        0.87
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0,
                        0,
                        0
                    ]
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
            "topleft": "MFD_7_TL",
            "topright": "MFD_7_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_smoke_indicator": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_smoke_BL",
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
                            0.5,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.4
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.7,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0417\u0410\u0412\u0415\u0421\u0410",
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
                            0.47,
                            0.5
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.47,
                            0
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.67,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0414\u042b\u041c\u041e\u0412\u0410\u042f",
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
            "topleft": "mfd_com_smoke_TL",
            "topright": "mfd_com_smoke_TR"
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
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
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
        "mfd_gunner_ammoindicator": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_3_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.92,
                    0.01,
                    0
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.3
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
                            1.3,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1000,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_2": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.6
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.3
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.3,
                            0.3
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1001,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_3": {
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
                            0.6
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.3,
                            0.6
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1002,
                    "sourcelength": 2,
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
            "topleft": "MFD_3_TL",
            "topright": "MFD_3_TR",
            "turret": [
                0
            ]
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
                            0.395,
                            0.143
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.065
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
                "gunner_text_2": {
                    "align": "left",
                    "down": [
                        [
                            0.395,
                            0.203
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.125
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.125
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
                "gunner_text_3": {
                    "align": "left",
                    "down": [
                        [
                            0.395,
                            0.263
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.185
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.185
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 2,
                    "sourcelength": 2,
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
                    "text": "\u0411\u0420",
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
                            0.075,
                            0.125
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0424",
                    "type": "text"
                },
                "main_armament_ammo_type_3": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.263
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.185
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.185
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0420",
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
            "bottomleft": "MFD_5_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.92,
                    0.01,
                    0
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.455,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.455,
                            0.05
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.355,
                            0.05
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
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
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
                    "align": "center",
                    "down": [
                        [
                            0.31,
                            0.388
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.31,
                            0.31
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.37,
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
                            0.015,
                            0.993
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.915
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.915
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
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
                    "text": "\u041f\u041e\u0412\u0420\u0415\u0416\u0414\u0415\u041d\u0418\u042f",
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
                    "text": "\u0414\u0410\u041b\u042c\u041d\u041e\u0421\u0422\u042c",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.34,
                            0.918
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.34,
                            0.84
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.4,
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
                    "text": "\u041f\u0423\u041b\u0415\u041c\u0415\u0422",
                    "type": "text"
                },
                "main_armament": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.073
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0413\u041b\u0410\u0412\u041d\u041e\u0415 \u041e\u0420\u0423\u0414\u0418\u0415",
                    "type": "text"
                },
                "main_armament_ammo_type": {
                    "align": "center",
                    "down": [
                        [
                            0.55,
                            0.073
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.55,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.61,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0422\u0418\u041f \u0410\u041c\u0423\u041d\u0418\u0426\u0418\u0418",
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
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
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
                            0.555,
                            0.185
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.555,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.635,
                            0.065
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
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
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
                    "text": "\u0413\u041e\u0422\u041e\u0412",
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
                    "text": "\u041a \u0421\u0422\u0420\u0415\u041b\u042c\u0411\u0415",
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
    "minomega": 60,
    "mintotaldamagethreshold": 0.005,
    "mintotaldamagetreshold": 0.4,
    "model": "rhsusf/addons/rhsusf_m113/m113a3_m240",
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
    "normalspeedforwardcoef": 0.82,
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
    "peaktorque": 770,
    "picture": "rhsusf/addons/rhsusf_m113/UI/M113A3_M240_ca",
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
    "radartype": 0,
    "redrpm": 2500,
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
            "hitpoint": "l svetlo",
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
            "hitpoint": "p svetlo",
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
    "reversed": 1,
    "rhs_fuelcapacity": 360,
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
    "selectionfireanim": "zasleh",
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
    "shownvggunner": 1,
    "side": 1,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.65,
    "smokelauncherangle": 90,
    "smokelaunchergrenadecount": 4,
    "smokelauncheronturret": 0,
    "smokelaunchervelocity": 14,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.166,
        "ArmorCrash1",
        0.166,
        "ArmorCrash2",
        0.166,
        "ArmorCrash3",
        0.166,
        "ArmorCrash4",
        0.166,
        "ArmorCrash5",
        0.166
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
        0.166,
        "buildCrash1",
        0.166,
        "buildCrash2",
        0.166,
        "buildCrash3",
        0.166,
        "buildCrash4",
        0.166,
        "buildCrash5",
        0.166
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
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Ext_Stop",
        1.99526,
        1,
        70
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Int_Stop",
        0.707946,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Ext_Start",
        1.99526,
        1,
        70
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Int_Start",
        0.501187,
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
        "A3/Sounds_F_EPB/Tracked/noises/get_in_out",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F_EPB/Tracked/noises/get_in_out",
        0.562341,
        1,
        20
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_4",
        0.398107,
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
        "soundsetsext": [
            "APC_Tracked_02_Engine_RPM0_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM1_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM2_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM3_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM4_EXT_SoundSet",
            "APC_Tracked_02_Tracks_01_EXT_SoundSet",
            "APC_Tracked_02_Tracks_02_EXT_SoundSet",
            "APC_Tracked_02_Tracks_03_EXT_SoundSet",
            "APC_Tracked_02_Tracks_04_EXT_SoundSet",
            "APC_Tracked_02_Tracks_05_EXT_SoundSet",
            "APC_Tracked_02_Tracks_06_EXT_SoundSet",
            "APC_Tracked_02_Rattling_EXT_SoundSet",
            "APC_Tracked_02_Rain_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Hard_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Soft_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Hard_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Soft_EXT_SoundSet",
            "APC_Tracked_02_Drive_Water_EXT_SoundSet",
            "APC_Tracked_02_Drive_Dirt_EXT_SoundSet",
            "Tracks_Movement_Dirt_Ext_01_SoundSet",
            "Tracks_Surface_Soft_Ext_SoundSet",
            "Tracks_Surface_Sand_Ext_SoundSet",
            "Tracks_Surface_Squeaks_Soft_Ext_SoundSet",
            "Tracks_Surface_Squeaks_Hard_Ext_SoundSet"
        ],
        "soundsetsint": [
            "APC_Tracked_02_Engine_RPM0_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM1_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM2_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM3_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM4_INT_SoundSet",
            "APC_Tracked_02_Tracks_01_INT_SoundSet",
            "APC_Tracked_02_Tracks_02_INT_SoundSet",
            "APC_Tracked_02_Tracks_03_INT_SoundSet",
            "APC_Tracked_02_Tracks_04_INT_SoundSet",
            "APC_Tracked_02_Tracks_05_INT_SoundSet",
            "APC_Tracked_02_Tracks_06_INT_SoundSet",
            "APC_Tracked_02_Interior_Tone_Engine_Off_SoundSet",
            "APC_Tracked_02_Interior_Tone_Engine_On_SoundSet",
            "APC_Tracked_02_Rattling_INT_SoundSet",
            "APC_Tracked_02_Stress_INT_SoundSet",
            "APC_Tracked_02_Rain_INT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Hard_INT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Soft_INT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Hard_INT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Soft_INT_SoundSet",
            "APC_Tracked_02_Drive_Water_INT_SoundSet",
            "APC_Tracked_02_Drive_Dirt_INT_SoundSet",
            "Tracks_Movement_Dirt_Int_01_SoundSet",
            "Tracks_Surface_Soft_Int_SoundSet",
            "Tracks_Surface_Sand_Int_SoundSet",
            "Tracks_Surface_Squeaks_Soft_Int_SoundSet",
            "Tracks_Surface_Squeaks_Hard_Int_SoundSet",
            "Tanks_Material_Strain_Int_SoundSet"
        ]
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
    "tankturnforce": 400000,
    "tankturnforceangminspd": 0.5,
    "tankturnforceangspd": 0.72,
    "tbody": 250,
    "textplural": "APCs",
    "textsingular": "APC",
    "texturelist": [],
    "texturesources": {
        "desert": {
            "author": "Red Hammer Studios",
            "displayname": "Desert",
            "factions": [
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_d_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_d_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_d_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_d_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m23_pintle_d_co.paa"
            ]
        },
        "olive": {
            "author": "Red Hammer Studios",
            "displayname": "Olive",
            "factions": [
                "rhs_faction_usarmy_wd"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_od_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_od_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_wd_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_wd_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m23_pintle_wd_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Woodland",
            "factions": [
                "rhs_faction_usarmy_wd"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_01_wd_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_02_wd_l_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_03_wd_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m113a3_int03_wd_co.paa",
                "rhsusf/addons/rhsusf_m113/data_new/m23_pintle_wd_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "threat": [
        0.8,
        0.6,
        0.6
    ],
    "thrustdelay": 0.3,
    "torquecurve": [
        [
            0.22,
            0.584416
        ],
        [
            0.4,
            0.646753
        ],
        [
            0.5,
            0.824675
        ],
        [
            0.6,
            0.968831
        ],
        [
            0.72,
            1
        ],
        [
            0.8,
            0.964935
        ],
        [
            0.9,
            0.924675
        ],
        [
            1.1056,
            0
        ]
    ],
    "tracksspeed": 1.35,
    "transmissionlosses": 15,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 4
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
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 50,
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
        "_xx_rhs_mag_m433_hedp": {
            "count": 20,
            "magazine": "rhs_mag_M433_HEDP"
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
        }
    },
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 9,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_m4_carryhandle": {
            "count": 4,
            "weapon": "rhs_weap_m4_carryhandle"
        }
    },
    "turncoef": 5,
    "turrets": {
        "cargoturret_01": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "",
            "animationsourcehatch": "rear_hatch_handler_1",
            "armorlights": 0.4,
            "body": "",
            "caneject": 1,
            "canhidegunner": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 0,
            "enabledbyanimationsource": "rear_hatch",
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
            "gunneraction": "vehicle_turnout_1",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "Ramp",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInMantis",
            "gunnergetoutaction": "GetOutMantis",
            "gunnerinaction": "RHS_M113_Cargo01_FFV",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Rear Hatch Right)",
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
            "lodturnedin": 1200,
            "lodturnedout": 1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 160,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo 1",
            "memorypointsgetingunnerdir": "pos cargo 1 dir",
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
            "minelev": -20,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -120,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 3,
            "proxytype": "CPCargo",
            "reflectors": {},
            "rhs_hatch_control": 1,
            "rhs_hatch_control_depeneds": [
                "rear_hatch_handler_2"
            ],
            "selectionfireanim": "",
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
                "limitsarraybottom": [
                    [
                        -1,
                        -1
                    ],
                    [
                        -1,
                        1
                    ]
                ],
                "limitsarraytop": [
                    [
                        1,
                        -1
                    ],
                    [
                        1,
                        1
                    ]
                ]
            },
            "turnout": {
                "limitsarraybottom": [
                    [
                        -7.4646,
                        -161.174
                    ],
                    [
                        -7.4264,
                        -106.981
                    ],
                    [
                        -12.8388,
                        -102.043
                    ],
                    [
                        -10.6611,
                        -88.8004
                    ],
                    [
                        -18.2532,
                        -59.667
                    ],
                    [
                        -7.4306,
                        -49.4319
                    ],
                    [
                        -11.1057,
                        -49.3832
                    ],
                    [
                        -7.7205,
                        -46.9855
                    ],
                    [
                        -10.1225,
                        -44.3478
                    ],
                    [
                        -19.7726,
                        -28.4836
                    ],
                    [
                        -16.0375,
                        17.8663
                    ],
                    [
                        -11.9149,
                        29.7774
                    ],
                    [
                        -7.7212,
                        38.3127
                    ],
                    [
                        -4.4575,
                        39.3049
                    ],
                    [
                        -5.2729,
                        43.6182
                    ],
                    [
                        -1.9005,
                        48.6889
                    ],
                    [
                        -4.8722,
                        73.8609
                    ],
                    [
                        -3.9671,
                        78.4205
                    ],
                    [
                        6.3736,
                        79.8659
                    ],
                    [
                        15.175,
                        91.7335
                    ],
                    [
                        30.0065,
                        113.787
                    ],
                    [
                        26.6582,
                        129.369
                    ],
                    [
                        3.4023,
                        135.919
                    ],
                    [
                        -15.3679,
                        144.278
                    ],
                    [
                        -16.1314,
                        160.087
                    ]
                ],
                "limitsarraytop": [
                    [
                        45,
                        -160
                    ],
                    [
                        45,
                        160
                    ]
                ]
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
            "weapons": [
                "rhsusf_weap_DummyLauncher"
            ]
        },
        "cargoturret_02": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "",
            "animationsourcehatch": "rear_hatch_handler_2",
            "armorlights": 0.4,
            "body": "",
            "caneject": 1,
            "canhidegunner": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 0,
            "enabledbyanimationsource": "rear_hatch",
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
            "gunneraction": "vehicle_turnout_1",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "Ramp",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInMantis",
            "gunnergetoutaction": "GetOutMantis",
            "gunnerinaction": "RHS_M113_Cargo02_FFV",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Rear Hatch Left)",
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
            "lodturnedin": 1200,
            "lodturnedout": 1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 160,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
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
            "minelev": -20,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -120,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 7,
            "proxytype": "CPCargo",
            "reflectors": {},
            "rhs_hatch_control": 1,
            "rhs_hatch_control_depeneds": [
                "rear_hatch_handler_1"
            ],
            "selectionfireanim": "",
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
                "limitsarraybottom": [
                    [
                        -1,
                        -1
                    ],
                    [
                        -1,
                        1
                    ]
                ],
                "limitsarraytop": [
                    [
                        1,
                        -1
                    ],
                    [
                        1,
                        1
                    ]
                ]
            },
            "turnout": {
                "limitsarraybottom": [
                    [
                        -15.0098,
                        -171.623
                    ],
                    [
                        -16.6821,
                        -154.958
                    ],
                    [
                        -11.7215,
                        -148.149
                    ],
                    [
                        -9.7461,
                        -147.78
                    ],
                    [
                        -9.8556,
                        -146.773
                    ],
                    [
                        -11.4685,
                        -146.32
                    ],
                    [
                        -11.573,
                        -145.918
                    ],
                    [
                        -16.224,
                        -137.448
                    ],
                    [
                        -11.0125,
                        -100.247
                    ],
                    [
                        9.7255,
                        -98.4888
                    ],
                    [
                        18.6911,
                        -96.8685
                    ],
                    [
                        -9.7613,
                        -96.5088
                    ],
                    [
                        23.9199,
                        -91.8655
                    ],
                    [
                        27.0373,
                        -83.6022
                    ],
                    [
                        27.0452,
                        -68.9423
                    ],
                    [
                        21.0796,
                        -57.9417
                    ],
                    [
                        19.9345,
                        -56.8518
                    ],
                    [
                        12.8666,
                        -54.0844
                    ],
                    [
                        -2.7019,
                        -45.4012
                    ],
                    [
                        -2.7096,
                        -44.2127
                    ],
                    [
                        -0.2736,
                        -43.947
                    ],
                    [
                        0.1972,
                        -38.4689
                    ],
                    [
                        -1.9929,
                        -37.4971
                    ],
                    [
                        -2.2836,
                        -35.1064
                    ],
                    [
                        -0.0074,
                        -34.8379
                    ],
                    [
                        -0.0715,
                        -32.4873
                    ],
                    [
                        -2.0306,
                        -31.7878
                    ],
                    [
                        -5.3829,
                        -23.1603
                    ],
                    [
                        0.1307,
                        -21.0844
                    ],
                    [
                        -8.0524,
                        -10.9118
                    ],
                    [
                        -19.3082,
                        20.7243
                    ],
                    [
                        -18.4856,
                        31.6046
                    ],
                    [
                        -12.0216,
                        43.6287
                    ],
                    [
                        -8.3882,
                        45.7286
                    ],
                    [
                        -19.8808,
                        58.2848
                    ],
                    [
                        -18.524,
                        94.6759
                    ],
                    [
                        -14.4017,
                        104.768
                    ],
                    [
                        -11.3235,
                        106.299
                    ],
                    [
                        -12.9417,
                        112.353
                    ],
                    [
                        -14.7703,
                        127.591
                    ],
                    [
                        -9.6985,
                        128.747
                    ],
                    [
                        -9.2638,
                        131.578
                    ],
                    [
                        -9.9322,
                        162.423
                    ],
                    [
                        -9.1396,
                        170.774
                    ]
                ],
                "limitsarraytop": [
                    [
                        45,
                        -120
                    ],
                    [
                        45,
                        160
                    ]
                ]
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
            "weapons": [
                "rhsusf_weap_DummyLauncher"
            ]
        },
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "",
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "armorlights": 0.4,
            "body": "mainTurret",
            "caneject": 1,
            "canhidegunner": 0,
            "canusescanners": 0,
            "castgunnershadow": 1,
            "commanderoptics": {},
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
            "disablesoundattenuation": 1,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                700,
                800,
                900,
                1000,
                1100,
                1200,
                1300,
                1400,
                1500
            ],
            "discretedistanceinitindex": 2,
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
            "gunneraction": "RHS_M113_Gunner_M240",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "ramp",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_M113_Gunner_M240",
            "gunnerlefthandanimname": "OtocHlaven_Shake",
            "gunnerleftleganimname": "",
            "gunnername": "Commander",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [
                "TankGunnerOptics2",
                "OpticsBlur1",
                "OpticsCHAbera1"
            ],
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
            "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
            "gunneroutopticsshowcursor": 0,
            "gunnerrighthandanimname": "OtocHlaven_Shake",
            "gunnerrightleganimname": "",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.6,
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.25,
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
            "ispersonturret": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhs_mag_762x51_M240_200",
                "rhsusf_mag_L8A3_8",
                "rhsusf_mag_L8A3_8",
                "rhsusf_mag_L8A3_8"
            ],
            "maxcamelev": 90,
            "maxelev": 60,
            "maxhorizontalrotspeed": 1.04,
            "maxoutelev": 40,
            "maxoutturn": 150,
            "maxturn": 360,
            "maxverticalrotspeed": 1.04,
            "memorypointgun": [
                "usti hlavne"
            ],
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "gunnerview",
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
            "minelev": -10,
            "minoutelev": -20,
            "minoutturn": -120,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "viewoptics": {
                    "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.75,
                    "maxanglex": 45,
                    "maxangley": 100,
                    "maxfov": 0.75,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -45,
                    "minangley": -100,
                    "minfov": 0.375,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": []
                }
            },
            "outgunnermayfire": 1,
            "personturretaction": "vehicle_turnout_2",
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
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
                        "hardlimitend": 1.5,
                        "hardlimitstart": 0.4,
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
                    "intensity": 4,
                    "outerangle": 175,
                    "position": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "size": 1,
                    "useflare": 0
                }
            },
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 2,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationGunner",
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
            "soundservovertical": [
                "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_gunner_vertical",
                0.562341,
                1,
                30
            ],
            "stabilizedinaxes": 0,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 45,
                "maxangley": 100,
                "maxfov": 0.75,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -45,
                "minangley": -100,
                "minfov": 0.375,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "thermalmode": [
                    0,
                    1
                ],
                "visionmode": []
            },
            "viewgunnerinexternal": 1,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.375,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.375,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.375,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "thermalmode": [
                    0,
                    1
                ],
                "visionmode": [
                    "Normal"
                ]
            },
            "weapons": [
                "rhs_weap_m240_m113",
                "rhsusf_weap_M259"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoTank",
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
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight"
        }
    },
    "vehicleclass": "rhs_vehclass_apc",
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
        "initfov": 0.75,
        "maxanglex": 35,
        "maxangley": 90,
        "maxfov": 1.25,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -45,
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
    "waterangulardampingcoef": 1.2,
    "waterdamageengine": 0.9,
    "watereffectspeed": 5,
    "waterfasteffectspeed": 28,
    "waterleakiness": 250,
    "waterlineardampingcoefx": 2,
    "waterlineardampingcoefy": 2,
    "waterppinvehicle": 0,
    "waterresistance": 1,
    "waterresistancecoef": 0.475,
    "weapons": [
        "rhs_weap_smokegen"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.375,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.22,
            "side": "left",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 700,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 700,
            "frictionvsslipgraph": [
                [
                    0,
                    0.4
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.75
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 25000,
            "mass": 100,
            "maxbraketorque": 3000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.22,
            "side": "right",
            "springdamperrate": 7458,
            "springstrength": 163500,
            "sprungmass": 1250,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.36
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "woodcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "woodcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "woodcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
        1,
        200
    ],
    "woodcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "woodcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ]
}