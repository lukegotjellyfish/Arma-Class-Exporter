d = {
    "access": 3,
    "afmax": 0,
    "aidispersioncoefx": 8,
    "aidispersioncoefy": 14,
    "aimtransitionspeed": 0.5,
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
    "baseweapon": "rhs_weap_pkm",
    "burst": 1,
    "cameradir": "eye_look",
    "candrop": 1,
    "canlock": 0,
    "canshootinwater": 0,
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
    "changefiremodesound": [
        "A3/sounds_f/weapons/closure/firemode_changer_2",
        0.562341,
        1,
        20
    ],
    "close": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 0.5,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 50,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 6,
        "burstrangemax": 12,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 50,
        "maxrangeprobab": 0.04,
        "midrange": 20,
        "midrangeprobab": 0.7,
        "minrange": 10,
        "minrangeprobab": 0.05,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "cmimmunity": 1,
    "count": 0,
    "cursor": "mg",
    "cursoraim": "EmptyCursor",
    "cursoraimon": "",
    "cursorsize": 1,
    "deployedpivot": "bipod",
    "descriptionshort": "Machine Gun<br/>Caliber: 7.62x54mmR",
    "detectrange": 0,
    "dexterity": 1,
    "discretedistance": [
        420,
        100,
        200,
        300,
        400,
        500,
        600,
        700,
        800,
        900,
        1000,
        1100,
        1200,
        1300,
        1400,
        1500
    ],
    "discretedistancecamerapoint": [
        "eye",
        "eye_100",
        "eye_200",
        "eye_300",
        "eye_400",
        "eye_500",
        "eye_600",
        "eye_700",
        "eye_800",
        "eye_900",
        "eye_1000",
        "eye_1100",
        "eye_1200",
        "eye_1300",
        "eye_1400",
        "eye_1500"
    ],
    "discretedistanceinitindex": 0,
    "dispersion": 0.00029,
    "displayname": "PKM",
    "distancezoommax": 300,
    "distancezoommin": 300,
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
        "rhs_pk_firedsoundhandler": {
            "fired": "_this params ['_unit','_weapon']; private _soundArray = ['RHS_rattle_pk_1','RHS_rattle_pk_2','RHS_rattle_pk_3','RHS_rattle_pk_4','RHS_rattle_pk_5','RHS_rattle_pk_6'];[_unit,_weapon,_soundArray,3] call RHS_fnc_beltRattle; private _sound = 'RHS_boltSnap_pk';[_unit,_weapon,_sound] call RHS_fnc_boltSnap"
        }
    },
    "far_optic1": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 10,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 1000,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 3,
        "burstrangemax": 6,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 650,
        "maxrangeprobab": 0.009,
        "midrange": 500,
        "midrangeprobab": 0.4,
        "minrange": 300,
        "minrangeprobab": 0.05,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": 1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "far_optic2": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 10,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 900,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 3,
        "burstrangemax": 6,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 900,
        "maxrangeprobab": 0.009,
        "midrange": 750,
        "midrangeprobab": 0.7,
        "minrange": 400,
        "minrangeprobab": 0.05,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": 2,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
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
    "fullauto": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 1e-06,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 500,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.00101,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 30,
        "maxrangeprobab": 0.1,
        "midrange": 15,
        "midrangeprobab": 0.7,
        "minrange": 0,
        "minrangeprobab": 0.9,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 1,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
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
        "rhs_barrelrefract": {
            "directionname": "usti hlavne up",
            "effectname": "RHS_BarrelRefract",
            "positionname": "usti hlavne"
        },
        "secondeffect": {
            "directionname": "Nabojniceend",
            "effectname": "CaselessAmmoCloud",
            "positionname": "Nabojnicestart"
        }
    },
    "handanim": [
        "OFP2_ManSkeleton",
        "/rhsafrf/addons/rhs_c_weapons/anims/pkm.rtm"
    ],
    "hasbipod": 1,
    "hiddenselections": [
        "camo"
    ],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_weapons/pkm/pkm_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "htmax": 600,
    "htmin": 1,
    "inertia": 0.85,
    "initspeed": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "irlaserend": "laser dir",
    "irlaserpos": "laser pos",
    "iteminfo": {
        "onhovertext": "TODO PKP DSS",
        "priority": 1,
        "rmbhint": "PKP"
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
    "magazinereloadswitchphase": 0.46,
    "magazinereloadtime": 0,
    "magazines": [
        "rhs_100rnd_762x54mmr",
        "rhs_100rnd_762x54mmr_green",
        "rhs_100rnd_762x54mmr_7n13",
        "rhs_100rnd_762x54mmr_7n26",
        "rhs_100rnd_762x54mmr_7bz3"
    ],
    "magazinewell": [
        "PK_762x54R"
    ],
    "manual": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 1e-06,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 500,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 1,
        "burstrangemax": -1,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 10,
        "maxrangeprobab": 0.04,
        "midrange": 5,
        "midrangeprobab": 0.7,
        "minrange": 0,
        "minrangeprobab": 0.3,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 1,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
    "maxleadspeed": 23,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "maxrecoilsway": 0.015,
    "maxzeroing": 1500,
    "medium": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 4,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 600,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 5,
        "burstrangemax": 9,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 500,
        "maxrangeprobab": 0.1,
        "midrange": 300,
        "midrangeprobab": 0.7,
        "minrange": 200,
        "minrangeprobab": 0.05,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
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
    "model": "rhsafrf/addons/rhs_weapons/pkm/pkm.p3d",
    "modelmagazine": "",
    "modeloptics": "-",
    "modelspecial": "",
    "modes": [
        "manual",
        "close",
        "short",
        "medium",
        "far_optic1",
        "far_optic2"
    ],
    "multiplier": 1,
    "muzzleend": "konec hlavne",
    "muzzlepos": "usti hlavne",
    "muzzles": [
        "this",
        "SAFE"
    ],
    "namesound": "Mgun",
    "optics": 0,
    "opticsdisableperipherialvision": 0.67,
    "opticsflare": 0,
    "opticsid": 0,
    "opticsppeffects": [],
    "opticszoominit": 0.75,
    "opticszoommax": 1,
    "opticszoommin": 0.25,
    "picture": "rhsafrf/addons/rhs_inventoryicons/data/weapons/rhs_weap_pkm_ca.paa",
    "primary": 10,
    "recoil": {
        "kickback": [
            0.02,
            0.08
        ],
        "muzzleinner": [
            0,
            0,
            0.1,
            0.1
        ],
        "muzzleouter": [
            0.5,
            1,
            0.7,
            0.3
        ],
        "permanent": 0.1,
        "temporary": 0.005
    },
    "recoilprone": [
        0,
        0,
        0,
        0.06,
        0.01,
        0.01,
        0.1,
        0,
        -0.02,
        0.1,
        -0.01,
        0.01,
        0.05,
        0,
        0
    ],
    "reloadaction": "GestureReloadM200",
    "reloadmagazinesound": [
        "rhsafrf/addons/rhs_sounds/pkp/reload",
        1.1,
        1,
        12
    ],
    "reloadsound": [
        "",
        1,
        1
    ],
    "reloadtime": 0.15,
    "rhs_1p29_type": "rhs_acc_1p29_pkp",
    "rhs_pgo7v2_type": "rhs_acc_pgo7v2_pkp",
    "rhs_pgo7v3_type": "rhs_acc_pgo7v3_pkp",
    "rhs_pgo7v_type": "rhs_acc_pgo7v_pkp",
    "rhs_pkas_type": "rhs_acc_pkas_pkp",
    "rhs_pso1m21_type": "rhs_acc_pso1m21_pkp",
    "rhs_pso1m2_type": "rhs_acc_pso1m2_pkp",
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
        "magazines": [],
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
        "recoil": {
            "kickback": [
                0.03,
                0.06
            ],
            "muzzleinner": [
                0,
                0,
                0.1,
                0.1
            ],
            "muzzleouter": [
                0.3,
                1,
                0.3,
                0.2
            ],
            "permanent": 0.1,
            "temporary": 0.01
        },
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.01,
            0.01,
            0.1,
            0,
            -0.02,
            0.1,
            -0.01,
            0.01,
            0.05,
            0,
            0
        ],
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
    "short": {
        "aiburstterminable": 1,
        "aidispersioncoefx": 2,
        "aidispersioncoefy": 3,
        "airateoffire": 2,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 300,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "autofire": 1,
        "burst": 6,
        "burstrangemax": 10,
        "canshootinwater": 0,
        "dispersion": 0.00093,
        "displayname": "Full",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 300,
        "maxrangeprobab": 0.04,
        "midrange": 150,
        "midrangeprobab": 0.7,
        "minrange": 50,
        "minrangeprobab": 0.05,
        "multiplier": 1,
        "recoil": [
            0,
            0,
            0,
            0.06,
            0.0443316,
            0.0243916,
            0.06,
            0.0477255,
            0.0105084,
            0.06,
            0.0335835,
            0.0073344,
            0.06,
            0.0140372,
            0.003192,
            0.03,
            -0.0007206,
            -0.002688,
            0.03,
            -0.001765,
            -0.00282,
            0.03,
            -0.0018385,
            -0.001764,
            0.06,
            0,
            0
        ],
        "recoilprone": [
            0,
            0,
            0,
            0.06,
            0.0110829,
            0.0021522,
            0.06,
            0.0095451,
            0.0007506,
            0.06,
            0.0059265,
            0.0004584,
            0.06,
            0.0022164,
            0.000171,
            0.06,
            0,
            0
        ],
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
        "soundend": [
            "sound",
            1
        ],
        "soundloop": [],
        "sounds": [
            "StandardSound"
        ],
        "standardsound": {
            "soundsetshot": [
                "RHS_pk_Shot_SoundSet",
                "RHS_rifle_med_Tail_SoundSet"
            ]
        },
        "texturetype": "fullAuto",
        "useaction": 0,
        "useactiontitle": "",
        "weaponsoundeffect": ""
    },
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
        "dispersion": 0.00101,
        "displayname": "Semi",
        "ffcount": 1,
        "fffrequency": 11,
        "ffmagnitude": 0.5,
        "flash": "gunfire",
        "flashsize": 0.1,
        "maxrange": 400,
        "maxrangeprobab": 0.01,
        "midrange": 200,
        "midrangeprobab": 0.01,
        "minrange": 2,
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
        "reloadtime": 0.092,
        "requiredoptictype": -1,
        "showtoplayer": 0,
        "silencedsound": {
            "soundsetshot": [
                "RHS_pkp_Closure_SoundSet",
                "RHS_pkp_Shot_SoundSet",
                "RHS_mmg1_Tail_SoundSet"
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
                "RHS_PK_Shot_SoundSet",
                "RHS_MMG1_Tail_SoundSet"
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
    "swaydecayspeed": 1.25,
    "tbody": 100,
    "texturetype": "default",
    "type": 1,
    "uipicture": "A3/weapons_f/data/UI/icon_mg_CA.paa",
    "useaction": 0,
    "useactiontitle": "",
    "useasbinocular": 0,
    "usemodeloptics": 1,
    "value": 4,
    "weaponinfotype": "rhs_rscOptics_pkm",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "weaponpoolavailable": 1,
    "weaponslotsinfo": {
        "allowedslots": [],
        "cowsslot": {
            "iconpicture": "A3/Weapons_F/Data/clear_empty.paa",
            "iconpinpoint": "Left",
            "iconposition": [
                0,
                0
            ],
            "iconscale": 1
        },
        "mass": 165,
        "muzzleslot": {
            "iconpicture": "A3/Weapons_F/Data/clear_empty.paa",
            "iconpinpoint": "Left",
            "iconposition": [
                0,
                0
            ],
            "iconscale": 1
        },
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
    "ww2_boltsnapdelay": 0.1,
    "ww2_boltsnapsound": "RHS_boltSnap_pk",
    "zeroingsound": [
        "A3/Sounds_F/arsenal/sfx/shared/zeroing_knob_tick_metal",
        0.316228,
        1,
        5
    ]
}