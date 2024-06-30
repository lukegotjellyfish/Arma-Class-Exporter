d = {
    "ammo": "M_AT",
    "author": "Bohemia Interactive",
    "count": 12,
    "descriptionshort": "Unguided rockets with high-explosive warhead",
    "displayname": "DAR",
    "displaynameshort": "HE",
    "hardpoints": [
        "B_MISSILE_PYLON",
        "DAR"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 140,
    "maxleadspeed": 41.6667,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mfdelements": {
        "heli_attack_01": {
            "bones": {},
            "draw": {
                "backgroundgroup": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        -0.005,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.065,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.065,
                                        0.15
                                    ],
                                    1
                                ],
                                [
                                    [
                                        -0.005,
                                        0.15
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
                    "ammo": {
                        "align": "center",
                        "down": [
                            [
                                0.03,
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.09
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                0.09
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "PylonAmmo",
                        "sourceindex": 1,
                        "sourcescale": 1,
                        "type": "text"
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
                                0.03,
                                0.075
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.05
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.06,
                                0.05
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "RKT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "empty": {
                    "ammo": {
                        "align": "center",
                        "down": [
                            [
                                0.03,
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.09
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                0.09
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourceindex": 1,
                        "sourcescale": 1,
                        "text": "-",
                        "type": "text"
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
                                0.03,
                                0.075
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.05
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.06,
                                0.05
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "RKT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "selected": {
                    "ammo": {
                        "align": "center",
                        "down": [
                            [
                                0.03,
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.09
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                0.09
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "PylonAmmo",
                        "sourceindex": 1,
                        "sourcescale": 1,
                        "type": "text"
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
                                0.03,
                                0.075
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                0.05
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.06,
                                0.05
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "RKT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                [
                                    0.065,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    0.15
                                ],
                                1
                            ],
                            [
                                [
                                    -0.005,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                }
            }
        }
    },
    "minthrowintensitycoef": 0.3,
    "model": "A3/Weapons_F/DynamicLoadout/PylonPod_12x_Rocket_DAR_F.p3d",
    "modelspecial": "",
    "muzzleend": "muzzleEnd",
    "muzzlepos": "muzzlePos",
    "namesound": "rockets",
    "picture": "",
    "pylonweapon": "missiles_DAR",
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
    "weight": 144
}