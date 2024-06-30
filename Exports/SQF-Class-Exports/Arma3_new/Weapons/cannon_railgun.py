d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 2,
    "aidispersioncoefy": 2,
    "aimtransitionspeed": 1,
    "airateoffire": 5,
    "airateoffiredispersion": 0,
    "airateoffiredistance": 500,
    "ammo": "",
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "autofire": 0,
    "autoreload": 1,
    "backgroundreload": 0,
    "ballisticscomputer": "2 + 16",
    "burst": 1,
    "candrop": 1,
    "canlock": 0,
    "canshootinwater": 0,
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
    "changefiremodesound": [
        "",
        1,
        1
    ],
    "cmimmunity": 1,
    "count": 0,
    "cursor": "EmptyCursor",
    "cursoraim": "coil",
    "cursoraimon": "",
    "cursorsize": 1,
    "descriptionshort": "",
    "detectrange": 0,
    "dispersion": 0.002,
    "displayname": "Railgun 75mm",
    "distancezoommax": 400,
    "distancezoommin": 400,
    "drysound": [
        "a3/Sounds_F_Decade/Assets/Arsenal/railgun_01/railgun_01_gun-dry2",
        3.54813,
        1,
        120
    ],
    "emptysound": [
        "",
        1,
        1
    ],
    "enableattack": 1,
    "eventhandlers": {
        "fired": "_this call BIS_fnc_RailGun_01_fireEH"
    },
    "fcsmaxleadspeed": 25,
    "fcszeroingdelay": 1,
    "ffcount": 1,
    "fffrequency": 1,
    "ffmagnitude": 0,
    "fireanims": [],
    "firelightambient": [
        0,
        0,
        0
    ],
    "firelightdiffuse": [
        0.937,
        0.631,
        0.259
    ],
    "firelightduration": 0.05,
    "firelightintensity": 0.2,
    "firespreadangle": 3,
    "forceoptics": 0,
    "gunclouds": {},
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
        "cloudletdensitycoef": -1,
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
        "interval": -0.01,
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
    "gunparticles": {
        "barreleffect1": {
            "directionname": "fx_barrel_exhaust_2_dir",
            "effectname": "RailgunFiredB1",
            "positionname": "fx_barrel_exhaust_2_pos"
        },
        "barreleffect2": {
            "directionname": "fx_barrel_exhaust_1_dir",
            "effectname": "RailgunFiredC1",
            "positionname": "fx_barrel_exhaust_1_pos"
        },
        "capacitoreffect1": {
            "directionname": "fx_battery_exhaust_l_dir",
            "effectname": "RailgunFiredE1",
            "positionname": "fx_battery_exhaust_l_pos"
        },
        "capacitoreffect2": {
            "directionname": "fx_battery_exhaust_r_dir",
            "effectname": "RailgunFiredE1",
            "positionname": "fx_battery_exhaust_r_pos"
        },
        "exhausteffect": {
            "directionname": "fx_apu_exhaust_dir",
            "effectname": "RailgunFiredD1",
            "positionname": "fx_apu_exhaust_pos"
        },
        "maineffect": {
            "directionname": "Konec hlavne",
            "effectname": "RailgunFiredA1",
            "positionname": "Usti hlavne"
        }
    },
    "handanim": [],
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 600,
    "htmin": 1,
    "inertia": 0.5,
    "initspeed": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "irlaserend": "laser dir",
    "irlaserpos": "laser pos",
    "laser": 0,
    "library": {
        "libtextdesc": ""
    },
    "lockacquire": 1,
    "lockedtargetsound": [
        "",
        0.000316228,
        6
    ],
    "lockingtargetsound": [
        "",
        0.000316228,
        2
    ],
    "magazinereloadswitchphase": 1,
    "magazinereloadtime": 0,
    "magazines": [
        "60rnd_75mm_railgun_apfsds_mag"
    ],
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "maxrecoilsway": 0.008,
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "minrange": 1,
    "minrangeprobab": 0.3,
    "model": "",
    "modelmagazine": "",
    "modeloptics": "",
    "modelspecial": "",
    "modes": [
        "player"
    ],
    "multiplier": 1,
    "muzzleend": "konec hlavne",
    "muzzlepos": "usti hlavne",
    "muzzles": [
        "this"
    ],
    "namesound": "",
    "optics": 1,
    "opticsdisableperipherialvision": 0.67,
    "opticsflare": 1,
    "opticsid": 0,
    "opticsppeffects": [],
    "opticszoominit": 0.75,
    "opticszoommax": 1.25,
    "opticszoommin": 0.25,
    "picture": "",
    "player": {
        "aidispersioncoefx": 1.4,
        "aidispersioncoefy": 1.7,
        "airateoffire": 1,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 10,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 0,
        "autoreload": 1,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.00057,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "magazinereloadtime": 3,
        "maxrange": 2,
        "maxrangeprobab": 0.01,
        "midrange": 1,
        "midrangeprobab": 0.01,
        "minrange": 0,
        "minrangeprobab": 0.01,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.03,
            0.0110829,
            0.043044,
            0.03,
            0.0159085,
            0.0170136,
            0.03,
            0.0138285,
            0.0116128,
            0.06,
            0.0066492,
            0.004788,
            0.06,
            -0.0007206,
            -0.002688,
            0.06,
            -0.001765,
            -0.00282,
            0.06,
            -0.0018385,
            -0.001764,
            0.06,
            -0.0009414,
            -0.0005,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.03,
            0.0110829,
            0.0021522,
            0.04,
            0.0095451,
            0.0007506,
            0.05,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0,
            0.06,
            -0.0007206,
            -2.88e-05,
            0.06,
            -0.001059,
            -8.46e-05,
            0.06,
            -0.0011031,
            -8.82e-05,
            0.06,
            -0.0009414,
            -7.5e-05,
            0.06,
            -0.0006618,
            -5.28e-05,
            0.06,
            -0.0003531,
            -2.82e-05,
            0.06,
            -0.0001029,
            -8.4e-06,
            0.06,
            -4.5e-05,
            0,
            0.06,
            0,
            0
        ],
        "reloadtime": 3,
        "requiredoptictype": -1,
        "showtoplayer": 0,
        "sound": [
            "",
            10,
            1
        ],
        "soundbegin": [
            "sound",
            1
        ],
        "soundbeginwater": [
            "sound",
            1
        ],
        "soundburst": 0,
        "soundclosure": [
            "sound",
            1
        ],
        "soundcontinuous": 0,
        "soundend": [],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "railgun_01_Discharge_01_SoundSet",
                "railgun_01_Tail_SoundSet"
            ]
        },
        "texturetype": "semi",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "primary": 10,
    "recoil": [],
    "reloadaction": "",
    "reloadmagazinesound": [
        "a3/Sounds_F_Decade/Assets/Arsenal/railgun_01/railgun_01_reload",
        2.81838,
        1,
        70
    ],
    "reloadsound": [
        "a3/Sounds_F_Decade/Assets/Arsenal/railgun_01/railgun_01_reload",
        2.81838,
        1,
        70
    ],
    "reloadtime": 1,
    "scope": 2,
    "selectionfireanim": "zasleh",
    "showaimcursorinternal": 1,
    "showempty": 1,
    "shownunderwaterselections": [],
    "showswitchaction": 0,
    "showtoplayer": 1,
    "simulation": "Weapon",
    "sound": [
        "",
        1,
        1
    ],
    "soundbegin": [
        "sound",
        1
    ],
    "soundbeginwater": [
        "sound",
        1
    ],
    "soundbullet": [
        "emptySound",
        1
    ],
    "soundburst": 1,
    "soundclosure": [
        "sound",
        1
    ],
    "soundcontinuous": 0,
    "soundend": [
        "sound",
        1
    ],
    "soundloop": [
        "sound",
        1
    ],
    "swaydecayspeed": 2,
    "tbody": 400,
    "texturetype": "default",
    "type": 65536,
    "uipicture": "",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 2,
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponsoundeffect": "",
    "weight": 0,
    "zeroingsound": [
        "",
        1,
        1
    ]
}