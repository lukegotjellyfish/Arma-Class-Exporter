d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "aimtransitionspeed": 1,
    "airateoffire": 5,
    "airateoffiredispersion": 0,
    "airateoffiredistance": 500,
    "ammo": "",
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "author": "Red Hammer Studios",
    "autofire": 0,
    "autoreload": 0,
    "backgroundreload": 0,
    "ballisticscomputer": 0,
    "basesoundmodetype": {
        "closure1": [
            "",
            1.03514,
            1,
            10
        ],
        "closure2": [
            "",
            1.03514,
            1.1,
            10
        ],
        "soundclosure": [
            "closure1",
            0.5,
            "closure2",
            0.5
        ],
        "weaponsoundeffect": "DefaultRifle"
    },
    "baseweapon": "rhs_weap_rsp30_green",
    "bullet1": [
        "A3/sounds_f/weapons/shells/9mm/metal_9mm_01",
        0.562341,
        1,
        15
    ],
    "bullet10": [
        "A3/sounds_f/weapons/shells/9mm/grass_9mm_02",
        0.562341,
        1,
        15
    ],
    "bullet11": [
        "A3/sounds_f/weapons/shells/9mm/grass_9mm_03",
        0.562341,
        1,
        15
    ],
    "bullet12": [
        "A3/sounds_f/weapons/shells/9mm/grass_9mm_04",
        0.562341,
        1,
        15
    ],
    "bullet2": [
        "A3/sounds_f/weapons/shells/9mm/metal_9mm_02",
        0.562341,
        1,
        15
    ],
    "bullet3": [
        "A3/sounds_f/weapons/shells/9mm/metal_9mm_03",
        0.562341,
        1,
        15
    ],
    "bullet4": [
        "A3/sounds_f/weapons/shells/9mm/metal_9mm_04",
        0.562341,
        1,
        15
    ],
    "bullet5": [
        "A3/sounds_f/weapons/shells/9mm/dirt_9mm_01",
        0.562341,
        1,
        15
    ],
    "bullet6": [
        "A3/sounds_f/weapons/shells/9mm/dirt_9mm_02",
        0.562341,
        1,
        15
    ],
    "bullet7": [
        "A3/sounds_f/weapons/shells/9mm/dirt_9mm_03",
        0.562341,
        1,
        15
    ],
    "bullet8": [
        "A3/sounds_f/weapons/shells/9mm/dirt_9mm_04",
        0.562341,
        1,
        15
    ],
    "bullet9": [
        "A3/sounds_f/weapons/shells/9mm/grass_9mm_01",
        0.562341,
        1,
        15
    ],
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
    "cursor": "hgun",
    "cursoraim": "cursorAim",
    "cursoraimon": "",
    "cursorsize": 1,
    "descriptionshort": "RSP-30 Green Flare",
    "detectrange": 0,
    "dexterity": 2,
    "discretedistance": [
        50
    ],
    "discretedistanceinitindex": 0,
    "dispersion": 0.002,
    "displayname": "RSP-30 (Green)",
    "displaynameshort": "RSP-30",
    "distancezoommax": 400,
    "distancezoommin": 400,
    "dlc": "RHS_AFRF",
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
        "rhs_disposableweapon": {
            "fired": "_this call rhs_fnc_disposable;"
        }
    },
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
            "directionname": "konec hlavne",
            "effectname": "StarterPistolCloud1",
            "positionname": "usti hlavne"
        },
        "effect2": {
            "directionname": "usti hlavne",
            "effectname": "StarterPistolCloud2",
            "positionname": "konec hlavne"
        }
    },
    "handanim": [
        "OFP2_ManSkeleton",
        "/rhsafrf/addons/rhs_c_weapons/anims/rsp30.rtm"
    ],
    "hiddenselections": [
        "camo1"
    ],
    "hiddenselectionsmaterials": [
        "rhsafrf/addons/rhs_weapons/rsp30/rhs_rsp30_green.rvmat"
    ],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_weapons/rsp30/rhs_rsp30_green_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 300,
    "htmin": 1,
    "inertia": 0.1,
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
    "magazinereloadtime": 2,
    "magazines": [
        "rhs_mag_rsp30_green"
    ],
    "maxrange": 50,
    "maxrangeprobab": 0.04,
    "maxrecoilsway": 0.008,
    "maxzeroing": 100,
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 30,
    "midrangeprobab": 0.3,
    "minrange": 0,
    "minrangeprobab": 0.1,
    "model": "rhsafrf/addons/rhs_weapons/rsp30/rhs_rsp30",
    "modelmagazine": "",
    "modeloptics": "-",
    "modelspecial": "",
    "modes": [
        "this"
    ],
    "multiplier": 1,
    "muzzleeffect": "BIS_fnc_effectFiredFlares",
    "muzzleend": "konec hlavne",
    "muzzlepos": "usti hlavne",
    "muzzles": [
        "this"
    ],
    "namesound": "Pistol",
    "optics": 0,
    "opticsdisableperipherialvision": 0.67,
    "opticsflare": 0,
    "opticsid": 0,
    "opticsppeffects": [],
    "opticszoominit": 0.75,
    "opticszoommax": 1.25,
    "opticszoommin": 0.25,
    "picture": "rhsafrf/addons/rhs_weapons/icons/rsp30_green.paa",
    "primary": 10,
    "recoil": [
        0,
        0,
        0,
        0.03,
        0.036943,
        0.0268696,
        0.09,
        0.019755,
        0.006112,
        0.12,
        0,
        0,
        0.18,
        -0.003138,
        -0.001,
        0.12,
        -0.001177,
        -0.000376,
        0.12,
        0,
        0
    ],
    "reloadaction": "GestureReloadPistol",
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
        "bullet1",
        0.083,
        "bullet2",
        0.083,
        "bullet3",
        0.083,
        "bullet4",
        0.083,
        "bullet5",
        0.083,
        "bullet6",
        0.083,
        "bullet7",
        0.083,
        "bullet8",
        0.083,
        "bullet9",
        0.083,
        "bullet10",
        0.083,
        "bullet11",
        0.083,
        "bullet12",
        0.083
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
    "sounds": [
        "StandardSound"
    ],
    "standardsound": {
        "begin1": [
            "A3/Sounds_F_Kart/Weapons/starting_pistol_1",
            1,
            1,
            700
        ],
        "begin2": [
            "A3/Sounds_F_Kart/Weapons/starting_pistol_2",
            1,
            1,
            700
        ],
        "begin3": [
            "A3/Sounds_F_Kart/Weapons/starting_pistol_3",
            1,
            1,
            700
        ],
        "closure1": [
            "",
            1.03514,
            1,
            10
        ],
        "closure2": [
            "",
            1.03514,
            1.1,
            10
        ],
        "soundbegin": [
            "begin1",
            0.33,
            "begin2",
            0.33,
            "begin3",
            0.34
        ],
        "soundclosure": [
            "closure1",
            0.5,
            "closure2",
            0.5
        ],
        "weaponsoundeffect": "DefaultRifle"
    },
    "swaydecayspeed": 2,
    "tbody": 100,
    "texturetype": "semi",
    "type": 2,
    "uipicture": "",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 2,
    "weaponinfotype": "rhs_rscOptics_rsp30",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponpoolavailable": 1,
    "weaponslotsinfo": {
        "holsterscale": 0,
        "mass": 10
    },
    "weaponsoundeffect": "",
    "weight": 0,
    "zeroingsound": [
        "",
        1,
        1
    ]
}