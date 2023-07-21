d = {
    "_generalmacro": "C_Van_02_medevac_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 3.2,
    "accelaidforceyoffset": -1.3,
    "access": 0,
    "accuracy": 0.25,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left",
            "Right",
            "Left2",
            "Right2",
            "Left3",
            "Right3"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.2,
    "alwaystarget": 0,
    "animated": 1,
    "animationlist": [
        "beacon_front_hide",
        0,
        "beacon_rear_hide",
        0,
        "LED_lights_hide",
        0,
        "reflective_tape_hide",
        0,
        "sidesteps_hide",
        0
    ],
    "animationsources": {
        "beacon_front_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide front beacon lights",
            "initphase": 1,
            "mass": -15,
            "onphasechanged": "",
            "source": "user",
            "usesource": 1
        },
        "beacon_rear_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide rear beacon lights",
            "initphase": 1,
            "mass": -15,
            "onphasechanged": "",
            "source": "user",
            "usesource": 1
        },
        "door_1_source": {
            "animperiod": 1,
            "displayname": "Open left front door",
            "forceanimate": [
                "hide_door_1_source",
                0
            ],
            "forceanimate2": [
                "hide_door_1_source",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "onphasechanged": "",
            "sound": "Van_02_Door_Front",
            "soundposition": "Door1_sound",
            "source": "door"
        },
        "door_2_source": {
            "animperiod": 1,
            "displayname": "Open right front door",
            "forceanimate": [
                "hide_door_2_source",
                0
            ],
            "forceanimate2": [
                "hide_door_2_source",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "onphasechanged": "",
            "sound": "Van_02_Door_Front",
            "soundposition": "Door2_sound",
            "source": "door"
        },
        "door_3_source": {
            "animperiod": 1,
            "displayname": "Open right side door",
            "forceanimate": [
                "hide_door_3_source",
                0
            ],
            "forceanimate2": [
                "hide_door_3_source",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "onphasechanged": "",
            "sound": "Van_02_Door_Slide",
            "soundposition": "Door3_sound",
            "source": "door"
        },
        "door_4_source": {
            "animperiod": 1,
            "displayname": "Open rear doors",
            "forceanimate": [
                "hide_door_4_source",
                0
            ],
            "forceanimate2": [
                "hide_door_4_source",
                0
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "onphasechanged": "",
            "sound": "Van_02_Door_Rear",
            "soundposition": "Door4_sound",
            "source": "door"
        },
        "front_protective_frame_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide front protective frame",
            "initphase": 1,
            "mass": -15,
            "source": "user",
            "usesource": 1
        },
        "hide_dashboard": {
            "animperiod": 0.01,
            "initphase": 0,
            "source": "user"
        },
        "hide_door_1_source": {
            "animperiod": 1,
            "displayname": "Hide left front door",
            "forceanimate": [],
            "forceanimate2": [
                "hide_door_1_source",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "mass": "- 50",
            "onphasechanged": "",
            "sound": "Van_02_Door_Front",
            "soundposition": "Door1_sound",
            "source": "user",
            "usesource": 1
        },
        "hide_door_2_source": {
            "animperiod": 1,
            "displayname": "Hide right front door",
            "forceanimate": [],
            "forceanimate2": [
                "hide_door_2_source",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "onphasechanged": "",
            "sound": "Van_02_Door_Front",
            "soundposition": "Door2_sound",
            "source": "user",
            "usesource": 1
        },
        "hide_door_3_source": {
            "animperiod": 1,
            "displayname": "Hide right side door",
            "forceanimate": [],
            "forceanimate2": [
                "hide_door_3_source",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "mass": "- 80",
            "onphasechanged": "",
            "sound": "Van_02_Door_Slide",
            "soundposition": "Door3_sound",
            "source": "user",
            "usesource": 1
        },
        "hide_door_4_source": {
            "animperiod": 1,
            "displayname": "Hide rear doors",
            "forceanimate": [],
            "forceanimate2": [
                "hide_door_4_source",
                0
            ],
            "forceanimatephase": 1,
            "initphase": 0,
            "mass": "- 100",
            "onphasechanged": "",
            "sound": "Van_02_Door_Rear",
            "soundposition": "Door4_sound",
            "source": "user",
            "usesource": 1
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
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
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
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "raw": 1,
            "source": "Hit"
        },
        "ladder_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide ladder",
            "initphase": 1,
            "mass": -30,
            "source": "user",
            "usesource": 1
        },
        "led_lights_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide secondary beacon lights",
            "initphase": 1,
            "mass": -7,
            "onphasechanged": "",
            "source": "user",
            "usesource": 1
        },
        "lights_em_hide": {
            "animperiod": 0.0001,
            "displayname": "Start beacon lights",
            "initphase": 0,
            "onphasechanged": "",
            "source": "user",
            "usesource": 1
        },
        "rearsteps_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide rear steps",
            "initphase": 1,
            "mass": -15,
            "source": "user",
            "usesource": 1
        },
        "reflective_tape_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide reflective tape",
            "initphase": 1,
            "mass": 0,
            "onphasechanged": "",
            "source": "user",
            "usesource": 1
        },
        "roof_rack_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide roof rack",
            "initphase": 1,
            "mass": -150,
            "source": "user",
            "usesource": 1
        },
        "side_protective_frame_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide side protective frame",
            "forceanimate": [
                "sidesteps_hide",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "mass": -15,
            "source": "user",
            "usesource": 1
        },
        "sidesteps_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide side steps",
            "forceanimate": [
                "side_protective_frame_hide",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "mass": -30,
            "source": "user",
            "usesource": 1
        },
        "spare_tyre_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide spare tire",
            "initphase": 1,
            "mass": -30,
            "source": "user",
            "usesource": 1
        },
        "spare_tyre_holder_hide": {
            "animperiod": 0.0001,
            "displayname": "Hide spare tire holder",
            "forceanimate": [
                "spare_tyre_hide",
                1
            ],
            "forceanimatephase": 1,
            "initphase": 1,
            "mass": -20,
            "source": "user",
            "usesource": 1
        }
    },
    "antirollbarforcecoef": 0.5,
    "antirollbarforcelimit": 15,
    "antirollbarspeedmax": 99,
    "antirollbarspeedmin": 10,
    "armor": 55,
    "armorcrash0": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "armorcrash1": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "armorcrash2": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "armorcrash3": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "armorcrash4": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "armorcrash5": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "armorcrash6": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "armorcrash7": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "armorlights": 0.01,
    "armorstructural": 4,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 1,
    "attenuationeffecttype": "SemiOpenCarAttenuation",
    "audible": 9,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 10,
    "brakeidlespeed": 0.87,
    "braketorque": 6000,
    "buildcrash0": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "buildcrash1": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "buildcrash2": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "buildcrash3": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "buildcrash4": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "buildcrash5": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "buildcrash6": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "buildcrash7": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_08",
        1.99526,
        1,
        75
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
    "camshakecoef": 0.2,
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
        "CoDriver_Van_02",
        "Passenger_Van_02_Medevac_Front",
        "Passenger_Van_02_Medevac_Back",
        "Patient_Van_02_Medevac_Front",
        "Patient_Van_02_Medevac_Back"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1",
        "Compartment2"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInLow"
    ],
    "cargogetoutaction": [
        "GetOutLow"
    ],
    "cargoiscodriver": [
        1,
        1
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
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "centrebias": 1.3,
    "changegearmineffectivity": [
        0.95,
        0.15,
        0.95,
        0.95,
        0.95,
        0.95,
        0.95
    ],
    "clutchstrength": 35,
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
            -3.8,
            "N",
            0,
            "D1",
            4.47,
            "D2",
            2.312,
            "D3",
            1.75,
            "D4",
            1.132,
            "D5",
            0.785
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            4.41
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
        "transportcountermeasurescomponent": {}
    },
    "cost": 50000,
    "countsforscoreboard": 1,
    "crash0": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "crash1": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "crash2": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "crash3": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "crash4": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "crash5": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "crash6": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "crash7": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "crew": "C_Man_Paramedic_01_F",
    "crewcrashprotection": 2.65,
    "crewexplosionprotection": 0.8,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "a3/Soft_F_Orange/Van_02/Data/van_sideskirt.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_sideskirt.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_sideskirt_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det1.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det1.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ambulance_det1_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_body.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_body_damage.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_body_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin_ambulance.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin_ambulance.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cabin_ambulance_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cargowall.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cargowall.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_cargowall_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ladder.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ladder.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_ladder_destruct.rvmat",
            "a3/soft_f_orange/van_02/data/van_viewpilot_int.rvmat",
            "a3/soft_f_orange/van_02/data/van_viewpilot_int.rvmat",
            "a3/soft_f_orange/van_02/data/van_destruct.rvmat",
            "a3/soft_f_orange/van_02/data/van_cabin_transport.rvmat",
            "a3/soft_f_orange/van_02/data/van_cabin_transport.rvmat",
            "a3/soft_f_orange/van_02/data/van_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_protectionframe.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_protectionframe.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_protectionframe_destruct.rvmat",
            "a3/Soft_F_Orange/Van_02/Data/van_glass_transport.rvmat",
            "A3/data_f/Glass_veh_damage2.rvmat",
            "A3/data_f/Glass_veh_damage2.rvmat",
            "a3/soft_f_orange/van_02/data/van_glass_utility.rvmat",
            "A3/data_f/Glass_veh_damage2.rvmat",
            "A3/data_f/Glass_veh_damage2.rvmat"
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
    "dampersbumpcoef": 0.3,
    "dampersize": 0.1,
    "dampingratefullthrottle": 0.08,
    "dampingratezerothrottleclutchdisengaged": 0.15,
    "dampingratezerothrottleclutchengaged": 0.35,
    "destrtype": "destructWreck",
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
    "differentialtype": "all_open",
    "displayname": "Van (Ambulance)",
    "dlc": "Orange",
    "driveraction": "Driver_Van_02",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
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
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "A3/EditorPreviews_F_Orange/Data/CfgVehicles/C_Van_02_medevac_F.jpg",
    "editorsubcategory": "EdSubcat_Cars",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 0,
    "enablemanualfire": 1,
    "enableradio": 0,
    "enablewatch": 0,
    "engineer": 0,
    "enginelosses": 30,
    "enginemoi": 1,
    "enginepower": 266,
    "enginestartspeed": 1.5,
    "epeimpulsedamagecoef": 10,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "postinit": "if (local (_this select 0)) then {[(_this select 0), `, [], true] call bis_fnc_initVehicle;};"
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust_dir",
            "effect": "ExhaustsEffect",
            "position": "exhaust"
        }
    },
    "explosioneffect": "FuelExplosion",
    "explosionshielding": 4,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0.5,
        2,
        -10
    ],
    "faction": "CIV_F",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 20,
    "frontbias": 1.3,
    "frontrearsplit": 0.5,
    "fuelcapacity": 18,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 1,
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
        "camo1",
        "camo2",
        "camo3",
        "monitors",
        "emergency_lights"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/a3/soft_f_orange/van_02/data/van_body_IdapAmbulance_CO.paa",
        "/a3/soft_f_orange/van_02/data/van_wheel_co.paa",
        "/a3/soft_f_orange/van_02/data/van_glass_medevac_ca.paa",
        "/a3/soft_f_orange/van_02/data/van_ambulance_monitors_co.paa",
        "/a3/soft_f_orange/van_02/data/van_body_IdapAmbulance_CO.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitbody": {
            "armor": 1,
            "explosionshielding": 1.5,
            "material": -1,
            "name": "karoserie",
            "passthrough": 1,
            "visual": "zbytek"
        },
        "hitengine": {
            "armor": 0.6,
            "explosionshielding": 2,
            "material": -1,
            "name": "engine",
            "passthrough": 0.5,
            "radius": 0.1,
            "visual": ""
        },
        "hitfuel": {
            "armor": 0.5,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "palivo",
            "passthrough": 0.5,
            "radius": 0.1,
            "visual": "-"
        },
        "hitglass1": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass5",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass6",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass6"
        },
        "hitglass7": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass7",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass7"
        },
        "hitglass8": {
            "armor": 0.05,
            "explosionshielding": 0.6,
            "minimalhit": 0.1,
            "name": "glass8",
            "passthrough": 0,
            "radius": 0.11,
            "visual": "glass8"
        },
        "hithull": {
            "armor": 0.8,
            "explosionshielding": 2.5,
            "material": -1,
            "minimalhit": 0.1,
            "name": "palivo",
            "passthrough": 0.9,
            "radius": 0.1,
            "visual": ""
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
            "armor": -80,
            "armorcomponent": "wheel_1_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0,
            "name": "wheel_1_2_steering",
            "passthrough": 0,
            "radius": 0.16,
            "visual": "wheel_1_2_damage"
        },
        "hitlfwheel": {
            "armor": -80,
            "armorcomponent": "wheel_1_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0,
            "name": "wheel_1_1_steering",
            "passthrough": 0,
            "radius": 0.16,
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
            "armor": -80,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0,
            "name": "wheel_2_2_steering",
            "passthrough": 0,
            "radius": 0.16,
            "visual": "wheel_2_2_damage"
        },
        "hitrfwheel": {
            "armor": -80,
            "armorcomponent": "wheel_2_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0,
            "name": "wheel_2_1_steering",
            "passthrough": 0,
            "radius": 0.16,
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
    "icon": "a3/Soft_F_Orange/Van_02/Data/UI/Map_Van_02_medevac_CA.paa",
    "idlerpm": 900,
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
    "insidesoundcoef": 0.9,
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
        "libtextdesc": "The standard van can be used for a huge variety of practical purposes. This particular model features a long load length and excellent roof height, allowing for the transport of passengers, cargo, or even some smaller vehicles. Several aftermarket exterior components, such as a ladder, protective guards and a roof rack, can be fitted where appropriate. Specialized variants are used for emergency healthcare, patient evacuation and various utility services."
    },
    "limitedspeedcoef": 0.5,
    "lockdetectionsystem": 0,
    "longstiff": 15000,
    "magazines": [],
    "mapsize": 9.55,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.5,
    "maxgforce": 3,
    "maximumload": 3000,
    "maxomega": 410,
    "maxspeed": 155,
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
        "pos codriver",
        "pos cargo",
        "pos cargo",
        "pos cargo rear"
    ],
    "memorypointsgetincargodir": [
        "pos codriver dir",
        "pos cargo dir",
        "pos cargo dir",
        "pos cargo rear dir"
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
    "mfd": {},
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
    "minomega": 70,
    "mintotaldamagethreshold": 0.003,
    "model": "a3/Soft_F_Orange/Van_02/Van_02_medevac_F.p3d",
    "namesound": "veh_vehicle_truck_s",
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
    "numberphysicalwheels": 6,
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
    "peaktorque": 836,
    "picture": "a3/Soft_F_Orange/Van_02/Data/UI/Van_02_medevac_CA.paa",
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
        "maxturnhundred": 0.7,
        "turndecreaseconst": 9,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "turnincreaseconst": 1,
        "turnincreaselinear": 2.1,
        "turnincreasetime": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 10,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "preferroads": 1,
    "pulsationsound": {},
    "radartype": 0,
    "rearbias": 1.3,
    "redrpm": 3920,
    "reflectors": {
        "left": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_L_end",
            "flaresize": 1,
            "hitpoint": "Light_L",
            "innerangle": 30,
            "intensity": 100,
            "outerangle": 179,
            "position": "Light_L",
            "selection": "Light_L_Hide",
            "size": 1,
            "useflare": 0
        },
        "left2": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_L_end",
            "flaresize": 1,
            "hitpoint": "Light_L",
            "innerangle": 60,
            "intensity": 10,
            "outerangle": 179,
            "position": "light_L_flare",
            "selection": "Light_L_Hide",
            "size": 1,
            "useflare": 1
        },
        "left3": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_L_end",
            "flaresize": 1,
            "hitpoint": "Light_L",
            "innerangle": 60,
            "intensity": 10,
            "outerangle": 179,
            "position": "light_L_flare2",
            "selection": "Light_L_Hide",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_R_end",
            "flaresize": 1,
            "hitpoint": "Light_R",
            "innerangle": 30,
            "intensity": 100,
            "outerangle": 179,
            "position": "Light_R",
            "selection": "Light_R_Hide",
            "size": 1,
            "useflare": 0
        },
        "right2": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_R_end",
            "flaresize": 1,
            "hitpoint": "Light_R",
            "innerangle": 60,
            "intensity": 10,
            "outerangle": 179,
            "position": "light_R_flare",
            "selection": "Light_R_Hide",
            "size": 1,
            "useflare": 1
        },
        "right3": {
            "ambient": [
                5,
                5,
                7
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 80,
                "hardlimitstart": 50,
                "linear": 0,
                "quadratic": 0.05,
                "start": 1
            },
            "color": [
                1.3,
                1.3,
                2.2
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "Light_R_end",
            "flaresize": 1,
            "hitpoint": "Light_R",
            "innerangle": 60,
            "intensity": 10,
            "outerangle": 179,
            "position": "light_R_flare2",
            "selection": "Light_R_Hide",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "mirror_center": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "mirror": {
                "fov": 0.35,
                "pointdirection": "PIP1_dir",
                "pointposition": "PIP1_pos",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget1"
        },
        "mirrorl": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "mirror": {
                "fov": 0.5,
                "pointdirection": "PIP2_dir",
                "pointposition": "PIP2_pos",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget2"
        },
        "mirrorr": {
            "bboxes": [
                "PIP_3_TL",
                "PIP_3_TR",
                "PIP_3_BL",
                "PIP_3_BR"
            ],
            "mirror": {
                "fov": 0.5,
                "pointdirection": "PIP3_dir",
                "pointposition": "PIP3_pos",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget3"
        },
        "reversecam": {
            "bboxes": [
                "PIP_0_TL",
                "PIP_0_TR",
                "PIP_0_BL",
                "PIP_0_BR"
            ],
            "mirror": {
                "fov": 0.5,
                "pointdirection": "PIP0_dir",
                "pointposition": "PIP0_pos",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget0"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
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
    "scopecurator": 2,
    "scudeffect": "ScudEffect",
    "scudmodel": "",
    "secondaryexplosion": -10,
    "selectionbacklights": "zadni svetlo",
    "selectionbrakelights": "brzdove svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 1.75,
    "sensitivityear": 0.125,
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
                "damagehide",
                0
            ],
            [
                "damagehidevez",
                0
            ],
            [
                "damagehidehlaven",
                0
            ],
            [
                "wheel_1_1_destruct",
                0
            ],
            [
                "wheel_1_2_destruct",
                0
            ],
            [
                "wheel_1_3_destruct",
                0
            ],
            [
                "wheel_1_4_destruct",
                0
            ],
            [
                "wheel_2_1_destruct",
                0
            ],
            [
                "wheel_2_2_destruct",
                0
            ],
            [
                "wheel_2_3_destruct",
                0
            ],
            [
                "wheel_2_4_destruct",
                0
            ],
            [
                "wheel_1_1_destruct_unhide",
                0
            ],
            [
                "wheel_1_2_destruct_unhide",
                0
            ],
            [
                "wheel_1_3_destruct_unhide",
                0
            ],
            [
                "wheel_1_4_destruct_unhide",
                0
            ],
            [
                "wheel_2_1_destruct_unhide",
                0
            ],
            [
                "wheel_2_2_destruct_unhide",
                0
            ],
            [
                "wheel_2_3_destruct_unhide",
                0
            ],
            [
                "wheel_2_4_destruct_unhide",
                0
            ],
            [
                "wheel_1_3_damage",
                0
            ],
            [
                "wheel_1_4_damage",
                0
            ],
            [
                "wheel_2_3_damage",
                0
            ],
            [
                "wheel_2_4_damage",
                0
            ],
            [
                "wheel_1_3_damper_damage_backanim",
                0
            ],
            [
                "wheel_1_4_damper_damage_backanim",
                0
            ],
            [
                "wheel_2_3_damper_damage_backanim",
                0
            ],
            [
                "wheel_2_4_damper_damage_backanim",
                0
            ],
            [
                "wheel_1_1",
                0
            ],
            [
                "wheel_2_1",
                0
            ],
            [
                "wheel_1_2",
                0
            ],
            [
                "wheel_2_2",
                0
            ],
            [
                "glass2_destruct",
                0
            ],
            [
                "glass3_destruct",
                0
            ],
            [
                "glass1_destruct_unhide",
                0
            ],
            [
                "glass4_destruct_unhide",
                0
            ],
            [
                "glass5_destruct_unhide",
                0
            ],
            [
                "glass6_destruct_unhide",
                0
            ],
            [
                "glass7_destruct_unhide",
                0
            ],
            [
                "glass8_destruct_unhide",
                0
            ],
            [
                "wheel_1_1_damage",
                0
            ],
            [
                "wheel_1_2_damage",
                0
            ],
            [
                "wheel_2_1_damage",
                0
            ],
            [
                "wheel_2_2_damage",
                0
            ],
            [
                "wheel_1_1_damper_damage_backanim",
                0
            ],
            [
                "wheel_1_2_damper_damage_backanim",
                0
            ],
            [
                "wheel_2_1_damper_damage_backanim",
                0
            ],
            [
                "wheel_2_2_damper_damage_backanim",
                0
            ],
            [
                "drivingwheel",
                0
            ],
            [
                "steering_1_1",
                0
            ],
            [
                "steering_2_1",
                0
            ],
            [
                "indicatorspeed",
                0
            ],
            [
                "indicatorrpm",
                0
            ],
            [
                "fuel",
                1
            ],
            [
                "watchhour",
                0.15
            ],
            [
                "watchminute",
                0.75
            ],
            [
                "compass",
                0
            ],
            [
                "daylights",
                0
            ],
            [
                "pedal_thrust",
                0
            ],
            [
                "dashboard_off",
                0
            ],
            [
                "dashboard",
                0
            ],
            [
                "hide_dashboard2",
                0
            ],
            [
                "hide_dashboard3",
                0
            ],
            [
                "hide_light_back_l",
                0
            ],
            [
                "hide_light_back_r",
                0
            ],
            [
                "hide_light_back_top",
                0
            ],
            [
                "hide_reverselight",
                0
            ],
            [
                "reverse_light",
                1
            ],
            [
                "reverse_camera",
                1
            ],
            [
                "reverse_camera_hide_ac",
                1
            ],
            [
                "gear_r",
                1
            ],
            [
                "gear_d",
                1
            ],
            [
                "wheel_1_1_damper",
                0
            ],
            [
                "wheel_2_1_damper",
                0
            ],
            [
                "wheel_1_2_damper",
                0
            ],
            [
                "wheel_2_2_damper",
                0
            ],
            [
                "door_1_source",
                0
            ],
            [
                "door_2_source",
                0
            ],
            [
                "door_3_source",
                0
            ],
            [
                "door_3b_source",
                0
            ],
            [
                "door_4_source",
                0
            ],
            [
                "door_4a_source",
                0
            ],
            [
                "door_5_source",
                0
            ],
            [
                "door_5a_source",
                0
            ],
            [
                "hide_door_5_source",
                0
            ],
            [
                "lights_em_1",
                489.46
            ],
            [
                "lights_em_2",
                489.46
            ],
            [
                "lights_em_1_flash",
                489.46
            ],
            [
                "lights_em_2_flash",
                489.46
            ],
            [
                "lights_em_1_door5",
                489.46
            ],
            [
                "lights_em_2_door4",
                489.46
            ],
            [
                "lights_em_1_door5_flash",
                489.46
            ],
            [
                "lights_em_2_door4_flash",
                489.46
            ],
            [
                "lights_em_1_door5_main_hide",
                0
            ],
            [
                "lights_em_2_door4_main_hide",
                0
            ],
            [
                "reflective_tape_door1_hide",
                0
            ],
            [
                "reflective_tape_door2_hide",
                0
            ],
            [
                "reflective_tape_door3_hide",
                0
            ],
            [
                "led_lights_door4_hide",
                0
            ],
            [
                "led_lights_door5_hide",
                0
            ],
            [
                "lights_em_1_side_hide",
                0
            ],
            [
                "lights_em_2_side_hide",
                0
            ],
            [
                "lights_em_1_door5_hide",
                0
            ],
            [
                "lights_em_2_door4_hide",
                0
            ],
            [
                "lights_em_1_roof_front_hide",
                0
            ],
            [
                "lights_em_2_roof_front_hide",
                0
            ],
            [
                "lights_em_1_roof_rear_hide",
                0
            ],
            [
                "lights_em_2_roof_rear_hide",
                0
            ],
            [
                "glass1_destruct",
                0
            ]
        ],
        "eden": 1,
        "hide": [
            "zasleh",
            "light_l_hide",
            "light_r_hide",
            "zadni svetlo",
            "brzdove svetlo",
            "clan",
            "podsvit pristroju",
            "poskozeni"
        ],
        "postinit": "[this, '', []] call bis_fnc_initVehicle",
        "verticaloffset": 1.594,
        "verticaloffsetworld": -0.196
    },
    "simulation": "carx",
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
    "slowspeedforwardcoef": 0.3,
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
        "emptySound",
        0
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
        1.77828,
        0.9
    ],
    "soundengineoffext": [
        "A3/Sounds_F_Exp/vehicles/soft/Offroad_02/engine_ext_stop",
        1.99526,
        1,
        50
    ],
    "soundengineoffint": [
        "A3/Sounds_F_Exp/vehicles/soft/Offroad_02/engine_ext_stop",
        0.562341,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F_Exp/vehicles/soft/Offroad_02/engine_ext_start",
        1.99526,
        1,
        50
    ],
    "soundengineonint": [
        "A3/Sounds_F_Exp/vehicles/soft/Offroad_02/engine_ext_start",
        0.707946,
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
        "soundsets": [],
        "soundsetsext": [
            "Van_02_Eng_01_Idle_Ext_SoundSet",
            "Van_02_Eng_01_Rpm_01_Ext_SoundSet",
            "Van_02_Eng_01_Rpm_02_Ext_SoundSet",
            "Van_02_Eng_01_Rpm_03_Ext_SoundSet",
            "Van_02_Eng_01_Rpm_04_Ext_SoundSet",
            "Van_02_Eng_01_Rpm_05_Ext_SoundSet",
            "Van_02_Tires_Gravel_01_Ext_SoundSet",
            "Van_02_Tires_Asphalt_01_Ext_SoundSet",
            "Van_02_Tires_Grass_Mud_01_Ext_SoundSet",
            "Van_02_Tires_Sand_01_Ext_SoundSet",
            "Van_02_Tires_Rock_01_Ext_SoundSet",
            "Van_02_Tires_Water_01_Ext_SoundSet",
            "Van_02_Brakes_Asphalt_01_Ext_SoundSet",
            "Van_02_TurnLeft_Asphalt_01_Ext_SoundSet",
            "Van_02_TurnRight_Asphalt_01_Ext_SoundSet",
            "Van_02_Brakes_Dirt_01_Ext_SoundSet",
            "Van_02_TurnLeft_Dirt_01_Ext_SoundSet",
            "Van_02_TurnRight_Dirt_01_Ext_SoundSet",
            "Van_02_Tires_Movement_Dirt_Ext_01_SoundSet",
            "Van_02_Rain_01_Ext_SoundSet",
            "Van_02_AmbulanceSiren_01_Ext_SoundSet"
        ],
        "soundsetsint": [
            "Van_02_Eng_01_Idle_Int_SoundSet",
            "Van_02_Eng_01_Rpm_01_Int_SoundSet",
            "Van_02_Eng_01_Rpm_02_Int_SoundSet",
            "Van_02_Eng_01_Rpm_03_Int_SoundSet",
            "Van_02_Eng_01_Rpm_04_Int_SoundSet",
            "Van_02_Eng_01_Rpm_05_Int_SoundSet",
            "Van_02_Noise_Hard_01_Int_SoundSet",
            "Van_02_Tires_Gravel_01_Int_SoundSet",
            "Van_02_Tires_Asphalt_01_Int_SoundSet",
            "Van_02_Tires_Grass_Mud_01_Int_SoundSet",
            "Van_02_Tires_Sand_01_Int_SoundSet",
            "Van_02_Tires_Rock_01_Int_SoundSet",
            "Van_02_Tires_Water_01_Int_SoundSet",
            "Van_02_Brakes_Asphalt_01_Int_SoundSet",
            "Van_02_TurnLeft_Asphalt_01_Int_SoundSet",
            "Van_02_TurnRight_Asphalt_01_Int_SoundSet",
            "Van_02_Brakes_Dirt_01_Int_SoundSet",
            "Van_02_Tires_Movement_Dirt_Int_01_SoundSet",
            "Van_02_Rain_01_Int_SoundSet",
            "Van_02_AmbulanceSiren_01_Int_SoundSet"
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
                "veh_vehicle_truck_p"
            ],
            "speechsingular": [
                "veh_vehicle_truck_s"
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
    "supplyradius": 2.5,
    "switchtime": 0.11,
    "tbody": 150,
    "terraincoef": 3,
    "textplural": "trucks",
    "textsingular": "truck",
    "texturelist": [
        "CivAmbulance",
        1
    ],
    "texturesources": {
        "civambulance": {
            "author": "Bohemia Interactive",
            "displayname": "Civilian Ambulance",
            "factions": [
                "CIV_F",
                "IND_G_F",
                "BLU_G_F"
            ],
            "materials": [
                "/a3/Soft_F_Orange/Van_02/Data/van_body.rvmat",
                "/A3/Soft_F_Orange/Van_02/Data/van_wheel.rvmat",
                "",
                "",
                "/a3/Data_f/Lights/Car_Beacon_Blue_emit.rvmat"
            ],
            "textures": [
                "A3/Soft_F_Orange/Van_02/Data/van_body_CivAmbulance_CO.paa",
                "a3/Soft_F_Orange/Van_02/Data/van_wheel_Red_CO.paa",
                "a3/soft_f_orange/van_02/data/van_glass_CivAmbulance_CA.paa",
                "a3/soft_f_orange/van_02/data/van_ambulance_monitors_co.paa",
                "A3/Soft_F_Orange/Van_02/Data/van_body_CivAmbulance_CO.paa"
            ]
        },
        "idapambulance": {
            "author": "Bohemia Interactive",
            "displayname": "IDAP Ambulance",
            "factions": [
                "CIV_IDAP_F"
            ],
            "materials": [
                "/a3/Soft_F_Orange/Van_02/Data/van_body_dirty.rvmat",
                "/A3/Soft_F_Orange/Van_02/Data/van_wheel_dirty.rvmat",
                "",
                "",
                "/a3/Data_f/Lights/Car_Beacon_Blue_emit.rvmat"
            ],
            "textures": [
                "A3/Soft_F_Orange/Van_02/Data/van_body_IdapAmbulance_CO.paa",
                "a3/Soft_F_Orange/Van_02/Data/van_wheel_Red_CO.paa",
                "a3/soft_f_orange/van_02/data/van_glass_medevac_dirty_ca.paa",
                "a3/soft_f_orange/van_02/data/van_ambulance_monitors_co.paa",
                "A3/Soft_F_Orange/Van_02/Data/van_body_IdapAmbulance_CO.paa"
            ]
        },
        "ldfambulance": {
            "author": "Bohemia Interactive",
            "displayname": "LDF Ambulance",
            "factions": [
                "IND_E_F"
            ],
            "materials": [
                "/a3/Soft_F_Orange/Van_02/Data/van_body_dirty.rvmat",
                "/A3/Soft_F_Orange/Van_02/Data/van_wheel_dirty.rvmat",
                "",
                "",
                "/a3/Data_f/Lights/Car_Beacon_Blue_emit.rvmat"
            ],
            "textures": [
                "A3/Soft_F_enoch/Van_02/Data/van_body_LdfAmbulance_CO.paa",
                "a3/Soft_F_enoch/Van_02/Data/van_wheel_ldf_MP_CO.paa",
                "a3/Soft_F_Enoch/Van_02/Data/van_glass_medevac_ldf_CA.paa",
                "a3/soft_f_orange/van_02/data/van_ambulance_monitors_co.paa",
                "A3/Soft_F_enoch/Van_02/Data/van_body_LdfAmbulance_CO.paa"
            ]
        }
    },
    "threat": [
        0,
        0,
        0
    ],
    "thrustdelay": 1,
    "torquecurve": [
        [
            0,
            0
        ],
        [
            0.16301,
            0.277273
        ],
        [
            0.231122,
            0.613636
        ],
        [
            0.306122,
            0.931818
        ],
        [
            0.357143,
            1
        ],
        [
            0.701531,
            1
        ],
        [
            0.97398,
            0.795455
        ],
        [
            1.28189,
            0.318182
        ]
    ],
    "tracksspeed": 0,
    "transmissionlosses": 100,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 24,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 4,
            "name": "MediKit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 64,
    "transportmaxmagazines": 256,
    "transportmaxweapons": 64,
    "transportrepair": 0,
    "transportsoldier": 5,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 3.4,
    "turrets": {},
    "type": 0,
    "typicalcargo": [
        "C_Man_Paramedic_01_F"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoNoWeapon",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "useractions": {
        "beacons_start": {
            "animperiod": 2,
            "condition": "(driver this == player) AND {{this animationSourcePhase _x isEqualTo 0} count ['beacon_rear_hide','beacon_front_hide','LED_lights_hide'] > 0} AND  {this animationPhase 'lights_em_hide' < 0.5} AND {Alive(this)} ",
            "displayname": "Beacons On",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_ON_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "this animateSource ['lights_em_hide',1];",
            "useractionid": 50
        },
        "beacons_stop": {
            "animperiod": 2,
            "condition": "(driver this == player) AND {{this animationSourcePhase _x isEqualTo 0} count ['beacon_rear_hide','beacon_front_hide','LED_lights_hide'] > 0} AND  {this animationPhase 'lights_em_hide' > 0.5} AND {Alive(this)} ",
            "displayname": "Beacons Off",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_OFF_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "this animateSource ['lights_em_hide',0];",
            "useractionid": 51
        },
        "siren_start": {
            "animperiod": 2,
            "condition": "(driver this == player) AND {{this animationSourcePhase _x isEqualTo 0} count ['beacon_rear_hide','beacon_front_hide','LED_lights_hide'] > 0} AND {getCustomSoundController [this,'CustomSoundController1'] < 0.5}",
            "displayname": "Siren On",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_ON_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "[this,'CustomSoundController1',1,0.2] remoteExec ['BIS_fnc_setCustomSoundController'];",
            "useractionid": 52
        },
        "siren_stop": {
            "animperiod": 2,
            "condition": "(driver this == player) AND {{this animationSourcePhase _x isEqualTo 0} count ['beacon_rear_hide','beacon_front_hide','LED_lights_hide'] > 0} AND {getCustomSoundController [this,'CustomSoundController1'] > 0.5}",
            "displayname": "Siren Off",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_OFF_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "[this,'CustomSoundController1',0,0.4] remoteExec ['BIS_fnc_setCustomSoundController'];",
            "useractionid": 53
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
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
    "waterspeedfactor": 0.2,
    "weapons": [
        "AmbulanceHorn"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.362,
    "wheeldamageradiuscoef": 0.75,
    "wheeldamagethreshold": 0.025,
    "wheeldestroyradiuscoef": 0.58,
    "wheeldestroythreshold": 0.99,
    "wheelmask": "wheel_X_X",
    "wheels": {
        "lf": {
            "bonename": "wheel_1_1_damper",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 0.5,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 200,
            "frictionvsslipgraph": [
                [
                    0,
                    0.9
                ],
                [
                    0.2,
                    1.9
                ],
                [
                    0.8,
                    0.7
                ]
            ],
            "latstiffx": 2.5,
            "latstiffy": 19,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 30,
            "maxbraketorque": 11000,
            "maxcompression": 0.0759,
            "maxdroop": 0.1771,
            "maxhandbraketorque": 0,
            "moi": 6.498,
            "side": "left",
            "springdamperrate": 8200,
            "springstrength": 73750,
            "sprungmass": 700,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_1_axis",
            "width": 0.23
        },
        "lr": {
            "bonename": "wheel_1_2_damper",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 0.5,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 200,
            "frictionvsslipgraph": [
                [
                    0,
                    0.9
                ],
                [
                    0.2,
                    1.9
                ],
                [
                    0.8,
                    0.7
                ]
            ],
            "latstiffx": 2.5,
            "latstiffy": 19,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 30,
            "maxbraketorque": 11000,
            "maxcompression": 0.0759,
            "maxdroop": 0.1771,
            "maxhandbraketorque": 9000,
            "moi": 6.498,
            "side": "left",
            "springdamperrate": 10600,
            "springstrength": 48750,
            "sprungmass": 850,
            "steering": 0,
            "suspforceapppointoffset": "wheel_1_2_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.23
        },
        "rf": {
            "bonename": "wheel_2_1_damper",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 0.5,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 200,
            "frictionvsslipgraph": [
                [
                    0,
                    0.9
                ],
                [
                    0.2,
                    1.9
                ],
                [
                    0.8,
                    0.7
                ]
            ],
            "latstiffx": 2.5,
            "latstiffy": 19,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 30,
            "maxbraketorque": 11000,
            "maxcompression": 0.0759,
            "maxdroop": 0.1771,
            "maxhandbraketorque": 0,
            "moi": 6.498,
            "side": "right",
            "springdamperrate": 8200,
            "springstrength": 73750,
            "sprungmass": 700,
            "steering": 1,
            "suspforceapppointoffset": "wheel_2_1_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_1_axis",
            "width": 0.23
        },
        "rr": {
            "bonename": "wheel_2_2_damper",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 0.5,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 200,
            "frictionvsslipgraph": [
                [
                    0,
                    0.9
                ],
                [
                    0.2,
                    1.9
                ],
                [
                    0.8,
                    0.7
                ]
            ],
            "latstiffx": 2.5,
            "latstiffy": 19,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 30,
            "maxbraketorque": 11000,
            "maxcompression": 0.0759,
            "maxdroop": 0.1771,
            "maxhandbraketorque": 9000,
            "moi": 6.498,
            "side": "right",
            "springdamperrate": 10600,
            "springstrength": 48750,
            "sprungmass": 850,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_2_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_2_axis",
            "width": 0.23
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_01",
        1.99526,
        1,
        75
    ],
    "woodcrash1": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_02",
        1.99526,
        1,
        75
    ],
    "woodcrash2": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_03",
        1.99526,
        1,
        75
    ],
    "woodcrash3": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_04",
        1.99526,
        1,
        75
    ],
    "woodcrash4": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_05",
        1.99526,
        1,
        75
    ],
    "woodcrash5": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_06",
        1.99526,
        1,
        75
    ],
    "woodcrash6": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_07",
        1.99526,
        1,
        75
    ],
    "woodcrash7": [
        "A3/Sounds_F_Orange/Vehicles/Shared/Crashes/Cars/Vehicle_Car_Collision_Medium_Wood_08",
        1.99526,
        1,
        75
    ]
}