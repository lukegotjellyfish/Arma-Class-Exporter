d = {
    "ammo": "Rocket_03_HE_F",
    "author": "Bohemia Interactive",
    "count": 20,
    "descriptionshort": "Unguided rockets with high-explosive warhead",
    "displayname": "Tratnyr 20x HE",
    "displaynameshort": "HE",
    "hardpoints": [
        "O_MISSILE_PYLON"
    ],
    "initspeed": 44,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 208,
    "maxleadspeed": 41.6667,
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
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_rocket_02_ca.paa",
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
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_rocket_02_ca.paa",
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
                        "texture": "a3/Weapons_F/MFD/UI/icon_place_cas_02_rocket_02_ca.paa",
                        "type": "polygon"
                    }
                }
            }
        },
        "vtol_02": {
            "bones": {
                "center": {
                    "pos": [
                        0,
                        0
                    ],
                    "type": "fixed"
                },
                "r1": {
                    "pos": [
                        0,
                        0.0125
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
                        0.15,
                        1
                    ],
                    "condition": "PylonAmmoRelative>0",
                    "pylonammo1": {
                        "align": "center",
                        "down": [
                            [
                                0,
                                0.028
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.027,
                                0
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                0,
                                -0.03
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.051
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.018,
                                -0.051
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
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 2
                    }
                },
                "empty": {
                    "alpha": 1,
                    "background": {
                        "points": [
                            [
                                [
                                    "R1",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.0169706,
                                        -0.0212132
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.024,
                                        1.31134e-09
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.0169706,
                                        0.0212132
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "R1",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.0169706,
                                        0.0212132
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -2.09815e-09,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.0169706,
                                        0.0212132
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "R1",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.0169706,
                                        0.0212132
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.024,
                                        -3.57746e-10
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.0169706,
                                        -0.0212132
                                    ],
                                    1
                                ]
                            ],
                            [
                                [
                                    "R1",
                                    1,
                                    [
                                        0,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.0169706,
                                        -0.0212132
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        4.19629e-09,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.0169706,
                                        -0.0212132
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
                    "pylonammo1": {
                        "align": "center",
                        "down": [
                            [
                                0,
                                0.028
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.027,
                                0
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                0,
                                -0.03
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.051
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.018,
                                -0.051
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
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 2
                    }
                },
                "selected": {
                    "alpha": 1,
                    "color": [
                        0.15,
                        1,
                        0.15,
                        1
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylonammo1": {
                        "align": "center",
                        "down": [
                            [
                                0,
                                0.028
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.027,
                                0
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "pylonammo",
                        "sourcescale": 1,
                        "type": "text"
                    },
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                0,
                                -0.03
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                0,
                                -0.051
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.018,
                                -0.051
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
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.024,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.020784,
                                    -0.015
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.012,
                                    -0.02598
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.03
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line",
                        "width": 2
                    }
                }
            }
        }
    },
    "minthrowintensitycoef": 0.3,
    "model": "A3/Weapons_F/DynamicLoadout/PylonPod_Rocket_01_F.p3d",
    "modelspecial": "",
    "muzzleend": "muzzleEnd",
    "muzzlepos": "muzzlePos",
    "namesound": "rockets",
    "picture": "",
    "pylonweapon": "Rocket_03_HE_Plane_CAS_02_F",
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