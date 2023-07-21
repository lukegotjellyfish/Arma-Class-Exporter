d = {
    "_generalmacro": "UAV_06_base_F",
    "_mainbladecenter": "rotor_center",
    "access": 0,
    "accuracy": 1.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "airbrakefrictioncoef": 3,
    "aircapacity": 10,
    "airfrictioncoefs0": [
        0,
        0,
        0
    ],
    "airfrictioncoefs1": [
        0.1,
        0.05,
        0.006
    ],
    "airfrictioncoefs2": [
        0.001,
        0.0005,
        6e-05
    ],
    "allowtablock": 1,
    "altfullforce": 1000,
    "altnoforce": 2000,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "antimine_drone": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "inventory_door": {
            "animperiod": 1.1,
            "displayname": "Open cargo case",
            "onphasechanged": "(_this select 0) animateDoor ['Inventory_door',_this select 1,is3den]",
            "scope": 0,
            "source": "door"
        },
        "leaflet_door": {
            "animperiod": 0.25,
            "source": "user"
        },
        "led_lights_hide": {
            "animperiod": 0,
            "displayname": "Hide beacon lights",
            "initphase": 1,
            "mass": -7,
            "onphasechanged": "(_this select 0) animateSource ['LED_lights_hide',(_this select 1),true];",
            "source": "user"
        },
        "lights_em_hide": {
            "animperiod": 0.0001,
            "displayname": "Start beacon lights",
            "initphase": 0,
            "onphasechanged": "(_this select 0) animateSource ['lights_em_hide',(_this select 1),true];",
            "source": "user"
        },
        "utility_drone": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 0.5,
    "armorcrash1": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_01",
        0.446684,
        1,
        50
    ],
    "armorcrash2": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_02",
        0.398107,
        1,
        50
    ],
    "armorcrash3": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_03",
        0.446684,
        1,
        50
    ],
    "armorcrash4": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_04",
        0.421696,
        1,
        50
    ],
    "armorlights": 0.4,
    "armorstructural": 4,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "OpenHeliAttenuation",
    "attributes": {
        "firearearestricted": {
            "control": "Checkbox",
            "defaultvalue": "false",
            "displayname": "Restrict Fire",
            "expression": "\t\t\t\t\t_this setVariable ['BIS_FireAreaRestricted',_value,true];\t\t\t\t\t_this spawn {\t\t\t\t\t\t_this setVariable ['BIS_FireAreaRestricted_Triggers',synchronizedobjects _this select {_x iskindof 'EmptyDetector'},true];\t\t\t\t\t};\t\t\t\t",
            "property": "C_IDAP_UAV_06_antimine_F_FireAreaRestricted",
            "tooltip": "Restrict dropping demining bombs only to areas defined by triggers synchronized to the vehicle."
        }
    },
    "audible": 0.1,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "backrotorforcecoef": 4.5,
    "backrotorspeed": 7,
    "bodyfrictioncoef": 0.58,
    "brakedistance": 200,
    "buildcrash1": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_01",
        0.398107,
        1,
        50
    ],
    "buildcrash2": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_02",
        0.446684,
        1,
        50
    ],
    "buildcrash3": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_03",
        0.421696,
        1,
        50
    ],
    "buildcrash4": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_04",
        0.446684,
        1,
        50
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
    "camouflage": 0.5,
    "camshake": {
        "distance": 50,
        "frequency": 20,
        "minspeed": 50,
        "power": 30
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
        "frequency": 3,
        "minspeed": 1,
        "power": 0.2
    },
    "canaccessminedetector": 1,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment2"
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
            "showheadphones": 1
        },
        "cargo2": {
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
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "transportcountermeasurescomponent": {},
        "transportpylonscomponent": {
            "pylons": {
                "pylons1": {
                    "attachment": "PylonRack_4Rnd_BombDemine_01_F",
                    "bay": -1,
                    "hardpoints": [
                        "ANTIMINE_DRONE_PYLON"
                    ],
                    "maxweight": 15,
                    "mirroredmissilepos": 0,
                    "priority": 1,
                    "turret": [],
                    "uiposition": [
                        0.32,
                        0.28
                    ]
                }
            },
            "uipicture": "a3/Air_F_Orange/UAV_06/Data/UI/UAV_06_Demining_3DEN_CA.paa"
        },
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent",
                    "range": 50,
                    "resource": "RscCustomInfoMineDetect"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
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
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent",
                    "range": 50,
                    "resource": "RscCustomInfoMineDetect"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 20000,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crash1": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_01",
        0.446684,
        1,
        50
    ],
    "crash2": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_02",
        0.421696,
        1,
        50
    ],
    "crash3": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_03",
        0.446684,
        1,
        50
    ],
    "crash4": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_DemineDrone_Collission_04",
        0.398107,
        1,
        50
    ],
    "crew": "C_man_pilot_F",
    "crewcrashprotection": 0.25,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "cyclicasideforcecoef": 2.75,
    "cyclicforwardforcecoef": 0.59,
    "damage": {
        "mat": [
            "A3/Air_F_Orange/UAV_06/Data/UAV_06_super.rvmat",
            "A3/Drones_F/Air_F_Gamma/UAV_02/Data/UAV_02_damage.rvmat",
            "A3/Drones_F/Air_F_Gamma/UAV_02/Data/UAV_02_destruct.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "UAVDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0.5,
    "dammagefull": [],
    "dammagehalf": [],
    "destrtype": "DestructDefault",
    "destructioneffects": {},
    "detectskill": 20,
    "disableinventory": 1,
    "displayname": "Helicopter",
    "dlc": "Orange",
    "driveraction": "",
    "drivercaneject": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment3",
    "driverdoor": "",
    "driverforceoptics": 1,
    "driverinaction": "",
    "driverlefthandanimname": "lever_pilot",
    "driverleftleganimname": "pedalL",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "a3/Weapons_F_Orange/Reticle/UAV_06_driver_F.p3d",
    "driverrighthandanimname": "stick_pilot",
    "driverrightleganimname": "pedalR",
    "driverweaponsinfotype": "RscOptics_UAV_06_TGP",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dusteffect": "UAVDust",
    "dusteffects": {
        "both": {},
        "left": {
            "default": [
                "LDustEffectsAir"
            ],
            "gdtasphalt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtcliff": [
                "LDustEffectsAir"
            ],
            "gdtconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdead": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdesert1": [
                "LDustEffectsAir",
                "LSandEffects",
                "LDirtEffects",
                "LStonesEffects"
            ],
            "gdtdesert2": [
                "LDustEffectsAir",
                "LSandEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtfield": [
                "LDustEffectsAir"
            ],
            "gdtforest": [
                "LDustEffectsAir"
            ],
            "gdtgrassdry": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtgrassshort": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasstall": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasswild": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtkldirt": [
                "LDustEffectsAir"
            ],
            "gdtklforestcon": [
                "LDustEffectsAir"
            ],
            "gdtklforestdec": [
                "LDustEffectsAir"
            ],
            "gdtklgrass1": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklgrass2": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklmud": [
                "LDustEffectsAir"
            ],
            "gdtklsoil": [
                "LDustEffectsAir"
            ],
            "gdtklstones": [
                "LDustEffectsAir"
            ],
            "gdtklstubble": [
                "LDustEffectsAir"
            ],
            "gdtkltarmac": [
                "LDustEffectsAir"
            ],
            "gdtreddirt": [
                "LDustEffectsAirRed"
            ],
            "gdtrock": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtrubble": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtseabed": [
                "LDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "LDustEffectsAir"
            ],
            "gdtsoil": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstony": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonygreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonythistle": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtthorn": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtvolcano": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtvolcanobeach": [
                "LDustEffectsAir"
            ],
            "gdtweed1": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtweed2": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtwildfield": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "surfintconcrete": [
                "LDustEffectsAir"
            ],
            "surfintmetal": [
                "LDustEffectsAir"
            ],
            "surfinttiles": [
                "LDustEffectsAir"
            ],
            "surfintwood": [
                "LDustEffectsAir"
            ],
            "surfmetal": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "LDustEffectsAir"
            ],
            "surfroaddirt": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "LDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "LDustEffectsAir"
            ],
            "surfrooftiles": [
                "LDustEffectsAir"
            ],
            "surfrooftin": [
                "LDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfwood": [
                "LDustEffectsAir"
            ]
        },
        "right": {
            "default": [
                "RDustEffectsAir"
            ],
            "gdtasphalt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtcliff": [
                "RDustEffectsAir"
            ],
            "gdtconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdead": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdesert1": [
                "RDustEffectsAir",
                "RSandEffects",
                "RDirtEffects",
                "RStonesEffects"
            ],
            "gdtdesert2": [
                "RDustEffectsAir",
                "RSandEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtfield": [
                "RDustEffectsAir"
            ],
            "gdtforest": [
                "RDustEffectsAir"
            ],
            "gdtgrassdry": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtgrassshort": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasstall": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasswild": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtkldirt": [
                "RDustEffectsAir"
            ],
            "gdtklforestcon": [
                "RDustEffectsAir"
            ],
            "gdtklforestdec": [
                "RDustEffectsAir"
            ],
            "gdtklgrass1": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklgrass2": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklmud": [
                "RDustEffectsAir"
            ],
            "gdtklsoil": [
                "RDustEffectsAir"
            ],
            "gdtklstones": [
                "RDustEffectsAir"
            ],
            "gdtklstubble": [
                "RDustEffectsAir"
            ],
            "gdtkltarmac": [
                "RDustEffectsAir"
            ],
            "gdtreddirt": [
                "RDustEffectsAirRed"
            ],
            "gdtrock": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtrubble": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtseabed": [
                "RDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "RDustEffectsAir"
            ],
            "gdtsoil": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstony": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonygreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonythistle": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtthorn": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtvolcano": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtvolcanobeach": [
                "RDustEffectsAir"
            ],
            "gdtweed1": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtweed2": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtwildfield": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "surfintconcrete": [
                "RDustEffectsAir"
            ],
            "surfintmetal": [
                "RDustEffectsAir"
            ],
            "surfinttiles": [
                "RDustEffectsAir"
            ],
            "surfintwood": [
                "RDustEffectsAir"
            ],
            "surfmetal": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "RDustEffectsAir"
            ],
            "surfroaddirt": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "RDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "RDustEffectsAir"
            ],
            "surfrooftiles": [
                "RDustEffectsAir"
            ],
            "surfrooftin": [
                "RDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfwood": [
                "RDustEffectsAir"
            ]
        }
    },
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorsubcategory": "EdSubcat_Drones",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablesweep": 1,
    "enablewatch": 0,
    "engineer": 0,
    "envelope": [
        0,
        0.2,
        0.9,
        2.1,
        2.5,
        3.3,
        3.5,
        3.6,
        3.7,
        3.8,
        3.8,
        3,
        0.9,
        0.7,
        0.5
    ],
    "epeimpulsedamagecoef": 1.5,
    "eventhandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "exhausts": {
        "exhaust_1": {
            "direction": "Exhaust_1_dir",
            "effect": "ExhaustsEffectDrone",
            "position": "Exhaust_1_pos"
        }
    },
    "explosionshielding": 0.04,
    "extcameraparams": [
        0.93,
        10,
        30,
        0.25,
        1,
        10,
        30,
        0,
        1
    ],
    "extcameraposition": [
        0,
        0.05,
        -2.55
    ],
    "faction": "CIV_F",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 10,
    "formationz": 10,
    "fuelcapacity": 100,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 0,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 2,
    "gearminalt": 0.5,
    "gearretracting": 0,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 3.33,
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 0,
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
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "gunnerhasflares": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.01,
        0.0025,
        0.01
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
        "Camo",
        "Medical"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": 0.15,
            "convexcomponent": "avionics_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "avionics_hit",
            "passthrough": 1,
            "visual": "elektronika"
        },
        "hitengine": {
            "armor": 0.25,
            "convexcomponent": "engine_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitengine1": {
            "armor": 0.25,
            "convexcomponent": "engine_1_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_1_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitengine2": {
            "armor": 0.25,
            "convexcomponent": "engine_2_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_2_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitengine3": {
            "armor": 0.25,
            "convexcomponent": "engine_3_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "engine_3_hit",
            "passthrough": 1,
            "visual": "motor"
        },
        "hitfuel": {
            "armor": 1,
            "convexcomponent": "fuel_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "fuel_hit",
            "passthrough": 1,
            "visual": "zbytek"
        },
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        "hitglass1": {
            "armor": 2,
            "convexcomponent": "glass1",
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 2,
            "convexcomponent": "glass2",
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 2,
            "convexcomponent": "glass3",
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 2,
            "convexcomponent": "glass4",
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 2,
            "convexcomponent": "glass5",
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 2,
            "convexcomponent": "glass6",
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "visual": "glass6"
        },
        "hithrotor": {
            "armor": 0.3,
            "convexcomponent": "main_rotor_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "main_rotor_hit",
            "passthrough": 0.1,
            "visual": "main rotor static"
        },
        "hithstabilizerl1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passthrough": 1
        },
        "hithstabilizerr1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passthrough": 0
        },
        "hithull": {
            "armor": 0.1,
            "convexcomponent": "hull_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "hull_hit",
            "passthrough": 1,
            "visual": "trup"
        },
        "hithydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passthrough": 0.8
        },
        "hitlglass": {
            "armor": 0.1,
            "convexcomponent": "sklo predni L",
            "explosionshielding": 1,
            "material": 51,
            "name": "sklo predni L",
            "passthrough": 0,
            "visual": "sklo predni L"
        },
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passthrough": 0
        },
        "hitmissiles": {
            "armor": 0.1,
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "ammo_hit",
            "passthrough": 0.5,
            "visual": "munice"
        },
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        "hitrglass": {
            "armor": 0.1,
            "convexcomponent": "sklo predni P",
            "explosionshielding": 1,
            "material": 51,
            "name": "sklo predni P",
            "passthrough": 0,
            "visual": "sklo predni P"
        },
        "hitstarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passthrough": 0
        },
        "hitstarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passthrough": 0
        },
        "hitstarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passthrough": 0
        },
        "hitstaticport": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passthrough": 1
        },
        "hittail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passthrough": 1
        },
        "hittransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passthrough": 0.8
        },
        "hitvrotor": {
            "armor": 0.3,
            "convexcomponent": "tail_rotor_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "tail_rotor_hit",
            "passthrough": 0.3,
            "visual": "tail rotor static"
        },
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        "hitwinch": {
            "armor": -40,
            "destructioneffects": {},
            "material": 51,
            "name": "slingLoad0",
            "passthrough": 0,
            "radius": 0.1,
            "visual": ""
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/Air_F_Orange/UAV_06/Data/UI/Map_UAV_06_CA.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.0316228,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 0,
    "irtargetsize": 1,
    "isbackpack": 0,
    "isuav": 1,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 0.1,
    "landingsoundint": [
        "landingSoundInt1",
        0.25,
        "landingSoundInt2",
        0.25,
        "landingSoundInt3",
        0.25,
        "landingSoundInt4",
        0.25
    ],
    "landingsoundint1": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_01",
        0.281838,
        0.5
    ],
    "landingsoundint2": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_02",
        0.281838,
        0.5
    ],
    "landingsoundint3": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_03",
        0.281838,
        0.5
    ],
    "landingsoundint4": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_04",
        0.281838,
        0.5
    ],
    "landingsoundout": [
        "landingSoundOut1",
        0.25,
        "landingSoundOut2",
        0.25,
        "landingSoundOut3",
        0.25,
        "landingSoundOut4",
        0.25
    ],
    "landingsoundout1": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_01",
        0.281838,
        1,
        50
    ],
    "landingsoundout2": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_02",
        0.281838,
        1,
        50
    ],
    "landingsoundout3": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_03",
        0.281838,
        1,
        50
    ],
    "landingsoundout4": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Land_Hit_04",
        0.281838,
        1,
        50
    ],
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffects": [
        [
            "GdtKLDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "LGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "LDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "LDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "LDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LGrassEffects"
        ],
        [
            "GdtGrassTall",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "LGrassEffects"
        ],
        [
            "GdtRedDirt",
            "LDustEffectsAirRed"
        ],
        [
            "GdtField",
            "LDustEffectsAir"
        ],
        [
            "GdtForest",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LStonesEffects"
        ],
        [
            "GdtCliff",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "LDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "LGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisGreenGrass",
            "LGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisRocky",
            "LGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "LDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisThistles",
            "LGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "LDirtEffects"
        ],
        [
            "GdtConcrete",
            "LDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "LDirtEffects"
        ],
        [
            "GdtAsphalt",
            "LDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "LDirtEffects"
        ],
        [
            "GdtRubble",
            "LDustEffectsAir"
        ],
        [
            "GdtRubble",
            "LDirtEffects"
        ],
        [
            "GdtSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtSoil",
            "LDirtEffects"
        ],
        [
            "GdtBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtBeach",
            "LStonesEffects"
        ],
        [
            "GdtRock",
            "LDustEffectsAir"
        ],
        [
            "GdtRock",
            "LDirtEffects"
        ],
        [
            "GdtDead",
            "LDustEffectsAir"
        ],
        [
            "GdtDead",
            "LDirtEffects"
        ],
        [
            "Default",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "LSandEffects"
        ],
        [
            "GdtDesert1",
            "LDirtEffects"
        ],
        [
            "GdtDesert1",
            "LStonesEffects"
        ],
        [
            "GdtDesert2",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert2",
            "LSandEffects"
        ],
        [
            "GdtDesert2",
            "LGrassEffects"
        ],
        [
            "GdtDesert2",
            "LDirtEffects"
        ],
        [
            "GdtDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtDirt",
            "LDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassGreen",
            "LGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "LDirtEffects"
        ],
        [
            "GdtGrassDry",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassDry",
            "LGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "LDirtEffects"
        ],
        [
            "GdtGrassWild",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassWild",
            "LGrassEffects"
        ],
        [
            "GdtGrassWild",
            "LDirtEffects"
        ],
        [
            "GdtWildField",
            "LDustEffectsAir"
        ],
        [
            "GdtWildField",
            "LGrassEffects"
        ],
        [
            "GdtWildField",
            "LDirtEffects"
        ],
        [
            "GdtWeed1",
            "LDustEffectsAir"
        ],
        [
            "GdtWeed1",
            "LGrassEffects"
        ],
        [
            "GdtWeed1",
            "LDirtEffects"
        ],
        [
            "GdtWeed2",
            "LDustEffectsAir"
        ],
        [
            "GdtWeed2",
            "LGrassEffects"
        ],
        [
            "GdtWeed2",
            "LDirtEffects"
        ],
        [
            "GdtThorn",
            "LDustEffectsAir"
        ],
        [
            "GdtThorn",
            "LGrassEffects"
        ],
        [
            "GdtThorn",
            "LDirtEffects"
        ],
        [
            "GdtStony",
            "LDustEffectsAir"
        ],
        [
            "GdtStony",
            "LGrassEffects"
        ],
        [
            "GdtStony",
            "LDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "LDustEffectsAir"
        ],
        [
            "GdtStonyGreen",
            "LGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "LDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "LDustEffectsAir"
        ],
        [
            "GdtStonyThistle",
            "LGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "LDirtEffects"
        ],
        [
            "GdtSeabedDeep",
            "LDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "LDustEffectsAir"
        ],
        [
            "SurfWood",
            "LDustEffectsAir"
        ],
        [
            "SurfMetal",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "LDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "LDustEffectsAir"
        ]
    ],
    "library": {
        "libtextdesc": "Engineers of the International Development &amp; Aid Project took a standard Utility Drone and modified it for highly effective mine clearance operations. This improvised drone uses a powerful sensor ring to detect mines as it flies low above the ground. It then releases one of its 4 demining charges from a higher altitude in order to safely detonate mines or other types of ordnance below."
    },
    "liftforcecoef": 1.6,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "lodturnedin": -1,
    "lodturnedout": -1,
    "magazines": [],
    "mainbladecenter": "rotor_center",
    "mainbladeradius": 0,
    "mainrotorspeed": -7,
    "mapsize": 2.32,
    "markerlights": {
        "collisionred": {
            "activelight": 0,
            "ambient": [
                0.09,
                0.015,
                0.01
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 1,
            "blinkingpattern": [
                0.2,
                1.3
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                0.9,
                0.15,
                0.1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "CollisionLight_red_1_pos",
            "useflare": 0
        },
        "collisionwhite": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                0.9
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "CollisionLight_white_1_pos",
            "useflare": 0
        },
        "greenstill": {
            "ambient": [
                0.003,
                0.03,
                0.003,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.03,
                0.3,
                0.03,
                1
            ],
            "name": "zeleny pozicni"
        },
        "positiongreen": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                0,
                0.8,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "PositionLight_green_1_pos",
            "useflare": 0
        },
        "positionred": {
            "activelight": 0,
            "ambient": [
                0.08,
                0,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                0.8,
                0,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "PositionLight_red_1_pos",
            "useflare": 0
        },
        "positionwhite": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 1,
                "hardlimitstart": 0.75,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "PositionLight_white_1_pos",
            "useflare": 0
        },
        "redblinking": {
            "ambient": [
                0.05,
                0.005,
                0.005,
                1
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                0.5,
                0.05,
                0.05,
                1
            ],
            "name": "cerveny pozicni blik"
        },
        "redstill": {
            "ambient": [
                0.03,
                0.003,
                0.003,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.3,
                0.03,
                0.03,
                1
            ],
            "name": "cerveny pozicni"
        },
        "whiteblinking": {
            "ambient": [
                0.1,
                0.1,
                0.1,
                1
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                1,
                1,
                1,
                1
            ],
            "name": "bily pozicni blik"
        },
        "whitestill": {
            "ambient": [
                0.03,
                0.03,
                0.03,
                1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.3,
                0.3,
                0.3,
                1
            ],
            "name": "bily pozicni"
        }
    },
    "maxbackrotordive": 0,
    "maxdetectrange": 20,
    "maxfordingdepth": 0.3,
    "maxgforce": 2,
    "maximumload": 0,
    "maxmainrotordive": 0,
    "maxsmokedamage": 0.99,
    "maxspeed": 100,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": "pip_pilot_pos",
    "memorypointgun": "",
    "memorypointlmissile": "L strela",
    "memorypointlrocket": "L raketa",
    "memorypointpilot": "pilot",
    "memorypointrmissile": "P strela",
    "memorypointrrocket": "P raketa",
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 0.2,
    "mfd": {},
    "mfmax": 100,
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
    "minbackrotordive": 0,
    "minealerticonrange": 200,
    "minedetectorrange": 50,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minmainrotordive": 0,
    "minsmokedamage": 0.3,
    "mintotaldamagethreshold": 0.1,
    "model": "A3/Air_F_Orange/UAV_06/UAV_06_F.p3d",
    "namesound": "veh_air_UAV_s",
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
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
    "normalspeedforwardcoef": 0.85,
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
    "obstructsoundswhenin": 0.316228,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 1,
    "picture": "A3/Air_F_Orange/UAV_06/Data/UI/UAV_06_CA.paa",
    "pilotcamera": {
        "controllable": 1,
        "initelev": 0,
        "initturn": 0,
        "maxelev": 89,
        "maxmousexrotspeed": 0.5,
        "maxmouseyrotspeed": 0.5,
        "maxturn": 60,
        "maxxrotspeed": 1,
        "maxyrotspeed": 1,
        "minelev": -45,
        "minturn": -60,
        "opticsin": {
            "showminimapinoptics": 1,
            "showslingloadmanagerinoptics": 0,
            "showuavviewinoptics": 0,
            "wide": {
                "directionstabilized": 1,
                "gunneropticsmodel": "a3/Weapons_F_Orange/Reticle/UAV_06_pilotCamera_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": 1,
                "minanglex": 0,
                "minangley": 0,
                "minfov": 1,
                "opticsdisplayname": "WFOV",
                "opticsppeffects": [
                    "OpticsCHAbera2",
                    "OpticsBlur2"
                ],
                "thermalmode": [],
                "visionmode": [
                    "Normal",
                    "NVG"
                ]
            }
        },
        "pilotopticsshowcursor": 1
    },
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 15,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 0.1,
    "radartype": 4,
    "reflectors": {},
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rightdusteffects": [
        [
            "GdtKLDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "RGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "RDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "RDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "RDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RGrassEffects"
        ],
        [
            "GdtGrassTall",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "RGrassEffects"
        ],
        [
            "GdtRedDirt",
            "RDustEffectsAirRed"
        ],
        [
            "GdtField",
            "RDustEffectsAir"
        ],
        [
            "GdtForest",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RStonesEffects"
        ],
        [
            "GdtCliff",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "RDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "RGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisGreenGrass",
            "RGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisRocky",
            "RGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "RDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisThistles",
            "RGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "RDirtEffects"
        ],
        [
            "GdtConcrete",
            "RDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "RDirtEffects"
        ],
        [
            "GdtAsphalt",
            "RDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "RDirtEffects"
        ],
        [
            "GdtRubble",
            "RDustEffectsAir"
        ],
        [
            "GdtRubble",
            "RDirtEffects"
        ],
        [
            "GdtSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtSoil",
            "RDirtEffects"
        ],
        [
            "GdtBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtBeach",
            "RStonesEffects"
        ],
        [
            "GdtRock",
            "RDustEffectsAir"
        ],
        [
            "GdtRock",
            "RDirtEffects"
        ],
        [
            "GdtDead",
            "RDustEffectsAir"
        ],
        [
            "GdtDead",
            "RDirtEffects"
        ],
        [
            "Default",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "RSandEffects"
        ],
        [
            "GdtDesert1",
            "RDirtEffects"
        ],
        [
            "GdtDesert1",
            "RStonesEffects"
        ],
        [
            "GdtDesert2",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert2",
            "RSandEffects"
        ],
        [
            "GdtDesert2",
            "RGrassEffects"
        ],
        [
            "GdtDesert2",
            "RDirtEffects"
        ],
        [
            "GdtDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtDirt",
            "RDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassGreen",
            "RGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "RDirtEffects"
        ],
        [
            "GdtGrassDry",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassDry",
            "RGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "RDirtEffects"
        ],
        [
            "GdtGrassWild",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassWild",
            "RGrassEffects"
        ],
        [
            "GdtGrassWild",
            "RDirtEffects"
        ],
        [
            "GdtWildField",
            "RDustEffectsAir"
        ],
        [
            "GdtWildField",
            "RGrassEffects"
        ],
        [
            "GdtWildField",
            "RDirtEffects"
        ],
        [
            "GdtWeed1",
            "RDustEffectsAir"
        ],
        [
            "GdtWeed1",
            "RGrassEffects"
        ],
        [
            "GdtWeed1",
            "RDirtEffects"
        ],
        [
            "GdtWeed2",
            "RDustEffectsAir"
        ],
        [
            "GdtWeed2",
            "RGrassEffects"
        ],
        [
            "GdtWeed2",
            "RDirtEffects"
        ],
        [
            "GdtThorn",
            "RDustEffectsAir"
        ],
        [
            "GdtThorn",
            "RGrassEffects"
        ],
        [
            "GdtThorn",
            "RDirtEffects"
        ],
        [
            "GdtStony",
            "RDustEffectsAir"
        ],
        [
            "GdtStony",
            "RGrassEffects"
        ],
        [
            "GdtStony",
            "RDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "RDustEffectsAir"
        ],
        [
            "GdtStonyGreen",
            "RGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "RDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "RDustEffectsAir"
        ],
        [
            "GdtStonyThistle",
            "RGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "RDirtEffects"
        ],
        [
            "GdtSeabedDeep",
            "RDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "RDustEffectsAir"
        ],
        [
            "SurfWood",
            "RDustEffectsAir"
        ],
        [
            "SurfMetal",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "RDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "RDustEffectsAir"
        ]
    ],
    "rotorlibhelicopterproperties": {
        "autohovercorrection": [
            0,
            0,
            0
        ],
        "defaultcollective": 0.7,
        "hasapu": 0,
        "horizontalwingsanglecollmax": 0,
        "horizontalwingsanglecollmin": 0,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxmainrotorstress": 10000,
        "maxtailrotorstress": 10000,
        "maxtorque": 10000,
        "maxverticalstabilizerstress": 10000,
        "retreatbladestallwarningspeed": 69.4,
        "rtdconfig": "",
        "stressdamagepersec": 0.01,
        "vrsshakepowercoef": 1
    },
    "scope": 0,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionhrotormove": "main rotor blur",
    "selectionhrotorstill": "main rotor static",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionshowdamage": "poskozeni",
    "selectionvrotormove": "tail rotor blur",
    "selectionvrotorstill": "tail rotor static",
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "shadow": 1,
    "showalltargets": 0,
    "showcrewaim": 0,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        0
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 3,
    "simulation": "helicopterrtd",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slingloadmaxcargomass": 0,
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmincargomass": 0,
    "slowspeedforwardcoef": 0.3,
    "soundarmorcrash": [
        "armorCrash1",
        0.25,
        "armorCrash2",
        0.25,
        "armorCrash3",
        0.25,
        "armorCrash4",
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
        "buildCrash1",
        0.25,
        "buildCrash2",
        0.25,
        "buildCrash3",
        0.25,
        "buildCrash4",
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
        "Crash1",
        0.25,
        "Crash2",
        0.25,
        "Crash3",
        0.25,
        "Crash4",
        0.25
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
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_Off_Ext",
        0.316228,
        1,
        50
    ],
    "soundengineoffint": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_Off_Int",
        0.158489,
        1,
        10
    ],
    "soundengineonext": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_On_Ext",
        0.316228,
        1,
        50
    ],
    "soundengineonint": [
        "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_On_Int",
        0.158489,
        1,
        10
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
    "soundgear": {},
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
        1,
        1
    ],
    "soundgetout": [
        "",
        1,
        1,
        50
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
    "soundlandinggear": [
        "",
        1,
        1
    ],
    "soundlocked": [
        "",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "engine_01_ext": {
            "frequency": "0.97 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (15 - 0)/(30 - 0)))+  ((1-engineon) * 0.01*(rpm factor [0,1]))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_01_Ext",
                1.12202,
                1,
                150
            ],
            "volume": "campos * 1 * (((abs(speed) factor [0,\t30]) factor[ 0 + (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2, (15 - 0)/(30 - 0) - (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2]) * ((abs(speed) factor [0,\t30]) factor[ (25 - 0)/(30 - 0) - (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2, (15 - 0)/(30 - 0) + (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2]))"
        },
        "engine_01_int": {
            "frequency": "0.97 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (15 - 0)/(30 - 0)))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_01_Int",
                0.501187,
                1
            ],
            "volume": "(1-campos) * 1 * (((abs(speed) factor [0,\t30]) factor[ 0 + (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2, (15 - 0)/(30 - 0) - (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2]) * ((abs(speed) factor [0,\t30]) factor[ (25 - 0)/(30 - 0) - (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2, (15 - 0)/(30 - 0) + (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2]))"
        },
        "engine_02_ext": {
            "frequency": "0.98 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (25 - 0)/(30 - 0)))+  ((1-engineon) * 0.01*(rpm factor [0,1]))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_02_Ext",
                1.12202,
                1,
                150
            ],
            "volume": "campos * 1 * (((abs(speed) factor [0,\t30]) factor[ (15 - 0)/(30 - 0) + (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2, (25 - 0)/(30 - 0) - (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2]) * ((abs(speed) factor [0,\t30]) factor[ (29 - 0)/(30 - 0) - (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2, (25 - 0)/(30 - 0) + (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2]))"
        },
        "engine_02_int": {
            "frequency": "0.98 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (25 - 0)/(30 - 0)))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_02_Int",
                0.501187,
                1
            ],
            "volume": "(1-campos) * 1 * (((abs(speed) factor [0,\t30]) factor[ (15 - 0)/(30 - 0) + (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2, (25 - 0)/(30 - 0) - (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0)) - (0.7 * (((25 - 0)/(30 - 0) - (15 - 0)/(30 - 0))))) / 2]) * ((abs(speed) factor [0,\t30]) factor[ (29 - 0)/(30 - 0) - (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2, (25 - 0)/(30 - 0) + (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2]))"
        },
        "engine_03_ext": {
            "frequency": "0.99 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (29 - 0)/(30 - 0)))+  ((1-engineon) * 0.01*(rpm factor [0,1]))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_03_Ext",
                1.25893,
                1,
                150
            ],
            "volume": "campos * 1 * ((abs(speed) factor [0,\t30]) factor[ (25 - 0)/(30 - 0) + (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2, (29 - 0)/(30 - 0) - (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2])"
        },
        "engine_03_int": {
            "frequency": "0.99 * 1  * (1.2 + 0.3  * ((abs(speed) factor [0,\t30]) - (29 - 0)/(30 - 0)))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_03_Int",
                0.501187,
                1
            ],
            "volume": "(1-campos) * 1 * ((abs(speed) factor [0,\t30]) factor[ (25 - 0)/(30 - 0) + (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2, (29 - 0)/(30 - 0) - (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0)) - (0.7 * (((29 - 0)/(30 - 0) - (25 - 0)/(30 - 0))))) / 2])"
        },
        "engine_idle_int": {
            "frequency": "0.96 * 1  * (1 + 0.3  * ((abs(speed) factor [0,\t30]) - 0))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_01_Int",
                0.398107,
                1
            ],
            "volume": "(1-campos) * 1 * ((abs(speed) factor [0,\t30]) factor[ (15 - 0)/(30 - 0) - (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2, 0 + (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2]) * (rotorSpeed factor[ 0.2, 1])"
        },
        "engine_lateral_movement_01_ext": {
            "frequency": "1 + angVelocity interpolate [0,3.5,1,1.2]",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Engine_Lateral_Movement",
                0.707946,
                1,
                150
            ],
            "volume": "camPos * (abs(speed) factor[10, 25]) * (angVelocity factor [0.5,2.5])"
        },
        "engine_lateral_movement_int": {
            "frequency": "0.1 * angVelocity interpolate [0,3.5,1,1.2]",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Engine_Lateral_Movement_Int",
                0.630957,
                0.8
            ],
            "volume": "(1-camPos) * (abs(speed) factor[10, 25]) * (angVelocity factor [0.5,2.5])"
        },
        "idle_ext": {
            "frequency": "0.96 * 1  * (1 + 0.3  * ((abs(speed) factor [0,\t30]) - 0))+  ((1-engineon) * 0.01*(rpm factor [0,1]))",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Eng_01_Ext",
                0.891251,
                1,
                150
            ],
            "volume": "campos * 1 * ((abs(speed) factor [0,\t30]) factor[ (15 - 0)/(30 - 0) - (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2, 0 + (((15 - 0)/(30 - 0) - 0) - (0.7 * (((15 - 0)/(30 - 0) - 0)))) / 2]) * (rotorSpeed factor[ 0.2, 1])"
        },
        "rotors_ext": {
            "frequency": "1 + rotorThrust*rpm",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/Rotors_Synth_03",
                0.630957,
                3,
                150
            ],
            "volume": "camPos * rpm * (rotorSpeed factor [0.01, 0.1]) + (abs(speed) factor[0, 25])"
        },
        "rotors_int": {
            "frequency": "rotorSpeed*rotorThrust*rpm",
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/Rotors_Synth_03",
                0.0501187,
                2.7
            ],
            "volume": "(1-camPos) * rpm * (rotorSpeed factor [0.01, 0.1]) + (abs(speed) factor[0, 25])"
        },
        "scrubarmor_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Land_Ext",
                0.177828,
                1,
                50
            ],
            "volume": "camPos * (scrubArmor envelope [0.001, 0.05, 0.10, 0.2])"
        },
        "scrubarmor_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Land_Int",
                0.158489,
                1
            ],
            "volume": "(1-camPos) * (scrubArmor envelope [0.001, 0.05, 0.10, 0.2])"
        },
        "scrubbuilding_01_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_01",
                0.177828,
                1,
                50
            ],
            "volume": "camPos * (scrubBuilding factor [0.01, 0.05])"
        },
        "scrubbuilding_01_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_01",
                0.177828,
                1
            ],
            "volume": "(1 - camPos) * (scrubBuilding factor [0.01, 0.05])"
        },
        "scrubbuilding_02_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_03",
                0.158489,
                1,
                50
            ],
            "volume": "camPos * (scrubBuilding factor [0.01, 0.05])"
        },
        "scrubbuilding_02_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_03",
                0.158489,
                1
            ],
            "volume": "(1 - camPos) * (scrubBuilding factor [0.01, 0.05])"
        },
        "scrubland_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Land_Ext",
                0.177828,
                1,
                50
            ],
            "volume": "camPos * (scrubLand envelope [0.001, 0.09, 0.12, 0.35])"
        },
        "scrubland_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Land_Int",
                0.158489,
                1
            ],
            "volume": "(1 - camPos) * (scrubLand envelope [0.001, 0.09, 0.12, 0.35])"
        },
        "scrubobject_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_01",
                0.177828,
                1,
                50
            ],
            "volume": "camPos * (scrubObject factor [0.01, 0.05])"
        },
        "scrubobject_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Object_01",
                0.158489,
                1
            ],
            "volume": "(1 - camPos) * (scrubObject factor [0.01, 0.05 ])"
        },
        "scrubtree_01_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Tree_01_Ext",
                1.12202,
                1,
                50
            ],
            "volume": "camPos * (scrubTree envelope [0.01, 0.05, 0.08,0.15])"
        },
        "scrubtree_01_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Tree_01_Int",
                0.630957,
                1
            ],
            "volume": "(1 - camPos) * (scrubTree envelope [0.01, 0.05, 0.08,0.15])"
        },
        "scrubtree_02_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Tree_02_Ext",
                1.12202,
                1,
                50
            ],
            "volume": "camPos * (scrubTree envelope [0.01, 0.05, 0.08,0.15])"
        },
        "scrubtree_02_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_Scrub_Tree_02_Int",
                0.630957,
                1
            ],
            "volume": "(1 - camPos) * (scrubTree envelope [0.01, 0.05, 0.08,0.15])"
        },
        "windnoise_01_ext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_WindNoise_01_Ext",
                0.141254,
                1,
                150
            ],
            "volume": "camPos * (abs(speed) factor[10, 20]) * (angVelocity factor [0.5,2.5])"
        },
        "windnoise_01_int": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F_Orange/Vehicles/Air/UAV_06/UAV_06_WindNoise_01_Ext",
                0.1,
                0.8
            ],
            "volume": "(1-camPos) * (abs(speed) factor[5, 20]) * (angVelocity factor [0.5,2.5])"
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
        "emptySound",
        0
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_air_UAV_p"
            ],
            "speechsingular": [
                "veh_air_UAV_s"
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
    "startduration": 3,
    "steeraheadplan": 0.7,
    "steeraheadsimul": 0.5,
    "supplyradius": 1.2,
    "tailbladecenter": "rotor_02_center",
    "tailbladeradius": 0.5,
    "tailbladevertical": 0,
    "tbody": 150,
    "textplural": "UAVs",
    "textsingular": "UAV",
    "texturesources": {},
    "threat": [
        0.1,
        0.1,
        0.1
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportfuel": 0,
    "transportitems": {},
    "transportmagazines": {},
    "transportmaxbackpacks": 1,
    "transportmaxmagazines": 20,
    "transportmaxweapons": 3,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {},
    "type": 2,
    "typicalcargo": [
        "Soldier"
    ],
    "uavcameradriverdir": "pip_pilot_dir",
    "uavcameradriverpos": "pip_pilot_pos",
    "uavcameragunnerdir": "",
    "uavcameragunnerpos": "",
    "uavhacker": 0,
    "unitinfotype": "RscOptics_UAV_06",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigital",
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "beacons_start": {
            "animperiod": 2,
            "condition": "(cameraOn == this) AND {this animationSourcePhase 'LED_lights_hide' isEqualTo 0} AND  {this animationSourcePhase 'lights_em_hide' < 0.5} AND {Alive(this)} ",
            "displayname": "Beacons On",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_ON_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "this animateSource ['lights_em_hide',1];",
            "useractionid": 50
        },
        "beacons_stop": {
            "animperiod": 2,
            "condition": "(cameraOn == this)  AND {this animationSourcePhase 'LED_lights_hide' isEqualTo 0} AND  {this animationSourcePhase 'lights_em_hide' > 0.5} AND {Alive(this)} ",
            "displayname": "Beacons Off",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_OFF_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "",
            "priority": 1.5,
            "radius": 1.8,
            "showwindow": 0,
            "statement": "this animateSource ['lights_em_hide',0];",
            "useractionid": 51
        }
    },
    "vehicleclass": "Autonomous",
    "vehicletransport": {
        "cargo": {
            "canbetransported": 1,
            "dimensions": [
                "BBox_1_1_pos",
                "BBox_1_2_pos"
            ],
            "parachuteclass": "B_Parachute_02_F",
            "parachuteheightlimit": 5
        },
        "carrier": {
            "cargoalignment": [
                "center",
                "front"
            ],
            "cargobaydimensions": [
                "VVT_cargo_1",
                "VVT_cargo_2"
            ],
            "cargospacing": [
                0,
                0,
                0
            ],
            "disableheightlimit": 0,
            "exits": [
                "VVT_exit"
            ],
            "loadingangle": 60,
            "loadingdistance": 5,
            "maxloadmass": 25000,
            "parachuteclassdefault": "B_Parachute_02_F",
            "parachuteheightlimitdefault": 5,
            "unloadinginterval": 2
        }
    },
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
        "initfov": 1,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 1,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 1,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0,
        "thermalmode": [],
        "visionmode": []
    },
    "viewpilot": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.75,
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
    "visualtargetsize": 0.1,
    "washdowndiameter": "10.0f",
    "washdownstrength": "0.25f",
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "UAVWater",
    "waterleakiness": 100,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "windsockexist": 0
}