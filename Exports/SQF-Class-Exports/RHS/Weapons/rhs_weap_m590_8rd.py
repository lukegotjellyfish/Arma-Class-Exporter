d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 6,
    "aidispersioncoefy": 6,
    "aimtransitionspeed": 1,
    "airateoffire": 0.5,
    "airateoffiredispersion": 0,
    "airateoffiredistance": 500,
    "ammo": "",
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "author": "Red Hammer Studios",
    "autofire": 1,
    "autoreload": 0,
    "backgroundreload": 0,
    "ballisticscomputer": 0,
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
    "cursor": "arifle",
    "cursoraim": "CursorAim",
    "cursoraimon": "",
    "cursorsize": 1,
    "deployedpivot": "bipod",
    "descriptionshort": "Shotgun <br />Caliber: 12 gauge",
    "detectrange": 0,
    "dexterity": 1.4,
    "discretedistance": [
        50
    ],
    "discretedistanceinitindex": 0,
    "dispersion": 0.00029,
    "displayname": "M590A1 (Long)",
    "distancezoommax": 50,
    "distancezoommin": 50,
    "dlc": "RHS_USAF",
    "drysound": [
        "",
        1,
        1
    ],
    "emptysound": [
        "",
        1,
        1
    ],
    "enableattack": 1,
    "eventhandlers": {
        "rhs_boltaction": {
            "fired": "[_this select 0,_this # 1,_this # 1,_this # 4] call rhs_fnc_boltAction;",
            "reload": "_this spawn rhs_fnc_reloadShotgun"
        }
    },
    "ffcount": 3,
    "fffrequency": 11,
    "ffmagnitude": 0.5,
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
    "firespreadangle": 0.95,
    "flash": "gunfire",
    "flashsize": 0.5,
    "forceoptics": 0,
    "gunclouds": {
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
        "interval": -0.02,
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
        "firsteffect": {
            "directionname": "Konec hlavne",
            "effectname": "RifleAssaultCloud",
            "positionname": "Usti hlavne"
        }
    },
    "handanim": [
        "OFP2_ManSkeleton",
        "/rhsusf/addons/rhsusf_c_weapons/anims/rhs_hand_m590.rtm"
    ],
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 600,
    "htmin": 1,
    "inertia": 0.6,
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
        "rhsusf_8rnd_00buck",
        "rhsusf_8rnd_slug",
        "rhsusf_8rnd_he",
        "rhsusf_8rnd_frag",
        "rhsgref_1rnd_00buck",
        "rhsgref_1rnd_slug",
        "rhsusf_5rnd_00buck",
        "rhsusf_5rnd_slug",
        "rhsusf_5rnd_he",
        "rhsusf_5rnd_frag"
    ],
    "magazinewell": [
        "CBA_12g_1rnd",
        "CBA_12g_2rnds",
        "CBA_12g_3rnds",
        "CBA_12g_4rnds",
        "CBA_12g_5rnds",
        "CBA_12g_6rnds",
        "CBA_12g_7rnds",
        "CBA_12g_8rnds"
    ],
    "maxleadspeed": 23,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "maxrecoilsway": 0.008,
    "maxzeroing": 1000,
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "minrange": 1,
    "minrangeprobab": 0.3,
    "model": "rhsusf/addons/rhsusf_weapons2/M590A1/M590_8MAG",
    "modelmagazine": "",
    "modeloptics": "-",
    "modelspecial": "",
    "modes": [
        "Single"
    ],
    "multiplier": 1,
    "muzzleend": "konec hlavne",
    "muzzlepos": "usti hlavne",
    "muzzles": [
        "this",
        "SAFE",
        "RHS_ReloadAction"
    ],
    "namesound": "rifle",
    "optics": 1,
    "opticsdisableperipherialvision": 0.67,
    "opticsflare": 0,
    "opticsid": 0,
    "opticsppeffects": [],
    "opticszoominit": 0.75,
    "opticszoommax": 1.25,
    "opticszoommin": 0.25,
    "picture": "rhsusf/addons/rhsusf_inventoryicons/data/weapons/rhs_weap_M590_8RD_ca.paa",
    "primary": 10,
    "recoil": "rhs_recoil_m590",
    "recoilprone": "assaultRifleBase",
    "reloadaction": "RHS_GestureReloadM590",
    "reloadmagazinesound": [
        "",
        1,
        1
    ],
    "reloadsound": [
        "A3/sounds_f/weapons/M320/M320_reload",
        0.1,
        1,
        30
    ],
    "reloadtime": 0.15,
    "rhs_boltactionanim": "RHS_GestureRechamberM590",
    "rhs_boltactioncasedelay": 0.1,
    "rhs_boltactioncasedir": [
        0.3,
        0.05,
        0.25
    ],
    "rhs_boltactioncasepos": [
        0,
        0.05,
        0.05
    ],
    "rhs_boltactioncaseselection": "rightHand",
    "rhs_boltactionsound": [
        "rhsusf/addons/rhsusf_c_weapons/sounds/m590_pump.ogg",
        0.9,
        1,
        20
    ],
    "rhs_reloadaction": {
        "access": 3,
        "afmax": 0,
        "aidispersioncoefx": 6,
        "aidispersioncoefy": 6,
        "aimtransitionspeed": 1,
        "airateoffire": 0.5,
        "airateoffiredispersion": 0,
        "airateoffiredistance": 500,
        "ammo": "",
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "autoreload": 0,
        "backgroundreload": 0,
        "ballisticscomputer": 0,
        "burst": 1,
        "candrop": 1,
        "canlock": 0,
        "canshootinwater": 0,
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "changefiremodesound": [
            "A3/sounds_f/weapons/closure/firemode_changer_2",
            0.551189,
            1,
            5
        ],
        "cmimmunity": 1,
        "count": 0,
        "cursor": "arifle",
        "cursoraim": "CursorAim",
        "cursoraimon": "",
        "cursorsize": 1,
        "deployedpivot": "bipod",
        "descriptionshort": "SAFE",
        "detectrange": 0,
        "dexterity": 1.7,
        "discretedistance": [
            0
        ],
        "discretedistanceinitindex": 0,
        "dispersion": 0.00029,
        "displayname": "SAFE",
        "distancezoommax": 300,
        "distancezoommin": 300,
        "drysound": [
            "A3/Sounds_F/arsenal/weapons/Rifles/MX/dry_Mx",
            0.562341,
            1,
            10
        ],
        "emptysound": [
            "",
            1,
            1
        ],
        "enableattack": 1,
        "eventhandlers": {},
        "ffcount": 3,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
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
        "flash": "gunfire",
        "flashsize": 0.5,
        "forceoptics": 0,
        "gunclouds": {
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
            "interval": -0.02,
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
            "firsteffect": {
                "directionname": "Konec hlavne",
                "effectname": "RifleAssaultCloud",
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
            "rhsusf_8rnd_00buck",
            "rhsusf_8rnd_slug",
            "rhsusf_8rnd_he",
            "rhsusf_8rnd_frag",
            "rhsgref_1rnd_00buck",
            "rhsgref_1rnd_slug",
            "rhsusf_5rnd_00buck",
            "rhsusf_5rnd_slug",
            "rhsusf_5rnd_he",
            "rhsusf_5rnd_frag"
        ],
        "maxleadspeed": 23,
        "maxrange": 500,
        "maxrangeprobab": 0.04,
        "maxrecoilsway": 0.008,
        "maxzeroing": 1000,
        "memorypointcamera": "eye",
        "mfact": 1,
        "mfmax": 0,
        "midrange": 150,
        "midrangeprobab": 0.58,
        "minrange": 1,
        "minrangeprobab": 0.3,
        "model": "",
        "modelmagazine": "",
        "modeloptics": "-",
        "modelspecial": "",
        "modes": [
            "this"
        ],
        "multiplier": 1,
        "muzzleend": "konec hlavne",
        "muzzlepos": "usti hlavne",
        "muzzles": [
            "this"
        ],
        "namesound": "rifle",
        "optics": 0,
        "opticsdisableperipherialvision": 0.67,
        "opticsflare": 0,
        "opticsid": 0,
        "opticsppeffects": [],
        "opticszoominit": 0.75,
        "opticszoommax": 1.25,
        "opticszoommin": 0.25,
        "picture": "",
        "primary": 10,
        "recoil": "recoil_default",
        "recoilprone": "assaultRifleBase",
        "reloadaction": "ReloadMagazine",
        "reloadmagazinesound": [
            "",
            1,
            1
        ],
        "reloadsound": [
            "",
            1,
            1
        ],
        "reloadtime": 0.1,
        "safe": {
            "aidispersioncoefx": 1.4,
            "aidispersioncoefy": 1.7,
            "airateoffire": 2,
            "airateoffiredispersion": 1,
            "airateoffiredistance": 500,
            "artillerycharge": 1,
            "artillerydispersion": 1,
            "autofire": 0,
            "burst": 1,
            "burstrangemax": -1,
            "canshootinwater": 0,
            "descriptionshort": "SAFE",
            "dispersion": 0.0002,
            "displayname": "SAFE",
            "ffcount": 1,
            "fffrequency": 11,
            "ffmagnitude": 0.5,
            "flash": "gunfire",
            "flashsize": 0.1,
            "maxrange": 0.001,
            "maxrangeprobab": 0.001,
            "midrange": 0.001,
            "midrangeprobab": 0.001,
            "minrange": 0,
            "minrangeprobab": 0.001,
            "multiplier": 1,
            "recoil": "recoil_single_primary_3outof10",
            "recoilprone": "recoil_single_primary_prone_3outof10",
            "reloadtime": 0.1,
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
            "sounds": [],
            "texturetype": "semi",
            "useaction": 0,
            "useactiontitle": "",
            "weaponsoundeffect": ""
        },
        "scope": 0,
        "selectionfireanim": "zasleh",
        "showaimcursorinternal": 1,
        "showempty": 1,
        "shownunderwaterselections": [],
        "showswitchaction": 0,
        "showtoplayer": 0,
        "simulation": "Weapon",
        "sound": [],
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
        "tbody": 100,
        "texturetype": "default",
        "type": 1,
        "uipicture": "",
        "useaction": 0,
        "useactiontitle": "",
        "useasbinocular": 0,
        "usemodeloptics": 1,
        "value": 4,
        "weaponinfotype": "RscWeaponZeroing",
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "weaponpoolavailable": 1,
        "weaponslotsinfo": {
            "allowedslots": [
                901
            ],
            "cowsslot": {
                "access": 1,
                "compatibleitems": [
                    "optic_Nightstalker",
                    "optic_tws",
                    "optic_tws_mg",
                    "optic_NVS",
                    "optic_DMS",
                    "optic_LRPS",
                    "optic_ams",
                    "optic_AMS_snd",
                    "optic_AMS_khk",
                    "optic_KHS_blk",
                    "optic_KHS_tan",
                    "optic_KHS_hex",
                    "optic_KHS_old",
                    "optic_SOS",
                    "optic_MRCO",
                    "optic_Arco",
                    "optic_aco",
                    "optic_ACO_grn",
                    "optic_aco_smg",
                    "optic_ACO_grn_smg",
                    "optic_hamr",
                    "optic_Holosight",
                    "optic_Holosight_smg",
                    "optic_Hamr_khk_F",
                    "optic_SOS_khk_F",
                    "optic_Arco_ghex_F",
                    "optic_Arco_blk_F",
                    "optic_DMS_ghex_F",
                    "optic_ERCO_blk_F",
                    "optic_ERCO_khk_F",
                    "optic_ERCO_snd_F",
                    "optic_LRPS_ghex_F",
                    "optic_LRPS_tna_F",
                    "optic_Holosight_blk_F",
                    "optic_Holosight_khk_F",
                    "optic_Holosight_smg_blk_F",
                    "optic_Holosight_smg_khk_F",
                    "optic_Arco_AK_blk_F",
                    "optic_Arco_AK_lush_F",
                    "optic_Arco_AK_arid_F",
                    "optic_DMS_weathered_F",
                    "optic_DMS_weathered_Kir_F",
                    "optic_Arco_lush_F",
                    "optic_Arco_arid_F",
                    "optic_Holosight_lush_F",
                    "optic_Holosight_arid_F"
                ],
                "displayname": "Optics Slot",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_top.paa",
                "iconpinpoint": "Bottom",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/TOP",
                "scope": 0
            },
            "mass": 2,
            "muzzleslot": {
                "access": 1,
                "compatibleitems": [],
                "displayname": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_muzzle.paa",
                "iconpinpoint": "Center",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/MUZZLE",
                "scope": 0
            },
            "pointerslot": {
                "access": 1,
                "compatibleitems": [
                    "acc_flashlight",
                    "acc_pointer_IR"
                ],
                "displayname": "Pointer Slot",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_side.paa",
                "iconpinpoint": "Center",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/SIDE",
                "scope": 0
            }
        },
        "weaponsoundeffect": "",
        "weight": 0,
        "zeroingsound": [
            "A3/Sounds_F/arsenal/sfx/shared/zeroing_knob_tick_metal",
            0.316228,
            1,
            5
        ]
    },
    "safe": {
        "access": 3,
        "afmax": 0,
        "aidispersioncoefx": 6,
        "aidispersioncoefy": 6,
        "aimtransitionspeed": 1,
        "airateoffire": 0.5,
        "airateoffiredispersion": 0,
        "airateoffiredistance": 500,
        "ammo": "",
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "autoreload": 0,
        "backgroundreload": 0,
        "ballisticscomputer": 0,
        "burst": 1,
        "candrop": 1,
        "canlock": 0,
        "canshootinwater": 0,
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "changefiremodesound": [
            "A3/sounds_f/weapons/closure/firemode_changer_2",
            0.551189,
            1,
            5
        ],
        "cmimmunity": 1,
        "count": 0,
        "cursor": "arifle",
        "cursoraim": "CursorAim",
        "cursoraimon": "",
        "cursorsize": 1,
        "deployedpivot": "bipod",
        "descriptionshort": "SAFE",
        "detectrange": 0,
        "dexterity": 1.7,
        "discretedistance": [
            0
        ],
        "discretedistanceinitindex": 0,
        "dispersion": 0.00029,
        "displayname": "SAFE",
        "distancezoommax": 300,
        "distancezoommin": 300,
        "drysound": [
            "A3/Sounds_F/arsenal/weapons/Rifles/MX/dry_Mx",
            0.562341,
            1,
            10
        ],
        "emptysound": [
            "",
            1,
            1
        ],
        "enableattack": 1,
        "eventhandlers": {},
        "ffcount": 3,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
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
        "flash": "gunfire",
        "flashsize": 0.5,
        "forceoptics": 0,
        "gunclouds": {
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
            "interval": -0.02,
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
            "firsteffect": {
                "directionname": "Konec hlavne",
                "effectname": "RifleAssaultCloud",
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
            "rhsusf_8rnd_00buck",
            "rhsusf_8rnd_slug",
            "rhsusf_8rnd_he",
            "rhsusf_8rnd_frag",
            "rhsgref_1rnd_00buck",
            "rhsgref_1rnd_slug",
            "rhsusf_5rnd_00buck",
            "rhsusf_5rnd_slug",
            "rhsusf_5rnd_he",
            "rhsusf_5rnd_frag"
        ],
        "maxleadspeed": 23,
        "maxrange": 500,
        "maxrangeprobab": 0.04,
        "maxrecoilsway": 0.008,
        "maxzeroing": 1000,
        "memorypointcamera": "eye",
        "mfact": 1,
        "mfmax": 0,
        "midrange": 150,
        "midrangeprobab": 0.58,
        "minrange": 1,
        "minrangeprobab": 0.3,
        "model": "",
        "modelmagazine": "",
        "modeloptics": "-",
        "modelspecial": "",
        "modes": [
            "Safe"
        ],
        "multiplier": 1,
        "muzzleend": "konec hlavne",
        "muzzlepos": "usti hlavne",
        "muzzles": [
            "this"
        ],
        "namesound": "rifle",
        "optics": 0,
        "opticsdisableperipherialvision": 0.67,
        "opticsflare": 0,
        "opticsid": 0,
        "opticsppeffects": [],
        "opticszoominit": 0.75,
        "opticszoommax": 1.25,
        "opticszoommin": 0.25,
        "picture": "",
        "primary": 10,
        "recoil": "recoil_default",
        "recoilprone": "assaultRifleBase",
        "reloadaction": "ReloadMagazine",
        "reloadmagazinesound": [
            "",
            1,
            1
        ],
        "reloadsound": [
            "",
            1,
            1
        ],
        "reloadtime": 0.15,
        "safe": {
            "aidispersioncoefx": 1.4,
            "aidispersioncoefy": 1.7,
            "airateoffire": 2,
            "airateoffiredispersion": 1,
            "airateoffiredistance": 500,
            "artillerycharge": 1,
            "artillerydispersion": 1,
            "autofire": 0,
            "burst": 1,
            "burstrangemax": -1,
            "canshootinwater": 0,
            "descriptionshort": "SAFE",
            "dispersion": 0.0002,
            "displayname": "SAFE",
            "ffcount": 1,
            "fffrequency": 11,
            "ffmagnitude": 0.5,
            "flash": "gunfire",
            "flashsize": 0.1,
            "maxrange": 0.001,
            "maxrangeprobab": 0.001,
            "midrange": 0.001,
            "midrangeprobab": 0.001,
            "minrange": 0,
            "minrangeprobab": 0.001,
            "multiplier": 1,
            "recoil": "recoil_single_primary_3outof10",
            "recoilprone": "recoil_single_primary_prone_3outof10",
            "reloadtime": 0.1,
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
            "sounds": [],
            "texturetype": "semi",
            "useaction": 0,
            "useactiontitle": "",
            "weaponsoundeffect": ""
        },
        "scope": 0,
        "selectionfireanim": "zasleh",
        "showaimcursorinternal": 1,
        "showempty": 1,
        "shownunderwaterselections": [],
        "showswitchaction": 0,
        "showtoplayer": 0,
        "simulation": "Weapon",
        "sound": [],
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
        "tbody": 100,
        "texturetype": "default",
        "type": 1,
        "uipicture": "",
        "useaction": 0,
        "useactiontitle": "",
        "useasbinocular": 0,
        "usemodeloptics": 1,
        "value": 4,
        "weaponinfotype": "RscWeaponZeroing",
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "weaponpoolavailable": 1,
        "weaponslotsinfo": {
            "allowedslots": [
                901
            ],
            "cowsslot": {
                "access": 1,
                "compatibleitems": [
                    "optic_Nightstalker",
                    "optic_tws",
                    "optic_tws_mg",
                    "optic_NVS",
                    "optic_DMS",
                    "optic_LRPS",
                    "optic_ams",
                    "optic_AMS_snd",
                    "optic_AMS_khk",
                    "optic_KHS_blk",
                    "optic_KHS_tan",
                    "optic_KHS_hex",
                    "optic_KHS_old",
                    "optic_SOS",
                    "optic_MRCO",
                    "optic_Arco",
                    "optic_aco",
                    "optic_ACO_grn",
                    "optic_aco_smg",
                    "optic_ACO_grn_smg",
                    "optic_hamr",
                    "optic_Holosight",
                    "optic_Holosight_smg",
                    "optic_Hamr_khk_F",
                    "optic_SOS_khk_F",
                    "optic_Arco_ghex_F",
                    "optic_Arco_blk_F",
                    "optic_DMS_ghex_F",
                    "optic_ERCO_blk_F",
                    "optic_ERCO_khk_F",
                    "optic_ERCO_snd_F",
                    "optic_LRPS_ghex_F",
                    "optic_LRPS_tna_F",
                    "optic_Holosight_blk_F",
                    "optic_Holosight_khk_F",
                    "optic_Holosight_smg_blk_F",
                    "optic_Holosight_smg_khk_F",
                    "optic_Arco_AK_blk_F",
                    "optic_Arco_AK_lush_F",
                    "optic_Arco_AK_arid_F",
                    "optic_DMS_weathered_F",
                    "optic_DMS_weathered_Kir_F",
                    "optic_Arco_lush_F",
                    "optic_Arco_arid_F",
                    "optic_Holosight_lush_F",
                    "optic_Holosight_arid_F"
                ],
                "displayname": "Optics Slot",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_top.paa",
                "iconpinpoint": "Bottom",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/TOP",
                "scope": 0
            },
            "mass": 2,
            "muzzleslot": {
                "access": 1,
                "compatibleitems": [],
                "displayname": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_muzzle.paa",
                "iconpinpoint": "Center",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/MUZZLE",
                "scope": 0
            },
            "pointerslot": {
                "access": 1,
                "compatibleitems": [
                    "acc_flashlight",
                    "acc_pointer_IR"
                ],
                "displayname": "Pointer Slot",
                "iconpicture": "A3/Weapons_F/Data/UI/attachment_side.paa",
                "iconpinpoint": "Center",
                "iconposition": [
                    0,
                    0
                ],
                "iconscale": 0,
                "linkproxy": "A3/data_f/proxies/weapon_slots/SIDE",
                "scope": 0
            }
        },
        "weaponsoundeffect": "",
        "weight": 0,
        "zeroingsound": [
            "A3/Sounds_F/arsenal/sfx/shared/zeroing_knob_tick_metal",
            0.316228,
            1,
            5
        ]
    },
    "scope": 2,
    "selectionfireanim": "zasleh",
    "showaimcursorinternal": 1,
    "showempty": 1,
    "shownunderwaterselections": [],
    "showswitchaction": 0,
    "showtoplayer": 1,
    "simulation": "Weapon",
    "single": {
        "aidispersioncoefx": 1.4,
        "aidispersioncoefy": 1.7,
        "airateoffire": 2,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 500,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 0,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.0002,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 600,
        "maxrangeprobab": 0.04,
        "midrange": 300,
        "midrangeprobab": 0.58,
        "minrange": 1,
        "minrangeprobab": 0.45,
        "multiplier": 1,
        "recoil": "recoil_single_primary_3outof10",
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "reloadtime": 0.6,
        "requiredoptictype": -1,
        "showtoplayer": 1,
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
                "RHSUSF_m590_Shot_SoundSet",
                "RHSUSF_MMG1_Tail_SoundSet"
            ]
        },
        "texturetype": "semi",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "sound": [],
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
    "tbody": 100,
    "texturetype": "default",
    "type": 1,
    "uipicture": "",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 4,
    "weaponinfotype": "rhs_m590_handler",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponpoolavailable": 1,
    "weaponslotsinfo": {
        "allowedslots": [
            901
        ],
        "mass": 71.72,
        "pointerslot": {
            "iconpicture": "A3/Weapons_F/Data/clear_empty.paa",
            "iconpinpoint": "Left",
            "iconposition": [
                0,
                0
            ],
            "iconscale": 1
        }
    },
    "weaponsoundeffect": "",
    "weight": 0,
    "zeroingsound": [
        "A3/Sounds_F/arsenal/sfx/shared/zeroing_knob_tick_metal",
        0.316228,
        1,
        5
    ]
}