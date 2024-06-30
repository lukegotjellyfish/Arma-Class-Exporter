d = {
    "ammo": "BombCluster_02_cap_Ammo_F",
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "1100lb, laser-guided cluster bomb",
    "displayname": "RBK-500F Cluster x1",
    "displaynameshort": "Cluster Bomb",
    "hardpoints": [
        "O_BOMB_PYLON",
        "O_KAB250_BOMB"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 500,
    "maxleadspeed": 25,
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
                                        0.13
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.17,
                                        0.13
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.17,
                                        0.31
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.1,
                                        0.31
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
                        "texture": "a3/Weapons_F_Orange/MFD/UI/icon_place_cas_02_bombcluster_02_ca.paa",
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
                        "texture": "a3/Weapons_F_Orange/MFD/UI/icon_place_cas_02_bombcluster_02_ca.paa",
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
                        "texture": "a3/Weapons_F_Orange/MFD/UI/icon_place_cas_02_bombcluster_02_ca.paa",
                        "type": "polygon"
                    }
                }
            }
        },
        "plane_fighter_01": {
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
                        0,
                        0.12,
                        0
                    ],
                    "condition": "PylonAmmoRelative>0",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.015,
                                        6.44463e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        0.0104253
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
                                        0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.31134e-09,
                                        0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        0.0104253
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
                                        -0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.015,
                                        -1.75816e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        -0.0104253
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
                                        -0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        2.62268e-09,
                                        -0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        -0.0104253
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
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.015,
                                        6.44463e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        0.0104253
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
                                        0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.31134e-09,
                                        0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        0.0104253
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
                                        -0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.015,
                                        -1.75816e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        -0.0104253
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
                                        -0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        2.62268e-09,
                                        -0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0,
                        0.12,
                        0
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
        },
        "plane_fighter_02": {
            "bones": {},
            "draw": {
                "backgroundgroup": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.135,
                                        0.04
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.165,
                                        0.04
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.165,
                                        0.11
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.135,
                                        0.11
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
                    "alpha": 0.22,
                    "color": [
                        0.94,
                        0.83,
                        0
                    ],
                    "condition": "PylonAmmoRelative>0+PylonSelected",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.085
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.06
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.06
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "R",
                        "type": "text"
                    },
                    "pylontext2": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.105
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.08
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.08
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "B",
                        "type": "text"
                    },
                    "pylontext3": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.1
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.1
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "K",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.154,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.154,
                                    0.0418461
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.146,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.146,
                                    0.0418461
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
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
                                "0.00+0.15",
                                0.085
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.06
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.06
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "R",
                        "type": "text"
                    },
                    "pylontext2": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.105
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.08
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.08
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "B",
                        "type": "text"
                    },
                    "pylontext3": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.1
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.1
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "K",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.154,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.154,
                                    0.0418461
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.146,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.146,
                                    0.0418461
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
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
                                "0.00+0.15",
                                0.085
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.06
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.06
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "R",
                        "type": "text"
                    },
                    "pylontext2": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.105
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.08
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.08
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "B",
                        "type": "text"
                    },
                    "pylontext3": {
                        "align": "center",
                        "down": [
                            [
                                "0.00+0.15",
                                0.125
                            ],
                            1
                        ],
                        "pos": [
                            [
                                "0.00+0.15",
                                0.1
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.175,
                                0.1
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "K",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.16,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.14,
                                    0.110769
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.115692
                                ],
                                1
                            ],
                            [
                                [
                                    0.136,
                                    0.135385
                                ],
                                1
                            ],
                            [
                                [
                                    0.164,
                                    0.135385
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.154,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.154,
                                    0.0418461
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    0.146,
                                    0.0492308
                                ],
                                1
                            ],
                            [
                                [
                                    0.146,
                                    0.0418461
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                }
            }
        },
        "plane_fighter_04": {
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
                        0,
                        0.12,
                        0
                    ],
                    "condition": "PylonAmmoRelative>0",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.015,
                                        6.44463e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        0.0104253
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
                                        0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.31134e-09,
                                        0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        0.0104253
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
                                        -0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.015,
                                        -1.75816e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        -0.0104253
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
                                        -0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        2.62268e-09,
                                        -0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        -0.0104253
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
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.015,
                                        6.44463e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        0.0104253
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
                                        0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -1.31134e-09,
                                        0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        0.0104253
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
                                        -0.0106066,
                                        0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.015,
                                        -1.75816e-10
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        -0.0106066,
                                        -0.0104253
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
                                        -0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        2.62268e-09,
                                        -0.0147436
                                    ],
                                    1
                                ],
                                [
                                    "Center",
                                    [
                                        0.0106066,
                                        -0.0104253
                                    ],
                                    1
                                ]
                            ]
                        ],
                        "type": "polygon"
                    },
                    "color": [
                        0,
                        0.12,
                        0
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "pylontext1": {
                        "align": "center",
                        "down": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.065
                            ],
                            1
                        ],
                        "pos": [
                            "Center",
                            1,
                            [
                                -0.005,
                                0.02
                            ],
                            1
                        ],
                        "right": [
                            "Center",
                            1,
                            [
                                0.045,
                                0.02
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "CBU",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    0.0147436
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.015,
                                    0
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.01299,
                                    -0.00737179
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0075,
                                    -0.0127679
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0,
                                    -0.0147436
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    -0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    0.0208506
                                ],
                                1
                            ],
                            [],
                            [
                                "Center",
                                [
                                    -0.0106066,
                                    -0.0104253
                                ],
                                1
                            ],
                            [
                                "Center",
                                [
                                    -0.0212132,
                                    -0.0208506
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
    "model": "a3/Weapons_F_Orange/DynamicLoadout/PylonMissile_1x_BombCluster_02_F.p3d",
    "modelspecial": "",
    "namesound": "cannon",
    "picture": "",
    "pylonweapon": "BombCluster_02_F",
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