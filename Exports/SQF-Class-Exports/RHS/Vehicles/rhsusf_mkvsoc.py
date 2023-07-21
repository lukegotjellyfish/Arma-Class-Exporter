d = {
    "_generalmacro": "Ship_F",
    "access": 0,
    "accuracy": 0.6,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [],
    "aircapacity": 10,
    "allowtablock": 1,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "attach_load_1": {
            "animperiod": 6,
            "initphase": 0,
            "source": "user"
        },
        "attach_load_2": {
            "animperiod": 6,
            "initphase": 0,
            "source": "user"
        },
        "attach_load_3": {
            "animperiod": 3,
            "initphase": 0,
            "source": "user"
        },
        "attach_load_4": {
            "animperiod": 6,
            "initphase": 0,
            "source": "user"
        },
        "beacons": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        },
        "c_displays_off_source": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "c_eng_ctrl_off_source": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "c_instr_off_source": {
            "animperiod": 0.001,
            "initphase": 0,
            "source": "user"
        },
        "m134_p_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M134"
        },
        "m134_p_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M134"
        },
        "m134_p_revolving_source": {
            "source": "revolving",
            "weapon": "RHS_MKV_M134"
        },
        "m2_p_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M2_p"
        },
        "m2_p_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M2_p"
        },
        "m2_p_reloadmagazine": {
            "source": "reloadMagazine",
            "weapon": "RHS_MKV_M2_p"
        },
        "m2_s_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M2_s"
        },
        "m2_s_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M2_s"
        },
        "m2_s_reloadmagazine": {
            "source": "reloadMagazine",
            "weapon": "RHS_MKV_M2_s"
        },
        "mk19_s_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_MK19"
        },
        "mk19_s_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_MK19"
        },
        "ml_pos_aft_source": {
            "markerlight": "mL_pos_aft",
            "source": "markerLight"
        },
        "ml_pos_port_source": {
            "markerlight": "mL_pos_port",
            "source": "markerLight"
        },
        "ml_pos_stbd_source": {
            "markerlight": "mL_pos_stbd",
            "source": "markerLight"
        },
        "rl_nav_source": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        },
        "rl_opr_source": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        },
        "rl_opt_source": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        },
        "rl_remspot_source": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 600,
    "armorcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_01",
        1.77828,
        1,
        200
    ],
    "armorcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_02",
        1.77828,
        1,
        200
    ],
    "armorcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_03",
        1.77828,
        1,
        200
    ],
    "armorcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_04",
        1.77828,
        1,
        200
    ],
    "armorlights": 0.4,
    "armorstructural": 1,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "CarAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_attachcargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Attach cargo",
            "expression": "if(_value == 1)then{[_this] spawn rhsusf_fnc_markvsoc_attachBoats};",
            "property": "rhs_attachCargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action"
        }
    },
    "audible": 4,
    "author": "Hatchet_AS",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 5,
    "buildcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_01",
        1.77828,
        1,
        200
    ],
    "buildcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_02",
        1.77828,
        1,
        200
    ],
    "buildcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_03",
        1.77828,
        1,
        200
    ],
    "buildcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_04",
        1.77828,
        1,
        200
    ],
    "cabinclosesound": [
        "",
        1,
        1
    ],
    "cabinclosesoundinternal": [
        "",
        1,
        1
    ],
    "cabinopensound": [
        "",
        1,
        1
    ],
    "cabinopensoundinternal": [
        "",
        1,
        1
    ],
    "camerasmoothspeed": 5,
    "camouflage": 3,
    "camshake": {
        "distance": 20,
        "frequency": 10,
        "minspeed": 5,
        "power": 10
    },
    "camshakecoef": 0,
    "camshakedamage": {
        "attenuation": 0.5,
        "distance": -1,
        "duration": 3,
        "frequency": 60,
        "minspeed": 1,
        "power": 0.5
    },
    "camshakegforce": {
        "distance": 0,
        "duration": 3,
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canbeshot": 1,
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_MKVSOC_Cargo01",
        "RHS_MKVSOC_Cargo02",
        "RHS_MKVSOC_Cargo03",
        "RHS_MKVSOC_Cargo04",
        "RHS_MKVSOC_Cargo05",
        "RHS_MKVSOC_Cargo06",
        "RHS_MKVSOC_Cargo07",
        "RHS_MKVSOC_Cargo08",
        "RHS_MKVSOC_Cargo09",
        "RHS_MKVSOC_Cargo010",
        "RHS_MKVSOC_Cargo011",
        "RHS_MKVSOC_Cargo012",
        "RHS_MKVSOC_Cargo013",
        "RHS_MKVSOC_Cargo014",
        "RHS_MKVSOC_Cargo015",
        "RHS_MKVSOC_Cargo016",
        "RHS_MKVSOC_Cargo017",
        "RHS_MKVSOC_Cargo018",
        "RHS_MKVSOC_Cargo019",
        "RHS_MKVSOC_Cargo020",
        "RHS_MKVSOC_Cargo021",
        "RHS_MKVSOC_Cargo022",
        "RHS_MKVSOC_Cargo023",
        "RHS_MKVSOC_Cargo024",
        "RHS_MKVSOC_Cargo025",
        "RHS_MKVSOC_Cargo026"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInLow"
    ],
    "cargogetoutaction": [
        "GetOutLow"
    ],
    "cargoiscodriver": [
        0
    ],
    "cargoprecisegetinout": [
        0
    ],
    "cargoproxyindexes": [],
    "cargospec": {
        "cargo1": {
            "showheadphones": 0
        }
    },
    "cargoturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 0,
        "disablesoundattenuation": 1,
        "dontcreateai": 1,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
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
        "gunend": "konec hlavne",
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
            "interval": 0.01,
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
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "cargo",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 0,
        "hitpoints": {},
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "ispersonturret": 1,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 45,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 95,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
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
            "interval": 0.02,
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
        "mincamelev": -90,
        "minelev": -45,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -95,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 1,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 0,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPCargo",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showascargo": 1,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 0,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 1,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "castcargoshadow": 1,
    "castdrivershadow": 1,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commanderaction": "RHS_MKVSOC_Commander",
    "commandercansee": "1+2+4+8+16",
    "commanderopticsmodel": "A3/weapons_f/reticle/Optics_Commander_02_F",
    "complexgearbox": {
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -7.625,
            "N",
            0,
            "D1",
            1.97
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            1
        ]
    },
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "activeradarsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 11000,
                        "minrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 20,
                    "animdirection": "",
                    "color": [
                        0,
                        1,
                        1,
                        1
                    ],
                    "componenttype": "ActiveRadarSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 11000,
                        "minrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxfogseethrough": 1,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 27.7778,
                    "maxtrackableatl": 100,
                    "maxtrackablespeed": 75,
                    "minspeedthreshold": 20.8333,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 4000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [
                        8000,
                        16000,
                        4000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "left": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        "vehiclesystemsdisplaymanagercomponentright": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [
                        8000,
                        16000,
                        4000
                    ],
                    "resource": "RscCustomInfoSensors"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "SensorDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 500000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_socom_swcc_officer",
    "crewcrashprotection": 0.1,
    "crewexplosionprotection": 0.5,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_markvsoc/data/mkvsoc_hull.rvmat",
            "rhsusf/addons/rhsusf_markvsoc/data/mkvsoc_hull_d.rvmat",
            "rhsusf/addons/rhsusf_markvsoc/data/rhs_destr_mkvsoc.rvmat",
            "rhsusf/addons/rhsusf_markvsoc/data/RHIB.rvmat",
            "rhsusf/addons/rhsusf_markvsoc/data/RHIB_d.rvmat",
            "rhsusf/addons/rhsusf_markvsoc/data/rhs_destr_mkvsoc.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "destrtype": "DestructDefault",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "Mk.V SOC",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "Slide"
    ],
    "driveraction": "RHS_MKVSOC_Driver",
    "drivercaneject": 1,
    "drivercansee": "1+2+8+16",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driveriscommander": 0,
    "driverlefthandanimname": "drv_hand_l",
    "driverleftleganimname": "drv_leg_l",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "drv_hand_r",
    "driverrightleganimname": "drv_leg_r",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/rhsusf_mkvsoc.paa",
    "editorsubcategory": "EdSubcat_Boats",
    "ejectdamagelimit": 0.9,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 0,
    "enableradio": 0,
    "enablewatch": 0,
    "engineeffectspeed": 1,
    "engineer": 0,
    "enginepower": 3908,
    "engineshifty": 1.125,
    "epeimpulsedamagecoef": 70,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_markvsoc_eh": {}
    },
    "exhausts": {
        "exhaust1": {
            "direction": "eng_1_exh_dir",
            "effect": "ExhaustsEffectBig",
            "position": "eng_1_exh"
        },
        "exhaust2": {
            "direction": "eng_2_exh_dir",
            "effect": "ExhaustsEffectBig",
            "position": "eng_2_exh"
        }
    },
    "explosionshielding": 4,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2.5,
        -25
    ],
    "faction": "rhs_faction_socom",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 20,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 1000,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 10,
    "fxexplo": {
        "access": 1
    },
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 10,
    "getoutaction": "GetOutLow",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunclouds": {
        "access": 0,
        "cloudletaccy": 0.4,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.3,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletgrowup": 1,
        "cloudletmaxyspeed": 0.8,
        "cloudletminyspeed": 0.2,
        "cloudletshape": "cloudletClouds",
        "cloudletsize": 1,
        "deltat": 0,
        "initt": 0,
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
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
        "interval": 0.01,
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
    "gunnercansee": "1+4+8+16",
    "gunnerhasflares": 0,
    "gunneriscommander": 0,
    "hascommander": 1,
    "hasdriver": 1,
    "hasgunner": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.015,
        0.015,
        0.02
    ],
    "headlimits": {
        "initanglex": 5,
        "initangley": 0,
        "maxanglex": 40,
        "maxangley": 90,
        "maxanglez": 45,
        "minanglex": -30,
        "minangley": -90,
        "minanglez": -45,
        "rotzradius": 0.2
    },
    "hiddenselections": [
        "camo1"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_markvsoc/data/hull_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponscommander": 1,
    "hideweaponsdriver": 1,
    "hideweaponsgunner": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 1,
            "material": 60,
            "name": "motor",
            "passthrough": 1,
            "visual": "motor"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/boat_f/Boat_Armed_01/data/ui/map_boat_armed_01.paa",
    "idlerpm": 600,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 16,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.75,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 1.7,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffect": "LDustEffects",
    "leftengineeffect": "LEngEffects",
    "leftfastwatereffect": "LFastWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "library": {
        "libtextdesc": "MKVLIB"
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8 + 4",
    "magazines": [],
    "mapsize": 22,
    "markerlights": {
        "ml_pos_aft": {
            "activelight": 0,
            "ambient": [
                0.08,
                0.08,
                0.08
            ],
            "blinking": 0,
            "color": [
                0.8,
                0.8,
                0.8
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.1,
            "drawlightsize": 1.2,
            "intensity": 100,
            "name": "mL_pos_aft",
            "useflare": 0
        },
        "ml_pos_port": {
            "activelight": 0,
            "ambient": [
                0.08,
                0,
                0
            ],
            "blinking": 0,
            "color": [
                0.8,
                0,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.1,
            "drawlightsize": 1.2,
            "intensity": 100,
            "name": "mL_pos_port",
            "useflare": 0
        },
        "ml_pos_stbd": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
                0
            ],
            "blinking": 0,
            "color": [
                0,
                0.8,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.1,
            "drawlightsize": 1.2,
            "intensity": 100,
            "name": "mL_pos_stbd",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 1,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 209.44,
    "maxspeed": 115,
    "memorypointcm": [
        "cm_port",
        "cm_stbd"
    ],
    "memorypointcmdir": [
        "cm_port_dir",
        "cm_stbd_dir"
    ],
    "memorypointcommondamage": "zamerny",
    "memorypointdriveroptics": [
        "driverview",
        "pilot"
    ],
    "memorypointexhaust": "eng_1_exh",
    "memorypointexhaustdir": "eng_1_exh_dir",
    "memorypointmissile": [
        "spice rakety",
        "usti hlavne"
    ],
    "memorypointmissiledir": [
        "konec rakety",
        "konec hlavne"
    ],
    "memorypointsgetincargo": "cargo_pos",
    "memorypointsgetincargodir": "cargo_dir",
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetincommander": "comm_pos",
    "memorypointsgetincommanderdir": "comm_dir",
    "memorypointsgetindriver": "driver_pos",
    "memorypointsgetindriverdir": "driver_dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetingunner": "gunner_pos",
    "memorypointsgetingunnerdir": "gunner_dir",
    "memorypointsleftengineeffect": "EngineEffectL",
    "memorypointsleftwatereffect": "waterEffectLeft",
    "memorypointsrightengineeffect": "EngineEffectR",
    "memorypointsrightwatereffect": "waterEffectRight",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 1,
    "mfd": {},
    "mfmax": 80,
    "mgunclouds": {
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
        "interval": 0.02,
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
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minspeed": -25,
    "mintotaldamagethreshold": 0.01,
    "model": "rhsusf/addons/rhsusf_markvsoc/mkvsoc.p3d",
    "namesound": "veh_ship_attackBoat_s",
    "newturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "mainTurret",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "mainTurret",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 1,
        "disablesoundattenuation": 0,
        "dontcreateai": 0,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "mainGun",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
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
        "gunend": "konec hlavne",
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
            "interval": 0.01,
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
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "Gunner",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 1,
        "hitpoints": {
            "hitgun": {
                "armor": 0.6,
                "explosionshielding": 1,
                "material": 52,
                "name": "gun",
                "passthrough": 1,
                "visual": "gun"
            },
            "hitturret": {
                "armor": 0.8,
                "explosionshielding": 1,
                "material": 51,
                "name": "turret",
                "passthrough": 1,
                "visual": "turret"
            }
        },
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 20,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 360,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
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
            "interval": 0.02,
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
        "mincamelev": -90,
        "minelev": -4,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -360,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 0,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 1,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPGunner",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 1,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "continuous": 0,
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "nightvision": 0,
    "normalspeedforwardcoef": 0.675,
    "numberphysicalwheels": 0,
    "nvgmarker": {
        "ambient": [
            1,
            1,
            1,
            1
        ],
        "blinking": 0,
        "brightness": 1,
        "diffuse": [
            1,
            1,
            1,
            1
        ],
        "onlyinnvg": 0
    },
    "nvgmarkers": {},
    "nvscanner": 0,
    "nvtarget": 0,
    "obstructsoundlfratio": 0,
    "obstructsoundswhenin": 0.562341,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 0,
    "overspeedbrakecoef": 0.01,
    "peaktorque": 16270,
    "periscopedepth": 2.8,
    "picture": "A3/boat_f/Boat_Armed_01/data/ui/Boat_Armed_01_base.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "pointcommander": "velitel",
    "pointpilot": "pilot",
    "portrait": "",
    "precisegetinout": 0,
    "precision": 80,
    "predictturnplan": 0.75,
    "predictturnsimul": 0.95,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.5,
    "radartype": 0,
    "redrpm": 2000,
    "reflectors": {
        "rl_nav": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0.1,
                "quadratic": 0,
                "start": 1
            },
            "color": [
                1900,
                1800,
                1700
            ],
            "conefadecoef": 3,
            "daylight": 0,
            "direction": "axis_rL_nav_dir",
            "flaremaxdistance": 350,
            "flaresize": 1,
            "hitpoint": "rL_nav_illum",
            "innerangle": 10,
            "intensity": 1500,
            "outerangle": 25,
            "position": "axis_rL_nav",
            "selection": "rL_nav_illum",
            "size": 5,
            "useflare": 1
        },
        "rl_opr_boom": {
            "ambient": [
                15,
                1,
                1
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 75,
                "hardlimitstart": 3,
                "linear": 1,
                "quadratic": 50,
                "start": 2
            },
            "blinking": 0,
            "color": [
                15000,
                100,
                100
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "axis_rL_opR_boom_dir",
            "flaremaxdistance": 20,
            "flaresize": 0.65,
            "hitpoint": "rL_op_red_illum",
            "innerangle": 45,
            "intensity": 3,
            "outerangle": 120,
            "position": "axis_rL_opR_boom_pos",
            "selection": "rL_op_red_illum",
            "size": 1,
            "useflare": 0
        },
        "rl_opr_cabin": {
            "ambient": [
                5,
                0,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                1800,
                0,
                0
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "axis_rL_opR_cabin_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "rL_op_red_illum",
            "innerangle": 90,
            "intensity": 11,
            "outerangle": 165,
            "position": "axis_rL_opR_cabin_pos",
            "selection": "rL_op_red_illum",
            "size": 1,
            "useflare": 1
        },
        "rl_opr_cabin2": {
            "ambient": [
                5,
                0,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                1800,
                0,
                0
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "axis_rL_opR_cabin2_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "rL_op_red_illum",
            "innerangle": 90,
            "intensity": 11,
            "outerangle": 165,
            "position": "axis_rL_opR_cabin2_pos",
            "selection": "rL_op_red_illum",
            "size": 1,
            "useflare": 1
        },
        "rl_opt_boom": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 150,
                "hardlimitstart": 25,
                "linear": 0.1,
                "quadratic": 0,
                "start": 1
            },
            "color": [
                1875,
                2475,
                2175
            ],
            "conefadecoef": 2,
            "daylight": 0,
            "direction": "axis_rL_opT_boom_dir",
            "flaremaxdistance": 250,
            "flaresize": 1,
            "hitpoint": "rL_op_teal_illum",
            "innerangle": 35,
            "intensity": 2,
            "outerangle": 90,
            "position": "axis_rL_opT_boom_pos",
            "selection": "rL_op_teal_illum",
            "size": 5,
            "useflare": 1
        },
        "rl_opt_cabin": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                1875,
                2475,
                2175
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "axis_rL_opT_cabin_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "rL_op_teal_illum",
            "innerangle": 90,
            "intensity": 1,
            "outerangle": 165,
            "position": "axis_rL_opT_cabin_pos",
            "selection": "rL_op_teal_illum",
            "size": 1,
            "useflare": 1
        },
        "rl_opt_cabin2": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                1875,
                2475,
                2175
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "axis_rL_opT_cabin2_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "rL_op_teal_illum",
            "innerangle": 90,
            "intensity": 1,
            "outerangle": 165,
            "position": "axis_rL_opT_cabin2_pos",
            "selection": "rL_op_teal_illum",
            "size": 1,
            "useflare": 1
        },
        "rl_rem_spot": {
            "ambient": [
                10,
                9,
                8
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 750,
                "hardlimitstart": 500,
                "linear": 0.1,
                "quadratic": 0,
                "start": 1
            },
            "color": [
                1900,
                1800,
                1700
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "axis_remSpot_dir",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "rL_remSpot_illum",
            "innerangle": 2,
            "intensity": 5000,
            "outerangle": 6,
            "position": "axis_remSpot_pos",
            "selection": "rL_remSpot_illum",
            "size": 5,
            "useflare": 1
        }
    },
    "rendertargets": {
        "cam_drv_bow": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "cameraview1": {
                "fov": 0.6,
                "pointdirection": "axis_cam_drv_bow_dir",
                "pointposition": "axis_cam_drv_bow_pos",
                "rendervisionmode": 1
            },
            "rendertarget": "rendertarget1"
        },
        "cam_drv_deck": {
            "bboxes": [
                "PIP_3_TL",
                "PIP_3_TR",
                "PIP_3_BL",
                "PIP_3_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "axis_cam_drv_deck_dir",
                "pointposition": "axis_cam_drv_deck_pos",
                "rendervisionmode": 0
            },
            "rendertarget": "rendertarget2"
        },
        "display_cam_cmdr": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "axis_camera_b_dir",
                "pointposition": "axis_camera_b_pos",
                "renderquality": 2,
                "rendervisionmode": 2
            },
            "rendertarget": "rendertarget0"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rightdusteffect": "RDustEffects",
    "rightengineeffect": "REngEffects",
    "rightfastwatereffect": "RFastWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "rudderforcecoef": 0.825,
    "rudderforcecoefatmaxspeed": 0.155,
    "safedepth": 2,
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionbrakelights": "brzdove svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 2,
    "sensitivityear": 0.0075,
    "shadow": 1,
    "shipsteercoef": 0.5,
    "showalltargets": 0,
    "showcrewaim": 0,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        1
    ],
    "shownvgcommander": 1,
    "shownvgdriver": 1,
    "shownvggunner": 1,
    "side": 1,
    "simulation": "shipx",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.275,
    "smokelauncherangle": 360,
    "smokelaunchergrenadecount": 8,
    "smokelauncheronturret": 0,
    "smokelaunchervelocity": 75,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.25,
        "ArmorCrash1",
        0.25,
        "ArmorCrash2",
        0.25,
        "ArmorCrash3",
        0.25
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "buildCrash0",
        0.25,
        "buildCrash1",
        0.25,
        "buildCrash2",
        0.25,
        "buildCrash3",
        0.25
    ],
    "soundburning": {},
    "soundbushcrash": [
        "emptySound",
        0
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "soundCrash",
        1
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "",
        1,
        1
    ],
    "sounddrown": {},
    "sounddrowning": {},
    "soundelevation": [
        "",
        0.00316228,
        0.5
    ],
    "soundengine": [
        "",
        1,
        1
    ],
    "soundengineoffext": [
        "",
        1,
        1
    ],
    "soundengineoffint": [
        "",
        1,
        1
    ],
    "soundengineonext": [
        "",
        1,
        1
    ],
    "soundengineonint": [
        "",
        1,
        1
    ],
    "soundenviron": [
        "",
        1,
        1
    ],
    "soundenvironext": {},
    "soundequipment": {},
    "soundevents": {},
    "soundflapsdown": [
        "",
        1,
        1
    ],
    "soundflapsup": [
        "",
        1,
        1
    ],
    "soundgear": [
        "",
        0.000177828,
        1
    ],
    "soundgeardown": [
        "",
        1,
        1
    ],
    "soundgearup": [
        "",
        1,
        1
    ],
    "soundgetin": [
        "",
        0.000316228,
        1
    ],
    "soundgetout": [
        "",
        0.000316228,
        1
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "",
        1,
        1
    ],
    "soundinjured": {},
    "soundlandcrash": [
        "",
        1,
        1
    ],
    "soundlandcrashes": [
        "soundLandCrash",
        1
    ],
    "soundlocked": [
        "",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "engine": {
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "sound": [
                "rhsusf/addons/rhsusf_markvsoc/data/Sound/engine_ext",
                1,
                1,
                350
            ],
            "volume": "engineOn*((rpm/ 2000) factor[(300/ 600),(2000/ 2000)])"
        },
        "enginemaxout": {
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "sound": [
                "rhsusf/addons/rhsusf_markvsoc/data/Sound/engine_rev",
                0.75,
                1,
                400
            ],
            "volume": "engineOn*((rpm/ 2000) factor[(1300/ 2000),(2000/ 2000)])"
        },
        "enginemidout": {
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "sound": [
                "rhsusf/addons/rhsusf_markvsoc/data/Sound/distance",
                1,
                1,
                800
            ],
            "volume": "engineOn*((rpm/ 2000) factor[(300/ 600),(2000/ 2000)])"
        },
        "idleout": {
            "frequency": "0.95 + ((rpm/ 2000) factor[(0/ 2000),(500/ 2000)])*0.5",
            "sound": [
                "rhsusf/addons/rhsusf_markvsoc/data/Sound/idle_ext",
                1,
                1,
                250
            ],
            "volume": "engineOn*(((rpm/ 2000) factor[(0/ 2000),(30/ 2000)]) * ((rpm/ 2000) factor[(500/ 2000),(300/ 2000)]))"
        },
        "scrublandext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/boat/noises/boat_land_on_shallow",
                1.77828,
                0.9,
                100
            ],
            "volume": "(scrubLand factor[0.01, 0.20])"
        },
        "waternoiseoutw0": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-0-speed1",
                0.707946,
                1,
                150
            ],
            "volume": "(speed factor[4, 1]) * water"
        },
        "waternoiseoutw1": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-20-speed",
                0.794328,
                1,
                250
            ],
            "volume": "((speed factor[2, 6]) min (speed factor[6, 4]))"
        },
        "waternoiseoutw2": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-50-speed",
                1,
                1,
                350
            ],
            "volume": "(speed factor[3, 9])"
        },
        "waternoiseoutw3": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-0-speed1",
                0.707946,
                1,
                150
            ],
            "volume": "(speed factor[-4, -1]) * water"
        },
        "waternoiseoutw4": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-20-speed",
                0.794328,
                0.9,
                250
            ],
            "volume": "((speed factor[-2, -6]) min (speed factor[-6, -4]))"
        },
        "waternoiseoutw5": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/boat/SFX/voda-o-bok-lodi-50-speed",
                1,
                0.9,
                350
            ],
            "volume": "(speed factor[-3, -9])"
        }
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundturnin": [
        "",
        0.000316228,
        1
    ],
    "soundturnininternal": [
        "",
        0.000316228,
        1
    ],
    "soundturnout": [
        "",
        0.000316228,
        1
    ],
    "soundturnoutinternal": [
        "",
        0.000316228,
        1
    ],
    "soundwatercrash": [
        "",
        0.177828,
        1
    ],
    "soundwatercrashes": [
        "soundWaterCrash",
        1
    ],
    "soundwoodcrash": [
        "woodCrash0",
        0.166,
        "woodCrash1",
        0.166,
        "woodCrash2",
        0.166,
        "woodCrash3",
        0.166,
        "woodCrash4",
        0.166,
        "woodCrash5",
        0.166
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_ship_attackBoat_p"
            ],
            "speechsingular": [
                "veh_ship_attackBoat_s"
            ]
        }
    },
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "squadtitles": {
        "color": [
            0,
            0,
            0,
            0.75
        ],
        "name": "clan_sign"
    },
    "steeraheadplan": 0.75,
    "steeraheadsimul": 0.95,
    "supplyradius": 0,
    "tbody": 150,
    "textplural": "attack boats",
    "textsingular": "attack boat",
    "texturelist": [],
    "texturesources": {
        "marsoc": {
            "author": "Red Hammer Studios",
            "displayname": "US",
            "textures": [
                "rhsusf/addons/rhsusf_markvsoc/data/hull_co.paa"
            ]
        }
    },
    "threat": [
        1,
        0.6,
        0.6
    ],
    "thrustdelay": 1.175,
    "torquecurve": [
        [
            0.3,
            0.850031
        ],
        [
            0.4,
            0.950031
        ],
        [
            0.5,
            1
        ],
        [
            0.6,
            0.950031
        ],
        [
            0.7,
            0.850031
        ],
        [
            0.8,
            0.650031
        ],
        [
            0.9,
            0.550031
        ],
        [
            1,
            0.410018
        ]
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportfuel": 0,
    "transportitems": {},
    "transportmagazines": {},
    "transportmaxbackpacks": 5,
    "transportmaxmagazines": 100,
    "transportmaxweapons": 10,
    "transportrepair": 0,
    "transportsoldier": 26,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 0.5,
    "turrets": {
        "camera_b_gunturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "camera_b_gunTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "camera_b_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "camera_b_gunTurret",
            "camera_b_viewgunner": {
                "initanglex": -15,
                "initangley": 0,
                "initfov": 0.9,
                "maxanglex": 45,
                "maxangley": 150,
                "maxfov": 0.9,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -45,
                "minangley": -150,
                "minfov": 0.42,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0,
                "visionmode": []
            },
            "camera_b_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.14,
                "maxanglex": 0,
                "maxangley": 180,
                "maxfov": 0.14,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": 0,
                "minangley": -180,
                "minfov": 0.0175,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0,
                "thermalmode": [
                    2,
                    3,
                    4
                ],
                "visionmode": [
                    "Normal",
                    "NVG",
                    "Ti"
                ]
            },
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                800,
                1000,
                1200,
                1500
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "camera_b_gun",
            "gunbeg": "axis_camera_b_dir",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "axis_camera_b_pos",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Commander",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "cmdr_hand_l",
            "gunnerleftleganimname": "cmdr_leg_l",
            "gunnername": "Commander",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/weapons_f_beta/reticle/reticle_SDV",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "cmdr_hand_r",
            "gunnerrightleganimname": "cmdr_leg_r",
            "gunnertype": "rhsusf_socom_swcc_officer",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 60,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "laser": 1,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [
                "Laserbatteries"
            ],
            "maxcamelev": 90,
            "maxelev": 60,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 180,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "axis_camera_b_pos",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "comm_pos",
            "memorypointsgetingunnerdir": "comm_dir",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -30,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -180,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 1,
            "proxyindex": 1,
            "proxytype": "CPCommander",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/Sounds_F/vehicles/armor/noises/servo_best",
                0.01,
                1,
                50
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 1,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "Laserdesignator_mounted"
            ]
        },
        "m134_p_gunturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "m134_p_gunTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "m134_p_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "m134_p_gunTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
                300
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 1,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "m134_p_gun",
            "gunbeg": "m134_p_beginBarrel",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "m134_p_endBarrel",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Gunner02",
            "gunnercompartments": "Compartment4",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "m134_p_hand_l",
            "gunnerleftleganimname": "m134_p_leg_l",
            "gunnername": "Port M134",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "a3/weapons_f/Reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "m134_p_hand_r",
            "gunnerrightleganimname": "m134_p_leg_r",
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun3": {
                    "armor": 0.6,
                    "material": 60,
                    "name": "m134_p_barrels",
                    "passthrough": 0,
                    "visual": "m134_p_gun"
                },
                "hitturret3": {
                    "armor": 0.8,
                    "material": 60,
                    "name": "m134_p_turret",
                    "passthrough": 0,
                    "visual": "m134_p_gunTurret"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 45,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 65,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m134_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m134_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [
                "2000Rnd_762x51_Belt_T_Red",
                "2000Rnd_762x51_Belt_T_Red"
            ],
            "maxcamelev": 90,
            "maxelev": 35,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 140,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "m134_p_sight",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "gunner_pos_m134",
            "memorypointsgetingunnerdir": "gunner_dir_m134",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 35,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 3,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/sounds_f/dummysound",
                0.00562341,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "RHS_MKV_M134"
            ]
        },
        "m2_s_gunturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "m2_s_gunTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "m2_s_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "m2_s_gunTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                800,
                1000,
                1200,
                1500
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 1,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "m2_s_gun",
            "gunbeg": "m2_s_beginBarrel",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "m2_s_endBarrel",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Gunner04",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "m2_s_hand_l",
            "gunnerleftleganimname": "m2_s_leg_l",
            "gunnername": "Stbd M2",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "a3/weapons_f/Reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "m2_s_hand_r",
            "gunnerrightleganimname": "m2_s_leg_r",
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun2": {
                    "armor": 0.6,
                    "isgun": 1,
                    "material": 60,
                    "name": "m2_s_barrels",
                    "passthrough": 0,
                    "visual": "-"
                },
                "hitturret2": {
                    "armor": 0.8,
                    "isturret": 1,
                    "material": 60,
                    "name": "m2_s_turret",
                    "passthrough": 0,
                    "visual": "-"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 45,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": -65,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red"
            ],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -5,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "m2_s_sight",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "gunner_pos_p_m2",
            "memorypointsgetingunnerdir": "gunner_dir_p_m2",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -145,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 2,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/sounds_f/dummysound",
                0.00562341,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "RHS_MKV_M2_s"
            ]
        },
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "mainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                800,
                1000,
                1200,
                1500
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 1,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mainGun",
            "gunbeg": "m2_p_beginBarrel",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "m2_p_endBarrel",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Gunner",
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "m2_p_hand_l",
            "gunnerleftleganimname": "m2_p_leg_l",
            "gunnername": "Port M2",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "a3/weapons_f/Reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "m2_p_hand_r",
            "gunnerrightleganimname": "m2_p_leg_r",
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun1": {
                    "armor": 0.6,
                    "isgun": 1,
                    "material": 60,
                    "name": "hit_gunBarrel_m2_1",
                    "passthrough": 0,
                    "visual": "gunBarrel_m2_1"
                },
                "hitturret1": {
                    "armor": 0.8,
                    "isturret": 1,
                    "material": 60,
                    "name": "hit_gunTurret_m2_1",
                    "passthrough": 0,
                    "visual": "gunTurret_m2_1"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 45,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 65,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red",
                "rhs_mag_100rnd_127x99_mag_Tracer_Red"
            ],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 145,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "m2_p_sight",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "gunner_pos_s_m2",
            "memorypointsgetingunnerdir": "gunner_dir_s_m2",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 5,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/sounds_f/dummysound",
                0.00562341,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "RHS_MKV_M2_p"
            ]
        },
        "mk19_s_gunturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "mk19_s_gunTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mk19_s_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "mk19_s_gunTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
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
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 1,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mk19_s_gun",
            "gunbeg": "mk19_s_beginBarrel",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "mk19_s_endBarrel",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Gunner03",
            "gunnercompartments": "Compartment5",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "mk19_s_hand_l",
            "gunnerleftleganimname": "mk19_s_leg_l",
            "gunnername": "Stbd Mk19",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "a3/weapons_f/Reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "mk19_s_hand_r",
            "gunnerrightleganimname": "mk19_s_leg_r",
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun4": {
                    "armor": 0.6,
                    "isgun": 1,
                    "material": 60,
                    "name": "m134_p_barrels",
                    "passthrough": 0,
                    "visual": "m134_p_gun"
                },
                "hitturret4": {
                    "armor": 0.8,
                    "isturret": 1,
                    "material": 60,
                    "name": "m134_p_turret",
                    "passthrough": 0,
                    "visual": "m134_p_gunTurret"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 45,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": -65,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [
                "RHS_48Rnd_40mm_MK19_M430A1",
                "RHS_48Rnd_40mm_MK19_M430A1",
                "RHS_48Rnd_40mm_MK19_M430A1",
                "RHS_48Rnd_40mm_MK19_M430A1"
            ],
            "maxcamelev": 90,
            "maxelev": 55,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -35,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "mk19_s_sight",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "gunner_pos_mk19",
            "memorypointsgetingunnerdir": "gunner_dir_mk19",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -137,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "mk19_s_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "mk19_s_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 4,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/sounds_f/dummysound",
                0.00562341,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": [
                "RHS_MKV_MK19"
            ]
        },
        "rem_spotl_gunturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "rem_spotL_gunTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "rem_spotL_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "rem_spotL_gunTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "disablesoundattenuation": 1,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                800,
                1000,
                1200,
                1500
            ],
            "discretedistanceinitindex": 2,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "rem_spotL_gun",
            "gunbeg": "axis_rem_spotL_dir",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
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
            "gunend": "axis_rem_spotL_pos",
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
                "interval": 0.01,
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
            "gunneraction": "RHS_MKVSOC_Commander02",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "m2_p_hand_l",
            "gunnerleftleganimname": "m2_p_leg_l",
            "gunnername": "Technician",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "a3/weapons_f/Reticle/optics_empty",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerreversedgetout": 0,
            "gunnerrighthandanimname": "m2_p_hand_r",
            "gunnerrightleganimname": "m2_p_leg_r",
            "gunnertype": "rhsusf_socom_swcc_officer",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 0,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "laser": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "m2_p_viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "m2_p_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 60,
            "maxhorizontalrotspeed": 1.8,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 145,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "rem_spotL_sight",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "gunner_pos",
            "memorypointsgetingunnerdir": "gunner_dir",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
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
                "interval": 0.02,
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
            "mincamelev": -90,
            "minelev": -7.5,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -145,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 2,
            "proxytype": "CPCommander",
            "reflectors": {},
            "rem_spotl_viewgunner": {
                "initanglex": -15,
                "initangley": 0,
                "initfov": 0.9,
                "maxanglex": 45,
                "maxangley": 150,
                "maxfov": 0.9,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -45,
                "minangley": -150,
                "minfov": 0.42,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0,
                "visionmode": []
            },
            "rem_spotl_viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.14,
                "maxanglex": 0,
                "maxangley": 150,
                "maxfov": 0.14,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": 0,
                "minangley": -150,
                "minfov": 0.0175,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0,
                "thermalmode": [],
                "visionmode": []
            },
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/Sounds_F/vehicles/armor/noises/servo_best",
                0.2,
                1,
                1
            ],
            "stabilizedinaxes": 4,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 0,
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": []
        }
    },
    "type": 1,
    "typicalcargo": [
        "rhsusf_socom_swcc_crewman",
        "rhsusf_socom_swcc_crewman",
        "rhsusf_socom_swcc_crewman",
        "rhsusf_socom_swcc_crewman"
    ],
    "uavhacker": 0,
    "unitinfotype": "UnitInfoShip",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "getondeck": {
            "animperiod": 2,
            "condition": "(getposasl (call rhsusf_fnc_findPlayer)) select 2 < -1",
            "displayname": "Get on deck",
            "onlyforplayer": 1,
            "position": "axis_ramp_roller",
            "priority": 11.008,
            "radius": 4,
            "statement": "[] spawn rhsusf_fnc_markvsoc_getIn",
            "useractionid": 74
        },
        "openloadmenu": {
            "animperiod": 2,
            "condition": "driver this == (call rhsusf_fnc_findPlayer)",
            "displayname": "<t color='#038D4A'>Open vehicle loading menu</t>",
            "onlyforplayer": 1,
            "position": "beacon_point",
            "priority": 10.008,
            "radius": 10,
            "statement": "[this] spawn rhsusf_fnc_markvsoc_loadMenuInit",
            "useractionid": 74
        },
        "openmenu": {
            "animperiod": 2,
            "condition": "driver this == (call rhsusf_fnc_findPlayer)",
            "displayname": "<t color='#FDDE00'>Open control panel</t>",
            "onlyforplayer": 1,
            "position": "beacon_point",
            "priority": 11.008,
            "radius": 10,
            "statement": "[this] call rhsusf_fnc_markvsoc_openMenu",
            "useractionid": 74
        }
    },
    "vehicleclass": "Ship",
    "verticalturncoef": 0.2,
    "viewcargo": {
        "initanglex": 5,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -75,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewcargoshadow": 1,
    "viewcargoshadowamb": 1,
    "viewcargoshadowdiff": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.35,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.07,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.9,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0.2,
        "maxmovey": 0.1,
        "maxmovez": 0.2,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": -0.2,
        "minmovey": -0.1,
        "minmovez": -0.1,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1.8,
    "waterangulardampingcoef": 1.125,
    "waterdamageengine": 0.2,
    "watereffectspeed": 10,
    "waterfasteffectspeed": 1,
    "waterleakiness": 95.5,
    "waterlineardampingcoefx": 1.15,
    "waterlineardampingcoefy": 1.65,
    "waterppinvehicle": 1,
    "waterresistance": 10,
    "waterresistancecoef": 0.0024,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "windsockexist": 0,
    "woodcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_01",
        1.77828,
        1,
        200
    ],
    "woodcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_02",
        1.77828,
        1,
        200
    ],
    "woodcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_03",
        1.77828,
        1,
        200
    ],
    "woodcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_04",
        1.77828,
        1,
        200
    ],
    "woodcrash4": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_05",
        1.77828,
        1,
        200
    ],
    "woodcrash5": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_06",
        1.77828,
        1,
        200
    ]
}