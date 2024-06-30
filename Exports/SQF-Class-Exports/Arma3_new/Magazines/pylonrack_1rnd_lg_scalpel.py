d = {
    "ammo": "M_Scalpel_AT",
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "Short-range, laser/infrared-guided, air-to-surface missile with tandem high-explosive anti-tank warhead",
    "displayname": "Scalpel",
    "displaynameshort": "AG",
    "hardpoints": [
        "B_MISSILE_PYLON",
        "SCALPEL_1RND_EJECTOR"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 110,
    "maxleadspeed": 100,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mfdelements": {
        "plane_cas_02": {
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
                "blackbackgroundgroup": {
                    "alpha": 1,
                    "blackbackground": {
                        "points": [
                            [
                                [
                                    [
                                        0.1,
                                        0.11
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.17,
                                        0.11
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.17,
                                        0.33
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.1,
                                        0.33
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
                "default": {
                    "alpha": 0.2,
                    "color": [
                        1,
                        1,
                        1
                    ],
                    "condition": "(PylonAmmoRelative>0.01) - PylonSelected",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                0.14,
                                0.301
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.14,
                                0.27
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.18,
                                0.27
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        0.1,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.34
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.1,
                                        0.34
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_scalpel_ca.paa",
                        "type": "polygon"
                    }
                },
                "empty": {
                    "alpha": 1,
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
                                0.14,
                                0.301
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.14,
                                0.27
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.18,
                                0.27
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        0.1,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.34
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.1,
                                        0.34
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_scalpel_ca.paa",
                        "type": "polygon"
                    }
                },
                "selected": {
                    "alpha": 1,
                    "color": [
                        0,
                        0.12,
                        0
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                0.14,
                                0.301
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.14,
                                0.27
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.18,
                                0.27
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    [
                                        0.1,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.1
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.18,
                                        0.34
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.1,
                                        0.34
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_scalpel_ca.paa",
                        "type": "polygon"
                    }
                }
            }
        }
    },
    "minthrowintensitycoef": 0.3,
    "model": "A3/Weapons_F/DynamicLoadout/PylonPod_1x_Missile_AA_04_F.p3d",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "pylonweapon": "missiles_SCALPEL",
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
    "weight": 400
}