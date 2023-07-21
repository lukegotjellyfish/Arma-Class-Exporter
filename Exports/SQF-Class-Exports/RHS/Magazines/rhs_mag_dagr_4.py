d = {
    "ammo": {
        "_dictAmmoName": "RHS_Ammo_DAGR",
        "access": 3,
        "afmax": 200,
        "aiammousageflags": "64 + 128+512",
        "airfriction": 0.1,
        "airlock": 0,
        "animated": 0,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "artillerylock": 0,
        "audiblefire": 32,
        "autoseektarget": 1,
        "caliber": 1,
        "camshakeexplode": {
            "distance": 208.363,
            "duration": 2.2,
            "frequency": 20,
            "power": 24.4
        },
        "camshakefire": {
            "distance": 88.3629,
            "duration": 2.2,
            "frequency": 20,
            "power": 3.32346
        },
        "camshakehit": {
            "distance": 1,
            "duration": 0.6,
            "frequency": 20,
            "power": 122
        },
        "camshakeplayerfire": {
            "distance": 1,
            "duration": 0.1,
            "frequency": 20,
            "power": 2
        },
        "cartridge": "",
        "cmimmunity": 0.9,
        "components": {
            "sensorsmanagercomponent": {
                "components": {
                    "lasersensorcomponent": {
                        "aimdown": 0,
                        "airtarget": {
                            "maxrange": 5000,
                            "minrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "allowsmarking": 1,
                        "anglerangehorizontal": 14,
                        "anglerangevertical": 14,
                        "animdirection": "",
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "componenttype": "LaserSensorComponent",
                        "groundnoisedistancecoef": -1,
                        "groundtarget": {
                            "maxrange": 5000,
                            "minrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "maxfogseethrough": 0.3,
                        "maxgroundnoisedistance": 0,
                        "maxspeedthreshold": 0,
                        "maxtrackableatl": 10000000000.0,
                        "maxtrackablespeed": 55,
                        "minspeedthreshold": 0,
                        "mintrackableatl": -10000000000.0,
                        "mintrackablespeed": -10000000000.0,
                        "typerecognitiondistance": 0
                    }
                }
            }
        },
        "cost": 100,
        "cratereffects": "ATMissileCrater",
        "cratershape": "",
        "craterwatereffects": "ImpactEffectsWater",
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
        "deflecting": 0,
        "deflectionslowdown": 0.8,
        "direct": {},
        "directionalexplosion": 0,
        "effectflare": "FlareShell",
        "effectfly": "",
        "effectsfire": "CannonFire",
        "effectsmissile": "rhs_missile1",
        "effectsmissileinit": "MissileDAR1",
        "effectssmoke": "SmokeShellWhite",
        "eventhandlers": {
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosioneffects": "ATMissileExplosion",
        "explosioneffectsdir": "explosionDir",
        "explosionforcecoef": 1,
        "explosionpos": "explosionPos",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 0,
        "explosiontype": "explosive",
        "explosive": 1,
        "flightprofiles": [
            "Direct",
            "LoalDistance"
        ],
        "fusedistance": 50,
        "grenadeburningsound": [],
        "grenadefiresound": [],
        "hit": 220,
        "hitarmor": [
            "soundHit",
            1
        ],
        "hitbuilding": [
            "soundHit",
            1
        ],
        "hitconcrete": [
            "soundHit",
            1
        ],
        "hitdefault": [
            "soundHit",
            1
        ],
        "hiteffects": {
            "hitwater": "ImpactEffectsWaterRocket"
        },
        "hitfoliage": [
            "soundHit",
            1
        ],
        "hitglass": [
            "soundHit",
            1
        ],
        "hitglassarmored": [
            "soundHit",
            1
        ],
        "hitgroundhard": [
            "soundHit",
            1
        ],
        "hitgroundsoft": [
            "soundHit",
            1
        ],
        "hitiron": [
            "soundHit",
            1
        ],
        "hitman": [
            "soundHit",
            1
        ],
        "hitmetal": [
            "soundHit",
            1
        ],
        "hitmetalplate": [
            "soundHit",
            1
        ],
        "hitonwater": 0,
        "hitplastic": [
            "soundHit",
            1
        ],
        "hitrubber": [
            "soundHit",
            1
        ],
        "hittyre": [
            "soundHit",
            1
        ],
        "hitwater": [
            "soundHit",
            1
        ],
        "hitwood": [
            "soundHit",
            1
        ],
        "htmax": 1800,
        "htmin": 60,
        "icon": "",
        "impactarmor": [
            "soundImpact",
            1
        ],
        "impactbuilding": [
            "soundImpact",
            1
        ],
        "impactconcrete": [
            "soundImpact",
            1
        ],
        "impactdefault": [
            "soundImpact",
            1
        ],
        "impactfoliage": [
            "soundImpact",
            1
        ],
        "impactglass": [
            "soundImpact",
            1
        ],
        "impactglassarmored": [
            "soundImpact",
            1
        ],
        "impactgroundhard": [
            "soundImpact",
            1
        ],
        "impactgroundsoft": [
            "soundImpact",
            1
        ],
        "impactiron": [
            "soundImpact",
            1
        ],
        "impactman": [
            "soundImpact",
            1
        ],
        "impactmetal": [
            "soundImpact",
            1
        ],
        "impactmetalplate": [
            "soundImpact",
            1
        ],
        "impactplastic": [
            "soundImpact",
            1
        ],
        "impactrubber": [
            "soundImpact",
            1
        ],
        "impacttyre": [
            "soundImpact",
            1
        ],
        "impactwater": [
            "soundImpact",
            1
        ],
        "impactwood": [
            "soundImpact",
            1
        ],
        "indirecthit": 50,
        "indirecthitrange": 10,
        "inittime": 0.002,
        "irlock": 0,
        "iscrateroriented": 0,
        "laserlock": 1,
        "loaldistance": {
            "lockseekdistancefromparent": 200
        },
        "lockseekradius": 1000,
        "locktype": 0,
        "maneuvrability": 14,
        "manualcontrol": 1,
        "maverickweaponindexoffset": 80,
        "maxcontrolrange": 8000,
        "maxspeed": 720,
        "mfact": 0,
        "mfmax": 100,
        "mindamageforcamshakehit": 0.55,
        "mineboundingdist": 3,
        "mineboundingtime": 3,
        "minedivespeed": 1,
        "minefloating": -1,
        "mineinconspicuousness": 10,
        "minejumpeffects": "",
        "mineplacedist": 0.5,
        "minetrigger": "RangeTrigger",
        "minimumsafezone": 0.1,
        "mintimetolive": 0,
        "missilekeeplockedcone": 25,
        "missilelockcone": 25,
        "missilelockmaxdistance": 6000,
        "missilelockmaxspeed": 56,
        "missilelockmindistance": 1000,
        "model": "rhsusf/addons/rhsusf_airweapons/proxyammo/rhsusf_r_DAGR_fly",
        "multisoundhit": [
            "soundHit1",
            0.34,
            "soundHit2",
            0.33,
            "soundHit3",
            0.33
        ],
        "muzzleeffect": "",
        "nvgmarkers": {},
        "nvlock": 0,
        "proxyshape": "rhsusf/addons/rhsusf_airweapons/proxyammo/rhsusf_r_DAGR",
        "shadow": 0,
        "shootdistraction": -1,
        "sideairfriction": 0.3,
        "simulation": "shotMissile",
        "simulationstep": 0.01,
        "soundactivation": [],
        "sounddeactivation": [],
        "soundengine": [
            "",
            1,
            1,
            50
        ],
        "soundfakefall": [
            "soundFall",
            1
        ],
        "soundfall": [
            "",
            1,
            1
        ],
        "soundfly": [
            "",
            1,
            1,
            400
        ],
        "soundhit": [
            "",
            100,
            1
        ],
        "soundhit1": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_01",
            2.51189,
            1,
            2000
        ],
        "soundhit2": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_02",
            2.51189,
            1,
            2000
        ],
        "soundhit3": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_03",
            2.51189,
            1,
            2000
        ],
        "soundimpact": [
            "",
            1,
            1
        ],
        "soundtrigger": [],
        "submunitionammo": "",
        "supersoniccrackfar": [
            "A3/Sounds_F/weapons/Explosion/supersonic_crack_50meters",
            0.316228,
            1,
            50
        ],
        "supersoniccracknear": [
            "A3/Sounds_F/weapons/Explosion/supersonic_crack_close",
            0.398107,
            1,
            20
        ],
        "suppressionradiusbulletclose": -1,
        "suppressionradiushit": 30,
        "tbody": 0,
        "thrust": 825,
        "thrusttime": 1.57,
        "timetolive": 20,
        "tracercolor": [
            0.7,
            0.7,
            0.5,
            0.04
        ],
        "tracercolorr": [
            0.7,
            0.7,
            0.5,
            0.04
        ],
        "tracklead": 1,
        "trackoversteer": 1,
        "typicalspeed": 900,
        "underwaterhitrangecoef": 1,
        "visiblefire": 32,
        "visiblefiretime": 20,
        "watereffectoffset": 0.45,
        "weaponlocksystem": 4,
        "weapontype": "Default",
        "whistledist": 4,
        "whistleonfire": 0
    },
    "author": "Bohemia Interactive",
    "count": 4,
    "descriptionshort": "\u00d74 Laser-homing 70mm rockets",
    "displayname": "DAGR",
    "displaynameshort": "SALH",
    "hardpoints": [
        "RHS_HP_HELLFIRE_SINGLE",
        "RHS_HP_LONGBOW_SINGLE"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 8,
    "maxleadspeed": 41.6667,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mfdelements": {
        "rhs_a10a_ammoname": {
            "bones": {},
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "pylontext1": {
                    "align": "center",
                    "down": [
                        [
                            0.005,
                            0.105
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.005,
                            0.02
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.05,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "LG",
                    "type": "text"
                }
            }
        },
        "rhs_a10a_box": {
            "bones": {},
            "draw": {
                "alpha": 1,
                "color": [
                    0.15,
                    1,
                    0.15
                ],
                "default": {
                    "alpha": 0.22,
                    "color": [
                        0.15,
                        1,
                        0.15,
                        1
                    ],
                    "condition": "PylonAmmoRelative>=0.001",
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        -0.015,
                                        -0.04
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.015,
                                        -0.04
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.015,
                                        0.04
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.015,
                                        0.04
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon",
                        "width": 4
                    }
                },
                "empty": {
                    "alpha": 0.22,
                    "color": [
                        0.87,
                        0,
                        0
                    ],
                    "condition": "PylonAmmoRelative<=0",
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        0.02,
                                        0.05
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.05,
                                        0.05
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.05,
                                        0.13
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.02,
                                        0.13
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon",
                        "width": 4
                    }
                },
                "selected": {
                    "alpha": 0.22,
                    "color": [
                        0.15,
                        1,
                        0.15,
                        1
                    ],
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        -0.015,
                                        0.05
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.015,
                                        0.05
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.015,
                                        0.13
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.015,
                                        0.13
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon",
                        "width": 4
                    }
                }
            }
        },
        "rhs_a29_weap_mfd": {
            "bones": {},
            "draw": {
                "default": {
                    "backgroundgroup": {
                        "background": {
                            "points": [
                                [
                                    [
                                        [
                                            -0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0225,
                                            0.03
                                        ],
                                        1
                                    ]
                                ]
                            ],
                            "type": "polygon"
                        },
                        "color": [
                            0,
                            0,
                            0
                        ]
                    },
                    "color": [
                        0,
                        0.12,
                        0
                    ],
                    "condition": "PylonAmmoRelative>0",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                "0.03+-0.03",
                                0.005
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.03+-0.03",
                                -0.01
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.015,
                                -0.01
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "LG",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -1.86265e-09,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "empty": {
                    "backgroundgroup": {
                        "alpha": 0.1,
                        "background": {
                            "points": [
                                [
                                    [
                                        [
                                            -0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0225,
                                            0.03
                                        ],
                                        1
                                    ]
                                ]
                            ],
                            "type": "polygon"
                        },
                        "color": [
                            0.99,
                            0.94,
                            0.59
                        ]
                    },
                    "blacktext": {
                        "backgroundgroup": {
                            "background": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.0225,
                                                -0.06
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.0225,
                                                -0.06
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.0225,
                                                0.03
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.0225,
                                                0.03
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            },
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        "color": [
                            0,
                            0,
                            0
                        ],
                        "condition": "PylonAmmoRelative>0",
                        "pylontext1": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext2": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext3": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext4": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext5": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext6": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "shape": {
                            "points": [
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0225,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.02025,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.018,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.01575,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.01125,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.009,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.00675,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.00225,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -1.86265e-09,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.00225,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.00675,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.009,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.01125,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.01575,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.018,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.02025,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 4
                        }
                    },
                    "color": [
                        1,
                        0,
                        0,
                        1
                    ],
                    "condition": "PylonAmmoRelative <= 0",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                "0.03+-0.03",
                                0.005
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.03+-0.03",
                                -0.01
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.015,
                                -0.01
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "LG",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -1.86265e-09,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 8
                    }
                },
                "selected": {
                    "backgroundgroup": {
                        "alpha": 0.1,
                        "background": {
                            "points": [
                                [
                                    [
                                        [
                                            -0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            -0.06
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            0.0225,
                                            0.03
                                        ],
                                        1
                                    ],
                                    [
                                        [
                                            -0.0225,
                                            0.03
                                        ],
                                        1
                                    ]
                                ]
                            ],
                            "type": "polygon"
                        },
                        "color": [
                            0.99,
                            0.94,
                            0.59
                        ]
                    },
                    "blacktext": {
                        "backgroundgroup": {
                            "background": {
                                "points": [
                                    [
                                        [
                                            [
                                                -0.0225,
                                                -0.06
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.0225,
                                                -0.06
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                0.0225,
                                                0.03
                                            ],
                                            1
                                        ],
                                        [
                                            [
                                                -0.0225,
                                                0.03
                                            ],
                                            1
                                        ]
                                    ]
                                ],
                                "type": "polygon"
                            },
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        "color": [
                            0,
                            0,
                            0
                        ],
                        "condition": "PylonAmmoRelative>0",
                        "pylontext1": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext2": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext3": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext4": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext5": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "pylontext6": {
                            "align": "center",
                            "down": [
                                [
                                    "0.03+-0.03",
                                    0.005
                                ],
                                1
                            ],
                            "pos": [
                                [
                                    "0.03+-0.03",
                                    -0.01
                                ],
                                1
                            ],
                            "right": [
                                [
                                    0.015,
                                    -0.01
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "LG",
                            "type": "text"
                        },
                        "shape": {
                            "points": [
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0225,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.02025,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.018,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.01575,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.01125,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.009,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.00675,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        -0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.00225,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -1.86265e-09,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.00225,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        0.0045,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.00675,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.009,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.01125,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [],
                                [
                                    [
                                        0.0135,
                                        -0.06
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.01575,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.018,
                                        -0.0675
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.02025,
                                        -0.06625
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.0225,
                                        -0.06
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line",
                            "width": 4
                        }
                    },
                    "color": [
                        0.99,
                        0.94,
                        0.59
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                "0.03+-0.03",
                                0.005
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.03+-0.03",
                                -0.01
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.015,
                                -0.01
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "LG",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    0.03
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    -0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    -0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    -1.86265e-09,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.00225,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0045,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.00675,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.009,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.01125,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0135,
                                    -0.06
                                ],
                                1
                            ],
                            [
                                [
                                    0.01575,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.018,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                [
                                    0.02025,
                                    -0.06625
                                ],
                                1
                            ],
                            [
                                [
                                    0.0225,
                                    -0.06
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 8
                    }
                }
            }
        },
        "rhs_a29_weap_mfd_inventory": {
            "bones": {},
            "draw": {
                "pylonamo": {
                    "align": "left",
                    "down": [
                        [
                            0.16,
                            0.074
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.16,
                            0.054
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.185,
                            0.054
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "pylonammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "pylontext1": {
                    "align": "right",
                    "down": [
                        [
                            0,
                            0.04
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0,
                            0.02
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.025,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "DAGR",
                    "type": "text"
                },
                "pylontext2": {
                    "align": "right",
                    "down": [
                        [
                            0,
                            0.074
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0,
                            0.054
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.025,
                            0.054
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "LG",
                    "type": "text"
                }
            }
        },
        "rhs_ah64_ammoname": {
            "bones": {},
            "draw": {
                "condition": "pylonSelected",
                "pylonammo": {
                    "align": "center",
                    "down": [
                        [
                            0.015,
                            0.105
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.02
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.06,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "pylontext1": {
                    "align": "center",
                    "down": [
                        [
                            0.005,
                            0.105
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.005,
                            0.02
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.05,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "LG",
                    "type": "text"
                }
            }
        }
    },
    "mindamageforcamshakehit": "RHS_Ammo_DAGR",
    "minthrowintensitycoef": 0.3,
    "mirrormissilesindexes": [
        2,
        1,
        4,
        3
    ],
    "model": "rhsusf/addons/rhsusf_airweapons/proxypylon/rhsusf_pylon_r_DAGR_4x",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "pylonweapon": "RHS_weap_DAGR_Launcher",
    "quickreload": 0,
    "reloadaction": "",
    "scope": 2,
    "selectionfireanim": "zasleh",
    "simulation": "ProxyMagazines",
    "type": 0,
    "useaction": 0,
    "useactiontitle": "",
    "value": 1,
    "weaponpoolavailable": 0,
    "weight": 32
}