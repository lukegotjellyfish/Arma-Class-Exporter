d = {
    "_generalmacro": "C_Heli_light_01_shadow_F",
    "_mainbladecenter": "rotor_center",
    "access": 0,
    "accuracy": 1,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "airbrakefrictioncoef": 3,
    "aircapacity": 10,
    "airfrictioncoefs0": [
        0,
        0,
        0
    ],
    "airfrictioncoefs1": [
        0.1,
        0.05,
        0.006
    ],
    "airfrictioncoefs2": [
        0.001,
        0.0005,
        6e-05
    ],
    "allowtablock": 1,
    "altfullforce": 2000,
    "altnoforce": 6000,
    "alwaystarget": 0,
    "animated": 1,
    "animationlist": [
        "AddDoors",
        0.9,
        "AddBackseats",
        0.9,
        "AddTread_Short",
        0.5,
        "AddTread",
        0.4
    ],
    "animationsources": {
        "addbackseats": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add back seats",
            "initphase": 1,
            "lockcargo": [
                0,
                1
            ],
            "lockcargoanimationphase": 0,
            "mass": 150,
            "scope": 2,
            "source": "user"
        },
        "addbenches": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add benches",
            "forceanimate": [
                "BenchL_Up_instant",
                0,
                "BenchR_Up_instant",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "lockcargo": [
                2,
                3,
                4,
                5
            ],
            "lockcargoanimationphase": 0,
            "mass": "_EVAL(120*2)",
            "scope": 0,
            "source": "user"
        },
        "addcargohook": {
            "animperiod": 1e-07,
            "initphase": 0,
            "iscomponent": 1,
            "source": "user"
        },
        "addcargohook_cover": {
            "animperiod": 1e-07,
            "initphase": 1,
            "iscomponent": 1,
            "source": "user"
        },
        "addcivilian_hide": {
            "animperiod": 1e-06,
            "initphase": -1,
            "source": "user"
        },
        "adddoors": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add doors",
            "initphase": 1,
            "mass": 300,
            "onphasechanged": "if ((_this select 1) == 1) then {(_this select 0) enablePersonTurret [[0], false];} else {(_this select 0) enablePersonTurret [[0], true];};",
            "scope": 2,
            "source": "user"
        },
        "addgunholder": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add gun holder",
            "initphase": 0,
            "mass": 0,
            "scope": 0,
            "source": "user"
        },
        "addholdingframe": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add holding frame",
            "initphase": 0,
            "mass": 0,
            "scope": 0,
            "source": "user"
        },
        "addmusicunit": {
            "animperiod": 1e-06,
            "initphase": 1,
            "scope": 0,
            "source": "user"
        },
        "addscreen1": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "addtread": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add tread",
            "forceanimate": [
                "AddTread_Short",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 1,
            "mass": 90,
            "source": "user"
        },
        "addtread_short": {
            "animperiod": 1e-06,
            "author": "Bohemia Interactive",
            "displayname": "Add short tread",
            "forceanimate": [
                "AddTread",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "mass": 50,
            "source": "user"
        },
        "benchl_up": {
            "animperiod": 0.8,
            "author": "Bohemia Interactive",
            "displayname": "Fold left bench",
            "forceanimate": [
                "BenchL_Up_instant",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "lockcargo": [
                3,
                4
            ],
            "lockcargoanimationphase": 1,
            "scope": 0,
            "source": "user"
        },
        "benchl_up_instant": {
            "animperiod": 0.1,
            "author": "Bohemia Interactive",
            "displayname": "Fold left bench (instant)",
            "forceanimate": [
                "BenchL_Up",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "lockcargo": [
                3,
                4
            ],
            "lockcargoanimationphase": 1,
            "scope": 0,
            "source": "user"
        },
        "benchr_up": {
            "animperiod": 0.8,
            "author": "Bohemia Interactive",
            "displayname": "Fold right bench",
            "forceanimate": [
                "BenchR_Up_instant",
                1
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "lockcargo": [
                2,
                5
            ],
            "lockcargoanimationphase": 1,
            "scope": 0,
            "source": "user"
        },
        "benchr_up_instant": {
            "animperiod": 0.01,
            "author": "Bohemia Interactive",
            "displayname": "Fold right bench (instant)",
            "forceanimate": [
                "BenchR_Up",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "lockcargo": [
                2,
                5
            ],
            "lockcargoanimationphase": 1,
            "scope": 0,
            "source": "user"
        },
        "collisionlightred_source": {
            "markerlight": "CollisionRed",
            "source": "MarkerLight"
        },
        "collisionlightwhite_source": {
            "markerlight": "CollisionWhite",
            "source": "MarkerLight"
        },
        "doorl_back_open": {
            "animperiod": 0.8,
            "source": "user"
        },
        "doorl_front_open": {
            "animperiod": 0.8,
            "source": "user"
        },
        "doorr_back_open": {
            "animperiod": 0.8,
            "source": "user"
        },
        "doorr_front_open": {
            "animperiod": 0.8,
            "source": "user"
        },
        "flir_hrot": {
            "animperiod": 1e-07,
            "initphase": 0,
            "scope": 0,
            "source": "user"
        },
        "flir_vrot": {
            "animperiod": 1e-07,
            "initphase": 0,
            "scope": 0,
            "source": "user"
        },
        "gunl_revolving": {
            "animperiod": 1e-07,
            "initphase": 0,
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        "gunr_revolving": {
            "animperiod": 1e-07,
            "initphase": 0,
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        "hideweapons": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "hitbatteries": {
            "hitpoint": "HitBatteries",
            "raw": 1,
            "source": "hit"
        },
        "hitengine": {
            "hitpoint": "HitEngine",
            "raw": 1,
            "source": "hit"
        },
        "hitengine1": {
            "hitpoint": "HitEngine1",
            "raw": 1,
            "source": "hit"
        },
        "hitengine2": {
            "hitpoint": "HitEngine2",
            "raw": 1,
            "source": "hit"
        },
        "hitfuel": {
            "hitpoint": "HitFuel",
            "raw": 1,
            "source": "hit"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass10": {
            "hitpoint": "HitGlass10",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass9": {
            "hitpoint": "HitGlass9",
            "raw": 1,
            "source": "Hit"
        },
        "hithrotor": {
            "hitpoint": "HitHRotor",
            "raw": 1,
            "source": "hit"
        },
        "hithydraulics": {
            "hitpoint": "HitHydraulics",
            "raw": 1,
            "source": "hit"
        },
        "hittransmission": {
            "hitpoint": "HitTransmission",
            "raw": 1,
            "source": "hit"
        },
        "hitvrotor": {
            "hitpoint": "HitVRotor",
            "raw": 1,
            "source": "hit"
        },
        "hitwinch_source": {
            "hitpoint": "HitWinch",
            "raw": 1,
            "source": "hit"
        },
        "missiles_revolving": {
            "source": "revolving",
            "weapon": "missiles_DAR"
        },
        "muzzle_flash": {
            "animperiod": 1e-06,
            "source": "ammorandom",
            "weapon": "M134_minigun"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 30,
    "armorlights": 0.4,
    "armorstructural": 4,
    "armory": {
        "description": "$str_a3_cfgvehicles_b_heli_light_01_armory0"
    },
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "OpenHeliAttenuation",
    "audible": 50,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [
        "Transport"
    ],
    "backrotorforcecoef": 1,
    "backrotorspeed": 1.5,
    "bodyfrictioncoef": 0.3,
    "brakedistance": 200,
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
    "camerabegin": "rtd1_pos",
    "cameraend": "rtd1_dir",
    "camerasmoothspeed": 5,
    "camouflage": 100,
    "camshake": {
        "distance": 50,
        "frequency": 20,
        "minspeed": 50,
        "power": 30
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
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "ChopperLight_C_R_static_H",
        "ChopperLight_C_L_static_H"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        0
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
    "cargoprecisegetinout": [
        0
    ],
    "cargoproxyindexes": [
        11,
        10
    ],
    "cargospec": {
        "cargo1": {
            "showheadphones": 1
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
    "castcargoshadow": 1,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
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
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
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
    "cost": 10000000.0,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "C_man_1_1_F",
    "crewcrashprotection": 0.25,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "cyclicasideforcecoef": 1.3,
    "cyclicforwardforcecoef": 1,
    "damage": {
        "mat": [
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_CIV.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_destruct.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_UNIColor.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_UNIColor_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_UNIColor_destruct.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass_in.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_glass_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_int.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_int_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_int_destruct.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_detail.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_detail_damage.rvmat",
            "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_detail_destruct.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.01039,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "M-900 (Shadow)",
    "dlc": "Heli",
    "driveoncomponent": [
        "Skids"
    ],
    "driveraction": "Chopperlight_L_Static_H",
    "drivercaneject": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": 0,
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "lever_pilot",
    "driverleftleganimname": "pedalL",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "stick_pilot",
    "driverrightleganimname": "pedalR",
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
    "editorpreview": "A3/EditorPreviews_F/Data/CfgVehicles/C_Heli_Light_01_civil_F.jpg",
    "editorsubcategory": "EdSubcat_Helicopters",
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
    "enablesweep": 0,
    "enablewatch": 0,
    "engineer": 0,
    "envelope": [
        0,
        0.2,
        0.9,
        2.1,
        2.5,
        3.3,
        3.5,
        3.6,
        3.7,
        3.8,
        3.8,
        3,
        0.9,
        0.7,
        0.5
    ],
    "epeimpulsedamagecoef": 20,
    "eventhandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "postinit": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};"
    },
    "exhausts": {
        "exhaust01": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust1"
        }
    },
    "explosionshielding": 4,
    "extcameraparams": [
        -1
    ],
    "extcameraposition": [
        0,
        2,
        -15
    ],
    "faction": "CIV_F",
    "features": "Randomization: Yes, 15 skins, disabled by: this setVariable [`BIS_enableRandomization`,false];\t\t\t\t\t\t<br />Specific skin may be set by: this setVariable [`color`,X]; (the number ranges from 0 to 14)\t\t\t\t\t\t<br />Camo selections: 1 - the whole exterior\t\t\t\t\t\t<br />Script door sources: DoorL_Front_Open, DoorR_Front_Open, DoorL_Back_Open, DoorR_Back_Open\t\t\t\t\t\t<br />Script animations: AddDoors, AddBackseats, AddTread\t\t\t\t\t\t<br />Executed scripts: /A3/Air_F_Heli/Heli_Light_01/scripts/randomize.sqf \t\t\t\t\t\t<br />Firing from vehicles: No\t\t\t\t\t\t<br />Slingload: Slingloads up to 500 kg\t\t\t\t\t\t<br />Cargo proxy indexes: 11, 10",
    "featuretype": 0,
    "fireresistance": 10,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 242,
    "fuelconsumptionrate": 0.0322,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 2,
    "gearminalt": 0.5,
    "gearretracting": 0,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 3.33,
    "getinaction": "ChopperLight_L_In_H",
    "getinoutonproxy": 0,
    "getinradius": 1.7,
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
    "gunnerusespilotview": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.01,
        0.0025,
        0.01
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
        "aiming_dot"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "A3/Air_F/Heli_Light_01/Data/Heli_Light_01_ext_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": 1,
            "convexcomponent": "avionics_hit",
            "explosionshielding": 2,
            "material": 51,
            "name": "avionics_hit",
            "passthrough": 1,
            "radius": 0.5,
            "visual": ""
        },
        "hitengine": {
            "armor": 0.25,
            "convexcomponent": "engine_hit",
            "explosionshielding": 2,
            "material": 51,
            "name": "engine_hit",
            "passthrough": 1,
            "radius": 0.2,
            "visual": ""
        },
        "hitengine1": {
            "armor": 0.25,
            "convexcomponent": "engine_1_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_1_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitengine2": {
            "armor": 0.25,
            "convexcomponent": "engine_2_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_2_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitengine3": {
            "armor": 0.25,
            "convexcomponent": "engine_3_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_3_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitfuel": {
            "armor": 1,
            "convexcomponent": "fuel_hit",
            "explosionshielding": 2,
            "material": 51,
            "name": "fuel_hit",
            "passthrough": 1,
            "radius": 0.1,
            "visual": ""
        },
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        "hitglass1": {
            "armor": 0.5,
            "convexcomponent": "glass1",
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.5,
            "convexcomponent": "glass2",
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.5,
            "convexcomponent": "glass3",
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.5,
            "convexcomponent": "glass4",
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 2,
            "convexcomponent": "glass5",
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 2,
            "convexcomponent": "glass6",
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "visual": "glass6"
        },
        "hithrotor": {
            "armor": 3,
            "convexcomponent": "main_rotor_hit",
            "explosionshielding": 2.5,
            "material": 51,
            "name": "main_rotor_hit",
            "passthrough": 0.1,
            "radius": 0.3,
            "visual": "main rotor static"
        },
        "hithstabilizerl1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passthrough": 1
        },
        "hithstabilizerr1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passthrough": 0
        },
        "hithull": {
            "armor": 999,
            "convexcomponent": "hull_hit",
            "depends": "Total",
            "explosionshielding": 1,
            "material": 51,
            "name": "hull_hit",
            "passthrough": 1,
            "radius": 0.01,
            "visual": "zbytek"
        },
        "hithydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passthrough": 0.8
        },
        "hitlglass": {
            "armor": 0.1,
            "convexcomponent": "sklo predni L",
            "explosionshielding": 1,
            "material": 51,
            "name": "sklo predni L",
            "passthrough": 0,
            "visual": "sklo predni L"
        },
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passthrough": 0
        },
        "hitmissiles": {
            "armor": 0.1,
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "ammo_hit",
            "passthrough": 0.5,
            "visual": "munice"
        },
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        "hitrglass": {
            "armor": 0.1,
            "convexcomponent": "sklo predni P",
            "explosionshielding": 1,
            "material": 51,
            "name": "sklo predni P",
            "passthrough": 0,
            "visual": "sklo predni P"
        },
        "hitstarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passthrough": 0
        },
        "hitstarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passthrough": 0
        },
        "hitstarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passthrough": 0
        },
        "hitstaticport": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passthrough": 1
        },
        "hittail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passthrough": 1
        },
        "hittransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passthrough": 0.8
        },
        "hitvrotor": {
            "armor": 2,
            "convexcomponent": "tail_rotor_hit",
            "explosionshielding": 6,
            "material": 51,
            "name": "tail_rotor_hit",
            "passthrough": 0.3,
            "radius": 0.06,
            "visual": "tail rotor static"
        },
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        "hitwinch": {
            "armor": -40,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "explo": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.06,
                    "position": "slingLoad0",
                    "simulation": "particles",
                    "type": "WinchDestructionExplo"
                },
                "sparks": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.1,
                    "position": "slingLoad0",
                    "simulation": "particles",
                    "type": "WinchDestructionSparks"
                }
            },
            "material": 51,
            "name": "slingLoad0",
            "passthrough": 0,
            "radius": 0.1,
            "visual": ""
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/Air_F/Heli_Light_01/Data/UI/Map_Heli_Light_01_CIV_CA.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.0316228,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 0.8,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "landingsoundint": [
        "landingSoundInt0",
        0.5,
        "landingSoundInt1",
        0.5
    ],
    "landingsoundint0": [
        "A3/Sounds_F/vehicles/air/noises/landing_skids_int1_open",
        1,
        1,
        100
    ],
    "landingsoundint1": [
        "A3/Sounds_F/vehicles/air/noises/landing_skids_int1_open",
        1,
        1,
        100
    ],
    "landingsoundout": [
        "landingSoundOut0",
        0.5,
        "landingSoundOut1",
        0.5
    ],
    "landingsoundout0": [
        "A3/Sounds_F/vehicles/air/noises/landing_skids_ext1",
        1.77828,
        1,
        100
    ],
    "landingsoundout1": [
        "A3/Sounds_F/vehicles/air/noises/landing_skids_ext1",
        1.77828,
        1,
        100
    ],
    "laserscanner": 0,
    "lasertarget": 0,
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
        "libtextdesc": "A light single-engine helicopter used in special operations by the US Army since the Vietnam War. It now exists in several variants used by both military and civilian transport. The M-900 is a civilian version. Closed cabin and comfortable interior provides space for two passengers."
    },
    "liftforcecoef": 1.5,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "magazines": [],
    "mainbladecenter": "rotor_center",
    "mainbladeradius": 3.8,
    "mainrotorspeed": 1,
    "mapsize": 10.56,
    "markerlights": {
        "collisionred": {
            "activelight": 0,
            "ambient": [
                0.09,
                0.015,
                0.01
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
                0.2,
                1.3
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                0.9,
                0.15,
                0.1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "CollisionLight_red_1_pos",
            "useflare": 0
        },
        "collisionwhite": {
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
            "blinkingpatternguarantee": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "CollisionLight_white_1_pos",
            "useflare": 0
        },
        "greenstill": {
            "ambient": [
                0.003,
                0.03,
                0.003,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.03,
                0.3,
                0.03,
                1
            ],
            "name": "zeleny pozicni"
        },
        "positiongreen": {
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
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "PositionLight_green_1_pos",
            "useflare": 0
        },
        "positionred": {
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
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "PositionLight_red_1_pos",
            "useflare": 0
        },
        "positionwhite": {
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
            "blinking": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "PositionLight_white_1_pos",
            "useflare": 0
        },
        "redblinking": {
            "ambient": [
                0.05,
                0.005,
                0.005,
                1
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                0.5,
                0.05,
                0.05,
                1
            ],
            "name": "cerveny pozicni blik"
        },
        "redstill": {
            "ambient": [
                0.03,
                0.003,
                0.003,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.3,
                0.03,
                0.03,
                1
            ],
            "name": "cerveny pozicni"
        },
        "whiteblinking": {
            "ambient": [
                0.1,
                0.1,
                0.1,
                1
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                1,
                1,
                1,
                1
            ],
            "name": "bily pozicni blik"
        },
        "whitestill": {
            "ambient": [
                0.03,
                0.03,
                0.03,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.3,
                0.3,
                0.3,
                1
            ],
            "name": "bily pozicni"
        }
    },
    "maxbackrotordive": 0,
    "maxdetectrange": 20,
    "maxfordingdepth": 1.35,
    "maxgforce": 2,
    "maximumload": 1000,
    "maxmainrotordive": 0,
    "maxsmokedamage": 0.99,
    "maxspeed": 245,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": "slingCamera",
    "memorypointgun": "",
    "memorypointlmissile": "L strela",
    "memorypointlrocket": "L raketa",
    "memorypointpilot": "pilot",
    "memorypointrmissile": "P strela",
    "memorypointrrocket": "P raketa",
    "memorypointsgetincargo": [
        "pos Cargo R",
        "pos Cargo L",
        "pos Cargo L",
        "pos Cargo R"
    ],
    "memorypointsgetincargodir": [
        "pos Cargo dir R",
        "pos Cargo dir L",
        "pos Cargo dir L",
        "pos Cargo dir R"
    ],
    "memorypointsgetincargoprecise": [
        "GetIn_Cargo",
        "GetIn_Cargo2"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "GetIn_Pilot",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 0.2,
    "mfd": {},
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
    "minbackrotordive": 0,
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minmainrotordive": 0,
    "minsmokedamage": 0.3,
    "mintotaldamagethreshold": 0.005,
    "model": "A3/Air_F/Heli_Light_01/Heli_Light_01_civil_F.p3d",
    "namesound": "veh_helicopter_s",
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
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
    "numberphysicalwheels": 0,
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
    "occludesoundswhenin": 0.562341,
    "outsidesoundfilter": 1,
    "overviewpicture": "A3/Data_F_Heli/Images/watermarkInfo_page03_ca.paa",
    "picture": "A3/Air_F/Heli_Light_01/Data/UI/Heli_Light_01_CA.paa",
    "pilotcamera": {
        "controllable": 0,
        "initelev": 80,
        "initturn": 0,
        "maxelev": 80,
        "maxturn": 0,
        "maxxrotspeed": 0.5,
        "maxyrotspeed": 0.5,
        "minelev": 80,
        "minturn": 0,
        "opticsin": {
            "showminimapinoptics": 0,
            "showslingloadmanagerinoptics": 1,
            "showuavviewpinoptics": 0,
            "wide": {
                "directionstabilized": 1,
                "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_wide_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.5,
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": 0.5,
                "minanglex": 0,
                "minangley": 0,
                "minfov": 0.5,
                "opticsdisplayname": "W",
                "thermalmode": [
                    0,
                    1
                ],
                "visionmode": [
                    "Normal",
                    "NVG"
                ]
            }
        },
        "pilotopticsshowcursor": 1
    },
    "pilotspec": {
        "showheadphones": 1
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 100,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 0.7,
    "radartype": 4,
    "reflectors": {
        "right": {
            "ambient": [
                70,
                75,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 200,
                "hardlimitstart": 100,
                "linear": 1,
                "quadratic": 1,
                "start": 0
            },
            "color": [
                7000,
                7500,
                10000
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "Light_dir",
            "flaremaxdistance": 250,
            "flaresize": 10,
            "hitpoint": "Light_hitpoint",
            "innerangle": 15,
            "intensity": 50,
            "outerangle": 65,
            "position": "Light_pos",
            "selection": "Light",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "lowermirror": {
            "bboxes": [
                "MIRROR_TL",
                "MIRROR_TR",
                "MIRROR_BL",
                "MIRROR_BR"
            ],
            "cameraview": {
                "fov": 0.7,
                "pointdirection": "rtd1_dir",
                "pointposition": "rtd1_pos",
                "renderquality": 0,
                "rendervisionmode": 0
            },
            "rendertarget": "rendertarget1"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
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
    "rotordamage": [
        "rotorDamageInt",
        "rotorDamageOut"
    ],
    "rotordamageint": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_int_open_1",
        1,
        1
    ],
    "rotordamageout": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_ext_1",
        2.51189,
        1,
        150
    ],
    "rotorlibhelicopterproperties": {
        "autohovercorrection": [
            0.28,
            2.88,
            0
        ],
        "defaultcollective": 0.5,
        "hasapu": 0,
        "horizontalwingsanglecollmax": 0,
        "horizontalwingsanglecollmin": 0,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxmainrotorstress": 31000,
        "maxtailrotorstress": 5200,
        "maxtorque": 900,
        "maxverticalstabilizerstress": 10000,
        "retreatbladestallwarningspeed": 77.222,
        "rtd_center": "rtd_center",
        "rtdconfig": "A3/Air_F/Heli_Light_01/RTD_Heli_Light_01.xml",
        "stressdamagepersec": 0.00333333,
        "vrsshakepowercoef": 1
    },
    "scope": 1,
    "scopecurator": 0,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionhrotormove": "main rotor blur",
    "selectionhrotorstill": "main rotor static",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionshowdamage": "poskozeni",
    "selectionvrotormove": "tail rotor blur",
    "selectionvrotorstill": "tail rotor static",
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
    "side": 3,
    "simpleobject": {
        "animate": [
            [
                "rotorshaftm",
                0
            ],
            [
                "bladem01_joint_horizontal_axis",
                0
            ],
            [
                "bladem02_joint_horizontal_axis",
                0
            ],
            [
                "bladem03_joint_horizontal_axis",
                0
            ],
            [
                "bladem04_joint_horizontal_axis",
                0
            ],
            [
                "bladem05_joint_horizontal_axis",
                0
            ],
            [
                "bladem01_dive",
                0
            ],
            [
                "bladem02_dive",
                0
            ],
            [
                "bladem03_dive",
                0
            ],
            [
                "bladem04_dive",
                0
            ],
            [
                "bladem05_dive",
                0
            ],
            [
                "bladem01_bank",
                0
            ],
            [
                "bladem02_bank",
                0
            ],
            [
                "bladem03_bank",
                0
            ],
            [
                "bladem04_bank",
                0
            ],
            [
                "bladem05_bank",
                0
            ],
            [
                "bladem01_blur_rotation",
                0
            ],
            [
                "bladem02_rotation",
                0
            ],
            [
                "bladem03_rotation",
                0
            ],
            [
                "bladem04_rotation",
                0
            ],
            [
                "bladem05_rotation",
                0
            ],
            [
                "vrotor",
                0
            ],
            [
                "stick_pilot_dive_01",
                0
            ],
            [
                "stick_pilot_dive_02",
                0
            ],
            [
                "stick_pilot_dive_03",
                0
            ],
            [
                "stick_pilot_dive_04",
                0
            ],
            [
                "stick_pilot_dive_05",
                0
            ],
            [
                "stick_pilot_bank_01",
                0
            ],
            [
                "stick_pilot_bank_02",
                0
            ],
            [
                "stick_pilot_bank_03",
                0
            ],
            [
                "stick_pilot_bank_04",
                0
            ],
            [
                "stick_pilot_bank_05",
                0
            ],
            [
                "stick_copilot_dive01",
                0
            ],
            [
                "stick_copilot_dive02",
                0
            ],
            [
                "stick_copilot_dive03",
                0
            ],
            [
                "stick_copilot_dive04",
                0
            ],
            [
                "stick_copilot_dive05",
                0
            ],
            [
                "stick_copilot_bank01",
                0
            ],
            [
                "stick_copilot_bank02",
                0
            ],
            [
                "stick_copilot_bank03",
                0
            ],
            [
                "stick_copilot_bank04",
                0
            ],
            [
                "stick_copilot_bank05",
                0
            ],
            [
                "i_speed",
                0
            ],
            [
                "i_bank",
                0
            ],
            [
                "i_altitude_100f",
                5.6
            ],
            [
                "i_altitude_1000f",
                5.6
            ],
            [
                "i_altitude_10000f",
                5.6
            ],
            [
                "i_compass",
                0
            ],
            [
                "i_wp",
                0
            ],
            [
                "i_vspeed",
                0
            ],
            [
                "i_fuel",
                1
            ],
            [
                "i_oilpress",
                0
            ],
            [
                "i_temp",
                5.6
            ],
            [
                "damagehide",
                0
            ],
            [
                "lever_pilot",
                0
            ],
            [
                "lever_copilot",
                0
            ],
            [
                "pedall",
                0
            ],
            [
                "pedalr",
                0
            ],
            [
                "tailrotorimpacthide",
                0
            ],
            [
                "i_speed_02",
                0
            ],
            [
                "i_speed_03",
                0
            ],
            [
                "i_speed_04",
                0
            ],
            [
                "i_rpm",
                0
            ],
            [
                "i_rpm02",
                0
            ],
            [
                "i_rpm03",
                0
            ],
            [
                "i_compass02",
                0
            ],
            [
                "i_horizont_dive",
                0
            ],
            [
                "i_torque",
                0
            ],
            [
                "i_fuel_01a",
                1
            ],
            [
                "i_fuel_01b",
                1
            ],
            [
                "i_fuel_02a",
                1
            ],
            [
                "i_fuel_02b",
                1
            ],
            [
                "i_fuel_03a",
                1
            ],
            [
                "i_fuel_03b",
                1
            ],
            [
                "i_oiltemp",
                0
            ],
            [
                "i_oiltemp_random",
                0
            ],
            [
                "gunl_revolving",
                0
            ],
            [
                "gunr_revolving",
                0
            ],
            [
                "rotortilt_bladem01",
                0
            ],
            [
                "rotortilt_bladem02",
                0
            ],
            [
                "rotortilt_bladem03",
                0
            ],
            [
                "rotortilt_bladem04",
                0
            ],
            [
                "rotortilt_bladem05",
                0
            ],
            [
                "hidepg_1",
                0
            ],
            [
                "hidepg_2",
                0
            ],
            [
                "hidepg_3",
                0
            ],
            [
                "hidepg_4",
                0
            ],
            [
                "hidepg_5",
                0
            ],
            [
                "hidepg_6",
                0
            ],
            [
                "hidepg_7",
                0
            ],
            [
                "hidepg_8",
                0
            ],
            [
                "hidepg_9",
                0
            ],
            [
                "hidepg_10",
                0
            ],
            [
                "hidepg_11",
                0
            ],
            [
                "hidepg_12",
                0
            ],
            [
                "hidepg_13",
                0
            ],
            [
                "hidepg_14",
                0
            ],
            [
                "hidepg_15",
                0
            ],
            [
                "hidepg_16",
                0
            ],
            [
                "hidepg_17",
                0
            ],
            [
                "hidepg_18",
                0
            ],
            [
                "hidepg_19",
                0
            ],
            [
                "hidepg_20",
                0
            ],
            [
                "hidepg_21",
                0
            ],
            [
                "hidepg_22",
                0
            ],
            [
                "hidepg_23",
                0
            ],
            [
                "hidepg_24",
                0
            ],
            [
                "zaslehrot",
                0
            ],
            [
                "zaslehrot_2",
                0
            ],
            [
                "positionlights",
                0
            ],
            [
                "collisionlight_red_blinking",
                0
            ],
            [
                "collisionlight_white_blinking",
                0
            ],
            [
                "rotorimpacthide",
                0
            ],
            [
                "hiderockets",
                1
            ]
        ],
        "eden": 0,
        "hide": [
            "clan",
            "zasleh",
            "light",
            "tail rotor blur",
            "main rotor blur",
            "zadni svetlo",
            "podsvit pristroju",
            "poskozeni"
        ],
        "postinit": "[this, '', []] call bis_fnc_initVehicle",
        "verticaloffset": 0.608,
        "verticaloffsetworld": 0.004
    },
    "simulation": "helicopterrtd",
    "slingcargoattach": [
        "slingCargoAttach0",
        "slingCargoAttach1"
    ],
    "slingcargoattach0": [
        "A3/Sounds_F/vehicles/air/noises/SL_engineDownEndINT",
        1,
        1
    ],
    "slingcargoattach1": [
        "A3/Sounds_F/vehicles/air/noises/SL_1hookLock",
        1.77828,
        1,
        200
    ],
    "slingcargodetach": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargodetach0": [
        "A3/Sounds_F/vehicles/air/noises/SL_engineUpEndINT",
        1,
        1
    ],
    "slingcargodetach1": [
        "A3/Sounds_F/vehicles/air/noises/SL_1hookUnlock",
        1.77828,
        1,
        200
    ],
    "slingcargodetachair": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargodetachair0": [
        "A3/Sounds_F/vehicles/air/noises/SL_unhook_air_int",
        1,
        1
    ],
    "slingcargodetachair1": [
        "A3/Sounds_F/vehicles/air/noises/SL_unhook_air_ext",
        1,
        1,
        300
    ],
    "slingcargoropebreak": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargoropebreak0": [
        "A3/Sounds_F/vehicles/air/noises/SL_rope_break_int",
        1,
        1
    ],
    "slingcargoropebreak1": [
        "A3/Sounds_F/vehicles/air/noises/SL_rope_break_ext",
        1,
        1,
        200
    ],
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slingloadmaxcargomass": 500,
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmincargomass": 0,
    "slowspeedforwardcoef": 0.3,
    "soundarmorcrash": [
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "soundburning": {},
    "soundbushcollision1": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_1",
        1,
        1,
        100
    ],
    "soundbushcollision2": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_2",
        1,
        1,
        100
    ],
    "soundbushcollision3": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_3",
        1,
        1,
        100
    ],
    "soundbushcrash": [
        "soundBushCollision1",
        0.33,
        "soundBushCollision2",
        0.33,
        "soundBushCollision3",
        0.33
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "soundGeneralCollision1",
        0.33,
        "soundGeneralCollision2",
        0.33,
        "soundGeneralCollision3",
        0.33
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_crash_default_ext_1",
        3.16228,
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
        "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_stop",
        0.794328,
        1,
        600
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_stop",
        0.316228,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_start",
        0.794328,
        1,
        600
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_start",
        0.316228,
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
    "soundgear": {},
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
    "soundgeneralcollision1": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_1",
        1,
        1,
        100
    ],
    "soundgeneralcollision2": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_2",
        1,
        1,
        100
    ],
    "soundgeneralcollision3": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_3",
        1,
        1,
        100
    ],
    "soundgetin": [
        "A3/Sounds_F/vehicles/air/noises/heli_get_in2",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles/air/noises/heli_get_out2",
        0.794328,
        1,
        20
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_1",
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
        "emptySound",
        0
    ],
    "soundlandinggear": [
        "",
        1,
        1
    ],
    "soundlocked": [
        "/A3/Sounds_F/weapons/Rockets/opfor_lock_1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "damagealarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_bluefor",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        "damagealarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_bluefor",
                0.316228,
                1
            ],
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        "enginebench": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_engine_bench",
                0.354813,
                1,
                400
            ],
            "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (0 max (rotorSpeed-0.4))"
        },
        "engineext": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_engine",
                1.25893,
                1,
                400
            ],
            "volume": "4 * camPos * (0 max (rotorSpeed-0.4))"
        },
        "engineint": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_engine",
                0.794328,
                1
            ],
            "volume": "(1-camPos)*2*(0 max (rotorSpeed-0.4))"
        },
        "gstress": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/vehicle_stress2b",
                0.316228,
                1,
                50
            ],
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        },
        "rainext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_ext",
                1,
                1,
                100
            ],
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        "rainint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_int_open",
                1,
                1,
                100
            ],
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        "rotorbench": {
            "cone": [
                1.6,
                3.14,
                1.6,
                0.95
            ],
            "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_rotor_normal_bench",
                0.501187,
                1,
                1000
            ],
            "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust) * 0.4"
        },
        "rotorext": {
            "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_rotor_normal_new",
                1.25893,
                1,
                1000
            ],
            "volume": "camPos * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust)"
        },
        "rotorint": {
            "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_rotor_normal_new",
                0.630957,
                1
            ],
            "volume": "(1 - camPos) * (rotorSpeed factor [0.3, 0.7]) * (1 + rotorThrust) * 0.7"
        },
        "rotorlowalarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        "rotorlowalarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                0.316228,
                1
            ],
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        "rotorswist": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_01/rotor_swist",
                0.707946,
                1,
                300
            ],
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
        },
        "scrubbuildingext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubBuildingExt",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        "scrubbuildingint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubBuildingInt",
                1,
                1,
                100
            ],
            "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
        },
        "scrublandext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubLandExt",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubLand factor[0.02, 0.05])"
        },
        "scrublandint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubLandInt_open",
                1,
                1,
                100
            ],
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
        },
        "scrubtreeext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                1,
                1,
                100
            ],
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        "scrubtreeint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                1,
                1,
                100
            ],
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        "slingloaddownext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineDownEXT",
                1.25893,
                1,
                500
            ],
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        "slingloaddownint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineDownINT",
                1,
                1,
                700
            ],
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        "slingloadupext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineUpEXT",
                1.25893,
                1,
                500
            ],
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        "slingloadupint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineUpINT",
                1,
                1,
                700
            ],
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        "transmissiondamageext_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_1",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageext_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_2",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_1",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_2",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "windbench": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wind_open_out",
                0.562341,
                1,
                50
            ],
            "volume": "4 * (playerPos factor [3.9, 4]) * (1 - camPos) * ((speed factor[0, 30]) + (speed factor[0, -30]))"
        },
        "windint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wind_open_int",
                1.12202,
                1,
                50
            ],
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        "windlateralmovementint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wind_lateral_open_int",
                1.99526,
                1,
                50
            ],
            "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
        }
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundsext": {
        "soundevents": {},
        "sounds": {
            "damagealarmext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_bluefor",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            "damagealarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_bluefor",
                    0.316228,
                    1
                ],
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            "enginebench": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_engine_bench",
                    0.354813,
                    1,
                    400
                ],
                "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (0 max (rotorSpeed-0.4))"
            },
            "engineext": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_engine",
                    1.25893,
                    1,
                    400
                ],
                "volume": "4 * camPos * (0 max (rotorSpeed-0.4))"
            },
            "engineint": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_engine",
                    0.794328,
                    1
                ],
                "volume": "(1-camPos)*2*(0 max (rotorSpeed-0.4))"
            },
            "gstress": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/vehicle_stress2b",
                    0.316228,
                    1,
                    50
                ],
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            "rainext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/rain1_ext",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            "rainint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/rain1_int_open",
                    1,
                    1,
                    100
                ],
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            "rotorbench": {
                "cone": [
                    1.6,
                    3.14,
                    1.6,
                    0.95
                ],
                "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_rotor_normal_bench",
                    0.501187,
                    1,
                    1000
                ],
                "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust) * 0.4"
            },
            "rotorext": {
                "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_ext_rotor_normal_new",
                    1.25893,
                    1,
                    1000
                ],
                "volume": "camPos * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust)"
            },
            "rotorint": {
                "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/4)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/Heli_Light_01_int_rotor_normal_new",
                    0.630957,
                    1
                ],
                "volume": "(1 - camPos) * (rotorSpeed factor [0.3, 0.7]) * (1 + rotorThrust) * 0.7"
            },
            "rotorlowalarmext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            "rotorlowalarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                    0.316228,
                    1
                ],
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            "rotorswist": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_01/rotor_swist",
                    0.707946,
                    1,
                    300
                ],
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
            },
            "scrubbuildingext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubBuildingExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            "scrubbuildingint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubBuildingInt",
                    1,
                    1,
                    100
                ],
                "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
            },
            "scrublandext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubLandExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubLand factor[0.02, 0.05])"
            },
            "scrublandint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubLandInt_open",
                    1,
                    1,
                    100
                ],
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
            },
            "scrubtreeext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            "scrubtreeint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                    1,
                    1,
                    100
                ],
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            "slingloaddownext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineDownEXT",
                    1,
                    1,
                    500
                ],
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            "slingloaddownint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineDownINT",
                    1,
                    1,
                    500
                ],
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            "slingloadupext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineUpEXT",
                    1,
                    1,
                    500
                ],
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            "slingloadupint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineUpINT",
                    1,
                    1,
                    500
                ],
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            "transmissiondamageext_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_1",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageext_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_2",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_1",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_2",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "windbench": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wind_open_out",
                    0.562341,
                    1,
                    50
                ],
                "volume": "4 * (playerPos factor [3.9, 4]) * (1 - camPos) * ((speed factor[0, 30]) + (speed factor[0, -30]))"
            },
            "windint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wind_open_int",
                    1.12202,
                    1,
                    50
                ],
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            "windlateralmovementint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wind_lateral_open_int",
                    1.99526,
                    1,
                    50
                ],
                "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
            }
        },
        "waternoise_ext": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/noises/air_driving_in_water",
                0.707946,
                1,
                300
            ],
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        "waternoise_int": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/noises/soft_driving_in_water_int",
                0.562341,
                1,
                100
            ],
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
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
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_air_helicopter_p"
            ],
            "speechsingular": [
                "veh_air_helicopter_s"
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
    "startduration": 20,
    "steeraheadplan": 0.7,
    "steeraheadsimul": 0.5,
    "supplyradius": -1,
    "tailbladecenter": "rotor_02_center",
    "tailbladeradius": 0.5,
    "tailbladevertical": 1,
    "taildamage": [
        "tailDamageInt",
        "tailDamageOut"
    ],
    "taildamageint": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_tail",
        1,
        1
    ],
    "taildamageout": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_tail",
        1,
        1,
        300
    ],
    "tbody": 150,
    "textplural": "helicopters",
    "textsingular": "helicopter",
    "texturelist": [
        "Shadow",
        1
    ],
    "texturesources": {
        "blue": {
            "author": "Bohemia Interactive",
            "displayname": "Blue",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/heli_light_01_ext_blue_co.paa"
            ]
        },
        "blueline": {
            "author": "Bohemia Interactive",
            "displayname": "BlueLine",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_blueLine_co.paa"
            ]
        },
        "digital": {
            "author": "Bohemia Interactive",
            "displayname": "Digital",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_digital_co.paa"
            ]
        },
        "elliptical": {
            "author": "Bohemia Interactive",
            "displayname": "Elliptical",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_elliptical_co.paa"
            ]
        },
        "furious": {
            "author": "Bohemia Interactive",
            "displayname": "Furious",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_furious_co.paa"
            ]
        },
        "graywatcher": {
            "author": "Bohemia Interactive",
            "displayname": "Graywatcher",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_graywatcher_co.paa"
            ]
        },
        "ion": {
            "author": "Bohemia Interactive",
            "displayname": "Ion",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/heli_light_01_ext_ion_co.paa"
            ]
        },
        "jeans": {
            "author": "Bohemia Interactive",
            "displayname": "Jeans",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_jeans_co.paa"
            ]
        },
        "light": {
            "author": "Bohemia Interactive",
            "displayname": "Light",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_light_co.paa"
            ]
        },
        "red": {
            "author": "Bohemia Interactive",
            "displayname": "Red",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/heli_light_01_ext_co.paa"
            ]
        },
        "shadow": {
            "author": "Bohemia Interactive",
            "displayname": "Shadow",
            "factions": [
                "CIV_F",
                "IND_C_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_shadow_co.paa"
            ]
        },
        "sheriff": {
            "author": "Bohemia Interactive",
            "displayname": "Sheriff",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_sheriff_co.paa"
            ]
        },
        "speedy": {
            "author": "Bohemia Interactive",
            "displayname": "Speedy",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_speedy_co.paa"
            ]
        },
        "sunset": {
            "author": "Bohemia Interactive",
            "displayname": "Sunset",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_sunset_co.paa"
            ]
        },
        "vrana": {
            "author": "Bohemia Interactive",
            "displayname": "Vrana",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_vrana_co.paa"
            ]
        },
        "wasp": {
            "author": "Bohemia Interactive",
            "displayname": "Wasp",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_wasp_co.paa"
            ]
        },
        "wave": {
            "author": "Bohemia Interactive",
            "displayname": "Wave",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/air_f/Heli_Light_01/Data/Skins/heli_light_01_ext_wave_co.paa"
            ]
        }
    },
    "threat": [
        0,
        0,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 4,
            "name": "FirstAidKit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 24,
    "transportmaxmagazines": 48,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 2,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {
        "copilotturret": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
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
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
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
            "dontcreateai": 0,
            "dynamicviewlimits": {
                "cargoturret_01": [
                    -70,
                    -20
                ]
            },
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
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
            "gunneraction": "Chopperlight_R_Static_H",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "Chopperlight_R_In_H",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "Chopperlight_R_Static_H",
            "gunnerlefthandanimname": "lever_copilot",
            "gunnerleftleganimname": "pedalL",
            "gunnername": "Copilot",
            "gunnernotspawned": 1,
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
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerrightleganimname": "pedalR",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "headaimdown": 3,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "passthrough": 0.1,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "passthrough": 0.3,
                    "visual": "vez"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 1,
            "ispersonturret": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 15,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -20,
            "maxverticalrotspeed": 3,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "memorypointsgetingunnerprecise": "GetIn_Turret",
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
            "minelev": -60,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -105,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "personturretaction": "vehicle_coshooter_1",
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
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
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 1
            },
            "useprecisegetinaction": 0,
            "viewgunner": {
                "initanglex": -3,
                "initangley": 0,
                "initfov": 0.9,
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -1,
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
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
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
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
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "passthrough": 0.1,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "passthrough": 0.3,
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
            "memorypointgun": "machinegun",
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
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 1
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
        }
    },
    "type": 2,
    "typicalcargo": [
        "B_HeliPilot_F"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoAirNoWeapon",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigitalNoWeapon",
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "doorlb_close": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorL_Back_Open') > 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Close Left Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorL_back",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorL_Back_Open', 0]",
            "texttooltip": "Close Left Door",
            "useractionid": 55
        },
        "doorlb_open": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorL_Back_Open') == 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Open Left Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorL_back",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorL_Back_Open', 1]",
            "texttooltip": "Open Left Door",
            "useractionid": 54
        },
        "doorlf_close": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorL_Front_Open') > 0) && (alive this) && ((this animationPhase 'AddDoors')  ==  1) && false",
            "displayname": "Close Left Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorL_front",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorL_Front_Open', 0]",
            "texttooltip": "Close Left Door",
            "useractionid": 51
        },
        "doorlf_open": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorL_Front_Open')  ==  0) && (alive this) && ((this animationPhase 'AddDoors')  ==  1) && false",
            "displayname": "Open Left Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorL_front",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorL_Front_Open', 1]",
            "texttooltip": "Open Left Door",
            "useractionid": 50
        },
        "doorrb_close": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorR_Back_Open') > 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Close Right Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorR_back",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorR_Back_Open', 0]",
            "texttooltip": "Close Right Door",
            "useractionid": 57
        },
        "doorrb_open": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorR_Back_Open') == 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Open Right Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorR_back",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorR_Back_Open', 1]",
            "texttooltip": "Open Right Door",
            "useractionid": 56
        },
        "doorrf_close": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorR_Front_Open') > 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Close Right Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorR_front",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorR_Front_Open', 0]",
            "texttooltip": "Close Right Door",
            "useractionid": 53
        },
        "doorrf_open": {
            "available": 0,
            "condition": "((this DoorPhase 'DoorR_Front_Open') == 0) && (alive this) && ((this animationPhase 'AddDoors') == 1) && false",
            "displayname": "Open Right Door",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/open_door_ca.paa' size='2.5' />",
            "onlyforplayer": 1,
            "position": "action_doorR_front",
            "priority": 1.5,
            "radius": 1.5,
            "radiusview": 0.2,
            "shortcut": "",
            "showin3d": 17,
            "showwindow": 1,
            "statement": "this animatedoor ['DoorR_Front_Open', 1]",
            "texttooltip": "Open Right Door",
            "useractionid": 52
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
        "maxanglex": 30,
        "maxangley": 86,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -86,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": -3,
        "initangley": 0,
        "initfov": 0.9,
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
    "visualtargetsize": 0.8,
    "washdowndiameter": "40.0f",
    "washdownstrength": "1.0f",
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 100,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "windsockexist": 0
}