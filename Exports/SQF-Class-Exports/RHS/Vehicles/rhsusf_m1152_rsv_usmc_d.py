d = {
    "_generalmacro": "MRAP_01_base_F",
    "accelaidforceyoffset": -1.25,
    "acceleration": 15,
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left",
            "Left2"
        ],
        [
            "Right",
            "Right2"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.2,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "antennas_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide antennas",
            "initphase": 0,
            "source": "user"
        },
        "bft_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide BFT system",
            "initphase": 0,
            "source": "user",
            "usesource": 1
        },
        "bft_map_move_x": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "bft_map_move_y": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "bft_map_scale": {
            "animperiod": 0,
            "initphase": 0.1,
            "source": "user"
        },
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "door_lb": {
            "animperiod": 0.8,
            "displayname": "",
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "osa_dvere_pp",
            "source": "door"
        },
        "door_lf": {
            "animperiod": 0.8,
            "displayname": "open left front door",
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "osa_dvere_lp",
            "source": "door"
        },
        "door_rb": {
            "animperiod": 0.8,
            "displayname": "",
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "osa_dvere_pp",
            "source": "door"
        },
        "door_rf": {
            "animperiod": 0.8,
            "displayname": "open right front door",
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "osa_dvere_pp",
            "source": "door"
        },
        "door_trunk": {
            "animperiod": 0.8,
            "displayname": "",
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "trunk_action",
            "source": "user",
            "usesource": 1
        },
        "duke_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "",
            "initphase": 1,
            "onphasechanged": "_this call rhs_fnc_duke_vg;",
            "source": "user"
        },
        "dwf_kit_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide deep water fording kit",
            "forceanimate": [
                "snorkel_lower",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "source": "user"
        },
        "hide_spare": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide spare wheel",
            "initphase": 0,
            "mass": -20,
            "source": "user"
        },
        "hitduke1": {
            "hitpoint": "HitDuke1",
            "source": "Hit"
        },
        "hitduke2": {
            "hitpoint": "HitDuke1",
            "source": "Hit"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
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
        "hitlbwheel": {
            "hitpoint": "HitLF2Wheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitlf2wheel": {
            "hitpoint": "HitLBWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitlfwheel": {
            "hitpoint": "HitLFWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrbwheel": {
            "hitpoint": "HitRF2Wheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrf2wheel": {
            "hitpoint": "HitRBWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "raw": 1,
            "source": "Hit"
        },
        "iff_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide CIP",
            "initphase": 0,
            "source": "user",
            "usesource": 1
        },
        "light_bo": {
            "animperiod": 1e-05,
            "initphase": 1,
            "source": "user"
        },
        "light_stop": {
            "animperiod": 1e-05,
            "initphase": 0,
            "source": "user"
        },
        "lights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "longlights_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "m1151_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "initphase": 1,
            "source": "user"
        },
        "m1152_bench_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "forceanimate": [
                "m1152_Hide",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "source": "user"
        },
        "m1152_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide rear frame",
            "initphase": 0,
            "source": "user"
        },
        "m1152_tent_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide rear cover",
            "forceanimate": [
                "m1152_Hide",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "source": "user"
        },
        "m1165_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "initphase": 1,
            "source": "user"
        },
        "shortlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "snorkel_lower": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "displayname": "hide raised air intake",
            "forceanimate": [
                "snorkel_lower",
                1
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "source": "user",
            "usesource": 1
        },
        "supply_hide": {
            "animperiod": 1e-05,
            "author": "Red Hammer Studios",
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 20,
    "antirollbarforcelimit": 5.5,
    "antirollbarspeedmax": 80,
    "antirollbarspeedmin": 10,
    "armor": 100,
    "armorcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "armorcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "armorcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "armorcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "armorcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "armorcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "armorcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "armorcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "armorlights": 0.01,
    "armorstructural": 10,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "MrapAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        }
    },
    "audible": 5,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 3,
    "brakeidlespeed": 1.8,
    "braketorque": 6000,
    "buildcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "buildcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "buildcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "buildcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "buildcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "buildcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "buildcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "buildcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "bushcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_01",
        0.630957,
        1,
        50
    ],
    "bushcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_02",
        0.630957,
        1,
        50
    ],
    "bushcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.630957,
        1,
        50
    ],
    "bushcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.630957,
        0.8,
        50
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
    "camouflage": 2,
    "camshakecoef": 0.3,
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
        "frequency": 60,
        "minspeed": 60,
        "power": 2
    },
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_HMMWV_Cargo"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        1,
        1
    ],
    "cargodoors": [
        "Door_LB",
        "Door_RB"
    ],
    "cargogetinaction": [
        "GetInMRAP_01_cargo"
    ],
    "cargogetoutaction": [
        "GetOutMRAP_01"
    ],
    "cargoiscodriver": [
        0
    ],
    "cargoprecisegetinout": [
        0
    ],
    "cargoproxyindexes": [
        1
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
    "category": "Car",
    "centrebias": 1.5,
    "changegearmineffectivity": [
        0.95,
        0.15,
        0.95,
        0.95,
        0.95,
        0.95,
        0.95
    ],
    "changegearomegaratios": [
        1,
        0.294118,
        0.205882,
        0.147059,
        0.926471,
        0.470588,
        0.764706,
        0.352941,
        0.852941,
        0.5,
        1,
        0.647059
    ],
    "changegeartype": "effective",
    "clutchstrength": 85,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "collisioneffect": "collisionEffect",
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
            -3.07,
            "N",
            0,
            "D1",
            2.78,
            "D2",
            1.48,
            "D3",
            1,
            "D4",
            0.75
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            6
        ]
    },
    "components": {
        "aicarsteeringcomponent": {
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "allowovertaking": 1,
            "commandturnfactor": 1,
            "convoypidweights": [
                1,
                0.01,
                0.01
            ],
            "differenceanglecoef": 0.4,
            "dopredictforward": 1,
            "doremapspeed": 1,
            "forwardanglecoef": 0.7,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.1,
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
            "speedpredictionmethod": 2,
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
        "sensorsmanagercomponent": {
            "components": {
                "datalinksensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "animdirection": "",
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "componenttype": "DataLinkSensorComponent",
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
                    "typerecognitiondistance": 0
                }
            }
        },
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
                    "resource": "RscCustomInfoMiniMap"
                }
            }
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
                    "resource": "RscCustomInfoMiniMap"
                }
            }
        }
    },
    "cost": 500000,
    "countsforscoreboard": 1,
    "crash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "crash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "crash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "crash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "crash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "crash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "crash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "crash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "crew": "rhsusf_usmc_marpat_d_rifleman_m4",
    "crewcrashprotection": 1.35,
    "crewexplosionprotection": 1,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Ext.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Ext_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152M1165.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152M1165_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152_SICPS.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152_SICPS_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1165_ASV.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1165_ASV_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV_Ext.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV_Ext_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_half_d.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_half_d.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_GPK.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_GPK_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/turrets/ogpk/data/ogpk_base.rvmat",
            "rhsusf/addons/rhsusf_hmmwv/turrets/ogpk/data/ogpk_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_rg33l/data/mctags.rvmat",
            "rhsusf/addons/rhsusf_rg33l/data/mctags_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV_SAG.rvmat",
            "rhsusf/addons/rhsusf_m1165/data/rhsusf_M1165A1_GMV_SAG_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_caiman/data/m153.rvmat",
            "rhsusf/addons/rhsusf_caiman/data/m153_dam.rvmat",
            "rhsusf/addons/rhsusf_m11xx/data/rhsusf_m11xx_destruction.rvmat",
            "rhsusf/addons/rhsusf_matv/data/rhsusf_matv_kamaz_glass.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_int.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
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
    "dammagefull": [],
    "dammagehalf": [],
    "damperdamping": 1,
    "damperforce": 1,
    "dampersbumpcoef": 0,
    "dampersize": 0.1,
    "dampingratefullthrottle": 0.15,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "dampingratezerothrottleclutchengaged": 2.8,
    "defaultusermfdvalues": [
        1000,
        13504,
        0
    ],
    "destrtype": "DestructDefault",
    "destructioneffects": {
        "fire1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small"
        },
        "fire2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small"
        },
        "firesparks1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "FireSparks"
        },
        "light1": {
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
            "type": "ObjectDestructionRefractSmall"
        },
        "smoke1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall"
        },
        "smoke1_2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small"
        },
        "smoke2": {
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
        "sparks1": {
            "intensity": 0,
            "interval": 1,
            "lifetime": 0,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSparks"
        }
    },
    "detectskill": 20,
    "differentialtype": "all_limited",
    "displayname": "M1152A1 RSV",
    "dlc": "RHS_USAF",
    "driveraction": "RHS_HMMWV_Driver",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "Door_LF",
    "driverforceoptics": 0,
    "driverinaction": "RHS_HMMWV_Driver",
    "driverlefthandanimname": "drivewheel",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "drivewheel",
    "driverrightleganimname": "pedal_thrust",
    "dustbackleftpos": "wheel_1_2_bound",
    "dustbackrightpos": "wheel_2_2_bound",
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
                "LDustEffects"
            ],
            "gdtbeach": [
                "LDustEffects"
            ],
            "gdtcliff": [
                "LDustEffects"
            ],
            "gdtconcrete": [
                "LDustEffects"
            ],
            "gdtdead": [
                "LDustEffects"
            ],
            "gdtdesert": [
                "LDustEffects"
            ],
            "gdtdesert1": [
                "LDustEffects"
            ],
            "gdtdesert2": [
                "LDustEffects"
            ],
            "gdtdirt": [
                "LDustEffects"
            ],
            "gdtfield": [
                "LDustEffects"
            ],
            "gdtforest": [
                "LDustEffects"
            ],
            "gdtgrassdry": [
                "LDustEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffects"
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
                "LDustEffects"
            ],
            "gdtrubble": [
                "LDustEffects"
            ],
            "gdtseabed": [
                "LDustEffects"
            ],
            "gdtseabeddeep": [
                "LDustEffects"
            ],
            "gdtsoil": [
                "LDustEffects"
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
                "LDustEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffects"
            ],
            "gdtstratisthistles": [
                "LDustEffects"
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
                "RDustEffects"
            ],
            "gdtbeach": [
                "RDustEffects"
            ],
            "gdtcliff": [
                "RDustEffects"
            ],
            "gdtconcrete": [
                "RDustEffects"
            ],
            "gdtdead": [
                "RDustEffects"
            ],
            "gdtdesert": [
                "RDustEffects"
            ],
            "gdtdesert1": [
                "RDustEffects"
            ],
            "gdtdesert2": [
                "RDustEffects"
            ],
            "gdtdirt": [
                "RDustEffects"
            ],
            "gdtfield": [
                "RDustEffects"
            ],
            "gdtforest": [
                "RDustEffects"
            ],
            "gdtgrassdry": [
                "RDustEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffects"
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
                "RDustEffects"
            ],
            "gdtrubble": [
                "RDustEffects"
            ],
            "gdtseabed": [
                "RDustEffects"
            ],
            "gdtseabeddeep": [
                "RDustEffects"
            ],
            "gdtsoil": [
                "RDustEffects"
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
                "RDustEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffects"
            ],
            "gdtstratisthistles": [
                "RDustEffects"
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
    "dustfrontleftpos": "wheel_1_1_bound",
    "dustfrontrightpos": "wheel_2_1_bound",
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/rhsusf_m1152_rsv_usmc_d.paa",
    "editorsubcategory": "EdSubcat_Cars",
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
    "enginebrakecoef": 0.8,
    "engineer": 0,
    "enginelosses": 12,
    "enginemoi": 7,
    "enginepower": 160,
    "enginestartspeed": 1.5,
    "epeimpulsedamagecoef": 15,
    "eventhandlers": {
        "bis_randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhsusf_eventhandlers": {
            "engine": "_this call rhs_fnc_engineCheckDamage",
            "init": "_this call rhs_fnc_m11xx_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "seatswitched": "if(not(_this select 1 in [driver (_this select 0),gunner (_this select 0)]))then{ (_this select 1) action ['turnIn',_this select 0]}",
            "turnin": "([0] + _this)  call rhsusf_fnc_turretAction;",
            "turnout": "([1] + _this) call rhsusf_fnc_turretAction;"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust2_2",
            "effect": "ExhaustsEffect",
            "position": "exhaust2_1"
        }
    },
    "explosioneffect": "FuelExplosion",
    "explosionshielding": 1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0.5,
        2,
        -10
    ],
    "faction": "rhs_faction_usmc_d",
    "features": "Randomization: No\t\t\t\t\t\t<br />Camo selections: 2 - the body, wheels and cover\t\t\t\t\t\t<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB\t\t\t\t\t\t<br />Script animations: None\t\t\t\t\t\t<br />Executed scripts: None\t\t\t\t\t\t<br />Firing from vehicles: No\t\t\t\t\t\t<br />Slingload: Slingloadable\t\t\t\t\t\t<br />Cargo proxy indexes: 1 to 3",
    "featuretype": 0,
    "fireresistance": 5,
    "forcehidedriver": 1,
    "forceingarage": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 20,
    "frontbias": 2.7,
    "frontrearsplit": 0.5,
    "fuelcapacity": 22.5,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 3,
    "fxexplo": {
        "access": 1
    },
    "gearbox": [
        -8,
        0,
        10,
        6.15,
        4.44,
        3.33
    ],
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1
    ],
    "getinradius": 2.5,
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
    "gunnerhasflares": 0,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.01,
        0.01,
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
        "camo",
        "camo1",
        "camo2",
        "camo3",
        "camo4",
        "camo5",
        "camo6",
        "camo11",
        "BFT_screen"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Ext_d_CO.paa",
        "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_d_CO.paa",
        "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int_CO.paa",
        "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_d_CO.paa",
        "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_d_co.paa",
        "rhsusf/addons/rhsusf_hmmwv/textures/tile_exmetal_d_co.paa",
        "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152M1165_d_CO.paa",
        "rhsusf/addons/rhsusf_hmmwv/textures/m998_2drcargo_d_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitbody": {
            "armor": 6,
            "explosionshielding": 1.5,
            "material": -1,
            "minimalhit": 0.01,
            "name": "karoserie",
            "passthrough": 1,
            "radius": 0.45,
            "visual": "zbytek"
        },
        "hitduke1": {
            "armor": 0.75,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.05,
            "name": "duke1",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "-"
        },
        "hitduke2": {
            "armor": 0.75,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.05,
            "name": "duke2",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "-"
        },
        "hitengine": {
            "armor": -100,
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
            "material": -1,
            "name": "motor",
            "passthrough": 0.2,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": -50,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "palivo",
            "passthrough": 0,
            "visual": "-"
        },
        "hitglass1": {
            "armor": -70,
            "armorcomponent": "glass1",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": -70,
            "armorcomponent": "glass2",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": -70,
            "armorcomponent": "glass3",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": -70,
            "armorcomponent": "glass4",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": -70,
            "armorcomponent": "glass5",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass5",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": -70,
            "armorcomponent": "glass6",
            "explosionshielding": 0.4,
            "minimalhit": -0.1,
            "name": "glass6",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass6"
        },
        "hithull": {
            "armor": -300,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": -45,
            "name": "karoserie",
            "passthrough": 1,
            "radius": 0.22,
            "visual": "zbytek"
        },
        "hitlbwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_4_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitlf2wheel": {
            "armor": -250,
            "armorcomponent": "wheel_1_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.016,
            "name": "wheel_1_2_steering",
            "passthrough": 0,
            "radius": 0.33,
            "visual": "wheel_1_2_damage"
        },
        "hitlfwheel": {
            "armor": -250,
            "armorcomponent": "wheel_1_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.016,
            "name": "wheel_1_1_steering",
            "passthrough": 0,
            "radius": 0.33,
            "visual": "wheel_1_1_damage"
        },
        "hitlglass": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": -1,
            "name": "sklo predni L",
            "passthrough": 0
        },
        "hitlmwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_3_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitrbwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_4_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitrf2wheel": {
            "armor": -250,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.016,
            "name": "wheel_2_2_steering",
            "passthrough": 0,
            "radius": 0.33,
            "visual": "wheel_2_2_damage"
        },
        "hitrfwheel": {
            "armor": -250,
            "armorcomponent": "wheel_2_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.016,
            "name": "wheel_2_1_steering",
            "passthrough": 0,
            "radius": 0.33,
            "visual": "wheel_2_1_damage"
        },
        "hitrglass": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": -1,
            "name": "sklo predni P",
            "passthrough": 0
        },
        "hitrmwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_3_steering",
            "passthrough": 0.3,
            "visual": "-"
        }
    },
    "holdoffroadformation": 1,
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsusf/addons/rhsusf_hmmwv/icons/ico_m1025.paa",
    "idlerpm": 650,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "inputturncurve": [
        [
            0,
            [
                0,
                0,
                1,
                1
            ]
        ],
        [
            30,
            [
                0,
                0,
                0.2,
                0.008,
                0.4,
                0.032,
                0.6,
                0.216,
                0.8,
                0.512,
                1,
                1
            ]
        ]
    ],
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.4,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "latency": 1,
    "latstiffx": 2000,
    "latstiffy": 18000,
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
        "libtextdesc": "The Hunter is a Mine-Resistant Ambush Protected (MRAP) vehicle manufactured by US arms factories to provide troops with enhanced protection. The armored hull can withstand light weapons and protects the crew against landmines and improvised explosive devices. Even though the heavy armor and powerful engine cause increased fuel consumption, it has been favored by frontline troops over the lighter vehicles for its easy maintenance and good protection level.<br />Armed version of the sturdy Hunter MRAP vehicle is fitted with a Remotely Controlled Weapons System turret. The turret is fitted with the universal 12.7 mm heavy machinegun or the multi-role 40 mm Grenade Machine Gun. The armed Hunters are used for troop transport in combat zones, as light reconnaissance vehicles or even in fire support role in COIN operations."
    },
    "limitedspeedcoef": 0.5,
    "lockdetectionsystem": 0,
    "longstiff": 15000,
    "magazines": [],
    "mapsize": 5.5,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.1,
    "maxgforce": 3,
    "maximumload": 2000,
    "maxomega": 356.05,
    "maxspeed": 109,
    "memorypointcirculumreference": "circulumReference",
    "memorypointdriveroptics": [
        "driverview",
        "pilot"
    ],
    "memorypointmissile": [
        "spice rakety",
        "usti hlavne"
    ],
    "memorypointmissiledir": [
        "konec rakety",
        "konec hlavne"
    ],
    "memorypointsgetincargo": [
        "pos codriver"
    ],
    "memorypointsgetincargodir": [
        "pos codriver dir"
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
    "memorypointtrackbll": "Stopa ZLL",
    "memorypointtrackblr": "Stopa ZLP",
    "memorypointtrackbrl": "Stopa ZPL",
    "memorypointtrackbrr": "Stopa ZPP",
    "memorypointtrackfll": "Stopa PLL",
    "memorypointtrackflr": "Stopa PLP",
    "memorypointtrackfrl": "Stopa PPL",
    "memorypointtrackfrr": "Stopa PPP",
    "mfact": 1,
    "mfd": {
        "mfd_bft": {
            "bones": {
                "direction_center": {
                    "pos": [
                        0.5,
                        0.5
                    ],
                    "type": "fixed"
                },
                "limitwaypoint": {
                    "limits": [
                        0.22,
                        0.06,
                        0.78,
                        0.06
                    ],
                    "type": "limit"
                },
                "movementx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "movementy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 5,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "rotation_wp_center": {
                    "aspectratio": 1.25714,
                    "center": [
                        0.5,
                        0.555
                    ],
                    "max": 360,
                    "maxangle": "-360-180",
                    "min": 0,
                    "minangle": -180,
                    "pos0": [
                        0,
                        0
                    ],
                    "pos10": [
                        0,
                        0
                    ],
                    "source": "heading",
                    "type": "rotational"
                },
                "rotation_wp_dir": {
                    "aspectratio": 1,
                    "center": [
                        0,
                        0
                    ],
                    "max": 360,
                    "maxangle": -360,
                    "min": 0,
                    "minangle": 0,
                    "pos0": [
                        0,
                        0
                    ],
                    "pos10": [
                        0,
                        0
                    ],
                    "source": "user",
                    "sourceindex": 10,
                    "type": "rotational"
                },
                "sensor_offset": {
                    "pos": [
                        0.5,
                        0.48
                    ],
                    "type": "fixed"
                },
                "sensor_rotation": {
                    "aspectratio": 1.25714,
                    "center": [
                        0,
                        0
                    ],
                    "max": 360,
                    "maxangle": -180,
                    "min": 0,
                    "minangle": 0,
                    "source": "heading",
                    "sourcescale": 1,
                    "type": "rotational"
                },
                "static_offset": {
                    "pos": [
                        0.5,
                        0.5
                    ],
                    "type": "fixed"
                },
                "wp10_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 44,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp10_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 45,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp11_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 46,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp11_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 47,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp1_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 26,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp1_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 27,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp2_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 28,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp2_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 29,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp3_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 30,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp3_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 31,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp4_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 32,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp4_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 33,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp5_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 34,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp5_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 35,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp6_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 36,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp6_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 37,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp7_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 38,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp7_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 39,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp8_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 40,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp8_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 41,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp9_posx": {
                    "max": 2,
                    "maxpos": [
                        -1,
                        0
                    ],
                    "min": 0,
                    "minpos": [
                        1,
                        0
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 42,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wp9_posy": {
                    "max": 2,
                    "maxpos": [
                        0,
                        1
                    ],
                    "min": 0,
                    "minpos": [
                        0,
                        -1
                    ],
                    "refreshrate": 0.1,
                    "source": "user",
                    "sourceindex": 43,
                    "sourcescale": 1,
                    "type": "linear"
                },
                "wppoint": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.71,
                        0.764
                    ],
                    "source": "WPPoint",
                    "type": "vector"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "BFT_Map_BL",
            "color": [
                1,
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0,
                    0,
                    0.12
                ],
                "lightblue": {
                    "alpha": 0.15,
                    "color": [
                        0.43,
                        0.8,
                        0.93
                    ],
                    "staticdrawpolygon": {
                        "points": [
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.00347296,
                                        -0.0247609
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0068404,
                                        -0.0236266
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.01,
                                        -0.0217744
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.01,
                                        -0.0217744
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0128558,
                                        -0.0192605
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0153209,
                                        -0.0161615
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0153209,
                                        -0.0161615
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0173205,
                                        -0.0125714
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0187939,
                                        -0.00859936
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0187939,
                                        -0.00859936
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0196962,
                                        -0.00436601
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.02,
                                        1.09903e-09
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.02,
                                        1.09903e-09
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0196962,
                                        0.00436601
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0187939,
                                        0.00859936
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0187939,
                                        0.00859936
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0173205,
                                        0.0125714
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0153209,
                                        0.0161615
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0153209,
                                        0.0161615
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0128557,
                                        0.0192606
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.01,
                                        0.0217744
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.01,
                                        0.0217744
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.0068404,
                                        0.0236266
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.00347297,
                                        0.0247609
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.00347297,
                                        0.0247609
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -1.74846e-09,
                                        0.0251429
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.00347297,
                                        0.0247609
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.00347297,
                                        0.0247609
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0068404,
                                        0.0236266
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.01,
                                        0.0217743
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.01,
                                        0.0217743
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0128558,
                                        0.0192605
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0153209,
                                        0.0161615
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0153209,
                                        0.0161615
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0173205,
                                        0.0125714
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0187939,
                                        0.00859936
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0187939,
                                        0.00859936
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0196962,
                                        0.00436601
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.02,
                                        -2.99826e-10
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.02,
                                        -2.99826e-10
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0196962,
                                        -0.00436602
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0187939,
                                        -0.00859936
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0187939,
                                        -0.00859936
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0173205,
                                        -0.0125714
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0153209,
                                        -0.0161615
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0153209,
                                        -0.0161615
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.0128557,
                                        -0.0192606
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.01,
                                        -0.0217744
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.01,
                                        -0.0217744
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.00684041,
                                        -0.0236266
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.00347296,
                                        -0.0247609
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Static_Offset",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        -0.00347296,
                                        -0.0247609
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        3.49691e-09,
                                        -0.0251429
                                    ],
                                    1
                                ],
                                [
                                    "Static_Offset",
                                    [
                                        0.00347297,
                                        -0.0247609
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    }
                },
                "sensorgroup": {
                    "sensor": {
                        "assignedtarget": {
                            "color": [
                                1,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            -0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.017,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.017,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.017,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.017,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "down": [
                            "Sensor_Offset",
                            1,
                            [
                                "0--1",
                                "0--1"
                            ],
                            1
                        ],
                        "lockingthreat": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line"
                            }
                        },
                        "markedtarget": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            -0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.017,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            -0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.017,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            -0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.017,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.017,
                                            0.0213714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.017,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "markingthreat": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line"
                            }
                        },
                        "missilethreat": {
                            "color": [
                                1,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.003472,
                                            -0.0247607
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.00684,
                                            -0.0236267
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            -0.0217737
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012856,
                                            -0.0192594
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01532,
                                            -0.0161618
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01732,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018794,
                                            -0.00859886
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.019696,
                                            -0.0043648
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.019696,
                                            0.0043648
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018794,
                                            0.00859886
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01732,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01532,
                                            0.0161618
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012856,
                                            0.0192594
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.01,
                                            0.0217737
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.00684,
                                            0.0236267
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.003472,
                                            0.0247607
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.003472,
                                            0.0247607
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.00684,
                                            0.0236267
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            0.0217737
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012856,
                                            0.0192594
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01532,
                                            0.0161618
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01732,
                                            0.0125714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018794,
                                            0.00859886
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.019696,
                                            0.0043648
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.019696,
                                            -0.0043648
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018794,
                                            -0.00859886
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01732,
                                            -0.0125714
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01532,
                                            -0.0161618
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012856,
                                            -0.0192594
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.01,
                                            -0.0217737
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.00684,
                                            -0.0236267
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.003472,
                                            -0.0247607
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            },
                            "textm": {
                                "align": "center",
                                "down": [
                                    [
                                        0,
                                        0.01
                                    ],
                                    1
                                ],
                                "pos": [
                                    [
                                        0,
                                        -0.01
                                    ],
                                    1
                                ],
                                "right": [
                                    [
                                        0.02,
                                        -0.01
                                    ],
                                    1
                                ],
                                "scale": 1,
                                "source": "static",
                                "text": "M",
                                "type": "text"
                            }
                        },
                        "pos": [
                            "Sensor_Offset",
                            1,
                            [
                                "-0+-1",
                                "-0+-1"
                            ],
                            1
                        ],
                        "range": "user0",
                        "rwr": {
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            }
                        },
                        "rwrdestroyed": {},
                        "rwrenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            }
                        },
                        "rwrfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            }
                        },
                        "rwrgroup": {
                            "color": [
                                1,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 2
                            }
                        },
                        "sensorlinetype": 0,
                        "sensorlinewidth": 3,
                        "showtargettypes": "2+4+8+16+32+64+128+256+512+1024",
                        "target": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetair": {
                            "color": [
                                1,
                                1,
                                1
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairdestroyed": {},
                        "targetairenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairgroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairremote": {
                            "color": [
                                1,
                                1,
                                1
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairremotedestroyed": {},
                        "targetairremoteenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -0.0075
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            -0.0075
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairremotefriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.004,
                                            -0.0281
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.008,
                                            -0.0224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.0129
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016,
                                            0.000400007
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetairremotegroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetarc": {
                                "points": [
                                    [
                                        [
                                            -0.02,
                                            0.0175
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            -0.025
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.02,
                                            0.0175
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ],
                                    [
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.012,
                                                -0.01
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetdestroyed": {},
                        "targetenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetground": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "staticdraw": {
                                "points": [
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            -0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.026
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.026
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "targetgrounddestroyed": {},
                        "targetgroundenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "staticdraw": {
                                "points": [
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            -0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.026
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.026
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.026,
                                            0
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "targetgroundfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "staticdraw": {
                                "points": [
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0264
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0036456,
                                            -0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.007182,
                                            -0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0105,
                                            -0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0134988,
                                            -0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016086,
                                            -0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018186,
                                            -0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0197337,
                                            -0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0206808,
                                            -0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.021,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0206808,
                                            0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0197337,
                                            0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018186,
                                            0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016086,
                                            0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0134988,
                                            0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0105,
                                            0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.007182,
                                            0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0036456,
                                            0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0264
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0036456,
                                            0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.007182,
                                            0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0105,
                                            0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0134988,
                                            0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016086,
                                            0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018186,
                                            0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0197337,
                                            0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0206808,
                                            0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.021,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0206808,
                                            -0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0197337,
                                            -0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018186,
                                            -0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016086,
                                            -0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0134988,
                                            -0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0105,
                                            -0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.007182,
                                            -0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0036456,
                                            -0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0264
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "targetgroundgroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "staticdraw": {
                                "points": [
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.012,
                                            -0.01
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            },
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0264
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0036456,
                                            -0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.007182,
                                            -0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0105,
                                            -0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0134988,
                                            -0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016086,
                                            -0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018186,
                                            -0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0197337,
                                            -0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0206808,
                                            -0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.021,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0206808,
                                            0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0197337,
                                            0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.018186,
                                            0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.016086,
                                            0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0134988,
                                            0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0105,
                                            0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.007182,
                                            0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0036456,
                                            0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            0.0264
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0036456,
                                            0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.007182,
                                            0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0105,
                                            0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0134988,
                                            0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016086,
                                            0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018186,
                                            0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0197337,
                                            0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0206808,
                                            0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.021,
                                            0
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0206808,
                                            -0.00458304
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0197337,
                                            -0.0090288
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.018186,
                                            -0.0132
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.016086,
                                            -0.0169699
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0134988,
                                            -0.0202224
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0105,
                                            -0.0228624
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.007182,
                                            -0.0248081
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0036456,
                                            -0.0259987
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0,
                                            -0.0264
                                        ],
                                        1
                                    ]
                                ],
                                "type": "line",
                                "width": 3
                            }
                        },
                        "targetgroundremote": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetgroundremotedestroyed": {},
                        "targetgroundremoteenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetgroundremotefriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetgroundremotegroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetgroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetlaser": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetlaserenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetlaserfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetlasergroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetlinelength": 0.02,
                        "targetlinewidth": -0.00192,
                        "targetman": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmangroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanremote": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanremoteenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanremotefriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetmanremotegroup": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.01,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                -0.01
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.01,
                                                0
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            }
                        },
                        "targetnvg": {
                            "color": [
                                1,
                                0.3,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetnvgenemy": {
                            "color": [
                                0.12,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetnvgfriendly": {
                            "color": [
                                0,
                                0,
                                0.12
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "targetnvggroup": {
                            "color": [
                                1,
                                0,
                                0
                            ],
                            "targetlines": {
                                "points": [
                                    [
                                        [
                                            0,
                                            -0.0251429
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -1.74846e-09,
                                            0.0251429
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.02,
                                            1.09903e-09
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.02,
                                            -2.99826e-10
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [],
                                    [
                                        [
                                            0.0106066,
                                            0.013334
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0106066,
                                            -0.013334
                                        ],
                                        1
                                    ],
                                    []
                                ],
                                "type": "line",
                                "width": 4
                            }
                        },
                        "type": "sensor",
                        "width": 4
                    }
                },
                "staticclip": {
                    "waypointgroup": {
                        "alpha": 0.6,
                        "color": [
                            0,
                            0,
                            0.12
                        ],
                        "wp": {
                            "condition": "wpvalid",
                            "customwp": {
                                "alpha": 0.5,
                                "color": [
                                    1,
                                    0.5,
                                    0
                                ],
                                "condition": "user46>=0",
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP11_PosX",
                                        1,
                                        "WP11_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP11_PosX",
                                        1,
                                        "WP11_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP11_PosX",
                                        1,
                                        "WP11_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "CWP",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP11_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP11_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        []
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "draw": {
                                "points": [],
                                "type": "line"
                            },
                            "wp1": {
                                "condition": "user26>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "1-WPIndex",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 16
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP1_PosX",
                                        1,
                                        "WP1_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP1_PosX",
                                        1,
                                        "WP1_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP1_PosX",
                                        1,
                                        "WP1_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "01",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP1_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        []
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp10": {
                                "condition": "user44>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=9)*(WPIndex<=9)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP10_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP10_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP10_PosX",
                                        1,
                                        "WP10_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP10_PosX",
                                        1,
                                        "WP10_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP10_PosX",
                                        1,
                                        "WP10_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "10",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP10_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            1,
                                            "WP9_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP10_PosX",
                                            1,
                                            "WP10_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp2": {
                                "condition": "user28>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=1)*(WPIndex<=1)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP2_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP2_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 16
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP2_PosX",
                                        1,
                                        "WP2_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP2_PosX",
                                        1,
                                        "WP2_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP2_PosX",
                                        1,
                                        "WP2_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "02",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP2_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP1_PosX",
                                            1,
                                            "WP1_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            1,
                                            "WP2_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp3": {
                                "condition": "user30>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=2)*(WPIndex<=2)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP3_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP3_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP3_PosX",
                                        1,
                                        "WP3_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP3_PosX",
                                        1,
                                        "WP3_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP3_PosX",
                                        1,
                                        "WP3_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "03",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP3_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP2_PosX",
                                            1,
                                            "WP2_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            1,
                                            "WP3_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp4": {
                                "condition": "user32>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=3)*(WPIndex<=3)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP4_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP4_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP4_PosX",
                                        1,
                                        "WP4_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP4_PosX",
                                        1,
                                        "WP4_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP4_PosX",
                                        1,
                                        "WP4_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "04",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP4_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP3_PosX",
                                            1,
                                            "WP3_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            1,
                                            "WP4_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp5": {
                                "condition": "user34>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=4)*(WPIndex<=4)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP5_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP5_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP5_PosX",
                                        1,
                                        "WP5_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP5_PosX",
                                        1,
                                        "WP5_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP5_PosX",
                                        1,
                                        "WP5_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "05",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP5_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP4_PosX",
                                            1,
                                            "WP4_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            1,
                                            "WP5_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp6": {
                                "condition": "user36>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=5)*(WPIndex<=5)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP6_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP6_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP6_PosX",
                                        1,
                                        "WP6_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP6_PosX",
                                        1,
                                        "WP6_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP6_PosX",
                                        1,
                                        "WP6_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "06",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP6_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP5_PosX",
                                            1,
                                            "WP5_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            1,
                                            "WP6_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp7": {
                                "condition": "user38>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=6)*(WPIndex<=6)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP7_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP7_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP7_PosX",
                                        1,
                                        "WP7_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP7_PosX",
                                        1,
                                        "WP7_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP7_PosX",
                                        1,
                                        "WP7_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "07",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP7_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP6_PosX",
                                            1,
                                            "WP6_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            1,
                                            "WP7_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp8": {
                                "condition": "user40>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=7)*(WPIndex<=7)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP8_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP8_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP8_PosX",
                                        1,
                                        "WP8_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP8_PosX",
                                        1,
                                        "WP8_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP8_PosX",
                                        1,
                                        "WP8_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "08",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP8_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP7_PosX",
                                            1,
                                            "WP7_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            1,
                                            "WP8_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            },
                            "wp9": {
                                "condition": "user42>=0",
                                "currentwaypoint": {
                                    "alpha": 1,
                                    "color": [
                                        0.9,
                                        0,
                                        0
                                    ],
                                    "condition": "(WPIndex>=8)*(WPIndex<=8)",
                                    "waypointshape": {
                                        "points": [
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0,
                                                    0.0125714
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.001736,
                                                    0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00342,
                                                    0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.005,
                                                    0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.006428,
                                                    0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00766,
                                                    0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00866,
                                                    0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.009397,
                                                    0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.009848,
                                                    0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.01,
                                                    0
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.009848,
                                                    -0.0021824
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.009397,
                                                    -0.00429943
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00866,
                                                    -0.00628571
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00766,
                                                    -0.00808091
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.006428,
                                                    -0.00962971
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.005,
                                                    -0.0108869
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.00342,
                                                    -0.0118134
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    -0.001736,
                                                    -0.0123803
                                                ],
                                                1
                                            ],
                                            [
                                                "WP9_PosY",
                                                1,
                                                "Direction_Center",
                                                1,
                                                "WP9_PosX",
                                                [
                                                    0,
                                                    -0.0125714
                                                ],
                                                1
                                            ],
                                            []
                                        ],
                                        "type": "line",
                                        "width": 22
                                    }
                                },
                                "texwpnumber": {
                                    "align": "center",
                                    "down": [
                                        "Direction_Center",
                                        1,
                                        "WP9_PosX",
                                        1,
                                        "WP9_PosY",
                                        1,
                                        [
                                            0.05,
                                            0.011
                                        ],
                                        1
                                    ],
                                    "pos": [
                                        "Direction_Center",
                                        1,
                                        "WP9_PosX",
                                        1,
                                        "WP9_PosY",
                                        1,
                                        [
                                            0.05,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "right": [
                                        "Direction_Center",
                                        1,
                                        "WP9_PosX",
                                        1,
                                        "WP9_PosY",
                                        1,
                                        [
                                            0.072,
                                            -0.008
                                        ],
                                        1
                                    ],
                                    "scale": 1,
                                    "source": "static",
                                    "sourcescale": 1,
                                    "text": "09",
                                    "type": "text"
                                },
                                "waypointshape": {
                                    "points": [
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0,
                                                0.0251429
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.003472,
                                                0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.00684,
                                                0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01,
                                                0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.012856,
                                                0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01532,
                                                0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01732,
                                                0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.018794,
                                                0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.019696,
                                                0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.02,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.019696,
                                                -0.0043648
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.018794,
                                                -0.00859886
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01732,
                                                -0.0125714
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01532,
                                                -0.0161618
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.012856,
                                                -0.0192594
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.01,
                                                -0.0217737
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.00684,
                                                -0.0236267
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                -0.003472,
                                                -0.0247607
                                            ],
                                            1
                                        ],
                                        [
                                            "WP9_PosY",
                                            1,
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            [
                                                0,
                                                -0.0251429
                                            ],
                                            1
                                        ],
                                        [],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP8_PosX",
                                            1,
                                            "WP8_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ],
                                        [
                                            "Direction_Center",
                                            1,
                                            "WP9_PosX",
                                            1,
                                            "WP9_PosY",
                                            1,
                                            [
                                                0,
                                                0
                                            ],
                                            1
                                        ]
                                    ],
                                    "type": "line",
                                    "width": 6
                                }
                            }
                        }
                    }
                },
                "staticdraw": {
                    "points": [
                        [
                            "Static_Offset",
                            [
                                0,
                                -0.0264
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0036456,
                                -0.0259987
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.007182,
                                -0.0248081
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0105,
                                -0.0228624
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0134988,
                                -0.0202224
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.016086,
                                -0.0169699
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.018186,
                                -0.0132
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0197337,
                                -0.0090288
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0206808,
                                -0.00458304
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.021,
                                0
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0206808,
                                0.00458304
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0197337,
                                0.0090288
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.018186,
                                0.0132
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.016086,
                                0.0169699
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0134988,
                                0.0202224
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0105,
                                0.0228624
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.007182,
                                0.0248081
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0.0036456,
                                0.0259987
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0,
                                0.0264
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0036456,
                                0.0259987
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.007182,
                                0.0248081
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0105,
                                0.0228624
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0134988,
                                0.0202224
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.016086,
                                0.0169699
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.018186,
                                0.0132
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0197337,
                                0.0090288
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0206808,
                                0.00458304
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.021,
                                0
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0206808,
                                -0.00458304
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0197337,
                                -0.0090288
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.018186,
                                -0.0132
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.016086,
                                -0.0169699
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0134988,
                                -0.0202224
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0105,
                                -0.0228624
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.007182,
                                -0.0248081
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                -0.0036456,
                                -0.0259987
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            [
                                0,
                                -0.0264
                            ],
                            1
                        ],
                        [],
                        [
                            "Static_Offset",
                            1,
                            [
                                -0.012,
                                -0.01
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            1,
                            [
                                -0.012,
                                0.01
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            1,
                            [
                                0.012,
                                0.01
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            1,
                            [
                                0.012,
                                -0.01
                            ],
                            1
                        ],
                        [
                            "Static_Offset",
                            1,
                            [
                                -0.012,
                                -0.01
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line",
                    "width": 6
                }
            },
            "font": "rhsusf_txled",
            "helmetdown": [
                0,
                -0.075,
                0
            ],
            "helmetmounteddisplay": 0,
            "helmetposition": [
                -0.0375,
                0.0375,
                0.1
            ],
            "helmetright": [
                0.075,
                0,
                0
            ],
            "material": {
                "ambient": [
                    33,
                    33,
                    33,
                    1
                ],
                "diffuse": [
                    31,
                    31,
                    31,
                    1
                ],
                "emissive": [
                    400,
                    200,
                    200,
                    1
                ]
            },
            "topleft": "BFT_Map_TL",
            "topright": "BFT_Map_TR"
        },
        "mfd_gps": {
            "alpha": 1,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0.01,
            "borderright": 0.01,
            "bordertop": 0,
            "bottomleft": "MFD_GPS_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 0.8,
                "back_text": {
                    "align": "right",
                    "down": [
                        [
                            0.74,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.74,
                            0.85
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.84,
                            0.85
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "Back",
                    "type": "text"
                },
                "color": [
                    0,
                    0,
                    0,
                    1
                ],
                "condition": "on",
                "cordx": {
                    "align": "right",
                    "down": [
                        [
                            0.09,
                            0.33
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.09,
                            0.15
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.215,
                            0.15
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "coordinateX",
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "sourcescale": 0.01,
                    "type": "text"
                },
                "cordy": {
                    "align": "right",
                    "down": [
                        [
                            0.26,
                            0.33
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.26,
                            0.15
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.385,
                            0.15
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "coordinateY",
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "sourcescale": 0.01,
                    "type": "text"
                },
                "date1_text": {
                    "align": "right",
                    "down": [
                        [
                            0.51,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.51,
                            0.73
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.61,
                            0.73
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "-",
                    "type": "text"
                },
                "date2_text": {
                    "align": "right",
                    "down": [
                        [
                            0.66,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.66,
                            0.73
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.76,
                            0.73
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "-",
                    "type": "text"
                },
                "date_day_value": {
                    "align": "left",
                    "down": [
                        [
                            0.5,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.73
                        ],
                        1
                    ],
                    "refreshrate": 0.08,
                    "right": [
                        [
                            0.6,
                            0.73
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "time",
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "text": "%d",
                    "type": "text"
                },
                "date_month_value": {
                    "align": "left",
                    "down": [
                        [
                            0.65,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.65,
                            0.73
                        ],
                        1
                    ],
                    "refreshrate": 0.08,
                    "right": [
                        [
                            0.75,
                            0.73
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "time",
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "text": "%b",
                    "type": "text"
                },
                "date_year_value": {
                    "align": "left",
                    "down": [
                        [
                            0.77,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.77,
                            0.73
                        ],
                        1
                    ],
                    "refreshrate": 0.08,
                    "right": [
                        [
                            0.87,
                            0.73
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "time",
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "text": "%y",
                    "type": "text"
                },
                "elevation2_text": {
                    "align": "right",
                    "down": [
                        [
                            0.71,
                            0.52
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.71,
                            0.43
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.78,
                            0.43
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "MSL",
                    "type": "text"
                },
                "elevation3_text": {
                    "align": "right",
                    "down": [
                        [
                            0.42,
                            0.66
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.42,
                            0.48
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.545,
                            0.48
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "+",
                    "type": "text"
                },
                "elevation4_text": {
                    "align": "right",
                    "down": [
                        [
                            0.74,
                            0.65
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.74,
                            0.5
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.84,
                            0.5
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "m",
                    "type": "text"
                },
                "elevation_text": {
                    "align": "right",
                    "down": [
                        [
                            0.4,
                            0.52
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.4,
                            0.43
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.47,
                            0.43
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "ELEVATION",
                    "type": "text"
                },
                "elevation_value": {
                    "align": "left",
                    "down": [
                        [
                            0.73,
                            0.66
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.73,
                            0.48
                        ],
                        1
                    ],
                    "refreshrate": 0.8,
                    "right": [
                        [
                            0.855,
                            0.48
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcelength": 5,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gotowp_text": {
                    "align": "right",
                    "down": [
                        [
                            0.03,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.03,
                            0.85
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.13,
                            0.85
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "GOTO WP",
                    "type": "text"
                },
                "mag_text": {
                    "align": "right",
                    "down": [
                        [
                            0.29,
                            0.74
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.29,
                            0.65
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.36,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "MAG",
                    "type": "text"
                },
                "mgrs_text": {
                    "align": "right",
                    "down": [
                        [
                            0.04,
                            0.2
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.04,
                            0.08
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.13,
                            0.08
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "MGRS-Arma",
                    "type": "text"
                },
                "o_text": {
                    "align": "right",
                    "down": [
                        [
                            0.31,
                            0.78
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.31,
                            0.69
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.38,
                            0.69
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "o",
                    "type": "text"
                },
                "on_text": {
                    "align": "left",
                    "down": [
                        [
                            0.89,
                            0.16
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.89,
                            0.09
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.94,
                            0.09
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "ON",
                    "type": "text"
                },
                "polygondraw": {
                    "alpha": 1,
                    "color": [
                        0.0705882,
                        0.0862745,
                        0.0235294
                    ],
                    "polygon": {
                        "points": [
                            [
                                [
                                    [
                                        0,
                                        -0.23
                                    ],
                                    1
                                ],
                                [
                                    [
                                        1,
                                        -0.23
                                    ],
                                    1
                                ],
                                [
                                    [
                                        1,
                                        1.12
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0,
                                        1.12
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "texture": "rhsusf/addons/rhsusf_matv/data/rhs_dagr_background_ca.paa",
                        "type": "polygon"
                    },
                    "polygon2": {
                        "points": [],
                        "type": "polygon"
                    }
                },
                "presentpos_text": {
                    "align": "right",
                    "down": [
                        [
                            0.05,
                            0.09
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.05,
                            0
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.12,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "PRESENT POSITION",
                    "type": "text"
                },
                "speed2_text": {
                    "align": "right",
                    "down": [
                        [
                            0.21,
                            0.65
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.21,
                            0.5
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.31,
                            0.5
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "kph",
                    "type": "text"
                },
                "speed_text": {
                    "align": "right",
                    "down": [
                        [
                            0.04,
                            0.52
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.04,
                            0.43
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.11,
                            0.43
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "SPEED",
                    "type": "text"
                },
                "speed_value": {
                    "align": "left",
                    "down": [
                        [
                            0.2,
                            0.66
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.2,
                            0.48
                        ],
                        1
                    ],
                    "refreshrate": 0.3,
                    "right": [
                        [
                            0.325,
                            0.48
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcelength": 1,
                    "sourcescale": 3.6,
                    "type": "text"
                },
                "static1_text": {
                    "align": "left",
                    "down": [
                        [
                            0.96,
                            0.325
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.96,
                            0.235
                        ],
                        1
                    ],
                    "right": [
                        [
                            1.02,
                            0.235
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": ">99dsf",
                    "type": "text"
                },
                "static2_text": {
                    "align": "left",
                    "down": [
                        [
                            0.96,
                            0.63
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.96,
                            0.54
                        ],
                        1
                    ],
                    "right": [
                        [
                            1.03,
                            0.54
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "32534",
                    "type": "text"
                },
                "stby_text": {
                    "align": "left",
                    "down": [
                        [
                            0.95,
                            0.085
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.95,
                            0.005
                        ],
                        1
                    ],
                    "right": [
                        [
                            1.02,
                            0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "STBY",
                    "type": "text"
                },
                "time_value": {
                    "align": "left",
                    "down": [
                        [
                            0.7,
                            0.78
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.7,
                            0.65
                        ],
                        1
                    ],
                    "refreshrate": 0.08,
                    "right": [
                        [
                            0.8,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "time",
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "text": "%X",
                    "type": "text"
                },
                "timetext": {
                    "align": "right",
                    "down": [
                        [
                            0.71,
                            0.78
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.71,
                            0.65
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.81,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "Z",
                    "type": "text"
                },
                "track_text": {
                    "align": "right",
                    "down": [
                        [
                            0.04,
                            0.74
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.04,
                            0.65
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.11,
                            0.65
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "TRACK",
                    "type": "text"
                },
                "track_value": {
                    "align": "left",
                    "down": [
                        [
                            0.3,
                            0.86
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.3,
                            0.69
                        ],
                        1
                    ],
                    "refreshrate": 0.3,
                    "right": [
                        [
                            0.43,
                            0.69
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourceindex": 2,
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "type": "text"
                },
                "wp": {
                    "condition": "wpvalid",
                    "wpdist": {
                        "align": "left",
                        "down": [
                            [
                                0.76,
                                0.45
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.76,
                                0.27
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.885,
                                0.27
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
                        "align": "left",
                        "down": [
                            [
                                0.76,
                                0.33
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.76,
                                0.15
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.885,
                                0.15
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "wpIndex",
                        "sourcelength": 2,
                        "sourcescale": 1,
                        "type": "text"
                    }
                },
                "wp_text": {
                    "align": "right",
                    "down": [
                        [
                            0.71,
                            0.2
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.71,
                            0.08
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.8,
                            0.08
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "WP",
                    "type": "text"
                },
                "wplist_text": {
                    "align": "right",
                    "down": [
                        [
                            0.38,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.38,
                            0.85
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.48,
                            0.85
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "WP List",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "rhsusf_digital_font_usa",
            "material": {
                "ambient": [
                    16,
                    16,
                    16,
                    1
                ],
                "diffuse": [
                    10,
                    10,
                    10,
                    1
                ],
                "emissive": [
                    2000,
                    4000,
                    2000,
                    1
                ]
            },
            "topleft": "MFD_GPS_TL",
            "topright": "MFD_GPS_TR"
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
    "minomega": 41,
    "mintotaldamagethreshold": 0.01,
    "model": "rhsusf/addons/rhsusf_m11xx/rhsusf_m1152",
    "namesound": "veh_vehicle_MRAP_s",
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
    "normalspeedforwardcoef": 0.7,
    "numberphysicalwheels": 4,
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
    "outsidesoundfilter": 0,
    "peaktorque": 597,
    "picture": "rhsusf/addons/rhsusf_m11xx/pictures/rhs_m1152_rsv_pic_ca.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "plateinfos": {
        "color": [
            0,
            0,
            0,
            0.75
        ],
        "name": "spz"
    },
    "playersteeringcoefficients": {
        "maxturnhundred": 1,
        "turndecreaseconst": 5,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "turnincreaseconst": 1,
        "turnincreaselinear": 1,
        "turnincreasetime": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 9,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "preferroads": 1,
    "pulsationsound": {},
    "radartype": 0,
    "rearbias": 1.9,
    "receiveremotetargets": 1,
    "redrpm": 3400,
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
            "direction": "Light_L_end",
            "flaresize": 1,
            "hitpoint": "Light_L",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "useflare": 0
        },
        "left2": {
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
            "direction": "Light_L_end",
            "flaresize": 1,
            "hitpoint": "Light_L",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "light_L_flare",
            "selection": "Light_L",
            "size": 1,
            "useflare": 1
        },
        "long_left": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 750,
                "hardlimitstart": 500,
                "linear": 0.1,
                "quadratic": 0,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "Light_L_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "Light_L",
            "innerangle": 22,
            "intensity": 100,
            "outerangle": 26,
            "position": "Light_L_Long",
            "selection": "Light_L",
            "size": 1,
            "useflare": 0
        },
        "long_left2": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_L_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "Light_L",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
            "position": "light_L_Long_flare",
            "selection": "Light_L",
            "size": 1,
            "useflare": 1
        },
        "long_right": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 750,
                "hardlimitstart": 500,
                "linear": 0.1,
                "quadratic": 0,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "Light_R_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "Light_R",
            "innerangle": 22,
            "intensity": 100,
            "outerangle": 26,
            "position": "Light_R_Long",
            "selection": "Light_R",
            "size": 1,
            "useflare": 0
        },
        "long_right2": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_R_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "Light_R",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
            "position": "light_R_Long_flare",
            "selection": "Light_R",
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
            "direction": "Light_R_end",
            "flaresize": 1,
            "hitpoint": "Light_R",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "Light_R",
            "selection": "Light_R",
            "size": 1,
            "useflare": 0
        },
        "right2": {
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
            "direction": "Light_R_end",
            "flaresize": 1,
            "hitpoint": "Light_R",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "light_R_flare",
            "selection": "Light_R",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "leftmirror": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "m1D",
                "pointposition": "m1P",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget0"
        },
        "rightmirror": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "m2D",
                "pointposition": "m2P",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget1"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reportownposition": 1,
    "reportremotetargets": 1,
    "reversed": 1,
    "rhs_duke_type": "rhsusf_duke",
    "rhs_towingsystem": {
        "carrier": {
            "rhs_attachpoint": "",
            "rhs_attachpointpos": [
                -0.05,
                -2.47,
                -1.02
            ],
            "rhs_maxcargomass": 1500
        }
    },
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
    "scope": 2,
    "scudeffect": "ScudEffect",
    "scudmodel": "",
    "secondaryexplosion": -10,
    "selectionbacklights": "light_drive",
    "selectionbrakelights": "light_brake",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 1.75,
    "sensitivityear": 0.125,
    "sensorposition": "sensorPos",
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
    "simulation": "carx",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [],
    "slownspeedforwardcoef": 0.55,
    "slowspeedforwardcoef": 0.3,
    "smokelauncherangle": 360,
    "smokelaunchergrenadecount": 8,
    "smokelauncheronturret": 0,
    "smokelaunchervelocity": 14,
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
        "A3/sounds_f/dummysound",
        1,
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
        1.77828,
        0.9
    ],
    "soundengineoffext": [
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Engine_Ext_stop",
        1.99526,
        1,
        50
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Engine_Int_stop",
        0.501187,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Engine_Ext_Start",
        1.99526,
        1,
        50
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Engine_Int_Start",
        0.630957,
        1
    ],
    "soundenviron": [
        "",
        0.000562341,
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
        1e-05,
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
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Enter",
        0.446684,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles2/soft/Mrap_01/Mrap_01_Exit",
        0.446684,
        1,
        40
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "",
        1,
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
        "soundsetsext": [
            "Mrap_01_Engine_RPM0_EXT_SoundSet",
            "Mrap_01_Engine_RPM1_EXT_SoundSet",
            "Mrap_01_Engine_RPM2_EXT_SoundSet",
            "Mrap_01_Engine_RPM3_EXT_SoundSet",
            "Mrap_01_Engine_RPM4_EXT_SoundSet",
            "Mrap_01_Engine_EXT_Burst_SoundSet",
            "Mrap_01_Rattling_EXT_SoundSet",
            "Mrap_01_Stress_EXT_SoundSet",
            "Mrap_01_Rain_EXT_SoundSet",
            "Mrap_01_Tires_Rock_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Grass_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Sand_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Gravel_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Mud_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Asphalt_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Water_Fast_EXT_SoundSet",
            "Mrap_01_Tires_Rock_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Grass_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Sand_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Gravel_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Mud_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Asphalt_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Water_Slow_EXT_SoundSet",
            "Mrap_01_Tires_Turn_Hard_EXT_SoundSet",
            "Mrap_01_Tires_Turn_Soft_EXT_SoundSet",
            "Mrap_01_Tires_Brake_Hard_EXT_SoundSet",
            "Mrap_01_Tires_Brake_Soft_EXT_SoundSet",
            "",
            "Tires_Movement_Dirt_Ext_01_SoundSet"
        ],
        "soundsetsint": [
            "Mrap_01_Engine_RPM0_INT_SoundSet",
            "Mrap_01_Engine_RPM1_INT_SoundSet",
            "Mrap_01_Engine_RPM2_INT_SoundSet",
            "Mrap_01_Engine_RPM3_INT_SoundSet",
            "Mrap_01_Engine_RPM4_INT_SoundSet",
            "Mrap_01_Engine_INT_Burst_SoundSet",
            "Mrap_01_Rattling_INT_SoundSet",
            "Mrap_01_Stress_INT_SoundSet",
            "Mrap_01_Rain_INT_SoundSet",
            "Mrap_01_Tires_Rock_Fast_INT_SoundSet",
            "Mrap_01_Tires_Grass_Fast_INT_SoundSet",
            "Mrap_01_Tires_Sand_Fast_INT_SoundSet",
            "Mrap_01_Tires_Gravel_Fast_INT_SoundSet",
            "Mrap_01_Tires_Mud_Fast_INT_SoundSet",
            "Mrap_01_Tires_Asphalt_Fast_INT_SoundSet",
            "Mrap_01_Tires_Water_Fast_INT_SoundSet",
            "Mrap_01_Tires_Rock_Slow_INT_SoundSet",
            "Mrap_01_Tires_Grass_Slow_INT_SoundSet",
            "Mrap_01_Tires_Sand_Slow_INT_SoundSet",
            "Mrap_01_Tires_Gravel_Slow_INT_SoundSet",
            "Mrap_01_Tires_Mud_Slow_INT_SoundSet",
            "Mrap_01_Tires_Asphalt_Slow_INT_SoundSet",
            "Mrap_01_Tires_Water_Slow_INT_SoundSet",
            "Mrap_01_Tires_Turn_Hard_INT_SoundSet",
            "Mrap_01_Tires_Turn_Soft_INT_SoundSet",
            "Mrap_01_Tires_Brake_Hard_INT_SoundSet",
            "Mrap_01_Tires_Brake_Soft_INT_SoundSet",
            "",
            "Tires_Movement_Dirt_Int_01_SoundSet"
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
                "veh_vehicle_MRAP_p"
            ],
            "speechsingular": [
                "veh_vehicle_MRAP_s"
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
    "steeraheadplan": 0.35,
    "steeraheadsimul": 0.5,
    "supplyradius": 12,
    "switchtime": 0.5,
    "tbody": 150,
    "terraincoef": 0.5,
    "textplural": "MRAPs",
    "textsingular": "MRAP",
    "texturelist": [
        "rhs_desert",
        1
    ],
    "texturesources": {
        "rhs_desert": {
            "author": "Red Hammer Studios",
            "decals": [
                8
            ],
            "displayname": "Desert",
            "factions": [],
            "textures": [
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Ext_d_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_d_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_d_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_d_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/tile_exmetal_d_co.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152M1165_d_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_2drcargo_d_co.paa"
            ]
        },
        "rhs_olive": {
            "author": "Red Hammer Studios",
            "decals": [
                7
            ],
            "displayname": "Olive",
            "factions": [],
            "textures": [
                "rhsusf/addons/rhsusf_m11xx/data/rhssaf_M1151_Ext_o_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_wd_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_w_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/tile_exmetal_co.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhssaf_M1152M1165_o_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_2drcargo_g_co.paa"
            ]
        },
        "rhs_woodland": {
            "author": "Red Hammer Studios",
            "decals": [
                8
            ],
            "displayname": "Woodland",
            "factions": [],
            "textures": [
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Ext_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_wd_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_w_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/tile_exmetal_co.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1152M1165_wd_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_2drcargo_w_co.paa"
            ]
        },
        "rhssaf_green": {
            "author": "Red Hammer Studios",
            "decals": [
                7
            ],
            "displayname": "SAF",
            "factions": [],
            "textures": [
                "rhsusf/addons/rhsusf_m11xx/data/rhssaf_M1151_Ext_o_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Tire_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Int_wd_CO.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhsusf_M1151_Acc_wd_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_exterior_g_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/tile_exmetal_co.paa",
                "rhsusf/addons/rhsusf_m11xx/data/rhssaf_M1152M1165_o_CO.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/m998_2drcargo_g_co.paa"
            ]
        }
    },
    "tf_haslrradio_api": 1,
    "threat": [
        0.1,
        0.1,
        0.1
    ],
    "thrustdelay": 0.8,
    "torquecurve": [
        [
            0.191176,
            0.703518
        ],
        [
            0.294118,
            0.778894
        ],
        [
            0.411765,
            0.911223
        ],
        [
            0.529412,
            1
        ],
        [
            0.705882,
            0.976549
        ],
        [
            0.764706,
            0.835846
        ],
        [
            0.941176,
            0.79062
        ],
        [
            1.05971,
            0
        ]
    ],
    "tracksspeed": 0,
    "transmissionlosses": 20,
    "transportammo": 250000,
    "transportbackpacks": {
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 1
        }
    },
    "transportfuel": 250000,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 10,
            "name": "FirstAidKit"
        },
        "_xx_toolkit": {
            "count": 1,
            "name": "Toolkit"
        }
    },
    "transportmagazines": {
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 10,
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag"
        },
        "_xx_rhs_mag_an_m8hc": {
            "count": 4,
            "magazine": "rhs_mag_an_m8hc"
        },
        "_xx_rhs_mag_m18_green": {
            "count": 2,
            "magazine": "rhs_mag_m18_green"
        },
        "_xx_rhs_mag_m18_red": {
            "count": 2,
            "magazine": "rhs_mag_m18_red"
        },
        "_xx_rhs_mag_m67": {
            "count": 2,
            "magazine": "rhs_mag_m67"
        }
    },
    "transportmaxbackpacks": 25,
    "transportmaxmagazines": 64,
    "transportmaxweapons": 12,
    "transportrepair": 5000000.0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_m4_carryhandle": {
            "count": 2,
            "weapon": "rhs_weap_m4_carryhandle"
        }
    },
    "turncoef": 3,
    "turrets": {
        "codriverturret": {
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
            "gunneraction": "RHS_M11XX_CoDriver",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "Door_RF",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_M11XX_CoDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Co-driver",
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
            "ispersonturret": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
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
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
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
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscMATV_Codriver",
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
        }
    },
    "type": 0,
    "typicalcargo": [
        "Soldier"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoMATV",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "useractions": {
        "adjustmap": {
            "condition": "((this turretUnit [0]) isEqualTo (call rhs_fnc_findPlayer)) && this animationSourcePhase 'bft_hide'<0.5;",
            "displayname": "Adjust BFT Map Scale",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 20,
            "statement": "createDialog 'RHS_BFT_Map_Scale_UI';sliderSetRange [1900,0.01,1];sliderSetPosition [1900,cameraon animationSourcePhase 'BFT_Map_Scale']"
        },
        "cabinlights_toggle": {
            "condition": "(player == driver this) AND (isLightOn this)",
            "displayname": "Toggle cabin lights",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "lockTarget",
            "showwindow": 0,
            "statement": "[this,1] call rhsusf_fnc_carLightToggle"
        },
        "light_bo_off": {
            "condition": "(player == driver this) && this animationPhase 'light_bo'<0.5;",
            "displayname": "B.O. Light off",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "radius": 2,
            "statement": "this animate ['light_bo', 1];this animate ['light_brake_bo', 1]"
        },
        "light_bo_on": {
            "condition": "(player == driver this) && this animationPhase 'light_bo'==1;",
            "displayname": "B.O. Light on",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "radius": 2,
            "statement": "this animate ['light_bo', 0];this animate ['light_brake_bo', 0]"
        },
        "light_stop_off": {
            "condition": "(player == driver this) && this animationPhase 'light_stop'<0.5",
            "displayname": "Stop Light off",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "radius": 2,
            "statement": "this animate ['light_stop', 1]"
        },
        "light_stop_on": {
            "condition": "(player == driver this) && this animationPhase 'light_stop'==1",
            "displayname": "Stop Light on",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "radius": 2,
            "statement": "this animate ['light_stop', 0]"
        },
        "lights_toggle": {
            "condition": "(player == driver this) AND (isLightOn this)",
            "displayname": "Toggle short/long lights",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "vehLockTargets",
            "showwindow": 0,
            "statement": "[this,0] call rhsusf_fnc_carLightToggle"
        },
        "trunk_close": {
            "condition": "this animationSourcePhase 'door_trunk'==1",
            "displayname": "Close Trunk",
            "onlyforplayer": 0,
            "position": "trunk_action",
            "radius": 2,
            "statement": "this animateSource ['door_trunk', 0]"
        },
        "trunk_open": {
            "condition": "this  animationSourcePhase 'm1151_Hide'==0 && this animationSourcePhase 'door_trunk'<0.5",
            "displayname": "Open Trunk",
            "onlyforplayer": 0,
            "position": "trunk_action",
            "radius": 2,
            "statement": "this animateSource ['door_trunk', 1];"
        }
    },
    "uvanimations": {
        "bft_map_move_x": {
            "center": [
                1,
                0
            ],
            "maxvalue": 100000,
            "offset0": [
                0,
                0
            ],
            "offset1": [
                100,
                0
            ],
            "section": "BFT_screen",
            "source": "BFT_Map_Move_X",
            "type": "translation"
        },
        "bft_map_move_y": {
            "center": [
                1,
                0
            ],
            "maxvalue": 100000,
            "offset0": [
                0,
                0
            ],
            "offset1": [
                0,
                -100
            ],
            "section": "BFT_screen",
            "source": "BFT_Map_Move_Y",
            "type": "translation"
        },
        "bft_map_rotate": {
            "angle0": "rad -180",
            "angle1": "rad 180",
            "center": [
                1,
                1
            ],
            "maxvalue": "rad 180",
            "minvalue": "rad -180",
            "scale0": [
                0,
                0
            ],
            "scale1": [
                1,
                1
            ],
            "section": "BFT_screen",
            "source": "direction",
            "type": "rotate"
        },
        "bft_map_scale": {
            "center": [
                1,
                1
            ],
            "maxvalue": 1,
            "minvalue": 0,
            "scale0": [
                0,
                0
            ],
            "scale1": [
                1,
                1
            ],
            "section": "BFT_screen",
            "source": "BFT_Map_Scale",
            "type": "scale"
        }
    },
    "vehicleclass": "Car",
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
    "viewcargoshadowamb": 1,
    "viewcargoshadowdiff": 1,
    "viewdriverinexternal": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.85,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.42,
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
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 20,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.2,
    "waterspeedfactor": 0.3,
    "weapons": [
        "TruckHorn2"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.95,
    "wheeldamageradiuscoef": 0.75,
    "wheeldamagethreshold": 0.18,
    "wheeldestroyradiuscoef": 0.48,
    "wheeldestroythreshold": 0.99,
    "wheelmask": "wheel_X_X",
    "wheels": {
        "l1": {
            "bonename": "wheel_1_1_damper",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2.5
                ],
                [
                    0.5,
                    2.3
                ],
                [
                    1,
                    2
                ]
            ],
            "latstiffx": 40,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 80,
            "maxbraketorque": 35000,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "maxhandbraketorque": 0,
            "moi": 25,
            "side": "left",
            "springdamperrate": 15725,
            "springstrength": 58550,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_1_axis",
            "width": 0.24
        },
        "l2": {
            "bonename": "wheel_1_2_damper",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2.5
                ],
                [
                    0.5,
                    2.3
                ],
                [
                    1,
                    2
                ]
            ],
            "latstiffx": 40,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 80,
            "maxbraketorque": 35000,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "maxhandbraketorque": 0,
            "moi": 25,
            "side": "left",
            "springdamperrate": 15725,
            "springstrength": 58550,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_1_2_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.24
        },
        "r1": {
            "bonename": "wheel_2_1_damper",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2.5
                ],
                [
                    0.5,
                    2.3
                ],
                [
                    1,
                    2
                ]
            ],
            "latstiffx": 40,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 80,
            "maxbraketorque": 35000,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "maxhandbraketorque": 0,
            "moi": 25,
            "side": "right",
            "springdamperrate": 15725,
            "springstrength": 58550,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_2_1_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_1_axis",
            "width": 0.24
        },
        "r2": {
            "bonename": "wheel_2_2_damper",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2.5
                ],
                [
                    0.5,
                    2.3
                ],
                [
                    1,
                    2
                ]
            ],
            "latstiffx": 40,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 80,
            "maxbraketorque": 35000,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "maxhandbraketorque": 0,
            "moi": 25,
            "side": "right",
            "springdamperrate": 15725,
            "springstrength": 58550,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_2_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_2_axis",
            "width": 0.24
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_01",
        1.99526,
        1,
        75
    ],
    "woodcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_02",
        1.99526,
        1,
        75
    ],
    "woodcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_03",
        1.99526,
        1,
        75
    ],
    "woodcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_04",
        1.99526,
        1,
        75
    ],
    "woodcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_05",
        1.99526,
        1,
        75
    ],
    "woodcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_06",
        1.99526,
        1,
        75
    ],
    "woodcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_07",
        1.99526,
        1,
        75
    ],
    "woodcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_08",
        1.99526,
        1,
        75
    ]
}