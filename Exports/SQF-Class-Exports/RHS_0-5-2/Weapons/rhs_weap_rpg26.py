d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "aimtransitionspeed": 0.75,
    "airateoffire": 7,
    "airateoffiredispersion": 0,
    "airateoffiredistance": 300,
    "ammo": "",
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "author": "Red Hammer Studios",
    "autoaimenabled": 0,
    "autofire": 0,
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
    "count": 1,
    "cursor": "rocket",
    "cursoraim": "EmptyCursor",
    "cursoraimon": "",
    "cursorsize": 1,
    "descriptionshort": "Rocket launcher<br/>Caliber: 72.5mm<br/>Type: Single-shot Anti-tank",
    "detectrange": 0,
    "dexterity": 1.7,
    "dispersion": 0.18,
    "displayname": "RPG-26",
    "distancezoommax": 100,
    "distancezoommin": 100,
    "dlc": "RHS_AFRF",
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
        "/rhsafrf/addons/rhs_c_weapons/anims/RPG26.rtm"
    ],
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 460,
    "htmin": 1,
    "inertia": 1,
    "initspeed": 30,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "irlaserend": "laser dir",
    "irlaserpos": "laser pos",
    "iteminfo": {
        "onhovertext": "RPG-26",
        "priority": 3,
        "rmbhint": "RPG-26"
    },
    "laser": 0,
    "library": {
        "libtextdesc": "The RPG-26 Aglen is a disposable anti-tank rocket launcher developed by the Soviet Union."
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
        "rhs_rpg26_mag"
    ],
    "maxrange": 350,
    "maxrangeprobab": 0.1,
    "maxrecoilsway": 0.008,
    "maxzeroing": 1000,
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 200,
    "midrangeprobab": 0.7,
    "minrange": 10,
    "minrangeprobab": 0.9,
    "model": "rhsafrf/addons/rhs_weapons/rpg26/rpg26",
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
            "cameradir": "op_look2",
            "discretedistance": [
                100,
                0
            ],
            "discretedistancecamerapoint": [
                "eye_ironsight",
                "eye_rangefinder"
            ],
            "discretedistanceinitindex": 0,
            "distancezoommax": 100,
            "distancezoommin": 100,
            "opticsdisableperipherialvision": 0,
            "opticsflare": 0,
            "opticsid": 2,
            "opticsppeffects": [
                "OpticsCHAbera1",
                "OpticsBlur1"
            ],
            "opticszoominit": 0.6,
            "opticszoommax": 0.6,
            "opticszoommin": 0.25,
            "usemodeloptics": 0,
            "visionmode": ""
        },
        "ironsight2": {
            "cameradir": "op_look",
            "discretedistance": [
                50,
                150,
                250
            ],
            "discretedistancecamerapoint": [
                "eye",
                "OP_eye1",
                "OP_eye2"
            ],
            "discretedistanceinitindex": 0,
            "distancezoommax": 250,
            "distancezoommin": 50,
            "opticsdisableperipherialvision": 0,
            "opticsflare": 0,
            "opticsid": 1,
            "opticsppeffects": [
                "OpticsCHAbera1",
                "OpticsBlur1"
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
    "picture": "rhsafrf/addons/rhs_inventoryicons/data/weapons/rhs_weap_rpg26_ca.paa",
    "primary": 0,
    "recoil": [
        0,
        0,
        0,
        0.03,
        0.0073886,
        0.0028696,
        0.04,
        0.0063634,
        0.0010008,
        0.05,
        0.003951,
        0.0006112,
        0.06,
        0.0014776,
        0.000228,
        0.06,
        0,
        0,
        0.06,
        -0.0004804,
        -7.68e-05,
        0.06,
        -0.000706,
        -0.0001128,
        0.06,
        -0.0007354,
        -0.0001176,
        0.06,
        -0.0006276,
        -0.0001,
        0.06,
        -0.0004412,
        -7.04e-05,
        0.06,
        -0.0002354,
        -3.76e-05,
        0.06,
        -6.86e-05,
        -1.12e-05,
        0.06,
        -3e-05,
        0,
        0.06,
        0,
        0
    ],
    "reloadaction": "ReloadRPG",
    "reloadmagazinesound": [
        "A3/sounds_f/weapons/rockets/titan_reload_final",
        0.562341,
        1,
        50
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
        "begin1": [
            "rhsafrf/addons/rhs_sounds/rpg/rpg_1",
            2.35,
            1,
            1100
        ],
        "begin2": [
            "rhsafrf/addons/rhs_sounds/rpg/rpg_2",
            2.35,
            1,
            1100
        ],
        "soundbegin": [
            "begin1",
            0.5,
            "begin2",
            0.5
        ],
        "weaponsoundeffect": "DefaultRifle"
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
        "mass": 63.8
    },
    "weaponsoundeffect": "",
    "weight": 0,
    "zeroingsound": [
        "",
        1,
        1
    ]
}