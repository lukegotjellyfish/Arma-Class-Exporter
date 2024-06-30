d = {
    "ammo": "M_Scalpel_AT",
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "Short-range, laser/infrared-guided, air-to-surface missile with tandem high-explosive anti-tank warhead",
    "displayname": "Scalpel",
    "displaynameshort": "AG",
    "hardpoints": [
        "SCALPEL_1RND",
        "UNI_SCALPEL"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 49,
    "maxleadspeed": 100,
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
                        "text": "AT",
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
                        "text": "AT",
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
                        "text": "AT",
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
        },
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
                        "text": "AT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    -0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    -0.0132582
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
                                        0.00636396,
                                        -0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.009,
                                        4.91753e-10
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.00636396,
                                        0.00795495
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
                                        0.00636396,
                                        0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -7.86805e-10,
                                        0.01125
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.00636396,
                                        0.00795495
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
                                        -0.00636396,
                                        0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.009,
                                        -1.34155e-10
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.00636396,
                                        -0.00795495
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
                                        -0.00636396,
                                        -0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        1.57361e-09,
                                        -0.01125
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.00636396,
                                        -0.00795495
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
                        "text": "AT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    -0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    -0.0132582
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
                                        0.00636396,
                                        -0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.009,
                                        4.91753e-10
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.00636396,
                                        0.00795495
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
                                        0.00636396,
                                        0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -7.86805e-10,
                                        0.01125
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.00636396,
                                        0.00795495
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
                                        -0.00636396,
                                        0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.009,
                                        -1.34155e-10
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        -0.00636396,
                                        -0.00795495
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
                                        -0.00636396,
                                        -0.00795495
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        1.57361e-09,
                                        -0.01125
                                    ],
                                    1
                                ],
                                [
                                    "R1",
                                    [
                                        0.00636396,
                                        -0.00795495
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
                        0.15,
                        1
                    ],
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
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
                        "text": "AT",
                        "type": "text"
                    },
                    "shape": {
                        "points": [
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.009,
                                    0
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.007794,
                                    -0.005625
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0045,
                                    -0.0097425
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    -0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    0.0132583
                                ],
                                1
                            ],
                            [],
                            [
                                "R1",
                                [
                                    -0.00636396,
                                    -0.00795495
                                ],
                                1
                            ],
                            [
                                "R1",
                                [
                                    -0.0106066,
                                    -0.0132582
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