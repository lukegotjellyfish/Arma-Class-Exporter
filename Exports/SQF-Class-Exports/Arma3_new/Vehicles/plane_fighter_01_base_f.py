d = {
    "_generalmacro": "Plane_Base_F",
    "acceleration": 200,
    "access": 0,
    "accuracy": 0.02,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "aileroncoef": [
        0.4,
        0.5,
        0.8,
        0.95,
        1.02,
        1.04,
        1.03,
        1.01,
        1,
        0.7,
        0.6,
        0.55,
        0.5,
        0.45,
        0.4,
        0.35
    ],
    "aileroncontrolssensitivitycoef": 3.5,
    "aileronsensitivity": 1.2,
    "airbrake": 1,
    "airbrakefrictioncoef": 2.4,
    "aircapacity": 10,
    "aircraftautomatedsystems": {
        "wingautounfoldspeed": 40,
        "wingfoldanimations": [
            "wing_fold_l",
            "wing_fold_r",
            "wing_fold_cover_l",
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
        0.0075
    ],
    "airfrictioncoefs2": [
        0.001,
        0.005,
        6.7e-05
    ],
    "allowtablock": 1,
    "altfullforce": 5000,
    "altnoforce": 15000,
    "alwaystarget": 0,
    "angleofindicence": "-1.0*3.1415/180",
    "animated": 1,
    "animationlist": [],
    "animationsources": {
        "canopy_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "collisionlightwhite_source": {
            "markerlight": "CollisionLightWhite1",
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
        "ejection_seat_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "ejection_seat_motion": {
            "animperiod": 0.25,
            "initphase": 0,
            "source": "user"
        },
        "gear_f_hook_down": {
            "animperiod": 1.5,
            "initphase": 0,
            "source": "user"
        },
        "hitavionics": {
            "hitpoint": "HitAvionics",
            "raw": 1,
            "source": "Hit"
        },
        "hitengine": {
            "hitpoint": "HitEngine",
            "raw": 1,
            "source": "Hit"
        },
        "hitengine2": {
            "hitpoint": "HitEngine2",
            "raw": 1,
            "source": "Hit"
        },
        "mfd_ammo_count_source": {
            "source": "revolving",
            "weapon": "weapon_Fighter_Gun20mm_AA"
        },
        "muzzle_rot_20mm": {
            "source": "ammorandom",
            "weapon": "weapon_Fighter_Gun20mm_AA"
        },
        "pylon_1_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "pylon_2_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "pylon_3_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "pylon_4_hide": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "tailhook": {
            "animperiod": 1.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_l": {
            "animperiod": 1.5,
            "initphase": 1,
            "source": "user"
        },
        "tailhook_door_r": {
            "animperiod": 1.5,
            "initphase": 1,
            "source": "user"
        },
        "throttle_pilot": {
            "animperiod": 0.5,
            "initphase": 0,
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
            "animperiod": 2.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_cover_r": {
            "animperiod": 2.5,
            "initphase": 0,
            "source": "user"
        },
        "wing_fold_l": {
            "animperiod": 2.5,
            "displayname": "Fold Wings",
            "forceanimate": [
                "wing_fold_l",
                1,
                "wing_fold_r",
                1,
                "wing_fold_cover_l",
                1,
                "wing_fold_cover_r",
                1
            ],
            "forceanimate2": [
                "wing_fold_l",
                0,
                "wing_fold_r",
                0,
                "wing_fold_cover_l",
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
        "wing_fold_r": {
            "animperiod": 2.5,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 60,
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
    "armorlights": 1,
    "armorstructural": 2,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "PlaneAttenuation",
    "audible": 60,
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
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/FX_Plane_Fighter_01_cabine_close_ext",
        3.16228,
        1,
        40
    ],
    "cabinclosesoundinternal": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/FX_Plane_Fighter_01_cabine_close_int",
        10,
        1,
        40
    ],
    "cabinopening": 1,
    "cabinopensound": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/FX_Plane_Fighter_01_cabine_open_ext",
        3.16228,
        1,
        40
    ],
    "cabinopensoundinternal": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/FX_Plane_Fighter_01_cabine_open_int",
        10,
        1,
        40
    ],
    "camerasmoothspeed": 5,
    "camouflage": 100,
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
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [],
    "cargocaneject": 0,
    "cargocompartments": [
        0
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
            "tailhook_door_l",
            "tailhook_door_r"
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
        "launchbarmemorypoint": "pos_gear_f_hook",
        "launchvelocity": 300,
        "launchvelocityincrease": 10
    },
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "clutchstrength": 100,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "activeradarsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 15000,
                        "minrange": 15000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 45,
                    "anglerangevertical": 45,
                    "animdirection": "",
                    "color": [
                        0,
                        1,
                        1,
                        1
                    ],
                    "componenttype": "ActiveRadarSensorComponent",
                    "groundnoisedistancecoef": 0.2,
                    "groundtarget": {
                        "maxrange": 8000,
                        "minrange": 8000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": 200,
                    "maxspeedthreshold": 27.7778,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 20.8333,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 8000
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
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 2500,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 90,
                    "animdirection": "",
                    "color": [
                        1,
                        0,
                        0,
                        1
                    ],
                    "componenttype": "IRSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 2000,
                        "minrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxfogseethrough": 0.995,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 400,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 2000
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
                    "aimdown": 1,
                    "airtarget": {
                        "maxrange": 4000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 26,
                    "anglerangevertical": 20,
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
                    "maxtrackablespeed": 100,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "nightrangecoef": 0,
                    "typerecognitiondistance": 2000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "transportpylonscomponent": {
            "bays": {
                "baycenter1": {
                    "autoclosewhenemptydelay": 3,
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0
                },
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
                "aa": {
                    "attachment": [
                        "PylonRack_Missile_AMRAAM_D_x2",
                        "PylonRack_Missile_AMRAAM_D_x2",
                        "PylonRack_Missile_AMRAAM_D_x2",
                        "PylonRack_Missile_AMRAAM_D_x2",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1"
                    ],
                    "displayname": "AA"
                },
                "cas": {
                    "attachment": [
                        "PylonRack_Missile_AGM_02_x1",
                        "PylonRack_Missile_AGM_02_x1",
                        "PylonRack_Missile_AGM_02_x2",
                        "PylonRack_Missile_AGM_02_x2",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "",
                        "",
                        "PylonMissile_Bomb_GBU12_x1",
                        "PylonMissile_Bomb_GBU12_x1"
                    ],
                    "displayname": "CAS"
                },
                "cluster": {
                    "attachment": [
                        "PylonRack_Missile_AMRAAM_D_x1",
                        "PylonRack_Missile_AMRAAM_D_x1",
                        "PylonRack_2Rnd_BombCluster_01_F",
                        "PylonRack_2Rnd_BombCluster_01_F",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "",
                        "",
                        "PylonMissile_1Rnd_BombCluster_01_F",
                        "PylonMissile_1Rnd_BombCluster_01_F"
                    ],
                    "displayname": "Cluster"
                },
                "default": {
                    "attachment": [
                        "PylonRack_Missile_AMRAAM_D_x1",
                        "PylonRack_Missile_AMRAAM_D_x1",
                        "PylonRack_Missile_AGM_02_x2",
                        "PylonRack_Missile_AGM_02_x2",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_BIM9X_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "PylonMissile_Missile_AMRAAM_D_INT_x1",
                        "",
                        "",
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
                    "attachment": "PylonRack_Missile_AMRAAM_D_x1",
                    "hardpoints": [
                        "B_BIM9X_RAIL",
                        "B_BIM9X_DUAL_RAIL",
                        "B_AMRAAM_D_RAIL",
                        "B_AMRAAM_D_DUAL_RAIL",
                        "B_AGM65_RAIL",
                        "B_GBU12"
                    ],
                    "maxweight": 300,
                    "priority": 12,
                    "uiposition": [
                        0.6,
                        0.45
                    ]
                },
                "pylon2": {
                    "attachment": "PylonRack_Missile_AMRAAM_D_x1",
                    "hardpoints": [
                        "B_BIM9X_RAIL",
                        "B_BIM9X_DUAL_RAIL",
                        "B_AMRAAM_D_RAIL",
                        "B_AMRAAM_D_DUAL_RAIL",
                        "B_AGM65_RAIL",
                        "B_GBU12"
                    ],
                    "maxweight": 300,
                    "mirroredmissilepos": 1,
                    "priority": 12,
                    "uiposition": [
                        0.05,
                        0.45
                    ]
                },
                "pylon3": {
                    "attachment": "PylonRack_Missile_AGM_02_x2",
                    "hardpoints": [
                        "B_BIM9X_RAIL",
                        "B_BIM9X_DUAL_RAIL",
                        "B_AMRAAM_D_RAIL",
                        "B_AMRAAM_D_DUAL_RAIL",
                        "B_AGM65_RAIL",
                        "B_AGM65_DUAL_RAIL",
                        "B_GBU12",
                        "B_GBU12_DUAL_RAIL",
                        "B_HARM_RAIL",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1050,
                    "priority": 11,
                    "uiposition": [
                        0.55,
                        0.35
                    ]
                },
                "pylon4": {
                    "attachment": "PylonRack_Missile_AGM_02_x2",
                    "hardpoints": [
                        "B_BIM9X_RAIL",
                        "B_BIM9X_DUAL_RAIL",
                        "B_AMRAAM_D_RAIL",
                        "B_AMRAAM_D_DUAL_RAIL",
                        "B_AGM65_RAIL",
                        "B_AGM65_DUAL_RAIL",
                        "B_GBU12",
                        "B_GBU12_DUAL_RAIL",
                        "B_HARM_RAIL",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1050,
                    "mirroredmissilepos": 3,
                    "priority": 11,
                    "uiposition": [
                        0.1,
                        0.35
                    ]
                },
                "pylonbaycenter1": {
                    "attachment": "PylonMissile_Missile_AMRAAM_D_INT_x1",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT"
                    ],
                    "maxweight": 1200,
                    "priority": 9,
                    "uiposition": [
                        0.33,
                        0.3
                    ]
                },
                "pylonbaycenter2": {
                    "attachment": "PylonMissile_Missile_AMRAAM_D_INT_x1",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT"
                    ],
                    "maxweight": 1200,
                    "mirroredmissilepos": 7,
                    "priority": 9,
                    "uiposition": [
                        0.33,
                        0.35
                    ]
                },
                "pylonbaycenter3": {
                    "attachment": "",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1200,
                    "priority": 7,
                    "uiposition": [
                        0.33,
                        0.4
                    ]
                },
                "pylonbaycenter4": {
                    "attachment": "",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT",
                        "B_SDB_QUAD_RAIL"
                    ],
                    "maxweight": 1200,
                    "mirroredmissilepos": 9,
                    "priority": 7,
                    "uiposition": [
                        0.33,
                        0.45
                    ]
                },
                "pylonbaycenter5": {
                    "attachment": "PylonMissile_Bomb_GBU12_x1",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT",
                        "B_GBU12"
                    ],
                    "maxweight": 1200,
                    "priority": 5,
                    "uiposition": [
                        0.33,
                        0.5
                    ]
                },
                "pylonbaycenter6": {
                    "attachment": "PylonMissile_Bomb_GBU12_x1",
                    "bay": 3,
                    "hardpoints": [
                        "B_AMRAAM_D_INT",
                        "B_GBU12"
                    ],
                    "maxweight": 1200,
                    "mirroredmissilepos": 11,
                    "priority": 5,
                    "uiposition": [
                        0.33,
                        0.55
                    ]
                },
                "pylonbayleft1": {
                    "attachment": "PylonMissile_Missile_BIM9X_x1",
                    "bay": 1,
                    "hardpoints": [
                        "B_BIM9X"
                    ],
                    "maxweight": 1200,
                    "mirroredmissilepos": 5,
                    "priority": 10,
                    "uiposition": [
                        0.16,
                        0.25
                    ]
                },
                "pylonbayright1": {
                    "attachment": "PylonMissile_Missile_BIM9X_x1",
                    "bay": 2,
                    "hardpoints": [
                        "B_BIM9X"
                    ],
                    "maxweight": 1200,
                    "priority": 10,
                    "uiposition": [
                        0.5,
                        0.25
                    ]
                }
            },
            "uipicture": "A3/Air_F_Jets/Plane_Fighter_01/Data/UI/Fighter_01_3DEN_CA.paa"
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
                        16000,
                        8000,
                        4000,
                        2000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehicledriverdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Driver"
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
                        16000,
                        8000,
                        4000,
                        2000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehicledriverdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Driver"
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
    "crew": "B_Fighter_Pilot_F",
    "crewcrashprotection": 0.15,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_01.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_01_damage.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_01_destruct.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_02.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_02_damage.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_fuselage_02_destruct.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass_damage.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass_damage.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass_in.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass_in_damage.rvmat",
            "a3/air_f_jets/plane_fighter_01/data/Fighter_01_glass_in_damage.rvmat"
        ],
        "tex": [
            "A3/Air_F_Jets/Plane_Fighter_01/Data/MFD/fighter_01_mfd_01_co.paa",
            "A3/Air_F_Jets/Plane_Fighter_01/Data/MFD/Fighter_01_MFD_01_damage.paa"
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
    "defaultusermfdvalues": [
        0.082,
        0.408,
        0.039,
        0.8
    ],
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "disableinventory": 1,
    "displayname": "F/A-181 Black Wasp II",
    "dlc": "Jets",
    "draconicforcexcoef": 7,
    "draconicforceycoef": 1.1,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [
        4,
        5.1,
        6.1,
        7,
        7.7,
        8.3,
        9,
        9.1,
        9.2,
        9.2,
        9.2
    ],
    "draconictorqueycoef": [
        6.8,
        5.5,
        4,
        1.5,
        0.1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
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
    "driveraction": "Pilot_Plane_Fighter_01",
    "drivercaneject": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": 0,
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "throttle_pilot",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "stick_pilot",
    "driverrightleganimname": "",
    "driverweaponsinfotype": "RscOptics_CAS_01_TGP",
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
    "editorpreview": "A3/EditorPreviews_F_Jets/Data/Cfgvehicles/B_Plane_Fighter_01_F.jpg",
    "editorsubcategory": "EdSubcat_Planes",
    "ejectdamagelimit": 0.45,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "ejectdeadgunner": 0,
    "ejectionsystem": {
        "canopyclass": "Plane_Fighter_01_Canopy_F",
        "canopyforce": 30,
        "canopyhideanim": "canopy_hide",
        "canopypos": "pos_eject_canopy",
        "ejectiondual": 0,
        "ejectionparachute": "Steerable_Parachute_F",
        "ejectionseatclass": "B_Ejection_Seat_Plane_Fighter_01_F",
        "ejectionseatenabled": 1,
        "ejectionseatforce": 50,
        "ejectionseathideanim": "ejection_seat_hide",
        "ejectionseatpos": "pos_eject",
        "ejectionseatrailanim": "ejection_seat_motion",
        "ejectionsoundext": "Plane_Fighter_01_ejection_ext_sound",
        "ejectionsoundint": "Plane_Fighter_01_ejection_in_sound"
    },
    "ejectspeed": [
        0,
        60,
        0
    ],
    "elevatorcoef": [
        0.3,
        0.5,
        0.66,
        0.52,
        0.49,
        0.46,
        0.43,
        0.4,
        0.35,
        0.3,
        0.25,
        0.18,
        0.17,
        0.16,
        0.15,
        0.15
    ],
    "elevatorcontrolssensitivitycoef": 4,
    "elevatorsensitivity": 1.4,
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
        0.11,
        0.43,
        0.97,
        1.72,
        2.69,
        3.87,
        5.27,
        6.89,
        8.72,
        9.7,
        9.6,
        9.2,
        8.5,
        8.2,
        8
    ],
    "epeimpulsedamagecoef": 120,
    "eventhandlers": {
        "engine": "_this call bis_fnc_aircraftFoldingWings",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "gear": "_this call bis_fnc_aircraftFoldingWings",
        "hit": "_this call bis_fnc_planeAiEject",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "landing": "[_this,true] call bis_fnc_aircraftTailhookAi",
        "landingcanceled": "[_this,false] call bis_fnc_aircraftTailhookAi"
    },
    "exhausts": {
        "exhaust_left": {
            "direction": "pos_Exhausts_end_left",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0,
            "position": "pos_Exhausts_start_left"
        },
        "exhaust_right": {
            "direction": "pos_Exhausts_end_right",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1,
            "position": "pos_Exhausts_start_right"
        }
    },
    "explosionshielding": 2,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        3,
        -20
    ],
    "faction": "BLU_F",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flaps": 1,
    "flapsfrictioncoef": 0.36,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 30,
    "formationz": 30,
    "fuelcapacity": 1550,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 10,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 3,
    "gearretracting": 1,
    "gearsupfrictioncoef": 0.8,
    "gearuptime": 4.5,
    "getinaction": "Pilot_Plane_Fighter_01_Enter",
    "getinoutonproxy": 0,
    "getinradius": 5.5,
    "getoutaction": "Pilot_Plane_Fighter_01_Exit",
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
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
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
        "CamoGlass",
        "camo_cockpit_1",
        "camo_cockpit_2",
        "camo_cockpit_3",
        "camo_cockpit_5",
        "number_01",
        "number_02",
        "number_03"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_01_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_02_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_glass_01_ca.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_01_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_02_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_03_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_05_co.paa",
        "a3/air_f_jets/plane_fighter_01/data/Numbers/Fighter_01_01_ca.paa",
        "a3/air_f_jets/plane_fighter_01/data/Numbers/Fighter_01_00_ca.paa",
        "a3/air_f_jets/plane_fighter_01/data/Numbers/Fighter_01_01_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitAvionics",
            "passthrough": 0.4,
            "radius": 0.3,
            "visual": ""
        },
        "hitengine": {
            "armor": 3,
            "depends": "0",
            "explosionshielding": 4.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitEngine",
            "passthrough": 0.8,
            "radius": 0.6,
            "visual": "Hit_Engine"
        },
        "hitengine2": {
            "armor": 3,
            "depends": "0",
            "explosionshielding": 4.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitEngine2",
            "passthrough": 0.8,
            "radius": 0.6,
            "visual": "Hit_Engine2"
        },
        "hitfuel": {
            "armor": 4,
            "depends": "0",
            "explosionshielding": 5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitFuel",
            "passthrough": 0.6,
            "radius": 0.3,
            "visual": "Hit_Fuel"
        },
        "hitfuel2": {
            "armor": 4,
            "depends": "0",
            "explosionshielding": 5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitFuel2",
            "passthrough": 0.6,
            "radius": 0.3,
            "visual": "Hit_Fuel2"
        },
        "hitglass1": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitGlass1",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "Hit_Glass1"
        },
        "hithull": {
            "armor": 3.5,
            "depends": "0",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitHull",
            "passthrough": 1,
            "radius": 0.45,
            "visual": "Hit_Hull"
        },
        "hitlaileron": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitLAileron",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_AileronL"
        },
        "hitlcelevator": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitLCElevator",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_ElevatorL"
        },
        "hitlcrudder": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitLCRudder",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_RudderL"
        },
        "hitraileron": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitRAileron",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_AileronR"
        },
        "hitrelevator": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitRElevator",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_ElevatorR"
        },
        "hitrrudder": {
            "armor": 1.8,
            "depends": "0",
            "explosionshielding": 3.5,
            "material": -1,
            "minimalhit": 0.05,
            "name": "HitRRudder",
            "passthrough": 0.3,
            "radius": 0.35,
            "visual": "Hit_RudderR"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/Air_F_Jets/Plane_Fighter_01/Data/UI/Fighter01_icon_ca.paa",
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
    "irtargetsize": 1,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "landingaoa": "9.2*3.1415/180",
    "landingspeed": 260,
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
    "library": {
        "libenable": 1,
        "libtextdesc": ""
    },
    "lightongear": 1,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 8,
    "magazines": [
        "magazine_Fighter01_Gun20mm_AA_x450",
        "Laserbatteries",
        "240Rnd_CMFlare_Chaff_Magazine"
    ],
    "mapsize": 18.25,
    "markerlights": {
        "collisionlightgreen1": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
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
            "blinking": 0,
            "color": [
                0,
                0.8,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_collision_light_green_1",
            "useflare": 0
        },
        "collisionlightgreen2": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
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
            "blinking": 0,
            "color": [
                0,
                0.8,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_collision_light_green_2",
            "useflare": 0
        },
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
            "blinking": 0,
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
        },
        "collisionlightred2": {
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
            "blinking": 0,
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
            "name": "pos_collision_light_red_2",
            "useflare": 0
        },
        "collisionlightwhite1": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
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
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.35,
            "intensity": 75,
            "name": "pos_collision_light_white_1",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 0.001,
    "maxgforce": 3,
    "maxgunelev": 0,
    "maxgunturn": 0,
    "maximumload": 500,
    "maxomega": 2000,
    "maxspeed": 1200,
    "memorypointcm": [
        "pos_flare_launcher1"
    ],
    "memorypointcmdir": [
        "pos_flare_launcher1_dir"
    ],
    "memorypointdriveroptics": "pos_PilotCamera",
    "memorypointgun": "pos_nosegun",
    "memorypointldust": "pos_dust_l",
    "memorypointlmissile": "l strela",
    "memorypointlrocket": "l raketa",
    "memorypointrdust": "pos_dust_r",
    "memorypointrmissile": "p strela",
    "memorypointrrocket": "p raketa",
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "GetIn_driver_pos",
    "memorypointsgetindriverdir": "GetIn_driver_dir",
    "memorypointsgetindriverprecise": "pos_getin_driver_precise",
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
        "b_plane_fighter_01_static_hud": {
            "bones": {
                "airport1": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "airportCorner1ToView",
                    "type": "vector"
                },
                "airport2": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "airportCorner2ToView",
                    "type": "vector"
                },
                "airport3": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "airportCorner3ToView",
                    "type": "vector"
                },
                "airport4": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "airportCorner4ToView",
                    "type": "vector"
                },
                "horizonbankrot": {
                    "aspectratio": 1,
                    "center": [
                        0.5,
                        0.5
                    ],
                    "max": "rad(30)",
                    "maxangle": "180.75+30",
                    "min": "-rad(30)",
                    "minangle": "180.25-30",
                    "source": "horizonBank",
                    "type": "rotational"
                },
                "ils_h": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos3": [
                        0.5822,
                        0.5
                    ],
                    "type": "ils"
                },
                "ils_w": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos3": [
                        0.5,
                        0.581
                    ],
                    "type": "ils"
                },
                "impactpoint": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "ImpactPointToView",
                    "type": "vector"
                },
                "impactpointrelative": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "impactpointtoviewweaponRelative",
                    "type": "vector"
                },
                "larammomax": {
                    "max": 1,
                    "maxpos": [
                        0,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        1
                    ],
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "type": "linear"
                },
                "larammomin": {
                    "max": 1,
                    "maxpos": [
                        0,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        1
                    ],
                    "source": "LarAmmoMin",
                    "sourcescale": 1,
                    "type": "linear"
                },
                "lartargetdist": {
                    "max": 1,
                    "maxpos": [
                        0,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        1
                    ],
                    "source": "LarTargetDist",
                    "sourcescale": 1,
                    "type": "linear"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm20": {
                    "angle": -20,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm25": {
                    "angle": -25,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm30": {
                    "angle": -30,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm35": {
                    "angle": -35,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm40": {
                    "angle": -40,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm45": {
                    "angle": -45,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm50": {
                    "angle": -50,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm60": {
                    "angle": -60,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm70": {
                    "angle": -70,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm80": {
                    "angle": -80,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelm90": {
                    "angle": -90,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp20": {
                    "angle": 20,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp25": {
                    "angle": 25,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp30": {
                    "angle": 30,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp35": {
                    "angle": 35,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp40": {
                    "angle": 40,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp45": {
                    "angle": 45,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp50": {
                    "angle": 50,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp60": {
                    "angle": 60,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp70": {
                    "angle": 70,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp80": {
                    "angle": 80,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "levelp90": {
                    "angle": 90,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.884,
                        0.88
                    ],
                    "type": "horizontoview"
                },
                "limit0109": {
                    "limits": [
                        0.1,
                        0.1,
                        0.9,
                        0.9
                    ],
                    "type": "limit"
                },
                "limitwaypoint": {
                    "limits": [
                        0.2,
                        0.1,
                        0.8,
                        0.1
                    ],
                    "type": "limit"
                },
                "missileflighttimerot1": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 0.5,
                    "maxangle": 18,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot10": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 5,
                    "maxangle": 180,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot11": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 5.5,
                    "maxangle": 198,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot12": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 6,
                    "maxangle": 216,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot13": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 6.5,
                    "maxangle": 234,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot14": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 7,
                    "maxangle": 252,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot15": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 7.5,
                    "maxangle": 270,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot16": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 8,
                    "maxangle": 288,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot17": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 8.5,
                    "maxangle": 306,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot18": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 9,
                    "maxangle": 324,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot19": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 9.5,
                    "maxangle": 342,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot2": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 1,
                    "maxangle": 36,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot20": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 10,
                    "maxangle": 360,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot3": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 1.5,
                    "maxangle": 54,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot4": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 2,
                    "maxangle": 72,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot5": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 2.5,
                    "maxangle": 90,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot6": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 3,
                    "maxangle": 108,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot7": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 3.5,
                    "maxangle": 126,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot8": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 4,
                    "maxangle": 144,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "missileflighttimerot9": {
                    "aspectratio": 0.985402,
                    "center": [
                        0,
                        0
                    ],
                    "max": 4.5,
                    "maxangle": 162,
                    "min": 0,
                    "minangle": 0,
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "normalizebombcircle": {
                    "aspectratio": 0.985402,
                    "limit": 0.08,
                    "type": "normalizedorsmaller"
                },
                "planeorientation": {
                    "pos": [
                        0.5,
                        0.5
                    ],
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "forward",
                    "type": "vector"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "type": "fixed"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "targetToView",
                    "type": "vector"
                },
                "targetingpoddir": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "pilotcameratoview",
                    "type": "vector"
                },
                "targetingpodtarget": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "pilotcameratargettoview",
                    "type": "vector"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "velocityToView",
                    "type": "vector"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "weaponToView",
                    "type": "vector"
                },
                "wppoint": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "WPPoint",
                    "type": "vector"
                },
                "wppointtoview": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.774,
                        0.77
                    ],
                    "source": "WPPointToView",
                    "type": "vector"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "HUD LD",
            "color": [
                0.082,
                0.408,
                0.039,
                1
            ],
            "draw": {
                "aamissilecrosshairgroup": {
                    "aamissilecrosshair": {
                        "points": [
                            [
                                "PlaneOrientation",
                                [
                                    0,
                                    -0.24635
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.0434,
                                    -0.242606
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.0855,
                                    -0.231495
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.125,
                                    -0.213339
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.1607,
                                    -0.188704
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.1915,
                                    -0.158354
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.2165,
                                    -0.123175
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.234925,
                                    -0.0842518
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.2462,
                                    -0.0427664
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.2462,
                                    0.0427664
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.234925,
                                    0.0842518
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.2165,
                                    0.123175
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.1915,
                                    0.158354
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.1607,
                                    0.188704
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.125,
                                    0.213339
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.0855,
                                    0.231495
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0.0434,
                                    0.242606
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0,
                                    0.24635
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.0434,
                                    0.242606
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.0855,
                                    0.231495
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.125,
                                    0.213339
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.1607,
                                    0.188704
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.1915,
                                    0.158354
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.2165,
                                    0.123175
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.234925,
                                    0.0842518
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.2462,
                                    0.0427664
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.2462,
                                    -0.0427664
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.234925,
                                    -0.0842518
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.2165,
                                    -0.123175
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.1915,
                                    -0.158354
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.1607,
                                    -0.188704
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.125,
                                    -0.213339
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.0855,
                                    -0.231495
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    -0.0434,
                                    -0.242606
                                ],
                                1
                            ],
                            [
                                "PlaneOrientation",
                                [
                                    0,
                                    -0.24635
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    },
                    "condition": "AAmissile",
                    "lines": {
                        "points": [
                            [
                                [
                                    0.21,
                                    0.55
                                ],
                                1
                            ],
                            [
                                [
                                    0.19,
                                    0.55
                                ],
                                1
                            ],
                            [
                                [
                                    0.19,
                                    0.71
                                ],
                                1
                            ],
                            [
                                [
                                    0.21,
                                    0.71
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.21,
                                    0.67
                                ],
                                1
                            ],
                            [
                                [
                                    0.19,
                                    0.67
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.21,
                                    0.63
                                ],
                                1
                            ],
                            [
                                [
                                    0.19,
                                    0.63
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.21,
                                    0.59
                                ],
                                1
                            ],
                            [
                                [
                                    0.19,
                                    0.59
                                ],
                                1
                            ],
                            [],
                            [
                                "LarTargetDist",
                                -0.16,
                                [
                                    0.17,
                                    0.73
                                ],
                                1
                            ],
                            [
                                "LarTargetDist",
                                -0.16,
                                [
                                    0.19,
                                    0.71
                                ],
                                1
                            ],
                            [
                                "LarTargetDist",
                                -0.16,
                                [
                                    0.17,
                                    0.69
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 4
                    },
                    "middletext": {
                        "align": "right",
                        "down": [
                            [
                                0.22,
                                0.65
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.22,
                                0.61
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.26,
                                0.61
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0005,
                        "type": "text"
                    },
                    "poly": {
                        "points": [
                            [
                                [
                                    "LarAmmoMin",
                                    -0.16,
                                    [
                                        0.191,
                                        0.71
                                    ],
                                    1
                                ],
                                [
                                    "LarAmmoMax",
                                    -0.16,
                                    [
                                        0.191,
                                        0.71
                                    ],
                                    1
                                ],
                                [
                                    "LarAmmoMax",
                                    -0.16,
                                    [
                                        0.208,
                                        0.71
                                    ],
                                    1
                                ],
                                [
                                    "LarAmmoMin",
                                    -0.16,
                                    [
                                        0.208,
                                        0.71
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "speedtext": {
                        "align": "left",
                        "down": [
                            "LarTargetDist",
                            -0.16,
                            [
                                0.16,
                                0.73
                            ],
                            1
                        ],
                        "pos": [
                            "LarTargetDist",
                            -0.16,
                            [
                                0.16,
                                0.69
                            ],
                            1
                        ],
                        "right": [
                            "LarTargetDist",
                            -0.16,
                            [
                                0.2,
                                0.69
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "LarTargetSpeed",
                        "sourcescale": 3.6,
                        "type": "text"
                    },
                    "toptext": {
                        "align": "right",
                        "down": [
                            [
                                0.22,
                                0.57
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.22,
                                0.53
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.26,
                                0.53
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "LarTop",
                        "sourcescale": 0.001,
                        "type": "text"
                    },
                    "type": "group"
                },
                "alpha": "user3",
                "altitudeindicatorbox": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                0.49,
                                -0.25
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.49,
                                -0.2
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.3,
                                -0.2
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.3,
                                -0.25
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.49,
                                -0.25
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "altitudenumberagl": {
                    "align": "left",
                    "down": [
                        "PlaneW",
                        [
                            0.48,
                            -0.15
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            0.48,
                            -0.19
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            0.54,
                            -0.19
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeAGL",
                    "sourcelength": 4,
                    "sourceoffset": -2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "altitudenumberasl": {
                    "align": "center",
                    "down": [
                        "PlaneW",
                        [
                            0.4,
                            -0.2
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            0.4,
                            -0.25
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            0.48,
                            -0.25
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "type": "text"
                },
                "altituderadartext": {
                    "align": "left",
                    "down": [
                        "PlaneW",
                        [
                            0.32,
                            "-0.192 + 0.041"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            0.32,
                            -0.192
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "+0.32 + 0.04",
                            -0.192
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "R",
                    "type": "text"
                },
                "ammotext": {
                    "align": "right",
                    "down": [
                        [
                            0.032,
                            0.925
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.032,
                            0.88
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.087,
                            0.88
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "atmissilecrosshairgroup": {
                    "atmissilecrosshair": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    -0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    -0.13
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    0.13
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    -0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    -0.13
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    0.13
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    -0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.13,
                                    -0.15
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.15,
                                    0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.13,
                                    0.15
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    -0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.13,
                                    -0.15
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.15,
                                    0.15
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.13,
                                    0.15
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    },
                    "condition": "ATmissile",
                    "type": "group"
                },
                "bombcrosshairgroup": {
                    "bombcrosshair": {
                        "points": [
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0886861
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0788321
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    -0.09,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.08,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0.09,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.08,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0019708
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0019708
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    -0.002,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.002,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.013888,
                                    -0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.02736,
                                    -0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.04,
                                    -0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.051424,
                                    -0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.06128,
                                    -0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.06928,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.075176,
                                    -0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.078784,
                                    -0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.08,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.078784,
                                    0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.075176,
                                    0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.06928,
                                    0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.06128,
                                    0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.051424,
                                    0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.04,
                                    0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.02736,
                                    0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.013888,
                                    0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0788321
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.013888,
                                    0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.02736,
                                    0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.04,
                                    0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.051424,
                                    0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.06128,
                                    0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.06928,
                                    0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.075176,
                                    0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.078784,
                                    0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.08,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.078784,
                                    -0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.075176,
                                    -0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.06928,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.06128,
                                    -0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.051424,
                                    -0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.04,
                                    -0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.02736,
                                    -0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.013888,
                                    -0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [],
                            [],
                            [
                                "ImpactPoint",
                                -1,
                                "Velocity",
                                1,
                                "NormalizeBombCircle",
                                1,
                                "ImpactPoint",
                                1,
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    0
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    },
                    "circle": {
                        "points": [
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0630657
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [
                                "MissileFlightTimeRot1",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot2",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot3",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot4",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot5",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot6",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot7",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot8",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot9",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot10",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot11",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot12",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot13",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot14",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot15",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot16",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot17",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot18",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot19",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot20",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ],
                            [
                                "MissileFlightTimeRot20",
                                [
                                    0,
                                    0.064
                                ],
                                1,
                                "ImpactPoint",
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 6
                    },
                    "condition": "bomb",
                    "distance": {
                        "align": "center",
                        "down": [
                            "ImpactPoint",
                            [
                                -0.002,
                                0.15
                            ],
                            1
                        ],
                        "max": 15,
                        "pos": [
                            "ImpactPoint",
                            [
                                -0.002,
                                0.11
                            ],
                            1
                        ],
                        "right": [
                            "ImpactPoint",
                            [
                                0.045,
                                0.11
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "ImpactDistance",
                        "sourceprecision": 1,
                        "sourcescale": 0.001,
                        "type": "text"
                    },
                    "type": "group"
                },
                "climbnumber": {
                    "align": "right",
                    "down": [
                        "PlaneW",
                        [
                            -0.39,
                            "+0.026 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.39,
                            0.026
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.39 + 0.04",
                            0.026
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "vspeed",
                    "sourcescale": 1,
                    "type": "text"
                },
                "climbtext": {
                    "align": "left",
                    "down": [
                        "PlaneW",
                        [
                            -0.41,
                            "+0.026 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.41,
                            0.026
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.41 + 0.04",
                            0.026
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "text": "C:",
                    "type": "text"
                },
                "color": [
                    "user0",
                    "user1",
                    "user2"
                ],
                "condition": "(1 - (cameraHeadingDiffY<=-19) + (abs(cameraHeadingDiffX)>=24))*on",
                "flaps": {
                    "condition": "flaps",
                    "flapstext": {
                        "align": "left",
                        "down": [
                            [
                                0.932,
                                0.965
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.932,
                                0.92
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.987,
                                0.92
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "FLAPS",
                        "type": "text"
                    }
                },
                "headingarrow": {
                    "points": [
                        [
                            "WPPoint",
                            1,
                            "LimitWaypoint",
                            1,
                            [
                                -0.02,
                                0.042
                            ],
                            1
                        ],
                        [
                            "WPPoint",
                            1,
                            "LimitWaypoint",
                            1,
                            [
                                0,
                                0.022
                            ],
                            1
                        ],
                        [
                            "WPPoint",
                            1,
                            "LimitWaypoint",
                            1,
                            [
                                0.02,
                                0.042
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "headingindicatorarrow": {
                    "points": [
                        [
                            [
                                "PlaneW",
                                [
                                    -0.015,
                                    -0.455
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    -0.445
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.015,
                                    -0.455
                                ],
                                1
                            ]
                        ]
                    ],
                    "type": "polygon"
                },
                "headingindicatorbox": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.035,
                                -0.455
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.035,
                                -0.5
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.035,
                                -0.5
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.035,
                                -0.455
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.035,
                                -0.455
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "headingnumber": {
                    "align": "center",
                    "down": [
                        "PlaneW",
                        [
                            0,
                            "(-0.5 + 0.045\t)"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            0,
                            "(-0.5\t\t\t)"
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            0.03,
                            "(-0.5\t\t\t)"
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcescale": 1,
                    "type": "text"
                },
                "headingrotation": {
                    "condition": "abs(cameraDir-heading)*( (abs(heading-cameraDir))<=355)-5",
                    "headingarrow": {
                        "points": [
                            [
                                [
                                    0.488,
                                    0.141
                                ],
                                1
                            ],
                            [
                                [
                                    0.512,
                                    0.141
                                ],
                                1
                            ],
                            [
                                [
                                    0.542,
                                    0.161
                                ],
                                1
                            ],
                            [
                                [
                                    0.512,
                                    0.181
                                ],
                                1
                            ],
                            [
                                [
                                    0.488,
                                    0.181
                                ],
                                1
                            ],
                            [
                                [
                                    0.458,
                                    0.161
                                ],
                                1
                            ],
                            [
                                [
                                    0.488,
                                    0.141
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 3
                    },
                    "headingheadnumber": {
                        "align": "center",
                        "down": [
                            [
                                "0.80-0.302",
                                "0.113+0.065"
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.80-0.302",
                                "0.082+0.065"
                            ],
                            1
                        ],
                        "right": [
                            [
                                "0.83-0.302",
                                "0.082+0.065"
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "cameraDir",
                        "sourcescale": 1,
                        "type": "text"
                    }
                },
                "headingscale": {
                    "align": "center",
                    "bottom": 0.9,
                    "center": 0.5,
                    "down": [
                        0.096,
                        0.093
                    ],
                    "horizontal": 1,
                    "linexleft": 0.105,
                    "linexleftmajor": 0.095,
                    "lineyright": 0.115,
                    "lineyrightmajor": 0.115,
                    "majorlineeach": 5,
                    "nevereatseaweed": 1,
                    "numbereach": 5,
                    "pos": [
                        0.096,
                        0.0546
                    ],
                    "right": [
                        0.143,
                        0.0546
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcescale": 1,
                    "step": "18 / 9",
                    "stepsize": "(0.70 - 0.3) / 15",
                    "top": 0.1,
                    "type": "scale",
                    "width": 3
                },
                "horizonbankrot": {
                    "points": [
                        [
                            "HorizonBankRot",
                            [
                                0,
                                "0.39421001-0.109"
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                0.01,
                                "0.41673699-0.109"
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                -0.01,
                                "0.41673699-0.109"
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                0,
                                "0.39421001-0.109"
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 2
                },
                "horizonbankrotlines": {
                    "points": [
                        [
                            [
                                0.619959,
                                0.712986
                            ],
                            1
                        ],
                        [
                            [
                                0.631439,
                                0.744203
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.58291,
                                0.739019
                            ],
                            1
                        ],
                        [
                            [
                                0.588087,
                                0.760778
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.540574,
                                0.748504
                            ],
                            1
                        ],
                        [
                            [
                                0.543184,
                                0.770838
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4975,
                                0.740421
                            ],
                            1
                        ],
                        [
                            [
                                0.4975,
                                0.77421
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.454426,
                                0.748504
                            ],
                            1
                        ],
                        [
                            [
                                0.451816,
                                0.770838
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.41209,
                                0.739019
                            ],
                            1
                        ],
                        [
                            [
                                0.406913,
                                0.760778
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.375041,
                                0.712986
                            ],
                            1
                        ],
                        [
                            [
                                0.363561,
                                0.744203
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "horizont": {
                    "clipbr": [
                        0.8,
                        0.8
                    ],
                    "cliptl": [
                        0.2,
                        0.2
                    ],
                    "dimmed": {
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        0.75,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.065,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        -0.065,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.75,
                                        0
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        }
                    },
                    "hideonturn": {
                        "condition": "5-abs(cameraDir-heading)*( (abs(heading-cameraDir))<=355)) ",
                        "limiter": {
                            "level0": {
                                "points": [],
                                "type": "line",
                                "width": 2
                            },
                            "levelm10": {
                                "points": [
                                    [
                                        "LevelM10",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM10",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM10",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm15": {
                                "points": [
                                    [
                                        "LevelM15",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM15",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM15",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm20": {
                                "points": [
                                    [
                                        "LevelM20",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM20",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM20",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm25": {
                                "points": [
                                    [
                                        "LevelM25",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM25",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM25",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm30": {
                                "points": [
                                    [
                                        "LevelM30",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM30",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM30",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm35": {
                                "points": [
                                    [
                                        "LevelM35",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM35",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM35",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm40": {
                                "points": [
                                    [
                                        "LevelM40",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM40",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM40",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm45": {
                                "points": [
                                    [
                                        "LevelM45",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM45",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM45",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm5": {
                                "points": [
                                    [
                                        "LevelM5",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM5",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM5",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm50": {
                                "points": [
                                    [
                                        "LevelM50",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM50",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM50",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm60": {
                                "points": [
                                    [
                                        "LevelM60",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM60",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM60",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm70": {
                                "points": [
                                    [
                                        "LevelM70",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM70",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM70",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm80": {
                                "points": [
                                    [
                                        "LevelM80",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM80",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM80",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelm90": {
                                "points": [
                                    [
                                        "LevelM90",
                                        [
                                            -0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            -0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            -0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.235,
                                            -0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.235,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.22,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.205,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.19,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.175,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.16,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.145,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.13,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.115,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.1,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.085,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelM90",
                                        [
                                            0.07,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelM90",
                                        [
                                            0.055,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp10": {
                                "points": [
                                    [
                                        "LevelP10",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP10",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP10",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP10",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP10",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP10",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp15": {
                                "points": [
                                    [
                                        "LevelP15",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP15",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP15",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP15",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP15",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP15",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp20": {
                                "points": [
                                    [
                                        "LevelP20",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP20",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP20",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP20",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP20",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP20",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp25": {
                                "points": [
                                    [
                                        "LevelP25",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP25",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP25",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP25",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP25",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP25",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp30": {
                                "points": [
                                    [
                                        "LevelP30",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP30",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP30",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP30",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP30",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP30",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp35": {
                                "points": [
                                    [
                                        "LevelP35",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP35",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP35",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP35",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP35",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP35",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp40": {
                                "points": [
                                    [
                                        "LevelP40",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP40",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP40",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP40",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP40",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP40",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp45": {
                                "points": [
                                    [
                                        "LevelP45",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP45",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP45",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP45",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP45",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP45",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp5": {
                                "points": [
                                    [
                                        "LevelP5",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP5",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP5",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP5",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP5",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP5",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp50": {
                                "points": [
                                    [
                                        "LevelP50",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP50",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP50",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP50",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP50",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP50",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp60": {
                                "points": [
                                    [
                                        "LevelP60",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP60",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP60",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP60",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP60",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP60",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp70": {
                                "points": [
                                    [
                                        "LevelP70",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP70",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP70",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP70",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP70",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP70",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp80": {
                                "points": [
                                    [
                                        "LevelP80",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP80",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP80",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP80",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP80",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP80",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "levelp90": {
                                "points": [
                                    [
                                        "LevelP90",
                                        [
                                            "-0.22-0.015",
                                            0.02
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP90",
                                        [
                                            "-0.22-0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP90",
                                        [
                                            -0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        "LevelP90",
                                        [
                                            0.06,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP90",
                                        [
                                            "+0.22+0.015",
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        "LevelP90",
                                        [
                                            "+0.22+0.015",
                                            0.02
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "valm_1_10": {
                                "align": "left",
                                "down": [
                                    "LevelM10",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM10",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM10",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -10,
                                "type": "text"
                            },
                            "valm_1_10_r": {
                                "align": "right",
                                "down": [
                                    "LevelM10",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM10",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM10",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -10,
                                "type": "text"
                            },
                            "valm_1_15": {
                                "align": "left",
                                "down": [
                                    "LevelM15",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM15",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM15",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -15,
                                "type": "text"
                            },
                            "valm_1_15_r": {
                                "align": "right",
                                "down": [
                                    "LevelM15",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM15",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM15",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -15,
                                "type": "text"
                            },
                            "valm_1_20": {
                                "align": "left",
                                "down": [
                                    "LevelM20",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM20",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM20",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -20,
                                "type": "text"
                            },
                            "valm_1_20_r": {
                                "align": "right",
                                "down": [
                                    "LevelM20",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM20",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM20",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -20,
                                "type": "text"
                            },
                            "valm_1_25": {
                                "align": "left",
                                "down": [
                                    "LevelM25",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM25",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM25",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -25,
                                "type": "text"
                            },
                            "valm_1_25_r": {
                                "align": "right",
                                "down": [
                                    "LevelM25",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM25",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM25",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -25,
                                "type": "text"
                            },
                            "valm_1_30": {
                                "align": "left",
                                "down": [
                                    "LevelM30",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM30",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM30",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -30,
                                "type": "text"
                            },
                            "valm_1_30_r": {
                                "align": "right",
                                "down": [
                                    "LevelM30",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM30",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM30",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -30,
                                "type": "text"
                            },
                            "valm_1_35": {
                                "align": "left",
                                "down": [
                                    "LevelM35",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM35",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM35",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -35,
                                "type": "text"
                            },
                            "valm_1_35_r": {
                                "align": "right",
                                "down": [
                                    "LevelM35",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM35",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM35",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -35,
                                "type": "text"
                            },
                            "valm_1_40": {
                                "align": "left",
                                "down": [
                                    "LevelM40",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM40",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM40",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -40,
                                "type": "text"
                            },
                            "valm_1_40_r": {
                                "align": "right",
                                "down": [
                                    "LevelM40",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM40",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM40",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -40,
                                "type": "text"
                            },
                            "valm_1_45": {
                                "align": "left",
                                "down": [
                                    "LevelM45",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM45",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM45",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -45,
                                "type": "text"
                            },
                            "valm_1_45_r": {
                                "align": "right",
                                "down": [
                                    "LevelM45",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM45",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM45",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -45,
                                "type": "text"
                            },
                            "valm_1_5": {
                                "align": "left",
                                "down": [
                                    "LevelM5",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM5",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM5",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -5,
                                "type": "text"
                            },
                            "valm_1_50": {
                                "align": "left",
                                "down": [
                                    "LevelM50",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM50",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM50",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -50,
                                "type": "text"
                            },
                            "valm_1_50_r": {
                                "align": "right",
                                "down": [
                                    "LevelM50",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM50",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM50",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -50,
                                "type": "text"
                            },
                            "valm_1_5_r": {
                                "align": "right",
                                "down": [
                                    "LevelM5",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM5",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM5",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -5,
                                "type": "text"
                            },
                            "valm_1_60": {
                                "align": "left",
                                "down": [
                                    "LevelM60",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM60",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM60",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -60,
                                "type": "text"
                            },
                            "valm_1_60_r": {
                                "align": "right",
                                "down": [
                                    "LevelM60",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM60",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM60",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -60,
                                "type": "text"
                            },
                            "valm_1_70": {
                                "align": "left",
                                "down": [
                                    "LevelM70",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM70",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM70",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -70,
                                "type": "text"
                            },
                            "valm_1_70_r": {
                                "align": "right",
                                "down": [
                                    "LevelM70",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM70",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM70",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -70,
                                "type": "text"
                            },
                            "valm_1_80": {
                                "align": "left",
                                "down": [
                                    "LevelM80",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM80",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM80",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -80,
                                "type": "text"
                            },
                            "valm_1_80_r": {
                                "align": "right",
                                "down": [
                                    "LevelM80",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM80",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM80",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -80,
                                "type": "text"
                            },
                            "valm_1_90": {
                                "align": "left",
                                "down": [
                                    "LevelM90",
                                    [
                                        -0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM90",
                                    [
                                        -0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM90",
                                    [
                                        -0.2,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -90,
                                "type": "text"
                            },
                            "valm_1_90_r": {
                                "align": "right",
                                "down": [
                                    "LevelM90",
                                    [
                                        0.26,
                                        0.018
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelM90",
                                    [
                                        0.26,
                                        -0.032
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelM90",
                                    [
                                        0.32,
                                        -0.032
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": -90,
                                "type": "text"
                            },
                            "valp_1_10": {
                                "align": "left",
                                "down": [
                                    "LevelP10",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP10",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP10",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "10",
                                "type": "text"
                            },
                            "valp_1_10_r": {
                                "align": "right",
                                "down": [
                                    "LevelP10",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP10",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP10",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "10",
                                "type": "text"
                            },
                            "valp_1_15": {
                                "align": "left",
                                "down": [
                                    "LevelP15",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP15",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP15",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "15",
                                "type": "text"
                            },
                            "valp_1_15_r": {
                                "align": "right",
                                "down": [
                                    "LevelP15",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP15",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP15",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "15",
                                "type": "text"
                            },
                            "valp_1_20": {
                                "align": "left",
                                "down": [
                                    "LevelP20",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP20",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP20",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "20",
                                "type": "text"
                            },
                            "valp_1_20_r": {
                                "align": "right",
                                "down": [
                                    "LevelP20",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP20",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP20",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "20",
                                "type": "text"
                            },
                            "valp_1_25": {
                                "align": "left",
                                "down": [
                                    "LevelP25",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP25",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP25",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "25",
                                "type": "text"
                            },
                            "valp_1_25_r": {
                                "align": "right",
                                "down": [
                                    "LevelP25",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP25",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP25",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "25",
                                "type": "text"
                            },
                            "valp_1_30": {
                                "align": "left",
                                "down": [
                                    "LevelP30",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP30",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP30",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "30",
                                "type": "text"
                            },
                            "valp_1_30_r": {
                                "align": "right",
                                "down": [
                                    "LevelP30",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP30",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP30",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "30",
                                "type": "text"
                            },
                            "valp_1_35": {
                                "align": "left",
                                "down": [
                                    "LevelP35",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP35",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP35",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "35",
                                "type": "text"
                            },
                            "valp_1_35_r": {
                                "align": "right",
                                "down": [
                                    "LevelP35",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP35",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP35",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "35",
                                "type": "text"
                            },
                            "valp_1_40": {
                                "align": "left",
                                "down": [
                                    "LevelP40",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP40",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP40",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "40",
                                "type": "text"
                            },
                            "valp_1_40_r": {
                                "align": "right",
                                "down": [
                                    "LevelP40",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP40",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP40",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "40",
                                "type": "text"
                            },
                            "valp_1_45": {
                                "align": "left",
                                "down": [
                                    "LevelP45",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP45",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP45",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "45",
                                "type": "text"
                            },
                            "valp_1_45_r": {
                                "align": "right",
                                "down": [
                                    "LevelP45",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP45",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP45",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "45",
                                "type": "text"
                            },
                            "valp_1_5": {
                                "align": "left",
                                "down": [
                                    "LevelP5",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP5",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP5",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "5",
                                "type": "text"
                            },
                            "valp_1_50": {
                                "align": "left",
                                "down": [
                                    "LevelP50",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP50",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP50",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "50",
                                "type": "text"
                            },
                            "valp_1_50_r": {
                                "align": "right",
                                "down": [
                                    "LevelP50",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP50",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP50",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "50",
                                "type": "text"
                            },
                            "valp_1_5_r": {
                                "align": "right",
                                "down": [
                                    "LevelP5",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP5",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP5",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "5",
                                "type": "text"
                            },
                            "valp_1_60": {
                                "align": "left",
                                "down": [
                                    "LevelP60",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP60",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP60",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "60",
                                "type": "text"
                            },
                            "valp_1_60_r": {
                                "align": "right",
                                "down": [
                                    "LevelP60",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP60",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP60",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "60",
                                "type": "text"
                            },
                            "valp_1_70": {
                                "align": "left",
                                "down": [
                                    "LevelP70",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP70",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP70",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "70",
                                "type": "text"
                            },
                            "valp_1_70_r": {
                                "align": "right",
                                "down": [
                                    "LevelP70",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP70",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP70",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "70",
                                "type": "text"
                            },
                            "valp_1_80": {
                                "align": "left",
                                "down": [
                                    "LevelP80",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP80",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP80",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "80",
                                "type": "text"
                            },
                            "valp_1_80_r": {
                                "align": "right",
                                "down": [
                                    "LevelP80",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP80",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP80",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "80",
                                "type": "text"
                            },
                            "valp_1_90": {
                                "align": "left",
                                "down": [
                                    "LevelP90",
                                    [
                                        -0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP90",
                                    [
                                        -0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP90",
                                    [
                                        -0.2,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "90",
                                "type": "text"
                            },
                            "valp_1_90_r": {
                                "align": "right",
                                "down": [
                                    "LevelP90",
                                    [
                                        0.26,
                                        0.033
                                    ],
                                    1
                                ],
                                "pos": [
                                    "LevelP90",
                                    [
                                        0.26,
                                        -0.017
                                    ],
                                    1
                                ],
                                "right": [
                                    "LevelP90",
                                    [
                                        0.32,
                                        -0.017
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "sourcescale": 1,
                                "text": "90",
                                "type": "text"
                            }
                        }
                    },
                    "unhideonturn": {
                        "condition": "abs(cameraDir-heading)*( (abs(heading-cameraDir))<=355)-5",
                        "cross": {
                            "points": [
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
                                        -0.04,
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
                                        0.04,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "PlaneW",
                                    [
                                        0,
                                        -0.019708
                                    ],
                                    1
                                ],
                                [
                                    "PlaneW",
                                    [
                                        0,
                                        -0.0394161
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "PlaneW",
                                    [
                                        0,
                                        0.019708
                                    ],
                                    1
                                ],
                                [
                                    "PlaneW",
                                    [
                                        0,
                                        0.0394161
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        }
                    }
                },
                "ils": {
                    "condition": "ils",
                    "geartext": {
                        "align": "left",
                        "down": [
                            [
                                0.932,
                                0.885
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.932,
                                0.84
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.987,
                                0.84
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "GEAR",
                        "type": "text"
                    },
                    "glideslope": {
                        "airport": {
                            "points": [
                                [
                                    "airport1",
                                    1
                                ],
                                [
                                    "airport2",
                                    1
                                ],
                                [
                                    "airport4",
                                    1
                                ],
                                [
                                    "airport3",
                                    1
                                ],
                                [
                                    "airport1",
                                    1
                                ]
                            ],
                            "type": "line"
                        },
                        "clipbr": [
                            1,
                            1
                        ],
                        "cliptl": [
                            0,
                            0
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        -0.0118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        0.0118248
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.06,
                                        -0.00886861
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.06,
                                        0.00886861
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        -0.0118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        0.0118248
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.06,
                                        -0.00886861
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.06,
                                        0.00886861
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        -0.0118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        0.0118248
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        -0.118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        0.118248
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        -0.012,
                                        -0.118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0.012,
                                        -0.118248
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        -0.009,
                                        -0.0591241
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0.009,
                                        -0.0591241
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        -0.012,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0.012,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        -0.009,
                                        0.0591241
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0.009,
                                        0.0591241
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        -0.012,
                                        0.118248
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0.012,
                                        0.118248
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 2
                        }
                    }
                },
                "incomingmissile": {
                    "blinkingpattern": [
                        0.3,
                        0.3
                    ],
                    "blinkingstartson": 1,
                    "condition": "incomingmissile",
                    "text": {
                        "align": "center",
                        "down": [
                            [
                                0.485,
                                0.266058
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.485,
                                0.216788
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.545,
                                0.216788
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "!INCOMING MISSILE!",
                        "type": "text"
                    }
                },
                "laser": {
                    "condition": "laseron",
                    "lasertext": {
                        "align": "left",
                        "down": [
                            [
                                0.932,
                                0.845
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.932,
                                0.8
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.987,
                                0.8
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "LASER",
                        "type": "text"
                    }
                },
                "machineguncrosshairgroup": {
                    "circle": {
                        "points": [
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0630657
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [
                                "MissileFlightTimeRot1",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot2",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot3",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot4",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot5",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot6",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot7",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot8",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot9",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot10",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot11",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot12",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot13",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot14",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot15",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot16",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot17",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot18",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot19",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot20",
                                [
                                    0,
                                    0.08
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ],
                            [
                                "MissileFlightTimeRot20",
                                [
                                    0,
                                    0.064
                                ],
                                1,
                                "ImpactPointRelative",
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 6
                    },
                    "circle_min_range": {
                        "points": [
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.013888,
                                    -0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.02736,
                                    -0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.04,
                                    -0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.051424,
                                    -0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.06128,
                                    -0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.06928,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.075176,
                                    -0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.078784,
                                    -0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.08,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.078784,
                                    0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.075176,
                                    0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.06928,
                                    0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.06128,
                                    0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.051424,
                                    0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.04,
                                    0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.02736,
                                    0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.013888,
                                    0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    0.0788321
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.013888,
                                    0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.02736,
                                    0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.04,
                                    0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.051424,
                                    0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.06128,
                                    0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.06928,
                                    0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.075176,
                                    0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.078784,
                                    0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.08,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.078784,
                                    -0.0136853
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.075176,
                                    -0.0269606
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.06928,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.06128,
                                    -0.0506733
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.051424,
                                    -0.0603854
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.04,
                                    -0.0682686
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.02736,
                                    -0.0740785
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.013888,
                                    -0.0776339
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 3
                    },
                    "condition": "-2+(mgun+rocket)*ImpactDistance",
                    "distance": {
                        "align": "center",
                        "down": [
                            "ImpactPointRelative",
                            [
                                -0.002,
                                0.15
                            ],
                            1
                        ],
                        "max": 15,
                        "pos": [
                            "ImpactPointRelative",
                            [
                                -0.002,
                                0.11
                            ],
                            1
                        ],
                        "right": [
                            "ImpactPointRelative",
                            [
                                0.045,
                                0.11
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "ImpactDistance",
                        "sourceprecision": 1,
                        "sourcescale": 0.001,
                        "type": "text"
                    },
                    "machineguncrosshair": {
                        "points": [
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0886861
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0788321
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    0.0886861
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    0.0788321
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.09,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.08,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPointRelative",
                                [
                                    0.09,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.08,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    -0.0019708
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0,
                                    0.0019708
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPointRelative",
                                [
                                    -0.002,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPointRelative",
                                [
                                    0.002,
                                    0
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 3
                    },
                    "type": "group"
                },
                "maincenterline1": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.49,
                                "0 + 0.025"
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.49,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.45,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "maincenterline2": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.33,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.25,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "maincenterline3": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                0.49,
                                "0 + 0.025"
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.49,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.25,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "mguntext": {
                    "condition": "mgun",
                    "weaponstext": {
                        "align": "right",
                        "down": [
                            [
                                0.032,
                                0.885
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.032,
                                0.84
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.087,
                                0.84
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "GUN",
                        "type": "text"
                    }
                },
                "pitchnumber": {
                    "align": "right",
                    "down": [
                        "PlaneW",
                        [
                            -0.39,
                            "-0.076 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.39,
                            -0.076
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.39 + 0.04",
                            -0.076
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "horizonDive",
                    "sourcescale": 57.2958,
                    "type": "text"
                },
                "pitchtext": {
                    "align": "left",
                    "down": [
                        "PlaneW",
                        [
                            -0.41,
                            "-0.076 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.41,
                            -0.076
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.41 + 0.04",
                            -0.076
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "text": "P:",
                    "type": "text"
                },
                "planemovementcrosshair": {
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
                                0.01,
                                -0.01732
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0.01732,
                                -0.01
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
                                0.01732,
                                0.01
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0.01,
                                0.01732
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
                                -0.01,
                                0.01732
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                -0.01732,
                                0.01
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
                                -0.01732,
                                -0.01
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                -0.01,
                                -0.01732
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
                        ],
                        [],
                        [
                            "Velocity",
                            [
                                0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                -0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                0,
                                -0.04
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
                    "type": "line",
                    "width": 3
                },
                "planew": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        1
                    ],
                    "points": [
                        [
                            "PlaneOrientation",
                            [
                                -0.04,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                -0.015,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                -0.0075,
                                0.015
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                0.0075,
                                0.015
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                0.015,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneOrientation",
                            [
                                0.04,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "radarboxes": {
                    "points": [
                        [
                            [
                                -0.002,
                                -0.002
                            ],
                            1
                        ],
                        [
                            [
                                0.002,
                                -0.002
                            ],
                            1
                        ],
                        [
                            [
                                0.002,
                                0.002
                            ],
                            1
                        ],
                        [
                            [
                                -0.002,
                                0.002
                            ],
                            1
                        ],
                        [
                            [
                                -0.002,
                                -0.002
                            ],
                            1
                        ]
                    ],
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.773,
                        0.773
                    ],
                    "type": "radartoview",
                    "width": 4
                },
                "rocketcrosshairgroup": {
                    "condition": "Rocket",
                    "distance": {
                        "align": "center",
                        "down": [
                            "ImpactPoint",
                            [
                                -0.002,
                                0.11
                            ],
                            1
                        ],
                        "max": 15,
                        "pos": [
                            "ImpactPoint",
                            [
                                -0.002,
                                0.07
                            ],
                            1
                        ],
                        "right": [
                            "ImpactPoint",
                            [
                                0.045,
                                0.07
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "ImpactDistance",
                        "sourceprecision": 1,
                        "sourcescale": 0.001,
                        "type": "text"
                    },
                    "machineguncrosshair": {
                        "points": [
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.019708
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.019708
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    -0.04,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0.04,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0.01,
                                    -0.0394161
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    -0.01,
                                    -0.0394161
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    -0.0019708
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0,
                                    0.0019708
                                ],
                                1
                            ],
                            [],
                            [
                                "ImpactPoint",
                                [
                                    -0.002,
                                    0
                                ],
                                1
                            ],
                            [
                                "ImpactPoint",
                                [
                                    0.002,
                                    0
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 3
                    },
                    "type": "group"
                },
                "rollnumber": {
                    "align": "right",
                    "down": [
                        "PlaneW",
                        [
                            -0.39,
                            "-0.025 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.39,
                            -0.025
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.39 + 0.04",
                            -0.025
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "horizonBank",
                    "sourcescale": 57.2958,
                    "type": "text"
                },
                "rolltext": {
                    "align": "left",
                    "down": [
                        "PlaneW",
                        [
                            -0.41,
                            "-0.025 + 0.05"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.41,
                            -0.025
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            "-0.41 + 0.04",
                            -0.025
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "text": "R:",
                    "type": "text"
                },
                "speedindicatorbox": {
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.49,
                                -0.25
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.49,
                                -0.2
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.3,
                                -0.2
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.3,
                                -0.25
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.49,
                                -0.25
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "speednumber": {
                    "align": "center",
                    "down": [
                        "PlaneW",
                        [
                            -0.4,
                            -0.2
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneW",
                        [
                            -0.4,
                            -0.25
                        ],
                        1
                    ],
                    "right": [
                        "PlaneW",
                        [
                            -0.3,
                            -0.25
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                },
                "stallgroup": {
                    "blinkingpattern": [
                        0.2,
                        0.2
                    ],
                    "blinkingstartson": 1,
                    "color": [
                        1,
                        0,
                        0
                    ],
                    "condition": "stall",
                    "stalltext": {
                        "align": "center",
                        "down": [
                            [
                                0.5,
                                0.29
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.5,
                                0.25
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.54,
                                0.25
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "STALL",
                        "type": "text"
                    },
                    "type": "group"
                },
                "tailhook": {
                    "condition": "user4",
                    "tailhooktext": {
                        "align": "left",
                        "down": [
                            [
                                0.932,
                                0.925
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.932,
                                0.88
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.987,
                                0.88
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "TAILHOOK",
                        "type": "text"
                    }
                },
                "targetdiamond": {
                    "shape": {
                        "points": [
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.02,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.02,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.02,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.02,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.02,
                                    0.02
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "targetingpodgroup": {
                    "condition": "1-pilotcameralock",
                    "targetingpoddir": {
                        "points": [
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0208056,
                                    0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0208056,
                                    -0.00407807
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0208056,
                                    -0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0208056,
                                    0.00407808
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0176381,
                                    0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0117854,
                                    0.0173806
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.00413849,
                                    0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.00413849,
                                    0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0117854,
                                    0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0176381,
                                    0.0116134
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0208056,
                                    0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0208056,
                                    -0.00407808
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.0117854,
                                    -0.0173807
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0041385,
                                    -0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodDir",
                                1,
                                [
                                    -0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [],
                            []
                        ],
                        "type": "line",
                        "width": 3
                    }
                },
                "targetingpodgroupon": {
                    "condition": "pilotcameralock",
                    "targetingpoddir": {
                        "points": [
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0208056,
                                    0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0208056,
                                    -0.00407807
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0208056,
                                    -0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0208056,
                                    0.00407808
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0176381,
                                    0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0117854,
                                    0.0173806
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.00413849,
                                    0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.00413849,
                                    0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0117854,
                                    0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0176381,
                                    0.0116134
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0208056,
                                    0.00407807
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0208056,
                                    -0.00407808
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.0117854,
                                    -0.0173807
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.00413849,
                                    -0.0205019
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0041385,
                                    -0.0205019
                                ],
                                1
                            ],
                            [],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0117854,
                                    -0.0173806
                                ],
                                1
                            ],
                            [
                                "TargetingPodTarget",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.0176381,
                                    -0.0116134
                                ],
                                1
                            ],
                            [],
                            []
                        ],
                        "type": "line",
                        "width": 3
                    }
                },
                "targetlocked": {
                    "condition": "missilelocked",
                    "shape": {
                        "points": [
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    -0.029562
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.03,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    0.029562
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.03,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    -0.029562
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "targetlocking": {
                    "blinkingpattern": [
                        0.2,
                        0.2
                    ],
                    "blinkingstartson": 1,
                    "condition": "missilelocking",
                    "shape": {
                        "points": [
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    -0.029562
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0.03,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    0.029562
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    -0.03,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                1,
                                "Limit0109",
                                1,
                                [
                                    0,
                                    -0.029562
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "weaponstext": {
                    "condition": "1- mgun",
                    "weaponstext": {
                        "align": "right",
                        "down": [
                            [
                                0.032,
                                0.885
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.032,
                                0.84
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.087,
                                0.84
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "weapon",
                        "sourcescale": 1,
                        "type": "text"
                    }
                },
                "width": 1,
                "wp": {
                    "condition": "wpvalid",
                    "wpdist": {
                        "align": "right",
                        "down": [
                            [
                                0.924,
                                0.542464
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.924,
                                0.505018
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.964,
                                0.505018
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "wpdist",
                        "sourceprecision": 1,
                        "sourcescale": 0.001,
                        "type": "text"
                    },
                    "wpindex": {
                        "align": "right",
                        "down": [
                            [
                                0.877,
                                0.542464
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.877,
                                0.505018
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.917,
                                0.505018
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "wpIndex",
                        "sourcelength": 2,
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "wpkm": {
                        "align": "left",
                        "down": [
                            [
                                "0.825+0.09",
                                0.5415
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.825+0.09",
                                0.5065
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.955,
                                0.5065
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": ":",
                        "type": "text"
                    },
                    "wpstatic": {
                        "align": "right",
                        "down": [
                            [
                                "0.825+0.01",
                                0.5415
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.825+0.01",
                                0.5065
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.875,
                                0.5065
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "WP",
                        "type": "text"
                    }
                }
            },
            "enableparallax": 0,
            "helmetdown": [
                0,
                -0.065,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.0325,
                0.0325,
                0.1
            ],
            "helmetright": [
                0.065,
                0,
                0
            ],
            "pos10vector": {
                "pos0": [
                    0.5,
                    0.5
                ],
                "pos10": [
                    1.225,
                    1.1
                ],
                "type": "vector"
            },
            "topleft": "HUD LH",
            "topright": "HUD PH"
        },
        "fa18_mfd_central": {
            "bones": {
                "center": {
                    "pos": [
                        0.37,
                        0.37
                    ],
                    "type": "fixed"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_1_BL",
            "color": [
                0.082,
                0.408,
                0.039,
                1
            ],
            "draw": {
                "alpha": 1,
                "ammotext": {
                    "align": "center",
                    "down": [
                        [
                            "0.49 - 0.015",
                            0.825
                        ],
                        1
                    ],
                    "pos": [
                        [
                            "0.49 - 0.015",
                            0.76
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.545,
                            0.76
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "cm_ammo": {
                    "align": "left",
                    "down": [
                        [
                            0.285,
                            0.211
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.285,
                            0.16
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.345,
                            0.16
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "CMAmmo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "cm_name": {
                    "align": "left",
                    "down": [
                        [
                            0.285,
                            0.171
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.285,
                            0.12
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.345,
                            0.12
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "CMWeapon",
                    "sourcescale": 1,
                    "type": "text"
                },
                "color": [
                    0,
                    0.12,
                    0
                ],
                "condition": "on",
                "gatling_ammo": {
                    "align": "center",
                    "down": [
                        [
                            0.49,
                            0.331
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.49,
                            0.27
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.56,
                            0.27
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcescale": 1,
                    "type": "text"
                },
                "pylon1": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.83,
                            0.5
                        ],
                        1
                    ],
                    "pylon": 1,
                    "type": "pylonicon"
                },
                "pylon10": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.395,
                            0.55
                        ],
                        1
                    ],
                    "pylon": 10,
                    "type": "pylonicon"
                },
                "pylon11": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.53,
                            0.52
                        ],
                        1
                    ],
                    "pylon": 11,
                    "type": "pylonicon"
                },
                "pylon12": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.46,
                            0.52
                        ],
                        1
                    ],
                    "pylon": 12,
                    "type": "pylonicon"
                },
                "pylon2": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.16,
                            0.5
                        ],
                        1
                    ],
                    "pylon": 2,
                    "type": "pylonicon"
                },
                "pylon3": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.715,
                            0.44
                        ],
                        1
                    ],
                    "pylon": 3,
                    "type": "pylonicon"
                },
                "pylon4": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.275,
                            0.44
                        ],
                        1
                    ],
                    "pylon": 4,
                    "type": "pylonicon"
                },
                "pylon5": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.615,
                            0.37
                        ],
                        1
                    ],
                    "pylon": 5,
                    "type": "pylonicon"
                },
                "pylon6": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.375,
                            0.37
                        ],
                        1
                    ],
                    "pylon": 6,
                    "type": "pylonicon"
                },
                "pylon7": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.665,
                            0.58
                        ],
                        1
                    ],
                    "pylon": 7,
                    "type": "pylonicon"
                },
                "pylon8": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.325,
                            0.58
                        ],
                        1
                    ],
                    "pylon": 8,
                    "type": "pylonicon"
                },
                "pylon9": {
                    "name": "Plane_Fighter_01",
                    "pos": [
                        [
                            0.595,
                            0.55
                        ],
                        1
                    ],
                    "pylon": 9,
                    "type": "pylonicon"
                },
                "pylontext1": {
                    "align": "center",
                    "down": [
                        [
                            "0.49 - 0.015",
                            0.705
                        ],
                        1
                    ],
                    "pos": [
                        [
                            "0.49 - 0.015",
                            0.66
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.525,
                            0.66
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "SELECTED WEAPON",
                    "type": "text"
                },
                "static": {
                    "points": [
                        [
                            [
                                0.11,
                                0.12
                            ],
                            1
                        ],
                        [
                            [
                                0.33,
                                0.12
                            ],
                            1
                        ],
                        [
                            [
                                0.33,
                                0.22
                            ],
                            1
                        ],
                        [
                            [
                                0.11,
                                0.22
                            ],
                            1
                        ],
                        [
                            [
                                0.11,
                                0.12
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 4
                },
                "weapontext": {
                    "align": "center",
                    "down": [
                        [
                            "0.49 - 0.015",
                            0.765
                        ],
                        1
                    ],
                    "pos": [
                        [
                            "0.49 - 0.015",
                            0.7
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.545,
                            0.7
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "weapon",
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR"
        },
        "fa18_mfd_horizon": {
            "bones": {
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm20": {
                    "angle": -20,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm25": {
                    "angle": -25,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm30": {
                    "angle": -30,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm35": {
                    "angle": -35,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm40": {
                    "angle": -40,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm45": {
                    "angle": -45,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm50": {
                    "angle": -50,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm60": {
                    "angle": -60,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm70": {
                    "angle": -70,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm80": {
                    "angle": -80,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelm90": {
                    "angle": -90,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp20": {
                    "angle": 20,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp25": {
                    "angle": 25,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp30": {
                    "angle": 30,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp35": {
                    "angle": 35,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp40": {
                    "angle": 40,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp45": {
                    "angle": 45,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp50": {
                    "angle": 50,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp60": {
                    "angle": 60,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp70": {
                    "angle": 70,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp80": {
                    "angle": 80,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "levelp90": {
                    "angle": 90,
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos10": [
                        0.774,
                        0.67
                    ],
                    "type": "horizon"
                },
                "planeorientation": {
                    "pos": [
                        0.5,
                        0.4
                    ],
                    "type": "fixed"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.53
                    ],
                    "pos10": [
                        1.5,
                        1.53
                    ],
                    "source": "velocityToView",
                    "type": "vector"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.555
                    ],
                    "pos10": [
                        1.5,
                        1.555
                    ],
                    "source": "weapon",
                    "type": "vector"
                }
            },
            "borderbottom": 0.1,
            "borderleft": 0.1,
            "borderright": 0.1,
            "bordertop": 0.1,
            "bottomleft": "mfd ld",
            "color": [
                0.082,
                0.408,
                0.039,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.082,
                    0.408,
                    0.039,
                    1
                ],
                "condition": "on",
                "enableparallax": 0,
                "horizont": {
                    "clipbr": [
                        0.845,
                        0.725
                    ],
                    "cliptl": [
                        0.255,
                        0.105
                    ],
                    "dimmed": {
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        0.75,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.75,
                                        0
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm10": {
                            "points": [
                                [
                                    "LevelM10",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm15": {
                            "points": [
                                [
                                    "LevelM15",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm20": {
                            "points": [
                                [
                                    "LevelM20",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm25": {
                            "points": [
                                [
                                    "LevelM25",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm30": {
                            "points": [
                                [
                                    "LevelM30",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm35": {
                            "points": [
                                [
                                    "LevelM35",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm40": {
                            "points": [
                                [
                                    "LevelM40",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm45": {
                            "points": [
                                [
                                    "LevelM45",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm5": {
                            "points": [
                                [
                                    "LevelM5",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm50": {
                            "points": [
                                [
                                    "LevelM50",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm60": {
                            "points": [
                                [
                                    "LevelM60",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM60",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM60",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm70": {
                            "points": [
                                [
                                    "LevelM70",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM70",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM70",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm80": {
                            "points": [
                                [
                                    "LevelM80",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM80",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM80",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm90": {
                            "points": [
                                [
                                    "LevelM90",
                                    [
                                        -0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        -0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        -0.055,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.235,
                                        -0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.235,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.22,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.205,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.19,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.175,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.16,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.145,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.115,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.085,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM90",
                                    [
                                        0.07,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM90",
                                    [
                                        0.055,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp10": {
                            "points": [
                                [
                                    "LevelP10",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP10",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP10",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP10",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP10",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP10",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp15": {
                            "points": [
                                [
                                    "LevelP15",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP15",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP15",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP15",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP15",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP15",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp20": {
                            "points": [
                                [
                                    "LevelP20",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP20",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp25": {
                            "points": [
                                [
                                    "LevelP25",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP25",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp30": {
                            "points": [
                                [
                                    "LevelP30",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP30",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp35": {
                            "points": [
                                [
                                    "LevelP35",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP35",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp40": {
                            "points": [
                                [
                                    "LevelP40",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP40",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp45": {
                            "points": [
                                [
                                    "LevelP45",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP45",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp5": {
                            "points": [
                                [
                                    "LevelP5",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP5",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp50": {
                            "points": [
                                [
                                    "LevelP50",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP50",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp60": {
                            "points": [
                                [
                                    "LevelP60",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP60",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP60",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP60",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP60",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP60",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp70": {
                            "points": [
                                [
                                    "LevelP70",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP70",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP70",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP70",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP70",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP70",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp80": {
                            "points": [
                                [
                                    "LevelP80",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP80",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP80",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP80",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP80",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP80",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp90": {
                            "points": [
                                [
                                    "LevelP90",
                                    [
                                        "-0.22-0.015",
                                        0.02
                                    ],
                                    1
                                ],
                                [
                                    "LevelP90",
                                    [
                                        "-0.22-0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP90",
                                    [
                                        -0.06,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP90",
                                    [
                                        0.06,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP90",
                                    [
                                        "+0.22+0.015",
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP90",
                                    [
                                        "+0.22+0.015",
                                        0.02
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "valm_1_10": {
                            "align": "left",
                            "down": [
                                "LevelM10",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_1_10_r": {
                            "align": "right",
                            "down": [
                                "LevelM10",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_1_15": {
                            "align": "left",
                            "down": [
                                "LevelM15",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_1_15_r": {
                            "align": "right",
                            "down": [
                                "LevelM15",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_1_20": {
                            "align": "left",
                            "down": [
                                "LevelM20",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_1_20_r": {
                            "align": "right",
                            "down": [
                                "LevelM20",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_1_25": {
                            "align": "left",
                            "down": [
                                "LevelM25",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_1_25_r": {
                            "align": "right",
                            "down": [
                                "LevelM25",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_1_30": {
                            "align": "left",
                            "down": [
                                "LevelM30",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_1_30_r": {
                            "align": "right",
                            "down": [
                                "LevelM30",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_1_35": {
                            "align": "left",
                            "down": [
                                "LevelM35",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_1_35_r": {
                            "align": "right",
                            "down": [
                                "LevelM35",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_1_40": {
                            "align": "left",
                            "down": [
                                "LevelM40",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_1_40_r": {
                            "align": "right",
                            "down": [
                                "LevelM40",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_1_45": {
                            "align": "left",
                            "down": [
                                "LevelM45",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_1_45_r": {
                            "align": "right",
                            "down": [
                                "LevelM45",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_1_5": {
                            "align": "left",
                            "down": [
                                "LevelM5",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_1_50": {
                            "align": "left",
                            "down": [
                                "LevelM50",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valm_1_50_r": {
                            "align": "right",
                            "down": [
                                "LevelM50",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valm_1_5_r": {
                            "align": "right",
                            "down": [
                                "LevelM5",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_1_60": {
                            "align": "left",
                            "down": [
                                "LevelM60",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM60",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM60",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -60,
                            "type": "text"
                        },
                        "valm_1_60_r": {
                            "align": "right",
                            "down": [
                                "LevelM60",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM60",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM60",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -60,
                            "type": "text"
                        },
                        "valm_1_70": {
                            "align": "left",
                            "down": [
                                "LevelM70",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM70",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM70",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -70,
                            "type": "text"
                        },
                        "valm_1_70_r": {
                            "align": "right",
                            "down": [
                                "LevelM70",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM70",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM70",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -70,
                            "type": "text"
                        },
                        "valm_1_80": {
                            "align": "left",
                            "down": [
                                "LevelM80",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM80",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM80",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -80,
                            "type": "text"
                        },
                        "valm_1_80_r": {
                            "align": "right",
                            "down": [
                                "LevelM80",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM80",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM80",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -80,
                            "type": "text"
                        },
                        "valm_1_90": {
                            "align": "left",
                            "down": [
                                "LevelM90",
                                [
                                    -0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM90",
                                [
                                    -0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM90",
                                [
                                    -0.2,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -90,
                            "type": "text"
                        },
                        "valm_1_90_r": {
                            "align": "right",
                            "down": [
                                "LevelM90",
                                [
                                    0.26,
                                    0.018
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM90",
                                [
                                    0.26,
                                    -0.032
                                ],
                                1
                            ],
                            "right": [
                                "LevelM90",
                                [
                                    0.32,
                                    -0.032
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -90,
                            "type": "text"
                        },
                        "valp_1_10": {
                            "align": "left",
                            "down": [
                                "LevelP10",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_1_10_r": {
                            "align": "right",
                            "down": [
                                "LevelP10",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_1_15": {
                            "align": "left",
                            "down": [
                                "LevelP15",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_1_15_r": {
                            "align": "right",
                            "down": [
                                "LevelP15",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_1_20": {
                            "align": "left",
                            "down": [
                                "LevelP20",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_1_20_r": {
                            "align": "right",
                            "down": [
                                "LevelP20",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_1_25": {
                            "align": "left",
                            "down": [
                                "LevelP25",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_1_25_r": {
                            "align": "right",
                            "down": [
                                "LevelP25",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_1_30": {
                            "align": "left",
                            "down": [
                                "LevelP30",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_1_30_r": {
                            "align": "right",
                            "down": [
                                "LevelP30",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_1_35": {
                            "align": "left",
                            "down": [
                                "LevelP35",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_1_35_r": {
                            "align": "right",
                            "down": [
                                "LevelP35",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_1_40": {
                            "align": "left",
                            "down": [
                                "LevelP40",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_1_40_r": {
                            "align": "right",
                            "down": [
                                "LevelP40",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_1_45": {
                            "align": "left",
                            "down": [
                                "LevelP45",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_1_45_r": {
                            "align": "right",
                            "down": [
                                "LevelP45",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_1_5": {
                            "align": "left",
                            "down": [
                                "LevelP5",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_1_50": {
                            "align": "left",
                            "down": [
                                "LevelP50",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "50",
                            "type": "text"
                        },
                        "valp_1_50_r": {
                            "align": "right",
                            "down": [
                                "LevelP50",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "50",
                            "type": "text"
                        },
                        "valp_1_5_r": {
                            "align": "right",
                            "down": [
                                "LevelP5",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_1_60": {
                            "align": "left",
                            "down": [
                                "LevelP60",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP60",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP60",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "60",
                            "type": "text"
                        },
                        "valp_1_60_r": {
                            "align": "right",
                            "down": [
                                "LevelP60",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP60",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP60",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "60",
                            "type": "text"
                        },
                        "valp_1_70": {
                            "align": "left",
                            "down": [
                                "LevelP70",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP70",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP70",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "70",
                            "type": "text"
                        },
                        "valp_1_70_r": {
                            "align": "right",
                            "down": [
                                "LevelP70",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP70",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP70",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "70",
                            "type": "text"
                        },
                        "valp_1_80": {
                            "align": "left",
                            "down": [
                                "LevelP80",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP80",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP80",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "80",
                            "type": "text"
                        },
                        "valp_1_80_r": {
                            "align": "right",
                            "down": [
                                "LevelP80",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP80",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP80",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "80",
                            "type": "text"
                        },
                        "valp_1_90": {
                            "align": "left",
                            "down": [
                                "LevelP90",
                                [
                                    -0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP90",
                                [
                                    -0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP90",
                                [
                                    -0.2,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "90",
                            "type": "text"
                        },
                        "valp_1_90_r": {
                            "align": "right",
                            "down": [
                                "LevelP90",
                                [
                                    0.26,
                                    0.033
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP90",
                                [
                                    0.26,
                                    -0.017
                                ],
                                1
                            ],
                            "right": [
                                "LevelP90",
                                [
                                    0.32,
                                    -0.017
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "90",
                            "type": "text"
                        }
                    }
                }
            },
            "enableparallax": 0,
            "pos10vector": {
                "pos0": [
                    0.5,
                    0.5
                ],
                "pos10": [
                    1.225,
                    1.1
                ],
                "type": "vector"
            },
            "topleft": "mfd lh",
            "topright": "mfd ph"
        },
        "fa18_mfd_horizon_numbers": {
            "bones": {
                "planeorientation": {
                    "pos": [
                        0.5,
                        0.5
                    ],
                    "type": "fixed"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd ld",
            "color": [
                0.082,
                0.408,
                0.039,
                1
            ],
            "draw": {
                "alpha": 0.7,
                "altnumber": {
                    "align": "center",
                    "down": [
                        "PlaneOrientation",
                        [
                            0.35,
                            "-0.47 + 0.145"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneOrientation",
                        [
                            0.35,
                            "-0.47 + 0.05"
                        ],
                        1
                    ],
                    "right": [
                        "PlaneOrientation",
                        [
                            "0.35 + 0.08",
                            "-0.47 + 0.05"
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "type": "text"
                },
                "asnumber": {
                    "align": "center",
                    "down": [
                        "PlaneOrientation",
                        [
                            -0.375,
                            "-0.47 + 0.145"
                        ],
                        1
                    ],
                    "pos": [
                        "PlaneOrientation",
                        [
                            -0.375,
                            "-0.47 + 0.05"
                        ],
                        1
                    ],
                    "right": [
                        "PlaneOrientation",
                        [
                            "-0.375 + 0.08",
                            "-0.47 + 0.05"
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                },
                "color": [
                    0.082,
                    0.408,
                    0.039,
                    1
                ],
                "condition": "on",
                "enableparallax": 0
            },
            "enableparallax": 0,
            "topleft": "mfd lh",
            "topright": "mfd ph"
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
    "mingforce": 0.3,
    "mingunelev": 0,
    "mingunturn": 0,
    "mintotaldamagethreshold": 0.005,
    "model": "A3/Air_F_Jets/Plane_Fighter_01/Plane_Fighter_01_F.p3d",
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
    "picture": "A3/Air_F_Jets/Plane_Fighter_01/Data/UI/Fighter01_picture_ca.paa",
    "pilotcamera": {
        "controllable": 1,
        "initelev": 25,
        "initturn": 0,
        "maxelev": 90,
        "maxmousexrotspeed": 0.5,
        "maxmouseyrotspeed": 0.5,
        "maxturn": 180,
        "maxxrotspeed": 1,
        "maxyrotspeed": 1,
        "minelev": -10,
        "minturn": -180,
        "opticsin": {
            "medium": {
                "directionstabilized": 1,
                "gunneropticsmodel": "A3/Drones_F/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_medium_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": "(14.4 / 120)",
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": "(14.4 / 120)",
                "minanglex": 0,
                "minangley": 0,
                "minfov": "(14.4 / 120)",
                "opticsdisplayname": "MFOV",
                "opticsppeffects": [
                    "OpticsCHAbera2",
                    "OpticsBlur2"
                ],
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
                "gunneropticsmodel": "A3/Drones_F/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_narrow_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": "(4.8 / 120)",
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": "(4.8 / 120)",
                "minanglex": 0,
                "minangley": 0,
                "minfov": "(4.8 / 120)",
                "opticsdisplayname": "NFOV",
                "opticsppeffects": [
                    "OpticsCHAbera2",
                    "OpticsBlur2"
                ],
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
                "gunneropticsmodel": "A3/Drones_F/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_wide_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": "(75 / 120)",
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": "(75 / 120)",
                "minanglex": 0,
                "minangley": 0,
                "minfov": "(75 / 120)",
                "opticsdisplayname": "WFOV",
                "opticsppeffects": [
                    "OpticsCHAbera2",
                    "OpticsBlur2"
                ],
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
        "pilotopticsshowcursor": 1
    },
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 1,
    "precision": 200,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 0.8,
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
            "hitpoint": "gear_f_lights",
            "innerangle": 15,
            "intensity": 500000,
            "outerangle": 50,
            "position": "pos_gear_front_light",
            "selection": "gear_f_lights",
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
        0.5,
        1.8,
        2.6,
        2.75,
        2.8,
        2.85,
        2.9,
        2.95,
        2.98,
        3.01,
        2.7,
        1.1,
        0.9,
        0.7,
        0.5,
        0.3
    ],
    "ruddercontrolssensitivitycoef": 4,
    "rudderinfluence": 0.766,
    "scope": 0,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "autobacklit",
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
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/B_PLANE_FIGHTER_01_engine_shut_ext",
        1.75,
        1,
        300
    ],
    "soundengineoffint": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/B_PLANE_FIGHTER_01_engine_shut_int",
        1,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/B_PLANE_FIGHTER_01_engine_start_ext",
        1.75,
        1,
        300
    ],
    "soundengineonint": [
        "A3/Sounds_F_Jets/vehicles/air/Plane_Fighter_01/B_PLANE_FIGHTER_01_engine_start_int",
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
            "Plane_Fighter_01_EngineLowExt_SoundSet",
            "Plane_Fighter_01_EngineHighExt_SoundSet",
            "Plane_Fighter_01_ForsageExt_SoundSet",
            "Plane_Fighter_01_WindNoiseExt_SoundSet",
            "Plane_Fighter_01_EngineExt_Dist_Front_SoundSet",
            "Plane_Fighter_01_EngineExt_Middle_SoundSet",
            "Plane_Fighter_01_EngineExt_Dist_Rear_SoundSet",
            "Plane_Fighter_01_EngineLowInt_SoundSet",
            "Plane_Fighter_01_EngineHighInt_SoundSet",
            "Plane_Fighter_01_ForsageInt_SoundSet",
            "Plane_Fighter_01_WindNoiseInt_SoundSet",
            "Plane_Fighter_01_VelocityInt_SoundSet"
        ]
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundsetsonicboom": [
        "Plane_Fighter_SonicBoom_SoundSet"
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
                "veh_air_plane_p"
            ],
            "speechsingular": [
                "veh_air_plane_s"
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
    "stallspeed": 220,
    "stallwarningtreshold": 0.12,
    "steeraheadplan": 2,
    "steeraheadsimul": 1,
    "supplyradius": 2,
    "tailhook": 1,
    "tbody": 150,
    "textplural": "fast movers",
    "textsingular": "fast mover",
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
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_01_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_02_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_glass_01_ca.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_01_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_02_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_03_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_05_co.paa"
            ]
        },
        "darkgreycamo": {
            "author": "Bravo Zero One Studios",
            "displayname": "Dark Grey [Camo]",
            "factions": [
                "BLU_F"
            ],
            "textures": [
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_01_Camo_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_fuselage_02_Camo_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_glass_01_ca.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_01_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_02_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_03_co.paa",
                "a3/air_f_jets/plane_fighter_01/data/fighter_01_cockpit_05_co.paa"
            ]
        }
    },
    "threat": [
        0.1,
        1,
        0.5
    ],
    "thrustcoef": [
        1.76,
        1.69,
        1.62,
        1.68,
        1.74,
        1.81,
        1.89,
        1.95,
        1.96,
        1.96,
        1.92,
        1.4,
        0.4,
        0,
        0,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {},
    "transportmagazines": {},
    "transportmaxbackpacks": 6,
    "transportmaxmagazines": 24,
    "transportmaxweapons": 6,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {},
    "type": 2,
    "typicalcargo": [
        "B_Fighter_Pilot_F"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscOptics_CAS_Pilot",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "plane_fighter_01_eject": {
            "condition": "player in this && {speed this > 1}",
            "displayname": "Eject",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "priority": 0.05,
            "radius": 10,
            "shortcut": "Eject",
            "showwindow": 0,
            "statement": "[this] spawn bis_fnc_planeEjection"
        },
        "plane_fighter_01_fold_wings": {
            "condition": "this animationPhase 'wing_fold_l' < 0.1 and (speed this) < 40 and player in this",
            "displayname": "Fold Wings",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "priority": 0.05,
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate ['wing_fold_l',1]; this animate ['wing_fold_r',1]; this animate ['wing_fold_cover_l',1]; this animate ['wing_fold_cover_r',1]; this say3D 'Plane_Fighter_01_foldwing_sound'"
        },
        "plane_fighter_01_tailhook_down": {
            "condition": "this animationPhase 'tailhook' > 0.1  and {speed this > 100}",
            "displayname": "Tailhook Down",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "priority": 0.05,
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate ['tailhook',0]; this animate ['tailhook_door_l',0]; this animate ['tailhook_door_r',0]; this say 'Plane_Fighter_01_tailhook_down_sound'; this say3D 'Plane_Fighter_01_tailhook_down_sound';this SetUserMFDvalue [4,1]; [this] spawn BIS_fnc_AircraftTailhook;"
        },
        "plane_fighter_01_tailhook_up": {
            "condition": "this animationPhase 'tailhook' < 0.1",
            "displayname": "Tailhook Up",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "priority": 0.05,
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate ['tailhook',1]; this animate ['tailhook_door_l',1]; this animate ['tailhook_door_r',1]; this say 'Plane_Fighter_01_tailhook_up_sound'; this SetUserMFDvalue [4,0];this say3D 'Plane_Fighter_01_tailhook_up_sound'"
        },
        "plane_fighter_01_unfold_wings": {
            "condition": "this animationPhase 'wing_fold_l' > 0.9 and (speed this) < 40 and player in this",
            "displayname": "Unfold Wings",
            "hideonuse": 1,
            "onlyforplayer": 1,
            "position": "pilotcontrol",
            "priority": 0.05,
            "radius": 10,
            "shortcut": "",
            "showwindow": 0,
            "statement": "this animate ['wing_fold_l',0]; this animate ['wing_fold_r',0]; this animate ['wing_fold_cover_l',0]; this animate ['wing_fold_cover_r',0]; this say3D 'Plane_Fighter_01_foldwing_sound'"
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
        "initfov": 0.5,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 0.5,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 0.5,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.9,
        "maxanglex": 85,
        "maxangley": 130,
        "maxfov": 1.25,
        "maxmovex": 0.1,
        "maxmovey": 0.05,
        "maxmovez": 0.1,
        "minanglex": -40,
        "minangley": -130,
        "minfov": 0.25,
        "minmovex": -0.1,
        "minmovey": -0.025,
        "minmovez": -0.1,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1,
    "vtol": 0,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "vtolyawinfluence": 2,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 2.5,
    "waterlineardampingcoefx": 5,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.04,
    "weapons": [
        "weapon_Fighter_Gun20mm_AA",
        "Laserdesignator_pilotCamera",
        "CMFlareLauncher_Singles"
    ],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "wheels": {
        "wheel_1": {
            "bonename": "wheels_f",
            "boundary": "pos_wheels_f_rim",
            "center": "pos_wheels_f_center",
            "dampingrate": 0.25,
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
            "longitudinalstiffnessperunitgravity": 2000,
            "mass": 80,
            "maxbraketorque": 4000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 8.09629,
            "side": "left",
            "springdamperrate": 70000,
            "springstrength": 250000,
            "sprungmass": 2500,
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
            "dampingrate": 0.25,
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
            "longitudinalstiffnessperunitgravity": 2500,
            "mass": 80,
            "maxbraketorque": 10000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 8.09629,
            "side": "left",
            "springdamperrate": 88000,
            "springstrength": 370000,
            "sprungmass": 4250,
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
            "dampingrate": 0.25,
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
            "longitudinalstiffnessperunitgravity": 2500,
            "mass": 80,
            "maxbraketorque": 10000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "maxhandbraketorque": 0,
            "moi": 8.09629,
            "side": "right",
            "springdamperrate": 88000,
            "springstrength": 370000,
            "sprungmass": 4250,
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
    "wheelsteeringsensitivity": 4,
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