d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 8,
    "aidispersioncoefy": 10,
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
    "baseweapon": "rhs_weap_m38_rail",
    "bullet1": [
        "A3/sounds_f/weapons/shells/7_62/metal_762_01",
        0.630957,
        1,
        15
    ],
    "bullet10": [
        "A3/sounds_f/weapons/shells/7_62/grass_762_02",
        0.630957,
        1,
        15
    ],
    "bullet11": [
        "A3/sounds_f/weapons/shells/7_62/grass_762_03",
        0.630957,
        1,
        15
    ],
    "bullet12": [
        "A3/sounds_f/weapons/shells/7_62/grass_762_04",
        0.630957,
        1,
        15
    ],
    "bullet2": [
        "A3/sounds_f/weapons/shells/7_62/metal_762_02",
        0.630957,
        1,
        15
    ],
    "bullet3": [
        "A3/sounds_f/weapons/shells/7_62/metal_762_03",
        0.630957,
        1,
        15
    ],
    "bullet4": [
        "A3/sounds_f/weapons/shells/7_62/metal_762_04",
        0.630957,
        1,
        15
    ],
    "bullet5": [
        "A3/sounds_f/weapons/shells/7_62/dirt_762_01",
        0.630957,
        1,
        15
    ],
    "bullet6": [
        "A3/sounds_f/weapons/shells/7_62/dirt_762_02",
        0.630957,
        1,
        15
    ],
    "bullet7": [
        "A3/sounds_f/weapons/shells/7_62/dirt_762_03",
        0.630957,
        1,
        15
    ],
    "bullet8": [
        "A3/sounds_f/weapons/shells/7_62/dirt_762_04",
        0.630957,
        1,
        15
    ],
    "bullet9": [
        "A3/sounds_f/weapons/shells/7_62/grass_762_01",
        0.630957,
        1,
        15
    ],
    "burst": 1,
    "cameradir": "eye_look",
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
    "descriptionshort": "Bolt action Rifle<br/>Caliber: 7.62x54mm",
    "detectrange": 0,
    "dexterity": 1.8,
    "discretedistance": [
        100
    ],
    "discretedistancecamerapoint": [
        "eye"
    ],
    "discretedistanceinitindex": 0,
    "dispersion": 0.00029,
    "displayname": "Mosin Nagant M38 (Railed)",
    "distancezoommax": 300,
    "distancezoommin": 300,
    "dlc": "RHS_GREF",
    "drysound": [
        "A3/sounds_f/weapons/Other/dry_1",
        0.01,
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
            "fired": "[_this select 0,_this select 1,_this select 1] call rhs_fnc_boltAction;"
        }
    },
    "far_optic1": {
        "aidispersioncoefx": 1.4,
        "aidispersioncoefy": 1.7,
        "airateoffire": 3,
        "airateoffiredispersion": 3,
        "airateoffiredistance": 700,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 0,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.0005818,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 1000,
        "maxrangeprobab": 0.3,
        "midrange": 500,
        "midrangeprobab": 0.7,
        "minrange": 150,
        "minrangeprobab": 0.1,
        "multiplier": 1,
        "recoil": "recoil_single_primary_3outof10",
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "reloadtime": 1.6,
        "requiredoptictype": 1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHSUSF_sd_xm2010_Shot_SoundSet",
                "RHS_sd_mmg1_Tail_SoundSet"
            ]
        },
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
                "RHSGREF_nagant_Shot_SoundSet",
                "RHSGREF_rifle2_Tail_SoundSet"
            ]
        },
        "texturetype": "semi",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "far_optic2": {
        "aidispersioncoefx": 1.4,
        "aidispersioncoefy": 1.7,
        "airateoffire": 5,
        "airateoffiredispersion": 5,
        "airateoffiredistance": 2000,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 0,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.0005818,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 2000,
        "maxrangeprobab": 0.3,
        "midrange": 1050,
        "midrangeprobab": 0.7,
        "minrange": 500,
        "minrangeprobab": 0.1,
        "multiplier": 1,
        "recoil": "recoil_single_primary_3outof10",
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "reloadtime": 1.6,
        "requiredoptictype": 2,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHSUSF_sd_xm2010_Shot_SoundSet",
                "RHS_sd_mmg1_Tail_SoundSet"
            ]
        },
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
                "RHSGREF_nagant_Shot_SoundSet",
                "RHSGREF_rifle2_Tail_SoundSet"
            ]
        },
        "texturetype": "semi",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
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
        },
        "rhsusf_barrelrefract": {
            "directionname": "usti hlavne up",
            "effectname": "RHSUSF_BarrelRefract",
            "positionname": "usti hlavne"
        }
    },
    "handanim": [
        "OFP2_ManSkeleton",
        "/rhsgref/addons/rhsgref_c_weapons/anims/rhs_hand_m38.rtm"
    ],
    "hiddenselections": [
        "camo"
    ],
    "hiddenselectionstextures": [
        "rhsgref/addons/rhsgref_weapons/m38/data/m38_2_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 600,
    "htmin": 1,
    "inertia": 0.87,
    "initspeed": -0.96,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "irlaserend": "laser dir",
    "irlaserpos": "laser pos",
    "iteminfo": {
        "onhovertext": "m38",
        "priority": 1,
        "rmbhint": "m38"
    },
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
        "rhsgref_5rnd_762x54_m38"
    ],
    "magazinewell": [
        "CBA_762x54R_Mosin"
    ],
    "maxleadspeed": 23,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "maxrecoilsway": 0.0125,
    "maxzeroing": 1000,
    "medium_optic2": {
        "aidispersioncoefx": 1.4,
        "aidispersioncoefy": 1.7,
        "airateoffire": 4,
        "airateoffiredispersion": 3,
        "airateoffiredistance": 1000,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 0,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.0005818,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 1000,
        "maxrangeprobab": 0.3,
        "midrange": 750,
        "midrangeprobab": 0.7,
        "minrange": 250,
        "minrangeprobab": 0.1,
        "multiplier": 1,
        "recoil": "recoil_single_primary_3outof10",
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "reloadtime": 1.6,
        "requiredoptictype": 2,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHSUSF_sd_xm2010_Shot_SoundSet",
                "RHS_sd_mmg1_Tail_SoundSet"
            ]
        },
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
                "RHSGREF_nagant_Shot_SoundSet",
                "RHSGREF_rifle2_Tail_SoundSet"
            ]
        },
        "texturetype": "semi",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "memorypointcamera": "eye",
    "mfact": 1,
    "mfmax": 0,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "minrange": 1,
    "minrangeprobab": 0.3,
    "model": "rhsgref/addons/rhsgref_weapons/m38/m38_rail.p3d",
    "modelmagazine": "",
    "modeloptics": "-",
    "modelspecial": "",
    "modes": [
        "Single",
        "far_optic1",
        "medium_optic2",
        "far_optic2"
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
    "opticszoommax": 1.1,
    "opticszoommin": 0.275,
    "picture": "rhsgref/addons/rhsgref_inventoryicons/data/weapons/rhs_weap_m38_rail_ca.paa",
    "primary": 10,
    "recoil": "recoil_dmr_01",
    "recoilprone": "assaultRifleBase",
    "reloadaction": "RHS_GestureReloadM38",
    "reloadmagazinesound": [
        "/rhsgref/addons/rhsgref_weapons/kar98k/data/sounds/1903A1_reload_noscope",
        0.8,
        1,
        10
    ],
    "reloadsound": [
        "",
        1,
        1
    ],
    "reloadtime": 0.15,
    "rhs_boltactionanim": "RHS_GestureRechamberM38",
    "rhs_boltactionsound": [
        "rhsgref/addons/rhsgref_weapons/kar98k/data/sounds/kar98k_bolt.wss",
        1.42,
        1,
        20
    ],
    "scope": 2,
    "scopearsenal": 2,
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
        "dispersion": 0.0005818,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 400,
        "maxrangeprobab": 0.04,
        "midrange": 250,
        "midrangeprobab": 0.7,
        "minrange": 2,
        "minrangeprobab": 0.3,
        "multiplier": 1,
        "recoil": "recoil_single_primary_3outof10",
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "reloadtime": 1.6,
        "requiredoptictype": -1,
        "showtoplayer": 1,
        "silencedsound": {
            "soundsetshot": [
                "RHSUSF_sd_xm2010_Shot_SoundSet",
                "RHS_sd_mmg1_Tail_SoundSet"
            ]
        },
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
                "RHSGREF_nagant_Shot_SoundSet",
                "RHSGREF_rifle2_Tail_SoundSet"
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
    "swaydecayspeed": 1.25,
    "tbody": 100,
    "texturetype": "default",
    "type": 1,
    "uipicture": "",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 4,
    "weaponinfotype": "rhs_mosin_handler",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponpoolavailable": 1,
    "weaponslotsinfo": {
        "allowedslots": [
            901
        ],
        "cowsslot": {
            "compatibleitems": {
                "optic_aco": 1,
                "optic_aco_grn": 1,
                "optic_aco_grn_smg": 1,
                "optic_aco_smg": 1,
                "optic_ams": 1,
                "optic_ams_khk": 1,
                "optic_ams_snd": 1,
                "optic_arco": 1,
                "optic_arco_blk_f": 1,
                "optic_arco_ghex_f": 1,
                "optic_dms": 1,
                "optic_dms_ghex_f": 1,
                "optic_erco_blk_f": 1,
                "optic_erco_khk_f": 1,
                "optic_erco_snd_f": 1,
                "optic_hamr": 1,
                "optic_hamr_khk_f": 1,
                "optic_holosight": 1,
                "optic_holosight_blk_f": 1,
                "optic_holosight_khk_f": 1,
                "optic_holosight_smg": 1,
                "optic_holosight_smg_blk_f": 1,
                "optic_khs_blk": 1,
                "optic_khs_hex": 1,
                "optic_khs_old": 1,
                "optic_khs_tan": 1,
                "optic_lrps": 1,
                "optic_lrps_ghex_f": 1,
                "optic_lrps_tna_f": 1,
                "optic_mrco": 1,
                "optic_nightstalker": 1,
                "optic_nvs": 1,
                "optic_sos": 1,
                "optic_sos_khk_f": 1,
                "optic_tws": 1,
                "optic_tws_mg": 1,
                "rhs_acc_1p87": 1,
                "rhs_acc_dh520x56": 1,
                "rhs_acc_ekp8_18": 1,
                "rhs_acc_ekp8_18b": 1,
                "rhs_acc_ekp8_18c": 1,
                "rhs_acc_ekp8_18d": 1,
                "rhs_acc_okp7_picatinny": 1,
                "rhs_acc_rakurspm": 1,
                "rhsgref_acc_rx01_camo": 1,
                "rhsgref_acc_rx01_nofilter_camo": 1,
                "rhsusf_acc_acog": 1,
                "rhsusf_acc_acog2": 1,
                "rhsusf_acc_acog2_3d": 1,
                "rhsusf_acc_acog2_pip": 1,
                "rhsusf_acc_acog2_usmc": 1,
                "rhsusf_acc_acog2_usmc_3d": 1,
                "rhsusf_acc_acog2_usmc_pip": 1,
                "rhsusf_acc_acog3": 1,
                "rhsusf_acc_acog3_3d": 1,
                "rhsusf_acc_acog3_pip": 1,
                "rhsusf_acc_acog3_usmc": 1,
                "rhsusf_acc_acog3_usmc_3d": 1,
                "rhsusf_acc_acog3_usmc_pip": 1,
                "rhsusf_acc_acog_3d": 1,
                "rhsusf_acc_acog_d": 1,
                "rhsusf_acc_acog_d_3d": 1,
                "rhsusf_acc_acog_d_pip": 1,
                "rhsusf_acc_acog_mdo": 1,
                "rhsusf_acc_acog_pip": 1,
                "rhsusf_acc_acog_rmr": 1,
                "rhsusf_acc_acog_rmr_3d": 1,
                "rhsusf_acc_acog_rmr_pip": 1,
                "rhsusf_acc_acog_sa": 1,
                "rhsusf_acc_acog_sa_3d": 1,
                "rhsusf_acc_acog_sa_pip": 1,
                "rhsusf_acc_acog_usmc": 1,
                "rhsusf_acc_acog_usmc_3d": 1,
                "rhsusf_acc_acog_usmc_pip": 1,
                "rhsusf_acc_acog_wd": 1,
                "rhsusf_acc_acog_wd_3d": 1,
                "rhsusf_acc_acog_wd_pip": 1,
                "rhsusf_acc_anpas13gv1": 1,
                "rhsusf_acc_anpvs27": 1,
                "rhsusf_acc_compm4": 1,
                "rhsusf_acc_elcan": 1,
                "rhsusf_acc_elcan_3d": 1,
                "rhsusf_acc_elcan_ard": 1,
                "rhsusf_acc_elcan_ard_3d": 1,
                "rhsusf_acc_elcan_ard_pip": 1,
                "rhsusf_acc_elcan_pip": 1,
                "rhsusf_acc_eotech": 1,
                "rhsusf_acc_eotech_552": 1,
                "rhsusf_acc_eotech_552_d": 1,
                "rhsusf_acc_eotech_552_wd": 1,
                "rhsusf_acc_eotech_xps3": 1,
                "rhsusf_acc_g33_t1": 1,
                "rhsusf_acc_g33_t1_flip": 1,
                "rhsusf_acc_g33_xps3": 1,
                "rhsusf_acc_g33_xps3_flip": 1,
                "rhsusf_acc_g33_xps3_tan": 1,
                "rhsusf_acc_g33_xps3_tan_flip": 1,
                "rhsusf_acc_leupoldmk4": 1,
                "rhsusf_acc_leupoldmk4_2": 1,
                "rhsusf_acc_leupoldmk4_2_d": 1,
                "rhsusf_acc_leupoldmk4_2_mrds": 1,
                "rhsusf_acc_leupoldmk4_d": 1,
                "rhsusf_acc_leupoldmk4_wd": 1,
                "rhsusf_acc_m2a1": 1,
                "rhsusf_acc_m8541": 1,
                "rhsusf_acc_m8541_d": 1,
                "rhsusf_acc_m8541_low": 1,
                "rhsusf_acc_m8541_low_d": 1,
                "rhsusf_acc_m8541_low_wd": 1,
                "rhsusf_acc_m8541_mrds": 1,
                "rhsusf_acc_m8541_wd": 1,
                "rhsusf_acc_mrds": 1,
                "rhsusf_acc_mrds_c": 1,
                "rhsusf_acc_nxs_3515x50_md": 1,
                "rhsusf_acc_nxs_3515x50f1_h58": 1,
                "rhsusf_acc_nxs_3515x50f1_h58_sun": 1,
                "rhsusf_acc_nxs_3515x50f1_md": 1,
                "rhsusf_acc_nxs_3515x50f1_md_sun": 1,
                "rhsusf_acc_nxs_5522x56_md": 1,
                "rhsusf_acc_nxs_5522x56_md_sun": 1,
                "rhsusf_acc_premier": 1,
                "rhsusf_acc_premier_low": 1,
                "rhsusf_acc_premier_mrds": 1,
                "rhsusf_acc_rm05": 1,
                "rhsusf_acc_rx01": 1,
                "rhsusf_acc_rx01_nofilter": 1,
                "rhsusf_acc_rx01_nofilter_tan": 1,
                "rhsusf_acc_rx01_tan": 1,
                "rhsusf_acc_specterdr": 1,
                "rhsusf_acc_specterdr_3d": 1,
                "rhsusf_acc_specterdr_a": 1,
                "rhsusf_acc_specterdr_a_3d": 1,
                "rhsusf_acc_specterdr_cx": 1,
                "rhsusf_acc_specterdr_cx_3d": 1,
                "rhsusf_acc_specterdr_d": 1,
                "rhsusf_acc_specterdr_d_3d": 1,
                "rhsusf_acc_specterdr_od": 1,
                "rhsusf_acc_specterdr_od_3d": 1,
                "rhsusf_acc_specterdr_pvs27": 1,
                "rhsusf_acc_su230": 1,
                "rhsusf_acc_su230_3d": 1,
                "rhsusf_acc_su230_c": 1,
                "rhsusf_acc_su230_c_3d": 1,
                "rhsusf_acc_su230_mrds": 1,
                "rhsusf_acc_su230_mrds_3d": 1,
                "rhsusf_acc_su230_mrds_c": 1,
                "rhsusf_acc_su230_mrds_c_3d": 1,
                "rhsusf_acc_su230a": 1,
                "rhsusf_acc_su230a_3d": 1,
                "rhsusf_acc_su230a_c": 1,
                "rhsusf_acc_su230a_c_3d": 1,
                "rhsusf_acc_su230a_mrds": 1,
                "rhsusf_acc_su230a_mrds_3d": 1,
                "rhsusf_acc_su230a_mrds_c": 1,
                "rhsusf_acc_su230a_mrds_c_3d": 1,
                "rhsusf_acc_t1_high": 1,
                "rhsusf_acc_t1_low": 1
            },
            "displayname": "Optics Slot",
            "iconpicture": "A3/Weapons_F/Data/UI/attachment_top.paa",
            "iconpinpoint": "Center",
            "iconposition": [
                0.45,
                0.25
            ],
            "iconscale": 0.2,
            "linkproxy": "A3/data_f/proxies/weapon_slots/TOP"
        },
        "icon": "rhsgref/addons/rhsgref_weapons/icons/w_m382_inv_ca.paa",
        "mass": 74.8,
        "muzzleslot": {
            "iconpicture": "A3/Weapons_F/Data/UI/attachment_muzzle.paa",
            "iconpinpoint": "Center",
            "iconposition": [
                0,
                0.45
            ],
            "iconscale": 0.2
        },
        "pointerslot": {
            "iconpicture": "A3/Weapons_F/Data/UI/attachment_muzzle.paa",
            "iconpinpoint": "Center",
            "iconposition": [
                0,
                0.45
            ],
            "iconscale": 0.2
        },
        "underbarrelslot": {
            "iconpicture": "A3/Weapons_F/Data/UI/attachment_muzzle.paa",
            "iconpinpoint": "Center",
            "iconposition": [
                0,
                0.45
            ],
            "iconscale": 0.2
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