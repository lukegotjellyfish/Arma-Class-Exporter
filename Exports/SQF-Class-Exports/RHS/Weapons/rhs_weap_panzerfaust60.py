d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "aimtransitionspeed": 0.75,
    "airateoffire": 4,
    "airateoffiredispersion": 0,
    "airateoffiredistance": 60,
    "ammo": "",
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "author": "Red Hammer Studios",
    "autoaimenabled": 0,
    "autofire": 0,
    "autoreload": 0,
    "backgroundreload": 0,
    "ballisticscomputer": 0,
    "baseweapon": "rhs_weap_panzerfaust60",
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
    "count": 1,
    "cursor": "rocket",
    "cursoraim": "EmptyCursor",
    "cursoraimon": "",
    "cursorsize": 1,
    "descriptionshort": "Rocket launcher<br/>Caliber: 149mm<br/>Type: Single-shot Anti-tank",
    "detectrange": 0,
    "dexterity": 1.7,
    "dispersion": 0.25,
    "displayname": "Panzerfaust 60",
    "distancezoommax": 100,
    "distancezoommin": 100,
    "dlc": "RHS_GREF",
    "drysound": [
        "A3/sounds_f/weapons/other/dry6",
        0.0316228,
        1,
        10
    ],
    "emptysound": [
        "",
        1,
        1
    ],
    "enableattack": 1,
    "eventhandlers": {
        "rhs_disposableweapon": {
            "fired": "_this call rhs_fnc_disposable;"
        }
    },
    "ffcount": 1,
    "fffrequency": 1,
    "ffmagnitude": 0.1,
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
        "effect1": {
            "directionname": "usti hlavne",
            "effectname": "RocketBackEffectsRPGNT",
            "positionname": "konec hlavne"
        }
    },
    "handanim": [
        "OFP2_ManSkeleton",
        "/rhsgref/addons/rhsgref_c_weapons/anims/rhs_hand_pzf60.rtm"
    ],
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 460,
    "htmin": 1,
    "inertia": 0.8,
    "initspeed": 30,
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
    "magazinereloadtime": 1,
    "magazines": [
        "rhs_panzerfaust60_mag"
    ],
    "maxrange": 80,
    "maxrangeprobab": 0.1,
    "maxrecoilsway": 0.008,
    "maxzeroing": 1000,
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 60,
    "midrangeprobab": 0.7,
    "minrange": 10,
    "minrangeprobab": 0.9,
    "model": "rhsgref/addons/rhsgref_weapons2/pzf/rhs_pzf60.p3d",
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
    "namesound": "atlauncher",
    "optics": 1,
    "opticsdisableperipherialvision": 1,
    "opticsflare": 1,
    "opticsid": 0,
    "opticsmodes": {
        "ironsight": {
            "cameradir": "eye_look",
            "discretedistance": [
                30,
                60,
                80
            ],
            "discretedistancecamerapoint": [
                "eye_30",
                "eye_60",
                "eye_80"
            ],
            "discretedistanceinitindex": 0,
            "distancezoommax": 100,
            "distancezoommin": 100,
            "opticsdisableperipherialvision": 0,
            "opticsflare": 0,
            "opticsid": 2,
            "opticsppeffects": [
                "OpticsCHAbera1",
                "WeaponsOptics"
            ],
            "opticszoominit": 0.6,
            "opticszoommax": 0.6,
            "opticszoommin": 0.25,
            "usemodeloptics": 0,
            "visionmode": ""
        }
    },
    "opticsppeffects": [],
    "opticszoominit": 0.75,
    "opticszoommax": 1.1,
    "opticszoommin": 0.375,
    "picture": "rhsgref/addons/rhsgref_inventoryicons/data/weapons/rhs_weap_panzerfaust60_ca.paa",
    "primary": 0,
    "recoil": "recoil_single_law",
    "recoilprone": "",
    "reloadaction": "ManActReloadAT",
    "reloadmagazinesound": [
        "A3/sounds_f/weapons/rockets/titan_reload_final",
        0.562341,
        1,
        20
    ],
    "reloadsound": [
        "",
        1,
        1
    ],
    "reloadtime": 1,
    "rhs_disposable": 1,
    "scope": 2,
    "selectionfireanim": "zasleh",
    "shotend": "konec hlavne",
    "shotpos": "usti hlavne",
    "showaimcursorinternal": 1,
    "showempty": 1,
    "shownunderwaterselections": [],
    "showswitchaction": 0,
    "showtoplayer": 1,
    "simulation": "Weapon",
    "sound": [
        "A3/Sounds_F/weapons/Launcher/rocket_launcher_5",
        1,
        1,
        800
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
    "soundfly": [
        "A3/sounds_f/weapons/rockets/rocket_fly_1",
        0.316228,
        1.5,
        700
    ],
    "soundloop": [
        "sound",
        1
    ],
    "sounds": [
        "StandardSound"
    ],
    "standardsound": {
        "soundsetshot": [
            "Launcher_RPG32_Shot_SoundSet",
            "Launcher_RPG32_Tail_SoundSet"
        ]
    },
    "swaycoef": 0.5,
    "swaydecayspeed": 2,
    "tbody": 100,
    "texturetype": "semi",
    "type": 4,
    "uipicture": "A3/Weapons_F/Data/UI/icon_at_CA.paa",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 10,
    "weaponinfotype": "rhs_rscOptics_disposable",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponpoolavailable": 1,
    "weaponslotsinfo": {
        "allowedslots": [
            901
        ],
        "mass": 137.5
    },
    "weaponsoundeffect": "",
    "weight": 0,
    "zeroingsound": [
        "",
        1,
        1
    ]
}