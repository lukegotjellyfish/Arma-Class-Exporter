d = {
    "ammo": "M_Air_AA",
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "Short-range, infrared-guided, air-to-air missile with high-explosive warhead",
    "displayname": "ASRAAM",
    "displaynameshort": "AA SRange",
    "hardpoints": [
        "B_ASRAAM"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 88,
    "maxleadspeed": 694.444,
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
                        "text": "AA",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    0.0174929
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0553333,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.0526667,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.05,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.0446667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0393333,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0353333,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.03,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.026,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.022,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0166667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0126667,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.00866666,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.00733334,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.135442
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
                        "text": "AA",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    0.0174929
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0553333,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.0526667,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.05,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.0446667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0393333,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0353333,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.03,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.026,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.022,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0166667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0126667,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.00866666,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.00733334,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.135442
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
                        "text": "AA",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    0.0174929
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.0553333,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.0526667,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.05,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.0446667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0393333,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0353333,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.0313333,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.03,
                                    -0.025755
                                ],
                                1
                            ],
                            [
                                [
                                    0.026,
                                    -0.0244445
                                ],
                                1
                            ],
                            [
                                [
                                    0.022,
                                    -0.0231339
                                ],
                                1
                            ],
                            [
                                [
                                    0.0166667,
                                    -0.0205128
                                ],
                                1
                            ],
                            [
                                [
                                    0.0126667,
                                    -0.0178917
                                ],
                                1
                            ],
                            [
                                [
                                    0.00866666,
                                    -0.0126496
                                ],
                                1
                            ],
                            [
                                [
                                    0.00733334,
                                    -0.00609687
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.00176638
                                ],
                                1
                            ],
                            [
                                [
                                    0.00600001,
                                    0.135442
                                ],
                                1
                            ],
                            [
                                [
                                    0.0553333,
                                    0.135442
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 4
                    }
                }
            }
        }
    },
    "minthrowintensitycoef": 0.3,
    "model": "A3/Weapons_F/DynamicLoadout/PylonMissile_1x_Bomb_04_F.p3d",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "pylonweapon": "missiles_ASRAAM",
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
    "weight": 360
}