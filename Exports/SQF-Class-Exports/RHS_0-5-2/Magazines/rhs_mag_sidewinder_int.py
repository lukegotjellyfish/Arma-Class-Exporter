d = {
    "ammo": {
        "_dictAmmoName": "rhs_ammo_Sidewinder_AA",
        "access": 3,
        "afmax": 200,
        "aiammousageflags": 256,
        "airfriction": 0.14,
        "airlock": 2,
        "animated": 0,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "artillerylock": 0,
        "audiblefire": 32,
        "autoseektarget": 0,
        "caliber": 1,
        "cartridge": "",
        "cmimmunity": 0.96,
        "components": {
            "sensorsmanagercomponent": {
                "components": {
                    "irsensorcomponent": {
                        "aimdown": 0,
                        "airtarget": {
                            "maxrange": 8000,
                            "minrange": 500,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": 1
                        },
                        "allowsmarking": 1,
                        "anglerangehorizontal": 120,
                        "anglerangevertical": 120,
                        "animdirection": "",
                        "color": [
                            1,
                            0,
                            0,
                            1
                        ],
                        "componenttype": "IRSensorComponent",
                        "groundnoisedistancecoef": 0.03,
                        "groundtarget": {
                            "maxrange": 8000,
                            "minrange": 500,
                            "objectdistancelimitcoef": 1,
                            "viewdistancelimitcoef": 1
                        },
                        "maxfogseethrough": 0.8,
                        "maxgroundnoisedistance": -1,
                        "maxspeedthreshold": 0,
                        "maxtrackableatl": 10000000000.0,
                        "maxtrackablespeed": 555,
                        "minspeedthreshold": 0,
                        "mintrackableatl": 20,
                        "mintrackablespeed": -10000000000.0,
                        "typerecognitiondistance": -1
                    }
                }
            }
        },
        "cost": 1500,
        "cratereffects": "AAMissileCrater",
        "cratershape": "",
        "craterwatereffects": "ImpactEffectsWater",
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
        "deflecting": 0,
        "deflectionslowdown": 0.8,
        "directionalexplosion": 0,
        "effectflare": "FlareShell",
        "effectfly": "",
        "effectsfire": "CannonFire",
        "effectsmissile": "missile3",
        "effectsmissileinit": "PylonBackEffects",
        "effectssmoke": "SmokeShellWhite",
        "eventhandlers": {
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosioneffects": "AAMissileExplosion",
        "explosioneffectsdir": "explosionDir",
        "explosionforcecoef": 1,
        "explosionpos": "explosionPos",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 0,
        "explosiontype": "explosive",
        "explosive": 1,
        "fusedistance": 300,
        "grenadeburningsound": [],
        "grenadefiresound": [],
        "hit": 150,
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
            "hitwater": "ImpactEffectsSmall"
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
        "indirecthit": 90,
        "indirecthitrange": 14,
        "inittime": 0,
        "irlock": 1,
        "iscrateroriented": 0,
        "laserlock": 0,
        "lockseekradius": 100,
        "locktype": 0,
        "maneuvrability": 30,
        "manualcontrol": 0,
        "maverickweaponindexoffset": 0,
        "maxcontrolrange": 4500,
        "maxspeed": 1029,
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
        "missilekeeplockedcone": 180,
        "missilelockcone": 180,
        "missilelockmaxdistance": 8000,
        "missilelockmaxspeed": 555,
        "missilelockmindistance": 300,
        "model": "A3/Weapons_F_Jets/Ammo/Missile_AA_08_fly_F",
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
        "proximityexplosiondistance": 19,
        "proxyshape": "A3/Weapons_F_Jets/Ammo/Missile_AA_08_F",
        "shadow": 0,
        "shootdistraction": -1,
        "sideairfriction": 0.2,
        "simulation": "shotMissile",
        "simulationstep": 0.001,
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
            "A3/Sounds_F/weapons/Rockets/rocket_fly_1",
            0.562341,
            1,
            1500
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
        "soundsetexplosion": [
            "RocketsMedium_Exp_SoundSet",
            "RocketsMedium_Tail_SoundSet",
            "Explosion_Debris_SoundSet"
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
        "thrust": 390,
        "thrusttime": 3,
        "timetolive": 35,
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
        "tracklead": 0.75,
        "trackoversteer": 0.95,
        "typicalspeed": 900,
        "underwaterhitrangecoef": 1,
        "visiblefire": 32,
        "visiblefiretime": 20,
        "warheadname": "HE",
        "watereffectoffset": 0.45,
        "weaponlocksystem": "2 + 16",
        "weapontype": "Default",
        "whistledist": 20,
        "whistleonfire": 0
    },
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "Sidewinder, IR-homing",
    "displayname": "AIM-9X",
    "displaynamemfdformat": "%1 AIM-9X",
    "displaynameshort": "IR",
    "hardpoints": [
        "RHS_HP_AIM9_int"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 8,
    "maxleadspeed": 450,
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
                    "text": "MFD_PYLON_NAME",
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
        "rhs_f22_pylon": {
            "bones": {
                "center": {
                    "pos": [
                        0,
                        0
                    ],
                    "type": "fixed"
                }
            },
            "draw": {
                "default": {
                    "alpha": 0.22,
                    "color": [
                        0.15,
                        1,
                        0.15
                    ],
                    "condition": "PylonAmmoRelative>0",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                0,
                                0.02
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.015
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.03,
                                -0.015
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "M",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
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
                    "alpha": 1,
                    "background": {
                        "points": [
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.02,
                                        8.99271e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.74846e-09,
                                        0.0205729
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.02,
                                        -2.4533e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        3.49691e-09,
                                        -0.0205729
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
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
                            "Center",
                            1,
                            [
                                0,
                                0.02
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.015
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.03,
                                -0.015
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "M",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "selected": {
                    "alpha": 1,
                    "background": {
                        "points": [
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.02,
                                        8.99271e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.74846e-09,
                                        0.0205729
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.02,
                                        -2.4533e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "Center",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        3.49691e-09,
                                        -0.0205729
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0141421,
                                        -0.0145472
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0.15,
                        1,
                        0.15
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                0,
                                0.02
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.015
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.03,
                                -0.015
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "M",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0205729
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01732,
                                    -0.0102865
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01,
                                    -0.0178161
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0205729
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 4
                    }
                }
            },
            "material": {
                "ambient": [
                    3,
                    3,
                    3,
                    1
                ],
                "diffuse": [
                    10,
                    10,
                    10,
                    1
                ],
                "emissive": [
                    400,
                    200,
                    200,
                    1
                ]
            }
        }
    },
    "mindamageforcamshakehit": "rhs_ammo_Sidewinder_AA",
    "minthrowintensitycoef": 0.3,
    "model": "rhsusf/addons/rhsusf_airweapons/proxypylon/rhsusf_pylon_m_aim9_1x",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "pylonweapon": "rhs_weap_SidewinderLauncher",
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
    "weight": 0
}