d = {
    "_generalmacro": "UGV_02_Base_F",
    "accelaidforcecoef": 0.7,
    "accelaidforcespd": 0.1,
    "accelaidforceyoffset": -0.8,
    "access": 0,
    "accuracy": 0.25,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 40,
    "aggregatereflectors": [
        [
            "Light_1",
            "Light_2"
        ],
        [
            "Light_3",
            "Light_4"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "antenna_1_hide": {
            "animperiod": 0.01,
            "initphase": 0,
            "source": "user"
        },
        "arm_forward": {
            "animperiod": 5,
            "initphase": 0,
            "source": "user"
        },
        "arm_reload": {
            "source": "reload",
            "weapon": "ProbingWeapon_02_F"
        },
        "beam_ammo": {
            "source": "ammo",
            "weapon": "ProbingWeapon_01_F"
        },
        "beam_length": {
            "animperiod": 0.01,
            "initphase": 100,
            "source": "user"
        },
        "beam_reload": {
            "source": "reload",
            "weapon": "ProbingWeapon_01_F"
        },
        "beam_reloadmagazine": {
            "source": "reloadMagazine",
            "weapon": "ProbingWeapon_01_F"
        },
        "biopsycapacity": {
            "animperiod": 0,
            "initphase": 0.4,
            "source": "user"
        },
        "chemdetectorlevel1": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "chemdetectorlevel2": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "chemdetectorlevel3": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "chemdetectorlight": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "demining_drone": {
            "animperiod": 0.01,
            "initphase": 0,
            "source": "user"
        },
        "detector1light1_green": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "detector1light1_red": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "detector1light2_green": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "detector1light2_red": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "detector2aux_hide": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "detector2speaker_off": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "detector2speaker_on": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "ew_drone": {
            "animperiod": 0.01,
            "initphase": 1,
            "source": "user"
        },
        "muzzleflash_rot": {
            "source": "ammorandom",
            "weapon": "DeminingDisruptor_01_F"
        },
        "science_drone": {
            "animperiod": 0.01,
            "initphase": 1,
            "source": "user"
        },
        "tracks_l_hit": {
            "hitpoint": "HitLTrack",
            "raw": 1,
            "source": "Hit"
        },
        "tracks_r_hit": {
            "hitpoint": "HitRTrack",
            "raw": 1,
            "source": "Hit"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 30,
    "armorcrash0": [
        "",
        0,
        1,
        25
    ],
    "armorcrash1": [
        "",
        0,
        1,
        25
    ],
    "armorcrash2": [
        "",
        0,
        1,
        25
    ],
    "armorcrash3": [
        "",
        0,
        1,
        25
    ],
    "armorcrash4": [
        "",
        0,
        1,
        25
    ],
    "armorcrash5": [
        "",
        0,
        1,
        25
    ],
    "armorcrash6": [
        "",
        0,
        1,
        25
    ],
    "armorcrash7": [
        "",
        0,
        1,
        25
    ],
    "armorlights": 0.4,
    "armorstructural": 20,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "OpenCarAttenuation",
    "attributes": {
        "lightcontrols": {},
        "platenumber": {
            "control": "EditShort",
            "defaultvalue": "getPlateNumber _this",
            "displayname": "Set plate number",
            "expression": "_this setPlateNumber format['%1',_value];",
            "property": "PlateNumber",
            "validate": "STRING"
        }
    },
    "audible": 0.1,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "BoundingEnd",
    "brakedistance": 5,
    "brakeidlespeed": 0.01,
    "buildcrash0": [
        "",
        0,
        1,
        25
    ],
    "buildcrash1": [
        "",
        0,
        1,
        25
    ],
    "buildcrash2": [
        "",
        0,
        1,
        25
    ],
    "buildcrash3": [
        "",
        0,
        1,
        25
    ],
    "buildcrash4": [
        "",
        0,
        1,
        25
    ],
    "buildcrash5": [
        "",
        0,
        1,
        25
    ],
    "buildcrash6": [
        "",
        0,
        1,
        25
    ],
    "buildcrash7": [
        "",
        0,
        1,
        25
    ],
    "bushcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_01",
        0.398107,
        1,
        25
    ],
    "bushcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_02",
        0.398107,
        1,
        25
    ],
    "bushcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.398107,
        1,
        25
    ],
    "bushcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.398107,
        0.8,
        25
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
    "camouflage": 0.5,
    "camshake": {
        "distance": 3,
        "frequency": 20,
        "minspeed": 5,
        "power": 0.1
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
    "cargoaction": [],
    "cargocancontroluav": 1,
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [],
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
    "cargoproxyindexes": [],
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
    "changegearomegaratios": [
        1,
        0.333333,
        0.333333,
        0,
        0.993333,
        0.333333
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 13,
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
    "complexgearbox": {
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -0.5,
            "N",
            0,
            "D1",
            1
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            1.3
        ]
    },
    "components": {
        "aitanksteeringcomponent": {
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "allowovertaking": 1,
            "allowturnaroundinpoint": 1,
            "commandturnfactor": 0.5,
            "convoypidweights": [
                1,
                0,
                0
            ],
            "differenceanglecoef": 0.7,
            "dopredictforward": 1,
            "doremapspeed": 1,
            "forwardanglecoef": 0.4,
            "maxwheelanglediff": 0.52616,
            "minspeedtokeep": 0.25,
            "predictforwardmaxspeed": 5,
            "predictforwardrange": [
                0.2,
                3.5
            ],
            "remapspeedrange": [
                15,
                125
            ],
            "remapspeedscalar": [
                13,
                0.35
            ],
            "speedpidweights": [
                0.7,
                0.3,
                0.16
            ],
            "speedpredictionmethod": 2,
            "steeraheadsaturation": [
                0.2,
                1.6
            ],
            "steeringanglecoef": 0.6,
            "steeringpidweights": [
                1.9,
                0.78,
                0.62
            ],
            "stuckmaxtime": 1,
            "wheelanglecoef": 0.8
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
    "cost": 20000,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crash0": [
        "",
        0,
        1,
        25
    ],
    "crash1": [
        "",
        0,
        1,
        25
    ],
    "crash2": [
        "",
        0,
        1,
        25
    ],
    "crash3": [
        "",
        0,
        1,
        25
    ],
    "crash4": [
        "",
        0,
        1,
        25
    ],
    "crash5": [
        "",
        0,
        1,
        25
    ],
    "crash6": [
        "",
        0,
        1,
        25
    ],
    "crash7": [
        "",
        0,
        1,
        25
    ],
    "crew": "Civilian",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 0,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "a3/Soft_F_Enoch/UGV_02/Data/UGV.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_damaged.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_destruct.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_aluminium.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_damaged.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_destruct.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_tracks.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_tracks_damaged.rvmat",
            "a3/Soft_F_Enoch/UGV_02/Data/UGV_tracks_destruct.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00719,
    "damagetexdelay": 0,
    "dampersbumpcoef": 4.5,
    "dampingratefullthrottle": 1.4,
    "dampingratezerothrottleclutchdisengaged": 0.8,
    "dampingratezerothrottleclutchengaged": 40.2,
    "destrtype": "DestructEngine",
    "destructioneffects": {
        "ammoexplosioneffect": "",
        "effectradius": 1,
        "firesparksbig1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 8.8,
            "position": "",
            "simulation": "particles",
            "type": "FireSparks"
        },
        "ignorefuel": 1,
        "sparksbig1": {
            "intensity": 0,
            "interval": 1,
            "lifetime": 8,
            "position": "",
            "simulation": "particles",
            "type": "ObjectDestructionSparks"
        }
    },
    "detectskill": 20,
    "disableinventory": 1,
    "displayname": "Tank",
    "dlc": "Enoch",
    "driveoncomponent": [
        "Track_L",
        "Track_R",
        "Slide"
    ],
    "driveraction": "",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 1,
    "driverinaction": "",
    "driverlefthandanimname": "",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "a3/Weapons_F_Enoch/Reticle/Optics_Driver_UGV_02_F",
    "driverrighthandanimname": "",
    "driverrightleganimname": "",
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
                "LDirtEffects"
            ],
            "gdtbeach": [
                "LDustEffects",
                "LStonesEffects"
            ],
            "gdtcliff": [
                "LDustEffects"
            ],
            "gdtconcrete": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtdead": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtdesert": [
                "LDustEffects",
                "LStonesEffects"
            ],
            "gdtdesert1": [
                "LDustEffects",
                "LSandEffects",
                "LDirtEffects",
                "LStonesEffects"
            ],
            "gdtdesert2": [
                "LDustEffects",
                "LSandEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtdirt": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtfield": [
                "LDustEffects"
            ],
            "gdtforest": [
                "LDustEffects"
            ],
            "gdtgrassdry": [
                "LDustEffects",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtgrassshort": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtgrasstall": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtgrasswild": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
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
                "LDirtEffects"
            ],
            "gdtrubble": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtseabed": [
                "LDustEffects"
            ],
            "gdtseabeddeep": [
                "LDustEffects"
            ],
            "gdtsoil": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtstony": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonygreen": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonythistle": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisbeach": [
                "LDustEffects",
                "LStonesEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffects",
                "LDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffects",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffects"
            ],
            "gdtstratisthistles": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtthorn": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtvolcano": [
                "LDustEffects",
                "LStonesEffects"
            ],
            "gdtvolcanobeach": [
                "LDustEffects"
            ],
            "gdtweed1": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtweed2": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtwildfield": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
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
                "RDirtEffects"
            ],
            "gdtbeach": [
                "RDustEffects",
                "RStonesEffects"
            ],
            "gdtcliff": [
                "RDustEffects"
            ],
            "gdtconcrete": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtdead": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtdesert": [
                "RDustEffects",
                "RStonesEffects"
            ],
            "gdtdesert1": [
                "RDustEffects",
                "RSandEffects",
                "RDirtEffects",
                "RStonesEffects"
            ],
            "gdtdesert2": [
                "RDustEffects",
                "RSandEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtdirt": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtfield": [
                "RDustEffects"
            ],
            "gdtforest": [
                "RDustEffects"
            ],
            "gdtgrassdry": [
                "RDustEffects",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtgrassshort": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtgrasstall": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtgrasswild": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
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
                "RDirtEffects"
            ],
            "gdtrubble": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtseabed": [
                "RDustEffects"
            ],
            "gdtseabeddeep": [
                "RDustEffects"
            ],
            "gdtsoil": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtstony": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonygreen": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonythistle": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisbeach": [
                "RDustEffects",
                "RStonesEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffects",
                "RDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffects",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffects"
            ],
            "gdtstratisthistles": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtthorn": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtvolcano": [
                "RDustEffects",
                "RStonesEffects"
            ],
            "gdtvolcanobeach": [
                "RDustEffects"
            ],
            "gdtweed1": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtweed2": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtwildfield": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
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
    "editorsubcategory": "EdSubcat_Drones",
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
    "enginemoi": 2.35,
    "enginepower": 45,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "(_this # 0) spawn {_this disableAI 'lights'};",
        "killed": "_this # 0 setVehicleAmmoDef 0;_this # 0 setFuel 0;"
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust_dir",
            "effect": "ExhaustsEffectBig",
            "position": "exhaust"
        }
    },
    "explosioneffect": "",
    "explosionshielding": 0.1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        0.5,
        -2
    ],
    "faction": "Default",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "FDustEffects",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 2,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": -1,
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
    "getinaction": "GetInMedium",
    "getinoutonproxy": 0,
    "getinradius": 0,
    "getoutaction": "GetOutMedium",
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
        0.0075,
        0.005,
        0.0075
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
        "Camo_1",
        "Camo_2",
        "Camo_3"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "a3/soft_f_enoch/ugv_02/data/ugv_co.paa",
        "a3/soft_f_enoch/ugv_02/data/tracks_co.paa",
        "a3/soft_f_enoch/ugv_02/data/ugv2_mdf_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitbattery_l": {
            "armor": -15,
            "armorcomponent": "Hit_Battery_L",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "explo": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.9,
                    "position": "FX_Battery_L",
                    "simulation": "particles",
                    "type": "WinchDestructionSparks"
                },
                "explo2": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.9,
                    "position": "FX_Battery_L",
                    "simulation": "particles",
                    "type": "AvionicsSmoke"
                },
                "ignorefuel": 1,
                "sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "FX_Battery_L",
                    "simulation": "sound",
                    "type": "SparklesWreck2"
                }
            },
            "explosionshielding": 0.01,
            "name": "Hit_Battery_L",
            "passthrough": 0
        },
        "hitbattery_r": {
            "armor": -15,
            "armorcomponent": "Hit_Battery_R",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "explo": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.9,
                    "position": "FX_Battery_R",
                    "simulation": "particles",
                    "type": "WinchDestructionSparks"
                },
                "explo2": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.9,
                    "position": "FX_Battery_R",
                    "simulation": "particles",
                    "type": "AvionicsSmoke"
                },
                "ignorefuel": 1,
                "sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "FX_Battery_R",
                    "simulation": "sound",
                    "type": "SparklesWreck2"
                }
            },
            "explosionshielding": 0.01,
            "name": "Hit_Battery_R",
            "passthrough": 0
        },
        "hitengine": {
            "armor": -30,
            "armorcomponent": "Hit_Engine",
            "explosionshielding": 0.01,
            "name": "Hit_Engine",
            "passthrough": 0
        },
        "hitfuel": {
            "armor": -999,
            "depends": "(HitBattery_L+HitBattery_R)*0.5",
            "explosionshielding": 0.01,
            "name": "Hit_Batteries",
            "passthrough": 0
        },
        "hithull": {
            "armor": 999,
            "depends": "Total",
            "explosionshielding": 0.01,
            "name": "karoserie",
            "passthrough": 0,
            "visual": "zbytek"
        },
        "hitlightback": {
            "armor": -5,
            "explosionshielding": 0.01,
            "name": "Hit_LightFront",
            "passthrough": 0
        },
        "hitlightfront": {
            "armor": -5,
            "explosionshielding": 0.01,
            "name": "Hit_LightFront",
            "passthrough": 0
        },
        "hitltrack": {
            "armor": -15,
            "armorcomponent": "Track_L_Hide",
            "explosionshielding": 0.01,
            "name": "Hit_Track_L",
            "passthrough": 0
        },
        "hitrtrack": {
            "armor": -15,
            "armorcomponent": "Track_R_Hide",
            "explosionshielding": 0.01,
            "name": "Hit_Track_R",
            "passthrough": 0
        }
    },
    "htmax": 180,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "a3/Soft_F_Enoch/UGV_02/Data/UI/map_RCAV_CA.paa",
    "idlerpm": 100,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "",
    "incomingmissiledetectionsystem": 16,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.5,
    "irscanground": 2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 0.1,
    "isbackpack": 0,
    "isuav": 1,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 0.1,
    "laserscanner": 0,
    "lasertarget": 0,
    "latency": 1.3,
    "leftdusteffect": "LDustEffects",
    "leftdusteffects": [
        [
            "GdtGrassShort",
            "LDustEffects"
        ],
        [
            "GdtGrassShort",
            "LGrassEffects"
        ],
        [
            "GdtGrassTall",
            "LDustEffects"
        ],
        [
            "GdtGrassTall",
            "LGrassEffects"
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
            "LStonesEffects"
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
            "LDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "LDustEffects"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "LDustEffects"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffects"
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
            "LGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "LDustEffects"
        ],
        [
            "GdtStratisRocky",
            "LGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "LDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "LDustEffects"
        ],
        [
            "GdtStratisThistles",
            "LGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "LDirtEffects"
        ],
        [
            "GdtConcrete",
            "LDustEffects"
        ],
        [
            "GdtConcrete",
            "LDirtEffects"
        ],
        [
            "GdtAsphalt",
            "LDustEffects"
        ],
        [
            "GdtAsphalt",
            "LDirtEffects"
        ],
        [
            "GdtRubble",
            "LDustEffects"
        ],
        [
            "GdtRubble",
            "LDirtEffects"
        ],
        [
            "GdtSoil",
            "LDustEffects"
        ],
        [
            "GdtSoil",
            "LDirtEffects"
        ],
        [
            "GdtBeach",
            "LDustEffects"
        ],
        [
            "GdtBeach",
            "LStonesEffects"
        ],
        [
            "GdtRock",
            "LDustEffects"
        ],
        [
            "GdtRock",
            "LDirtEffects"
        ],
        [
            "GdtDead",
            "LDustEffects"
        ],
        [
            "GdtDead",
            "LDirtEffects"
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
            "LStonesEffects"
        ],
        [
            "GdtDesert1",
            "LDustEffects"
        ],
        [
            "GdtDesert1",
            "LSandEffects"
        ],
        [
            "GdtDesert1",
            "LDirtEffects"
        ],
        [
            "GdtDesert1",
            "LStonesEffects"
        ],
        [
            "GdtDesert2",
            "LDustEffects"
        ],
        [
            "GdtDesert2",
            "LSandEffects"
        ],
        [
            "GdtDesert2",
            "LGrassEffects"
        ],
        [
            "GdtDesert2",
            "LDirtEffects"
        ],
        [
            "GdtDirt",
            "LDustEffects"
        ],
        [
            "GdtDirt",
            "LDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "LDustEffects"
        ],
        [
            "GdtGrassGreen",
            "LGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "LDirtEffects"
        ],
        [
            "GdtGrassDry",
            "LDustEffects"
        ],
        [
            "GdtGrassDry",
            "LGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "LDirtEffects"
        ],
        [
            "GdtGrassWild",
            "LDustEffects"
        ],
        [
            "GdtGrassWild",
            "LGrassEffects"
        ],
        [
            "GdtGrassWild",
            "LDirtEffects"
        ],
        [
            "GdtWildField",
            "LDustEffects"
        ],
        [
            "GdtWildField",
            "LGrassEffects"
        ],
        [
            "GdtWildField",
            "LDirtEffects"
        ],
        [
            "GdtWeed1",
            "LDustEffects"
        ],
        [
            "GdtWeed1",
            "LGrassEffects"
        ],
        [
            "GdtWeed1",
            "LDirtEffects"
        ],
        [
            "GdtWeed2",
            "LDustEffects"
        ],
        [
            "GdtWeed2",
            "LGrassEffects"
        ],
        [
            "GdtWeed2",
            "LDirtEffects"
        ],
        [
            "GdtThorn",
            "LDustEffects"
        ],
        [
            "GdtThorn",
            "LGrassEffects"
        ],
        [
            "GdtThorn",
            "LDirtEffects"
        ],
        [
            "GdtStony",
            "LDustEffects"
        ],
        [
            "GdtStony",
            "LGrassEffects"
        ],
        [
            "GdtStony",
            "LDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "LDustEffects"
        ],
        [
            "GdtStonyGreen",
            "LGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "LDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "LDustEffects"
        ],
        [
            "GdtStonyThistle",
            "LGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "LDirtEffects"
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
            "LDustEffects"
        ]
    ],
    "leftfastwatereffect": "LWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "library": {
        "libtextdesc": "ED-1 is a commercial off-the-shelf series of robotic systems built upon a man-portable modular platform. The tracked mini UGV has convenient front and rear obstacle climbers that allow it to traverse relatively complex terrain. Standard lithium-ion batteries power the electric propulsion, and are placed to facilitate so-called 'hot swaps' in the field. Two primary uses in military remote operations are Explosive Ordnance Disposal and CBRN Defense. The former has an integrated mine detector and mounts a custom 12 gauge disruptor weapon on its swivel arm, intended to disable explosive devices. The latter is a literal driving laboratory, complete with a full suite of CBRN sensors, and a chemical compound sampling laser as well as telescopic biopsy probe on its arm."
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "magazines": [],
    "mapsize": 1.21,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 3,
    "maxgforce": 2,
    "maximumload": 0,
    "maxomega": 73.3038,
    "maxspeed": 15,
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
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
    "mfact": 0,
    "mfd": {},
    "mfmax": 5,
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
    "minomega": 10.472,
    "mintotaldamagethreshold": 0.005,
    "model": "a3/Soft_F_Enoch/UGV_02/UGV_02_F",
    "namesound": "veh_vehicle_UGV_s",
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
    "normalspeedforwardcoef": 0.45,
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
    "peaktorque": 1670,
    "picture": "a3/Soft_F_Enoch/UGV_02/Data/UI/UGV_02_EW_CA.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "plateinfos": {
        "color": [
            1,
            1,
            1,
            0.4
        ],
        "name": "PlateNumber",
        "platefont": "RobotoCondensedLight",
        "plateformat": "0##",
        "plateletters": "ABCDEFHIKLMOPRSTVXYZ"
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 0.65,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 0.1,
    "radartype": 0,
    "redrpm": 700,
    "reflectors": {
        "light_1": {
            "ambient": [
                1,
                1,
                1
            ],
            "attenuation": {
                "constant": 0.8,
                "hardlimitend": 1,
                "hardlimitstart": 0,
                "linear": 0.4,
                "quadratic": 1.3,
                "start": 0
            },
            "color": [
                1,
                1,
                1
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_1_dir",
            "hitpointclass": "HitLightFront",
            "innerangle": 5,
            "intensity": 743,
            "outerangle": 175,
            "position": "Light_1_pos",
            "selection": "Light_1",
            "size": 1,
            "useflare": 1
        },
        "light_2": {
            "ambient": [
                1,
                1,
                1
            ],
            "attenuation": {
                "constant": 0.8,
                "hardlimitend": 1,
                "hardlimitstart": 0,
                "linear": 0.4,
                "quadratic": 1.3,
                "start": 0
            },
            "color": [
                1,
                1,
                1
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_2_dir",
            "hitpointclass": "HitLightFront",
            "innerangle": 5,
            "intensity": 743,
            "outerangle": 175,
            "position": "Light_2_pos",
            "selection": "Light_2",
            "size": 1,
            "useflare": 1
        },
        "light_3": {
            "ambient": [
                1,
                1,
                1
            ],
            "attenuation": {
                "constant": 0.8,
                "hardlimitend": 1,
                "hardlimitstart": 0,
                "linear": 0.4,
                "quadratic": 1.3,
                "start": 0
            },
            "color": [
                1,
                1,
                1
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_3_dir",
            "hitpointclass": "HitLightBack",
            "innerangle": 5,
            "intensity": 743,
            "outerangle": 175,
            "position": "Light_3_pos",
            "selection": "Light_3",
            "size": 1,
            "useflare": 1
        },
        "light_4": {
            "ambient": [
                1,
                1,
                1
            ],
            "attenuation": {
                "constant": 0.8,
                "hardlimitend": 1,
                "hardlimitstart": 0,
                "linear": 0.4,
                "quadratic": 1.3,
                "start": 0
            },
            "color": [
                1,
                1,
                1
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_4_dir",
            "hitpointclass": "HitLightBack",
            "innerangle": 5,
            "intensity": 743,
            "outerangle": 175,
            "position": "Light_4_pos",
            "selection": "Light_4",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rightdusteffect": "RDustEffects",
    "rightdusteffects": [
        [
            "GdtGrassShort",
            "RDustEffects"
        ],
        [
            "GdtGrassShort",
            "RGrassEffects"
        ],
        [
            "GdtGrassTall",
            "RDustEffects"
        ],
        [
            "GdtGrassTall",
            "RGrassEffects"
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
            "RStonesEffects"
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
            "RDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "RDustEffects"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "RDustEffects"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffects"
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
            "RGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "RDustEffects"
        ],
        [
            "GdtStratisRocky",
            "RGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "RDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "RDustEffects"
        ],
        [
            "GdtStratisThistles",
            "RGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "RDirtEffects"
        ],
        [
            "GdtConcrete",
            "RDustEffects"
        ],
        [
            "GdtConcrete",
            "RDirtEffects"
        ],
        [
            "GdtAsphalt",
            "RDustEffects"
        ],
        [
            "GdtAsphalt",
            "RDirtEffects"
        ],
        [
            "GdtRubble",
            "RDustEffects"
        ],
        [
            "GdtRubble",
            "RDirtEffects"
        ],
        [
            "GdtSoil",
            "RDustEffects"
        ],
        [
            "GdtSoil",
            "RDirtEffects"
        ],
        [
            "GdtBeach",
            "RDustEffects"
        ],
        [
            "GdtBeach",
            "RStonesEffects"
        ],
        [
            "GdtRock",
            "RDustEffects"
        ],
        [
            "GdtRock",
            "RDirtEffects"
        ],
        [
            "GdtDead",
            "RDustEffects"
        ],
        [
            "GdtDead",
            "RDirtEffects"
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
            "RStonesEffects"
        ],
        [
            "GdtDesert1",
            "RDustEffects"
        ],
        [
            "GdtDesert1",
            "RSandEffects"
        ],
        [
            "GdtDesert1",
            "RDirtEffects"
        ],
        [
            "GdtDesert1",
            "RStonesEffects"
        ],
        [
            "GdtDesert2",
            "RDustEffects"
        ],
        [
            "GdtDesert2",
            "RSandEffects"
        ],
        [
            "GdtDesert2",
            "RGrassEffects"
        ],
        [
            "GdtDesert2",
            "RDirtEffects"
        ],
        [
            "GdtDirt",
            "RDustEffects"
        ],
        [
            "GdtDirt",
            "RDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "RDustEffects"
        ],
        [
            "GdtGrassGreen",
            "RGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "RDirtEffects"
        ],
        [
            "GdtGrassDry",
            "RDustEffects"
        ],
        [
            "GdtGrassDry",
            "RGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "RDirtEffects"
        ],
        [
            "GdtGrassWild",
            "RDustEffects"
        ],
        [
            "GdtGrassWild",
            "RGrassEffects"
        ],
        [
            "GdtGrassWild",
            "RDirtEffects"
        ],
        [
            "GdtWildField",
            "RDustEffects"
        ],
        [
            "GdtWildField",
            "RGrassEffects"
        ],
        [
            "GdtWildField",
            "RDirtEffects"
        ],
        [
            "GdtWeed1",
            "RDustEffects"
        ],
        [
            "GdtWeed1",
            "RGrassEffects"
        ],
        [
            "GdtWeed1",
            "RDirtEffects"
        ],
        [
            "GdtWeed2",
            "RDustEffects"
        ],
        [
            "GdtWeed2",
            "RGrassEffects"
        ],
        [
            "GdtWeed2",
            "RDirtEffects"
        ],
        [
            "GdtThorn",
            "RDustEffects"
        ],
        [
            "GdtThorn",
            "RGrassEffects"
        ],
        [
            "GdtThorn",
            "RDirtEffects"
        ],
        [
            "GdtStony",
            "RDustEffects"
        ],
        [
            "GdtStony",
            "RGrassEffects"
        ],
        [
            "GdtStony",
            "RDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "RDustEffects"
        ],
        [
            "GdtStonyGreen",
            "RGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "RDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "RDustEffects"
        ],
        [
            "GdtStonyThistle",
            "RGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "RDirtEffects"
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
    "scope": 0,
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
    "shownvggunner": 0,
    "side": 4,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [
        "SlingLoadCargo1_dir",
        "SlingLoadCargo2_dir",
        "SlingLoadCargo3_dir",
        "SlingLoadCargo4_dir"
    ],
    "slowspeedforwardcoef": 0.1,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.125,
        "ArmorCrash1",
        0.125,
        "ArmorCrash2",
        0.125,
        "ArmorCrash3",
        0.125,
        "ArmorCrash4",
        0.125,
        "ArmorCrash5",
        0.125,
        "ArmorCrash6",
        0.125,
        "ArmorCrash7",
        0.125
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
        0.125,
        "buildCrash1",
        0.125,
        "buildCrash2",
        0.125,
        "buildCrash3",
        0.125,
        "buildCrash4",
        0.125,
        "buildCrash5",
        0.125,
        "buildCrash6",
        0.125,
        "buildCrash7",
        0.125
    ],
    "soundburning": {},
    "soundbushcrash": [
        "BushCrash1",
        0.25,
        "BushCrash2",
        0.25,
        "BushCrash3",
        0.25,
        "BushCrash4",
        0.25
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "Crash0",
        0.125,
        "Crash1",
        0.125,
        "Crash2",
        0.125,
        "Crash3",
        0.125,
        "Crash4",
        0.125,
        "Crash5",
        0.125,
        "Crash6",
        0.125,
        "Crash7",
        0.125
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "",
        1,
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
        "",
        1,
        1,
        25
    ],
    "soundengineoffint": [
        "",
        0.562341,
        1
    ],
    "soundengineonext": [
        "",
        1,
        1,
        25
    ],
    "soundengineonint": [
        "",
        0.707946,
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
        "",
        0.000316228,
        1
    ],
    "soundgetout": [
        "",
        0.000316228,
        1
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_3",
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
        "",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "engine": {
            "frequency": "1.0 + thrust factor [0,1]",
            "sound": [
                "a3/Sounds_F/air/UAV_01/quad_engine_full_01",
                0.316228,
                1,
                40
            ],
            "volume": "thrust factor [0,1]"
        },
        "soundsets": [],
        "soundsetsext": [
            "Ugv_02_Arm_01_Mech_Up_Ext_SoundSet",
            "Ugv_02_Arm_01_Mech_Down_Ext_SoundSet",
            "Ugv_02_Arm_02_Mech_Up_Ext_SoundSet",
            "Ugv_02_Arm_02_Mech_Down_Ext_SoundSet",
            "Ugv_02_Arm_01_Up_Ext_SoundSet",
            "Ugv_02_Arm_01_Down_Ext_SoundSet",
            "Ugv_02_Arm_02_Ext_SoundSet",
            "ProbingWeapon_01_System_Start_SoundSet",
            "ProbingWeapon_01_System_End_SoundSet",
            "ProbingWeapon_01_System_Successful_SoundSet",
            "ProbingWeapon_01_System_Failed_SoundSet",
            "Ugv_02_Eng_01_SoundSet",
            "Ugv_02_Eng_Low_SoundSet",
            "Ugv_02_Eng_High_SoundSet",
            "Ugv_02_Movement_Dirt_Ext_01_SoundSet",
            "Ugv_02_Movement_Gravel_Ext_01_SoundSet",
            "Ugv_02_Movement_Grass_Ext_01_SoundSet",
            "Ugv_02_Movement_Water_Ext_01_SoundSet",
            "Ugv_02_Movement_Sand_Ext_01_SoundSet",
            "Van_02_Rain_01_Ext_SoundSet"
        ],
        "soundsetsint": [
            "Ugv_02_Arm_01_Up_Int_SoundSet",
            "Ugv_02_Arm_01_Down_Int_SoundSet",
            "Ugv_02_Arm_02_Int_SoundSet",
            "ProbingWeapon_01_System_Start_Int_SoundSet",
            "ProbingWeapon_01_System_End_Int_SoundSet",
            "ProbingWeapon_01_System_Successful_Int_SoundSet",
            "ProbingWeapon_01_System_Failed_Int_SoundSet",
            "Ugv_02_Eng_01_Int_SoundSet",
            "Ugv_02_Eng_Low_Int_SoundSet",
            "Ugv_02_Eng_High_Int_SoundSet",
            "Ugv_02_Movement_Dirt_Int_01_SoundSet",
            "Ugv_02_Movement_Gravel_Int_01_SoundSet",
            "Ugv_02_Movement_Grass_Int_01_SoundSet",
            "Ugv_02_Movement_Water_Int_01_SoundSet",
            "Ugv_02_Movement_Sand_Int_01_SoundSet",
            "Van_02_Rain_01_Int_SoundSet"
        ]
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundturnin": [
        "",
        0.000316228,
        1
    ],
    "soundturnininternal": [
        "",
        0.000316228,
        1
    ],
    "soundturnout": [
        "",
        0.000316228,
        1
    ],
    "soundturnoutinternal": [
        "",
        0.000316228,
        1
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
        0.125,
        "woodCrash1",
        0.125,
        "woodCrash2",
        0.125,
        "woodCrash3",
        0.125,
        "woodCrash4",
        0.125,
        "woodCrash5",
        0.125,
        "woodCrash6",
        0.125,
        "woodCrash7",
        0.125
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_vehicle_UGV_p"
            ],
            "speechsingular": [
                "veh_vehicle_UGV_s"
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
    "switchtime": 0,
    "tankturnforce": 0,
    "tankturnforceangminspd": 7.6,
    "tankturnforceangspd": 8,
    "tbody": 0,
    "textplural": "UGVs",
    "textsingular": "UGV",
    "texturetrackwheel": 0,
    "threat": [
        0.05,
        0,
        0
    ],
    "thrustdelay": 0,
    "torquecurve": [
        [
            0.166667,
            0.6
        ],
        [
            0.5,
            1
        ],
        [
            1,
            0.8
        ]
    ],
    "tracksspeed": -0.4,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {},
    "transportmagazines": {},
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 5,
    "turrets": {
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourceelevation": "Arm",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourceturret": "mainTurret",
            "armorlights": 0.4,
            "body": "MainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
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
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
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
            "elevationanimsourcespeed": 0.3,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "MainGun",
            "gunbeg": "PIP1_dir",
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
            "gunend": "PIP1_pos",
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
            "gunneraction": "ManActTestDriverOut",
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
            "gunneropticseffect": [
                "TankGunnerOptics2",
                "OpticsBlur1",
                "OpticsCHAbera1"
            ],
            "gunneropticsmodel": "A3/Weapons_F_beta/Binocular/lasermarker_optics",
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
                    "armor": -8,
                    "armorcomponent": "Hit_Gun",
                    "destructioneffects": {
                        "ammoexplosioneffect": "",
                        "effectradius": 1,
                        "explo": {
                            "intensity": 1,
                            "interval": 1,
                            "lifetime": 0.9,
                            "position": "FX_Gun",
                            "simulation": "particles",
                            "type": "AvionicsSparks"
                        },
                        "explo2": {
                            "intensity": 1,
                            "interval": 1,
                            "lifetime": 0.9,
                            "position": "FX_Gun",
                            "simulation": "particles",
                            "type": "AvionicsSmoke"
                        },
                        "ignorefuel": 1,
                        "sound": {
                            "intensity": 1,
                            "interval": 1,
                            "lifetime": 1,
                            "position": "FX_Gun",
                            "simulation": "sound",
                            "type": "SparklesWreck2"
                        }
                    },
                    "explosionshielding": 0.01,
                    "isgun": 1,
                    "name": "Hit_Gun",
                    "passthrough": 0,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": -8,
                    "armorcomponent": "Hit_Turret",
                    "explosionshielding": 0.01,
                    "isturret": 1,
                    "name": "Hit_Turret",
                    "passthrough": 0,
                    "visual": "-"
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
            "magazines": [
                "ProbingWeapon_01_magazine",
                "ProbingWeapon_02_magazine",
                "Laserbatteries"
            ],
            "maxcamelev": 90,
            "maxelev": 80,
            "maxhorizontalrotspeed": 2.4,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 75,
            "maxverticalrotspeed": 2.4,
            "memorypointgun": "PIP1_pos",
            "memorypointgunneroptics": "cam_arm",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -75,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "cameraarm": {
                    "campos": "cam_arm",
                    "gunneropticsmodel": "a3/Weapons_F_Enoch/Reticle/Optics_Gunner_UGV_02_cam3_F",
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
                    "opticsdisplayname": "cam1",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "thermalmode": [
                        2
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                },
                "cameraarmzoom": {
                    "campos": "cam_arm",
                    "gunneropticsmodel": "a3/Weapons_F_Enoch/Reticle/Optics_Gunner_UGV_02_cam3_zoom_F",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.0583333,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.0583333,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.0583333,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "cam1",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "thermalmode": [
                        2
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                },
                "camerabottom": {
                    "camdir": "driverview_dir",
                    "campos": "driverview",
                    "gunneropticsmodel": "a3/Weapons_F_Enoch/Reticle/Optics_Gunner_UGV_02_cam1_F",
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
                    "opticsdisplayname": "cam2",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "thermalmode": [
                        2
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                },
                "cameraclaw": {
                    "camdir": "cam_rear_dir",
                    "campos": "cam_rear",
                    "gunneropticsmodel": "a3/Weapons_F_Enoch/Reticle/Optics_Gunner_UGV_02_cam2_F",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.35,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.35,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.35,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "cam3",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "thermalmode": [
                        2
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                }
            },
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {
                "arm_lamp": {
                    "ambient": [
                        1,
                        1,
                        1
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 30.2,
                        "hardlimitstart": 2.7,
                        "linear": 0.0005,
                        "quadratic": 0,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        1,
                        1,
                        1
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "PiP1_dir",
                    "flaremaxdistance": 25,
                    "flaresize": 0.5,
                    "hitpoint": "cam_gunner",
                    "innerangle": 5,
                    "intensity": 743,
                    "outerangle": 25,
                    "position": "PiP1_pos",
                    "selection": "Light_Camera",
                    "size": 1,
                    "useflare": 0
                },
                "arm_lamp_flare": {
                    "ambient": [
                        1,
                        1,
                        1
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 0.0002,
                        "hardlimitstart": 0.0001,
                        "linear": 0.7,
                        "quadratic": 999,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        1,
                        1,
                        1
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "PiP1_dir",
                    "flaremaxdistance": 25,
                    "flaresize": 0.5,
                    "hitpoint": "cam_gunner",
                    "innerangle": 5,
                    "intensity": 55,
                    "outerangle": 175,
                    "position": "PiP1_pos",
                    "selection": "Light_Camera",
                    "size": 1,
                    "useflare": 1
                }
            },
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0,
                1,
                25
            ],
            "soundservo": [
                "A3/Sounds_F_Enoch/Assets/Vehicles/Ugv_02/Ugv_02_Servo_01",
                0.5,
                1,
                15
            ],
            "soundservovertical": [
                "A3/Sounds_F_Enoch/Assets/Vehicles/Ugv_02/Ugv_02_Servo_01",
                0.5,
                0.8,
                15
            ],
            "stabilizedinaxes": 1,
            "startengine": 1,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RscOptics_UGV_02_Tracked_gunner",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "uavcameragunnerdir": "PIP1_dir",
            "uavcameragunnerpos": "PIP1_pos",
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
                "gunneropticsmodel": "A3/Weapons_F_beta/Binocular/lasermarker_optics",
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.1242,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.1242,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.0125,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0,
                "thermalmode": [
                    2
                ],
                "visionmode": [
                    "Normal",
                    "NVG",
                    "TI"
                ]
            },
            "weapons": [
                "ProbingWeapon_01_F",
                "ProbingWeapon_02_F",
                "ProbingLaser_01_F"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavcameradriverdir": "driverview_dir",
    "uavcameradriverpos": "driverview",
    "uavcameragunnerdir": "PiP1_dir",
    "uavcameragunnerpos": "PiP1_pos",
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoTank",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "light_off": {
            "condition": "alive this AND {cameraon isEqualTo this} && {isLightOn cameraon}",
            "displayname": "Lights off",
            "displaynamedefault": "Lights off",
            "onlyforplayer": 1,
            "position": "",
            "radius": 0.7,
            "showwindow": 0,
            "statement": "this switchLight 'OFF';"
        },
        "light_on": {
            "condition": "alive this AND {cameraon isEqualTo this} && {!isLightOn cameraon}",
            "displayname": "Lights on",
            "displaynamedefault": "Lights on",
            "onlyforplayer": 1,
            "position": "",
            "radius": 0.7,
            "showwindow": 0,
            "statement": "this switchLight 'ON';"
        },
        "pressxtoflipthething": {
            "condition": "alive this AND {not canmove this} AND {(player distance this < 2)}",
            "displayname": "Unflip UGV",
            "displaynamedefault": "Unflip UGV",
            "onlyforplayer": 1,
            "position": "",
            "radius": 2.7,
            "statement": "this setposASL ((getposASLVisual this) vectorAdd [0,0,0.5]);this setVectorDirAndUp [vectorDir this,[0,0,1]]"
        }
    },
    "uvanimations": {
        "laserbeam": {
            "maxvalue": 1.6,
            "minvalue": 0,
            "offset0": [
                0,
                0
            ],
            "offset1": [
                1,
                0
            ],
            "section": "laserbeam_outter",
            "source": "time",
            "sourceaddress": "loop",
            "type": "translation"
        },
        "laserbeam2": {
            "maxvalue": 10.2,
            "minvalue": 0,
            "offset0": [
                0,
                0
            ],
            "offset1": [
                0,
                1
            ],
            "section": "laserbeam_outter",
            "source": "time",
            "sourceaddress": "loop",
            "type": "translation"
        }
    },
    "vehicleclass": "Autonomous",
    "vehiclehasturnout": 0,
    "vehicletransport": {
        "cargo": {
            "canbetransported": 1,
            "dimensions": [
                "BBox_1_1_pos",
                "BBox_1_2_pos"
            ],
            "parachuteclass": "B_Parachute_02_F",
            "parachuteheightlimit": 5
        }
    },
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
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
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
        "initfov": 0.7,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 0.7,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.7,
        "minmovex": -0.075,
        "minmovey": -0.075,
        "minmovez": -0.075,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualsize": 0.1,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 10,
    "waterresistancecoef": 0.3,
    "weapons": [],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 0.1,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "Wheel_1_1_Damper",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.15,
            "maxdroop": 0.03,
            "moi": 0.025,
            "side": "left",
            "springdamperrate": 342,
            "springstrength": 510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "l2": {
            "bonename": "",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "left",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "l3": {
            "bonename": "wheel_1_3_hide",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "left",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "l4": {
            "bonename": "",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "left",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "l5": {
            "bonename": "wheel_1_5_Damper",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.15,
            "maxdroop": 0.03,
            "moi": 0.025,
            "side": "left",
            "springdamperrate": 342,
            "springstrength": 510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "r1": {
            "bonename": "wheel_2_1_Damper",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.15,
            "maxdroop": 0.03,
            "moi": 0.025,
            "side": "right",
            "springdamperrate": 342,
            "springstrength": 510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "r2": {
            "bonename": "",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "right",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "r3": {
            "bonename": "",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "right",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "r4": {
            "bonename": "",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.001,
            "maxdroop": 0.001,
            "moi": 0.025,
            "side": "right",
            "springdamperrate": 642,
            "springstrength": 4510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.05
        },
        "r5": {
            "bonename": "wheel_2_5_Damper",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_center",
            "dampingrate": 2.4,
            "dampingratedestroyed": 4000,
            "dampingrateinair": 2.4,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.1,
                    2.5
                ],
                [
                    0.5,
                    4.5
                ]
            ],
            "latstiffx": 1.5,
            "latstiffy": 15,
            "longitudinalstiffnessperunitgravity": 70,
            "mass": 5,
            "maxbraketorque": 22,
            "maxcompression": 0.15,
            "maxdroop": 0.03,
            "moi": 0.025,
            "side": "right",
            "springdamperrate": 342,
            "springstrength": 510,
            "sprungmass": 38.75,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.05
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "",
        0,
        1,
        25
    ],
    "woodcrash1": [
        "",
        0,
        1,
        25
    ],
    "woodcrash2": [
        "",
        0,
        1,
        25
    ],
    "woodcrash3": [
        "",
        0,
        1,
        25
    ],
    "woodcrash4": [
        "",
        0,
        1,
        25
    ],
    "woodcrash5": [
        "",
        0,
        1,
        25
    ],
    "woodcrash6": [
        "",
        0,
        1,
        25
    ],
    "woodcrash7": [
        "",
        0,
        1,
        25
    ]
}