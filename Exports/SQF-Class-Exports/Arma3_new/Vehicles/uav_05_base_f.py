d = {
    "_generalmacro": "UAV",
    "acceleration": 200,
    "access": 0,
    "accuracy": 0.1,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "aileroncoef": [
        0,
        0.12,
        0.38,
        0.4,
        0.45,
        0.46,
        0.47,
        0.48,
        0.49,
        0.5,
        0.49,
        0.48,
        0.45
    ],
    "aileroncontrolssensitivitycoef": 3,
    "aileronsensitivity": 0.7,
    "airbrake": 1,
    "airbrakefrictioncoef": 2.2,
    "aircapacity": 10,
    "aircraftautomatedsystems": {
        "wingautounfoldspeed": 40,
        "wingfoldanimations": [
            "wing_fold_l",
            "wing_fold_l_arm",
            "wing_fold_cover_l_arm",
            "wing_fold_cover_l",
            "wing_fold_r",
            "wing_fold_r_arm",
            "wing_fold_cover_r_arm",
            "wing_fold_cover_r"
        ],
        "wingstatecontrol": 1,
        "wingstatefolded": 1,
        "wingstateunfolded": 0
    },
    "airfrictioncoefs0": [
        0,
        0,
        0
    ],
    "airfrictioncoefs1": [
        0.1,
        0.5,
        0.0055
    ],
    "airfrictioncoefs2": [
        0.001,
        0.005,
        5.6e-05
    ],
    "allowtablock": 1,
    "altfullforce": 4000,
    "altnoforce": 14000,
    "alwaystarget": 0,
    "angleofindicence": "-0.25*3.1415/180",
    "animated": 1,
    "animationlist": [],
    "animationsources": {
        "collisionlightred1_source": {
            "markerlight": "CollisionLightRed1",
            "source": "MarkerLight"
        },
        "collisionlightred_source": {
            "markerlight": "CollisionRed",
            "source": "MarkerLight"
        },
        "collisionlightwhite_source": {
            "markerlight": "CollisionWhite",
            "source": "MarkerLight"
        },
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        "gear_front_hook_down": {
            "animperiod": 2.5,
            "initphase": 0,
            "source": "user"
        },
        "tailhook": {
            "animperiod": 2.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_l_1": {
            "animperiod": 2.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_l_2": {
            "animperiod": 2.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_r_1": {
            "animperiod": 2.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_r_2": {
            "animperiod": 2.5,
            "initphase": 1,
            "source": "user"
        },
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        "wing_fold_cover_l": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_cover_l_arm": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_cover_r": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_cover_r_arm": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_l": {
            "animperiod": 4.5,
            "displayname": "Fold Wings",
            "forceanimate": [
                "wing_fold_l",
                1,
                "wing_fold_l_arm",
                1,
                "wing_fold_cover_l_arm",
                1,
                "wing_fold_cover_l",
                1,
                "wing_fold_r",
                1,
                "wing_fold_r_arm",
                1,
                "wing_fold_cover_r_arm",
                1,
                "wing_fold_cover_r",
                1
            ],
            "forceanimate2": [
                "wing_fold_l",
                0,
                "wing_fold_l_arm",
                0,
                "wing_fold_cover_l_arm",
                0,
                "wing_fold_cover_l",
                0,
                "wing_fold_r",
                0,
                "wing_fold_r_arm",
                0,
                "wing_fold_cover_r_arm",
                0,
                "wing_fold_cover_r",
                0
            ],
            "forceanimatephase": 1,
            "forceanimatephase2": 0,
            "initphase": 0,
            "mass": 0,
            "source": "user"
        },
        "wing_fold_l_arm": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_r": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_r_arm": {
            "animperiod": 4.5,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 50,
    "armorcrash0": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_1",
        1,
        1,
        900
    ],
    "armorcrash1": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_2",
        1,
        1,
        900
    ],
    "armorcrash2": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_3",
        1,
        1,
        900
    ],
    "armorcrash3": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_4",
        1,
        1,
        900
    ],
    "armorlights": 0.4,
    "armorstructural": 1,
    "armory": {
        "description": "The Sentinel [UCAV] is a fifth-generation, state of the line, twin-engine, all-weather tactical unmanned combat vehicle. The UAV was designed primarily as a stealth reconnaissance platform, but also has precision ground attack capabilities. This aircraft is fitted with required equipment for carrier operations."
    },
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "PlaneAttenuation",
    "audible": 1,
    "author": "Bravo Zero One Studios",
    "autocenter": 1,
    "availableforsupporttypes": [
        "CAS_Bombing"
    ],
    "brakedistance": 250,
    "buildcrash0": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_1",
        1,
        1,
        900
    ],
    "buildcrash1": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_2",
        1,
        1,
        900
    ],
    "buildcrash2": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_3",
        1,
        1,
        900
    ],
    "buildcrash3": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_4",
        1,
        1,
        900
    ],
    "cabinclosesound": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_UAV_05_cabine_close_ext",
        3.16228,
        1,
        40
    ],
    "cabinclosesoundinternal": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_UAV_05_cabine_close_int",
        10,
        1,
        40
    ],
    "cabinopening": 0,
    "cabinopensound": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_UAV_05_cabine_open_ext",
        3.16228,
        1,
        40
    ],
    "cabinopensoundinternal": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_UAV_05_cabine_open_int",
        10,
        1,
        40
    ],
    "camerasmoothspeed": 5,
    "camouflage": 150,
    "camshake": {
        "distance": 50,
        "frequency": 20,
        "minspeed": 200,
        "power": 50
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
        "frequency": 3,
        "minspeed": 1,
        "power": 0.2
    },
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment2"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInHigh"
    ],
    "cargogetoutaction": [
        "GetOutHigh"
    ],
    "cargoiscodriver": [
        0
    ],
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
    "carrieropscompatability": {
        "arresthookanimationlist": [
            "tailhook",
            "tailhook_door_l_1",
            "tailhook_door_l_1",
            "tailhook_door_r_1",
            "tailhook_door_r_1"
        ],
        "arresthookanimationstates": [
            0,
            0.53,
            1
        ],
        "arresthookmemorypoint": "pos_tailhook",
        "arrestmaxallowedspeed": 295,
        "arrestslowdownstep": 0.7,
        "arrestvelocityreduction": -12,
        "launchaccelerationstep": 0.001,
        "launchvelocity": 275,
        "launchvelocityincrease": 10
    },
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": 31,
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "activeradarsensorcomponent": {
                    "aimdown": 20,
                    "airtarget": {
                        "maxrange": 8000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 60,
                    "anglerangevertical": 60,
                    "animdirection": "",
                    "color": [
                        0,
                        1,
                        1,
                        1
                    ],
                    "componenttype": "ActiveRadarSensorComponent",
                    "groundnoisedistancecoef": 0.5,
                    "groundtarget": {
                        "maxrange": 6000,
                        "minrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxgroundnoisedistance": 200,
                    "maxspeedthreshold": 27.7778,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 20.8333,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 6000
                },
                "antiradiationsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 60,
                    "anglerangevertical": 180,
                    "animdirection": "",
                    "color": [
                        0.5,
                        1,
                        0.5,
                        0.5
                    ],
                    "componenttype": "PassiveRadarSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 100,
                    "maxtrackablespeed": 60,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 12000
                },
                "irsensorcomponent": {
                    "aimdown": -0.5,
                    "airtarget": {
                        "maxrange": 4000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 51,
                    "anglerangevertical": 37,
                    "animdirection": "mainGun",
                    "color": [
                        1,
                        0,
                        0,
                        1
                    ],
                    "componenttype": "IRSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 3000,
                        "minrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxfogseethrough": 0.995,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 50,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 4000
                },
                "lasersensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "animdirection": "",
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "componenttype": "LaserSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 0
                },
                "nvsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "animdirection": "",
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "componenttype": "NVSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 0
                },
                "passiveradarsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 0,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "animdirection": "",
                    "color": [
                        0.5,
                        1,
                        0.5,
                        0.5
                    ],
                    "componenttype": "PassiveRadarSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 12000
                },
                "visualsensorcomponent": {
                    "aimdown": -0.5,
                    "airtarget": {
                        "maxrange": 3500,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 51,
                    "anglerangevertical": 37,
                    "animdirection": "mainGun",
                    "color": [
                        1,
                        1,
                        0.5,
                        0.8
                    ],
                    "componenttype": "VisualSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 3000,
                        "minrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxfogseethrough": 0.94,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 50,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "nightrangecoef": 0,
                    "typerecognitiondistance": 3000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "transportpylonscomponent": {
            "bays": {
                "bayleft1": {
                    "autoclosewhenemptydelay": 2,
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0
                },
                "bayright1": {
                    "autoclosewhenemptydelay": 2,
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0
                }
            },
            "presets": {
                "at": {
                    "attachment": [
                        "PylonMissile_Missile_AGM_02_x2",
                        "PylonMissile_Missile_AGM_02_x2"
                    ],
                    "displayname": "CAS"
                },
                "default": {
                    "attachment": [
                        "PylonMissile_Bomb_GBU12_x1",
                        "PylonMissile_Bomb_GBU12_x1"
                    ],
                    "displayname": "Default"
                },
                "empty": {
                    "attachment": [],
                    "displayname": "Empty"
                }
            },
            "pylons": {
                "pylon1": {
                    "attachment": "PylonMissile_Bomb_GBU12_x1",
                    "bay": 2,
                    "hardpoints": [
                        "B_GBU12",
                        "B_AGM65_DUAL",
                        "B_HARM_INT",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1500,
                    "priority": 1,
                    "turret": [
                        0
                    ],
                    "uiposition": [
                        0.5,
                        0.25
                    ]
                },
                "pylon2": {
                    "attachment": "PylonMissile_Bomb_GBU12_x1",
                    "bay": 1,
                    "hardpoints": [
                        "B_GBU12",
                        "B_AGM65_DUAL",
                        "B_HARM_INT",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1500,
                    "mirroredmissilepos": 1,
                    "priority": 1,
                    "turret": [
                        0
                    ],
                    "uiposition": [
                        0.15,
                        0.25
                    ]
                }
            },
            "uipicture": "A3/Air_F_Jets/UAV_05/Data/UI/UAV_05_3DEN_CA.paa"
        },
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [
                        4000,
                        2000,
                        16000,
                        8000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclemissiledisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Missile"
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
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [
                        4000,
                        2000,
                        16000,
                        8000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclemissiledisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Missile"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "SensorDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 2000000.0,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crash0": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_1",
        1,
        1,
        900
    ],
    "crash1": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_2",
        1,
        1,
        900
    ],
    "crash2": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_3",
        1,
        1,
        900
    ],
    "crash3": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_default_ext_4",
        1,
        1,
        900
    ],
    "crew": "B_UAV_AI",
    "crewcrashprotection": 0.15,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01.rvmat",
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01_damage.rvmat",
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01_destruct.rvmat",
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02.rvmat",
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02_damage.rvmat",
            "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02_destruct.rvmat"
        ],
        "tex": [
            "A3/Air_F_Jets/UAV_05/Data/uav05_engine_fire_ca.paa",
            "A3/Air_F_Jets/UAV_05/Data/uav05_engine_fire_ca.paa",
            "A3/Data_F/clear_empty.paa"
        ]
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "damperdamping": 0,
    "damperforce": 0.01,
    "dampersize": 0.01,
    "destrtype": "DestructDefault",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "UCAV Sentinel",
    "dlc": "Jets",
    "draconicforcexcoef": 9.5,
    "draconicforceycoef": 0.9,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [
        8,
        8.3,
        8.6,
        8.9,
        9.3,
        9.7,
        10.1,
        10.6,
        11.1,
        11.6,
        12,
        12.4,
        12.8
    ],
    "draconictorqueycoef": [
        14,
        9,
        2,
        0.1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "driveoncomponent": [],
    "driveraction": "",
    "drivercaneject": 1,
    "drivercansee": "31+32",
    "drivercompartments": "Compartment3",
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
    "driveropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UGV_01_Optics_Driver_F.p3d",
    "driverrighthandanimname": "",
    "driverrightleganimname": "",
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dusteffect": "HeliDust",
    "dusteffects": {
        "both": {},
        "left": {
            "default": [
                "LDustEffectsAir"
            ],
            "gdtasphalt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtcliff": [
                "LDustEffectsAir"
            ],
            "gdtconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdead": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdesert1": [
                "LDustEffectsAir",
                "LSandEffects",
                "LDirtEffects",
                "LStonesEffects"
            ],
            "gdtdesert2": [
                "LDustEffectsAir",
                "LSandEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtfield": [
                "LDustEffectsAir"
            ],
            "gdtforest": [
                "LDustEffectsAir"
            ],
            "gdtgrassdry": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtgrassshort": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasstall": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasswild": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtkldirt": [
                "LDustEffectsAir"
            ],
            "gdtklforestcon": [
                "LDustEffectsAir"
            ],
            "gdtklforestdec": [
                "LDustEffectsAir"
            ],
            "gdtklgrass1": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklgrass2": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklmud": [
                "LDustEffectsAir"
            ],
            "gdtklsoil": [
                "LDustEffectsAir"
            ],
            "gdtklstones": [
                "LDustEffectsAir"
            ],
            "gdtklstubble": [
                "LDustEffectsAir"
            ],
            "gdtkltarmac": [
                "LDustEffectsAir"
            ],
            "gdtreddirt": [
                "LDustEffectsAirRed"
            ],
            "gdtrock": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtrubble": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtseabed": [
                "LDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "LDustEffectsAir"
            ],
            "gdtsoil": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstony": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonygreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonythistle": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtthorn": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtvolcano": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtvolcanobeach": [
                "LDustEffectsAir"
            ],
            "gdtweed1": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtweed2": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtwildfield": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "surfintconcrete": [
                "LDustEffectsAir"
            ],
            "surfintmetal": [
                "LDustEffectsAir"
            ],
            "surfinttiles": [
                "LDustEffectsAir"
            ],
            "surfintwood": [
                "LDustEffectsAir"
            ],
            "surfmetal": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "LDustEffectsAir"
            ],
            "surfroaddirt": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "LDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "LDustEffectsAir"
            ],
            "surfrooftiles": [
                "LDustEffectsAir"
            ],
            "surfrooftin": [
                "LDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfwood": [
                "LDustEffectsAir"
            ]
        },
        "right": {
            "default": [
                "RDustEffectsAir"
            ],
            "gdtasphalt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtcliff": [
                "RDustEffectsAir"
            ],
            "gdtconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdead": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdesert1": [
                "RDustEffectsAir",
                "RSandEffects",
                "RDirtEffects",
                "RStonesEffects"
            ],
            "gdtdesert2": [
                "RDustEffectsAir",
                "RSandEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtfield": [
                "RDustEffectsAir"
            ],
            "gdtforest": [
                "RDustEffectsAir"
            ],
            "gdtgrassdry": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtgrassshort": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasstall": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasswild": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtkldirt": [
                "RDustEffectsAir"
            ],
            "gdtklforestcon": [
                "RDustEffectsAir"
            ],
            "gdtklforestdec": [
                "RDustEffectsAir"
            ],
            "gdtklgrass1": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklgrass2": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklmud": [
                "RDustEffectsAir"
            ],
            "gdtklsoil": [
                "RDustEffectsAir"
            ],
            "gdtklstones": [
                "RDustEffectsAir"
            ],
            "gdtklstubble": [
                "RDustEffectsAir"
            ],
            "gdtkltarmac": [
                "RDustEffectsAir"
            ],
            "gdtreddirt": [
                "RDustEffectsAirRed"
            ],
            "gdtrock": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtrubble": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtseabed": [
                "RDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "RDustEffectsAir"
            ],
            "gdtsoil": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstony": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonygreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonythistle": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtthorn": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtvolcano": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtvolcanobeach": [
                "RDustEffectsAir"
            ],
            "gdtweed1": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtweed2": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtwildfield": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "surfintconcrete": [
                "RDustEffectsAir"
            ],
            "surfintmetal": [
                "RDustEffectsAir"
            ],
            "surfinttiles": [
                "RDustEffectsAir"
            ],
            "surfintwood": [
                "RDustEffectsAir"
            ],
            "surfmetal": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "RDustEffectsAir"
            ],
            "surfroaddirt": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "RDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "RDustEffectsAir"
            ],
            "surfrooftiles": [
                "RDustEffectsAir"
            ],
            "surfrooftin": [
                "RDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfwood": [
                "RDustEffectsAir"
            ]
        }
    },
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "A3/EditorPreviews_F_Jets/Data/Cfgvehicles/B_UAV_05_F.jpg",
    "editorsubcategory": "EdSubcat_Drones",
    "ejectdamagelimit": 0.45,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "ejectspeed": [
        0,
        40,
        0
    ],
    "elevatorcoef": [
        0,
        0.36,
        1.44,
        0.65,
        0.5,
        0.45,
        0.4,
        0.35,
        0.3,
        0.26,
        0.22,
        0.19,
        0.13
    ],
    "elevatorcontrolssensitivitycoef": 3,
    "elevatorsensitivity": 0.6,
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
    "envelope": [
        0,
        0.28,
        1.04,
        2.16,
        3.2,
        4,
        4.32,
        5.12,
        5.49,
        5.88,
        6
    ],
    "epeimpulsedamagecoef": 120,
    "eventhandlers": {
        "engine": "_this call bis_fnc_aircraftFoldingWings",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "gear": "_this call bis_fnc_aircraftFoldingWings",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "landing": "[_this,true] call bis_fnc_aircraftTailhookAi",
        "landingcanceled": "[_this,false] call bis_fnc_aircraftTailhookAi"
    },
    "exhausts": {
        "exhaust1": {
            "direction": "pos_exhaust1_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0,
            "position": "pos_exhaust1"
        },
        "exhaust2": {
            "direction": "pos_exhaust2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1,
            "position": "pos_exhaust2"
        }
    },
    "explosionshielding": 2,
    "extcameraparams": [
        0.5,
        10,
        50,
        0.5,
        1,
        10,
        30,
        0,
        1
    ],
    "extcameraposition": [
        0,
        3,
        -30
    ],
    "faction": "BLU_F",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flaps": 1,
    "flapsfrictioncoef": 0.15,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 30,
    "formationz": 30,
    "fuelcapacity": 1000,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 10,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 5,
    "gearretracting": 1,
    "gearsupfrictioncoef": 0.8,
    "gearuptime": 5,
    "getinaction": "GetInHigh",
    "getinoutonproxy": 0,
    "getinradius": 0,
    "getoutaction": "GetOutHigh",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunaimdown": 0,
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
    "gunnercansee": "31+32",
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "gunnerhasflares": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.005,
        0.001,
        0.025
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
        "Camo1",
        "Camo2",
        "Camo_engine_fire"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01_co.paa",
        "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02_co.paa",
        "A3/Air_F_Jets/UAV_05/Data/UAV05_engine_fire_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitammo": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0.02,
            "name": "HitAmmo",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "HitAmmo_visual"
        },
        "hitavionics": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0.02,
            "name": "HitAvionics",
            "passthrough": 0.2,
            "radius": 0.2,
            "visual": "HitAvionics_visual"
        },
        "hitengine": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitEngine",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "HitEngineL_visual"
        },
        "hitengine2": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitEngine2",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "HitEngineR_visual"
        },
        "hitfuel": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitFuel",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "HitHull_visual"
        },
        "hitfuel2": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitFuel2",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "HitHull_visual"
        },
        "hithull": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 5,
            "material": -1,
            "minimalhit": 0.02,
            "name": "HitHull",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "HitHull_visual"
        },
        "hitlaileron": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitLAileron",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "HitAileronL_visual"
        },
        "hitlcelevator": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitLCElevator",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "HitElevatorL_visual"
        },
        "hitraileron": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitRAileron",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "HitAileronR_visual"
        },
        "hitrelevator": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitRElevator",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "HitElevatorR_visual"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/Air_F_Jets/UAV_05/Data/UI/uav_05_icon_ca.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "8 + 16",
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.0316228,
    "irscanground": 1,
    "irscanrangemax": 10000,
    "irscanrangemin": 2000,
    "irscantoeyefactor": 2,
    "irtarget": 1,
    "irtargetsize": 0.8,
    "isbackpack": 0,
    "isuav": 1,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 0.1,
    "landingaoa": "8.5*3.1415/180",
    "landingspeed": 225,
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffect": "LDustEffects",
    "leftdusteffects": [
        [
            "GdtKLDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "LGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "LDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "LDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "LDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LGrassEffects"
        ],
        [
            "GdtGrassTall",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "LGrassEffects"
        ],
        [
            "GdtRedDirt",
            "LDustEffectsAirRed"
        ],
        [
            "GdtField",
            "LDustEffectsAir"
        ],
        [
            "GdtForest",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LStonesEffects"
        ],
        [
            "GdtCliff",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "LDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "LDirtEffects"
        ],
        [
            "GdtAsphalt",
            "LDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "LDirtEffects"
        ],
        [
            "GdtRubble",
            "LDustEffectsAir"
        ],
        [
            "GdtRubble",
            "LDirtEffects"
        ],
        [
            "GdtSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtSoil",
            "LDirtEffects"
        ],
        [
            "GdtBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtBeach",
            "LStonesEffects"
        ],
        [
            "GdtRock",
            "LDustEffectsAir"
        ],
        [
            "GdtRock",
            "LDirtEffects"
        ],
        [
            "GdtDead",
            "LDustEffectsAir"
        ],
        [
            "GdtDead",
            "LDirtEffects"
        ],
        [
            "Default",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
        ],
        [
            "GdtDirt",
            "LDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
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
            "LDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "LDustEffectsAir"
        ],
        [
            "SurfWood",
            "LDustEffectsAir"
        ],
        [
            "SurfMetal",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "LDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "LDustEffectsAir"
        ]
    ],
    "lightongear": 1,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 8,
    "magazines": [
        "120Rnd_CMFlare_Chaff_Magazine"
    ],
    "mapsize": 20.1,
    "markerlights": {
        "collisionlightred1": {
            "activelight": 0,
            "ambient": [
                0.08,
                0,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                0.9
            ],
            "blinkingpatternguarantee": 1,
            "blinkingstartson": 1,
            "color": [
                0.8,
                0,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_collision_light_red_1",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 0.001,
    "maxgforce": 2,
    "maxgunelev": 0,
    "maxgunturn": 0,
    "maxomega": 3000,
    "maxspeed": 800,
    "memorypointcm": [
        "pos_flare_launcher1",
        "pos_flare_launcher2"
    ],
    "memorypointcmdir": [
        "pos_flare_launcher1_dir",
        "pos_flare_launcher2_dir"
    ],
    "memorypointdriveroptics": "pos_pip0",
    "memorypointgun": "kulomet",
    "memorypointldust": "pos_Dust_L",
    "memorypointlrocket": "L raketa",
    "memorypointrdust": "pos_Dust_R",
    "memorypointrrocket": "P raketa",
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
    "memorypointtaskmarker": "",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 0.2,
    "mfd": {
        "hud": {
            "bones": {
                "aglmove1": {
                    "max": 100,
                    "maxpos": [
                        0.05,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.05,
                        0.1
                    ],
                    "source": "altitudeAGL",
                    "type": "linear"
                },
                "aglmove2": {
                    "pos": [
                        0.05,
                        0.8
                    ],
                    "type": "fixed"
                },
                "aslmove1": {
                    "max": 500,
                    "maxpos": [
                        0.1,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.1,
                        0.1
                    ],
                    "source": "altitudeASL",
                    "type": "linear"
                },
                "aslmove2": {
                    "pos": [
                        0.1,
                        0.8
                    ],
                    "type": "fixed"
                },
                "ils": {
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos3": [
                        0.7,
                        0.6
                    ],
                    "type": "ils"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.27
                    ],
                    "type": "fixed"
                },
                "spdmove2": {
                    "max": 200,
                    "maxpos": [
                        0.94,
                        0.87
                    ],
                    "min": 33,
                    "minpos": [
                        0.94,
                        0.1
                    ],
                    "source": "speed",
                    "type": "linear"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "target",
                    "type": "vector"
                },
                "targetdistancemgun": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 1000,
                    "maxangle": 90,
                    "min": 100,
                    "minangle": -180,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "targetdistancemissile": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 3000,
                    "maxangle": 120,
                    "min": 100,
                    "minangle": -120,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "vertspeed": {
                    "max": 25,
                    "maxpos": [
                        0,
                        0.4
                    ],
                    "min": -25,
                    "minpos": [
                        0,
                        -0.4
                    ],
                    "source": "vSpeed",
                    "type": "linear"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "weapon",
                    "type": "vector"
                }
            },
            "borderbottom": 0.1,
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "bottomleft": "HUD LD",
            "color": [
                0,
                1,
                0,
                0.1
            ],
            "draw": {
                "alpha": 0.8,
                "altitude": {
                    "points": [
                        [
                            "AGLMove1",
                            1
                        ],
                        [
                            "AGLMove2",
                            1
                        ],
                        [],
                        [
                            "ASLMove2",
                            1
                        ],
                        [
                            "ASLMove1",
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1,
                            "VertSpeed",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "clipbr": [
                    1,
                    0.9
                ],
                "cliptl": [
                    0,
                    0.05
                ],
                "color": [
                    0.1,
                    0.5,
                    0.05
                ],
                "condition": "on",
                "dimmedbase": {
                    "alpha": 0.3,
                    "altitudebase": {
                        "points": [
                            [
                                "AGLMove2",
                                1
                            ],
                            [
                                "ASLMove2",
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "horizont": {
                    "clipbr": [
                        0.8,
                        0.9
                    ],
                    "cliptl": [
                        0.2,
                        0.1
                    ],
                    "dimmed": {
                        "alpha": 0.6,
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.4,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.4,
                                        0
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    },
                    "levelm10": {
                        "points": [
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm15": {
                        "points": [
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    -0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm5": {
                        "points": [
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp10": {
                        "points": [
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp15": {
                        "points": [
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp5": {
                        "points": [
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "ils": {
                    "aoabracket": {
                        "points": [
                            [
                                [
                                    0.42,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.88
                                ],
                                1
                            ],
                            [
                                [
                                    0.42,
                                    0.88
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "ils",
                    "glideslope": {
                        "clipbr": [
                            0.71,
                            0.71
                        ],
                        "cliptl": [
                            0.29,
                            0.29
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS",
                                    [
                                        -10,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        10,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS",
                                    [
                                        0,
                                        -10
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        0,
                                        10
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    }
                },
                "mgun": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(-180)",
                                    "-0.03*cos(-180)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(-180)",
                                    "-0.07*cos(-180)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(+90)",
                                    "-0.03*cos(+90)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(+90)",
                                    "-0.07*cos(+90)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.04
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "mgun"
                },
                "missile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(-120)",
                                    "-0.1*0.8*cos(-120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(-120)",
                                    "-0.1*1.2*cos(-120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(+120)",
                                    "-0.1*0.8*cos(+120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(+120)",
                                    "-0.1*1.2*cos(+120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*0.8"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*1.2"
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "missile",
                    "target": {
                        "points": [
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "planew": {
                    "clipbr": [
                        1,
                        0.9
                    ],
                    "cliptl": [
                        0,
                        0.1
                    ],
                    "linehl": {
                        "points": [
                            [
                                "PlaneW",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "velocity": {
                        "points": [
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "speed": {
                    "points": [
                        [
                            [
                                0.95,
                                0.87
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.1
                            ],
                            1
                        ],
                        [],
                        [
                            "SpdMove2",
                            [
                                -0.05,
                                0
                            ],
                            1
                        ],
                        [
                            "SpdMove2",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "speednumber": {
                    "align": "left",
                    "down": [
                        "SpdMove2",
                        [
                            -0.05,
                            0.03
                        ],
                        1
                    ],
                    "pos": [
                        "SpdMove2",
                        [
                            -0.05,
                            -0.03
                        ],
                        1
                    ],
                    "right": [
                        "SpdMove2",
                        [
                            0.01,
                            -0.03
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                }
            },
            "helmetdown": [
                0,
                -0.05,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.025,
                0.025,
                0.1
            ],
            "helmetright": [
                0.05,
                0,
                0
            ],
            "pos10vector": {
                "pos0": [
                    0.5,
                    0.27
                ],
                "pos10": [
                    "0.5+0.9",
                    "0.27+0.7"
                ],
                "type": "vector"
            },
            "topleft": "HUD LH",
            "topright": "HUD PH"
        }
    },
    "mfmax": 100,
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
    "mgunfire": {
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
        "cloudletduration": 0,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "cloudletgrowup": 0.06,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletFire",
        "cloudletsize": 1,
        "deltat": -4000,
        "initt": 3200,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
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
    "minealerticonrange": 200,
    "minfiretime": 60,
    "mingforce": 0.2,
    "mingunelev": 0,
    "mingunturn": 0,
    "mintotaldamagethreshold": 0.005,
    "model": "A3/Air_F_Jets/UAV_05/UAV_05_F.p3d",
    "namesound": "veh_air_plane_s",
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
    "normalspeedforwardcoef": 0.85,
    "numberphysicalwheels": 3,
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
    "nvgmarkers": {},
    "nvscanner": 0,
    "nvtarget": 0,
    "obstructsoundlfratio": 0,
    "obstructsoundswhenin": 0.316228,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 1,
    "picture": "A3/Air_F_Jets/UAV_05/Data/UI/uav_05_picture_ca.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 200,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 0.15,
    "radartype": 4,
    "rainext": {
        "frequency": 1,
        "sound": [
            "A3/Sounds_F/vehicles/noises/rain1_ext",
            1.77828,
            1,
            100
        ],
        "volume": "camPos * rain * (speed factor[50, 0])"
    },
    "rainint": {
        "frequency": 1,
        "sound": [
            "A3/Sounds_F/vehicles/noises/rain1_int",
            1,
            1,
            100
        ],
        "volume": "(1-camPos) * rain * (speed factor[50, 0])"
    },
    "reflectors": {
        "gear_front_light_1": {
            "ambient": [
                0.0085,
                0.0095,
                0.01
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 650,
                "hardlimitstart": 350,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                0.85,
                0.95,
                1
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "pos_gear_front_light_dir",
            "flaremaxdistance": 500,
            "flaresize": 2,
            "hitpoint": "pos_gear_front_light",
            "innerangle": 15,
            "intensity": 500000,
            "outerangle": 50,
            "position": "pos_gear_front_light",
            "selection": "gear_front_light",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reportownposition": 1,
    "reportremotetargets": 1,
    "reversed": 1,
    "rightdusteffect": "RDustEffects",
    "rightdusteffects": [
        [
            "GdtKLDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "RGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "RDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "RDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "RDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RGrassEffects"
        ],
        [
            "GdtGrassTall",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "RGrassEffects"
        ],
        [
            "GdtRedDirt",
            "RDustEffectsAirRed"
        ],
        [
            "GdtField",
            "RDustEffectsAir"
        ],
        [
            "GdtForest",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RStonesEffects"
        ],
        [
            "GdtCliff",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "RDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "RDirtEffects"
        ],
        [
            "GdtAsphalt",
            "RDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "RDirtEffects"
        ],
        [
            "GdtRubble",
            "RDustEffectsAir"
        ],
        [
            "GdtRubble",
            "RDirtEffects"
        ],
        [
            "GdtSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtSoil",
            "RDirtEffects"
        ],
        [
            "GdtBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtBeach",
            "RStonesEffects"
        ],
        [
            "GdtRock",
            "RDustEffectsAir"
        ],
        [
            "GdtRock",
            "RDirtEffects"
        ],
        [
            "GdtDead",
            "RDustEffectsAir"
        ],
        [
            "GdtDead",
            "RDirtEffects"
        ],
        [
            "Default",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
        ],
        [
            "GdtDirt",
            "RDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
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
            "RDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "RDustEffectsAir"
        ],
        [
            "SurfWood",
            "RDustEffectsAir"
        ],
        [
            "SurfMetal",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "RDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "RDustEffectsAir"
        ]
    ],
    "ruddercoef": [
        0,
        0.2,
        0.9,
        1.9,
        2,
        2.1,
        2.1,
        2.2,
        2.2,
        2.1,
        2.1,
        1.9,
        1.5
    ],
    "ruddercontrolssensitivitycoef": 3,
    "rudderinfluence": 0.9396,
    "scope": 0,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionrotormove": "vrtule blur",
    "selectionrotorstill": "vrtule staticka",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
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
    "simulation": "airplaneX",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.3,
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
        "emptySound",
        0
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "Crash0",
        0.25,
        "Crash1",
        0.25,
        "Crash2",
        0.25,
        "Crash3",
        0.25
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
        "A3/Sounds_F_Jets/vehicles/air/UAV_05/B_UAV_05_engine_shut_ext",
        1.75,
        1,
        300
    ],
    "soundengineoffint": [
        "A3/Sounds_F_Jets/vehicles/air/UAV_05/B_UAV_05_engine_shut_int",
        1,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F_Jets/vehicles/air/UAV_05/B_UAV_05_engine_start_ext",
        1.75,
        1,
        300
    ],
    "soundengineonint": [
        "A3/Sounds_F_Jets/vehicles/air/UAV_05/B_UAV_05_engine_start_int",
        1,
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
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_Flaps_Down",
        1.5,
        1,
        150
    ],
    "soundflapsup": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_Flaps_Up",
        1.5,
        1,
        150
    ],
    "soundgear": {},
    "soundgeardown": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_gear_down",
        2.25,
        1,
        250
    ],
    "soundgearup": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_gear_up",
        2.25,
        1,
        250
    ],
    "soundgetin": [
        "A3/Sounds_F/vehicles/air/CAS_01/getin_wipeout",
        1,
        1,
        40
    ],
    "soundgetout": [
        "A3/Sounds_F/air/Plane_Fighter_03/getout",
        1,
        1,
        40
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_lockedon2",
        1,
        1.5
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
        "A3/Sounds_F_Jets/vehicles/air/Shared/FX_Plane_Jet_lockedOn1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "soundsets": [
            "UAV_05_EngineLowExt_SoundSet",
            "UAV_05_EngineHighExt_SoundSet",
            "UAV_05_ForsageExt_SoundSet",
            "UAV_05_WindNoiseExt_SoundSet",
            "UAV_05_DistanceRumble_SoundSet",
            "UAV_05_EngineLowInt_SoundSet",
            "UAV_05_EngineHighInt_SoundSet",
            "UAV_05_ForsageInt_SoundSet",
            "UAV_05_WindNoiseInt_SoundSet"
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
    "soundwatercollision1": [
        "A3/Sounds_F/vehicles/crashes/planes/plane_crash_water_1",
        1.41254,
        1,
        500
    ],
    "soundwatercollision2": [
        "A3/Sounds_F/vehicles/crashes/planes/plane_crash_water_2",
        1.41254,
        1,
        500
    ],
    "soundwatercrash": [
        "",
        0.177828,
        1
    ],
    "soundwatercrashes": [
        "soundWaterCollision1",
        0.5,
        "soundWaterCollision2",
        0.5
    ],
    "soundwoodcrash": [
        "woodCrash0",
        0.25,
        "woodCrash1",
        0.25,
        "woodCrash2",
        0.25,
        "woodCrash3",
        0.25
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_air_UAV_p"
            ],
            "speechsingular": [
                "veh_air_UAV_s"
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
    "stallspeed": 200,
    "stallwarningtreshold": 0.1,
    "steeraheadplan": 2,
    "steeraheadsimul": 1,
    "supplyradius": 1.2,
    "tailhook": 1,
    "tbody": 150,
    "textplural": "UAVs",
    "textsingular": "UAV",
    "texturelist": [
        "DarkGrey",
        1,
        "DarkGreyCamo",
        0
    ],
    "texturesources": {
        "darkgrey": {
            "author": "Bravo Zero One Studios",
            "displayname": "Dark Grey",
            "factions": [
                "BLU_F"
            ],
            "textures": [
                "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01_co.paa",
                "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02_co.paa"
            ]
        },
        "darkgreycamo": {
            "author": "Bravo Zero One Studios",
            "displayname": "Dark Grey [Camo]",
            "factions": [
                "BLU_F"
            ],
            "textures": [
                "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_01_Camo_co.paa",
                "A3/Air_F_Jets/UAV_05/Data/UAV05_fuselage_02_Camo_co.paa"
            ]
        }
    },
    "threat": [
        0.1,
        1,
        0.5
    ],
    "thrustcoef": [
        1.4,
        1.35,
        1.32,
        1.37,
        1.42,
        1.46,
        1.48,
        1.5,
        1.51,
        1.25,
        0.9,
        0,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportfuel": 0,
    "transportitems": {},
    "transportmagazines": {},
    "transportmaxbackpacks": 0,
    "transportmaxmagazines": 20,
    "transportmaxweapons": 3,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {
        "mainturret": {
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
            "commanding": -1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                4000,
                                2000,
                                16000,
                                8000
                            ],
                            "resource": "RscCustomInfoSensors"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        "vehiclemissiledisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Missile"
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
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                4000,
                                2000,
                                16000,
                                8000
                            ],
                            "resource": "RscCustomInfoSensors"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        "vehiclemissiledisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Missile"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "SensorDisplay",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mainGun",
            "gunbeg": "pos_pip1_dir",
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
            "gunend": "pos_pip1",
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
            "gunnername": "UCAV Sentinel operator",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UGV_01_Optics_Gunner_F.p3d",
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
            "initelev": -45,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "Laserbatteries"
            ],
            "maxcamelev": 90,
            "maxelev": 5,
            "maxhorizontalrotspeed": 10,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 180,
            "maxverticalrotspeed": 10,
            "memorypointgun": "pos_pip1",
            "memorypointgunneroptics": "pos_pip1_dir",
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
            "minelev": -90,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -180,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "medium": {
                    "directionstabilized": 1,
                    "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_medium_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.1,
                    "maxanglex": 85,
                    "maxangley": 130,
                    "maxfov": 0.1,
                    "minanglex": -35,
                    "minangley": -130,
                    "minfov": 0.1,
                    "opticsdisplayname": "M",
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "Ti"
                    ]
                },
                "narrow": {
                    "directionstabilized": 1,
                    "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_narrow_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.0286,
                    "maxanglex": 85,
                    "maxangley": 130,
                    "maxfov": 0.0286,
                    "minanglex": -35,
                    "minangley": -130,
                    "minfov": 0.0286,
                    "opticsdisplayname": "N",
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "Ti"
                    ]
                },
                "wide": {
                    "directionstabilized": 1,
                    "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_wide_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.5,
                    "maxanglex": 85,
                    "maxangley": 130,
                    "maxfov": 0.5,
                    "minanglex": -35,
                    "minangley": -130,
                    "minfov": 0.5,
                    "opticsdisplayname": "W",
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "Ti"
                    ]
                }
            },
            "opticsout": {
                "monocular": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 1.1,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.133,
                    "visionmode": [
                        "Normal",
                        "NVG"
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
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RscOptics_UAV_gunner",
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
            "weapons": [
                "Laserdesignator_mounted"
            ]
        }
    },
    "type": 2,
    "typicalcargo": [
        "B_UAV_AI"
    ],
    "uavcameradriverdir": "pos_pip0_dir",
    "uavcameradriverpos": "pos_pip0",
    "uavcameragunnerdir": "pos_pip1_dir",
    "uavcameragunnerpos": "pos_pip1",
    "uavhacker": 0,
    "unitinfotype": "RscOptics_AV_airplane_pilot",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "uav05_fold_wings": {
            "condition": "this animationPhase `wing_fold_l` < 0.1 and (getpos this select 2) < 1 and (speed this) < 40",
            "displayname": "Fold Wings",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "radius": 5,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate [`wing_fold_l`,1]; this animate [`wing_fold_l_arm`,1]; this animate [`wing_fold_cover_l_arm`,1]; this animate [`wing_fold_cover_l`,1]; this animate [`wing_fold_r`,1]; this animate [`wing_fold_r_arm`,1]; this animate [`wing_fold_cover_r_arm`,1]; this animate [`wing_fold_cover_r`,1]; this say3D `UAV_05_foldwing_sound"
        },
        "uav05_tailhook_down": {
            "condition": "this animationPhase `tailhook` > 0.1 and speed this > 100",
            "displayname": "Tailhook Down",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate [`tailhook`,0]; this animate [`tailhook_door_l_1`,0]; this animate [`tailhook_door_l_2`,0]; this animate [`tailhook_door_r_1`,0]; this animate [`tailhook_door_r_2`,0]; this say `UAV_05_tailhook_down_sound`; this say3D `UAV_05_tailhook_down_sound`; [this] spawn BIS_fnc_AircraftTailhook;"
        },
        "uav05_tailhook_up": {
            "condition": "this animationPhase `tailhook` < 0.1",
            "displayname": "Tailhook Up",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate [`tailhook`,1]; this animate [`tailhook_door_l_1`,1]; this animate [`tailhook_door_l_2`,1]; this animate [`tailhook_door_r_1`,1]; this animate [`tailhook_door_r_2`,1]; this say `UAV_05_tailhook_up_sound`; this say3D `UAV_05_tailhook_up_sound"
        },
        "uav05_unfold_wings": {
            "condition": "this animationPhase `wing_fold_l` > 0.9",
            "displayname": "Unfold Wings",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "radius": 5,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate [`wing_fold_l`,0]; this animate [`wing_fold_l_arm`,0]; this animate [`wing_fold_cover_l_arm`,0]; this animate [`wing_fold_cover_l`,0]; this animate [`wing_fold_r`,0]; this animate [`wing_fold_r_arm`,0]; this animate [`wing_fold_cover_r_arm`,0]; this animate [`wing_fold_cover_r`,0]; this say3D `UAV_05_foldwing_sound"
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
    "viewcargoshadowamb": 1,
    "viewcargoshadowdiff": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0,
        "thermalmode": [
            0,
            1
        ],
        "visionmode": [
            "Normal",
            "NVG",
            "Ti"
        ]
    },
    "viewpilot": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0.2,
        "maxmovey": 0.1,
        "maxmovez": 0.2,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": -0.2,
        "minmovey": -0.1,
        "minmovez": -0.1,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 0.9,
    "vtol": 0,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "vtolyawinfluence": 2,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 100,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
    "weapons": [
        "CMFlareLauncher"
    ],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "wheels": {
        "disablewheelswhendestroyed": 1,
        "wheel_1": {
            "bonename": "wheels_f",
            "boundary": "pos_wheels_f_rim",
            "center": "pos_wheels_f_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    0.6
                ],
                [
                    0.2,
                    1
                ],
                [
                    0.6,
                    0.8
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 20,
            "longitudinalstiffnessperunitgravity": 1500,
            "mass": 150,
            "maxbraketorque": 1000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 2,
            "side": "left",
            "springdamperrate": 62000,
            "springstrength": 230000,
            "sprungmass": 3000,
            "steering": 1,
            "suspforceapppointoffset": "pos_wheels_f_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "pos_wheels_f_center",
            "width": 0.3
        },
        "wheel_2": {
            "bonename": "wheel_l",
            "boundary": "pos_wheel_l_rim",
            "center": "pos_wheel_l_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    0.6
                ],
                [
                    0.2,
                    1
                ],
                [
                    0.6,
                    0.8
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 20,
            "longitudinalstiffnessperunitgravity": 1800,
            "mass": 150,
            "maxbraketorque": 2000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 2,
            "side": "left",
            "springdamperrate": 82000,
            "springstrength": 310000,
            "sprungmass": 4225,
            "steering": 0,
            "suspforceapppointoffset": "pos_wheel_l_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "pos_wheel_l_center",
            "width": 0.28
        },
        "wheel_3": {
            "bonename": "wheel_r",
            "boundary": "pos_wheel_r_rim",
            "center": "pos_wheel_r_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    0.6
                ],
                [
                    0.2,
                    1
                ],
                [
                    0.6,
                    0.8
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 20,
            "longitudinalstiffnessperunitgravity": 1800,
            "mass": 150,
            "maxbraketorque": 2000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 2,
            "side": "right",
            "springdamperrate": 82000,
            "springstrength": 310000,
            "sprungmass": 4225,
            "steering": 0,
            "suspforceapppointoffset": "pos_wheel_r_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "pos_wheel_r_center",
            "width": 0.28
        }
    },
    "wheelsteeringsensitivity": 2,
    "windsockexist": 0,
    "wingvortices": {
        "bodyleft_inner_1": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_L_1"
        },
        "bodyleft_inner_2": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_L_2"
        },
        "bodyleft_inner_3": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_L_3"
        },
        "bodyright_inner_1": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_R_1"
        },
        "bodyright_inner_2": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_R_2"
        },
        "bodyright_inner_3": {
            "effectname": "FX_FuselageVapour_FighterJet",
            "position": "pos_body_vapour_R_3"
        },
        "wingtipleft": {
            "effectname": "FX_WingVortices_FighterJet",
            "position": "pos_wingtip_vapour_L"
        },
        "wingtipright": {
            "effectname": "FX_WingVortices_FighterJet",
            "position": "pos_wingtip_vapour_R"
        }
    },
    "woodcrash0": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_wood_ext_1",
        3.16228,
        1,
        900
    ],
    "woodcrash1": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_wood_ext_2",
        3.16228,
        1,
        900
    ],
    "woodcrash2": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_wood_ext_6",
        3.16228,
        1,
        900
    ],
    "woodcrash3": [
        "A3/Sounds_F/vehicles/crashes/cars/cars_coll_big_wood_ext_8",
        3.16228,
        1,
        900
    ]
}