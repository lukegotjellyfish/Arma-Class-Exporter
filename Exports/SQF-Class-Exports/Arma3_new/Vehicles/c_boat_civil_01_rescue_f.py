d = {
    "_generalmacro": "C_Boat_Civil_01_rescue_F",
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [],
    "aircapacity": 10,
    "allowtablock": 1,
    "alwaystarget": 0,
    "animated": 1,
    "animationlist": [
        "hidePolice",
        1,
        "HideRescueSigns",
        0,
        "HidePoliceSigns",
        1
    ],
    "animationsources": {
        "beacons": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "hidepolice": {
            "author": "Bohemia Interactive",
            "displayname": "Hide police light bar",
            "initphase": 1,
            "source": "user"
        },
        "hidepolicesigns": {
            "author": "Bohemia Interactive",
            "displayname": "Hide police signs",
            "forceanimate": [
                "HideRescueSigns",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "source": "user"
        },
        "hiderescuesigns": {
            "author": "Bohemia Interactive",
            "displayname": "Hide rescue signs",
            "forceanimate": [
                "HidePoliceSigns",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "source": "user"
        },
        "proxy": {
            "animperiod": 1,
            "initphase": 1,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 60,
    "armorcrash0": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_01",
        3.16228,
        1,
        200
    ],
    "armorcrash1": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_02",
        3.16228,
        1,
        200
    ],
    "armorcrash2": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_03",
        3.16228,
        1,
        200
    ],
    "armorlights": 0.4,
    "armorstructural": 1,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "OpenCarAttenuation",
    "audible": 6,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 14,
    "buildcrash0": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_building_01",
        1.77828,
        1,
        200
    ],
    "buildcrash1": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_building_02",
        1.77828,
        1,
        200
    ],
    "buildcrash2": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_building_03",
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
    "camouflage": 2,
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
    "canfloat": 1,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "passenger_low01"
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
        "GetOutBoat"
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
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "complexgearbox": {
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -0.782,
            "N",
            0,
            "D1",
            1.9
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
        "transportcountermeasurescomponent": {}
    },
    "cost": 20000,
    "countsforscoreboard": 1,
    "crew": "C_man_1",
    "crewcrashprotection": 0.1,
    "crewexplosionprotection": 0.5,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_damage.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_destruct.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_chrome.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_chrome.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_destruct.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_damage.rvmat",
            "A3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_destruct.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_ext.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_ext_damage.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_ext_destruct.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_int.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_int_damage.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/Boat_Civil_01_int_destruct.rvmat",
            "A3/data_f/glass_veh.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/boat_glass_dmg.rvmat",
            "A3/Boat_F_Gamma/Boat_Civil_01/data/boat_glass_dmg.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00882,
    "damagetexdelay": 0,
    "destrtype": "DestructDefault",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "Motorboat (Rescue)",
    "driveraction": "driver_mid01",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "drivingWheel",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "drivingWheel",
    "driverrightleganimname": "",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "A3/EditorPreviews_F/Data/CfgVehicles/C_Boat_Civil_01_rescue_F.jpg",
    "editorsubcategory": "EdSubcat_Boats",
    "ejectdeadcargo": 1,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablewatch": 0,
    "engineeffectspeed": 5,
    "engineer": 0,
    "enginepower": 235,
    "engineshifty": 0.1,
    "epeimpulsedamagecoef": 70,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "_this select 0 animate ['HidePoliceSigns',1]; _this select 0 animate ['HideRescueSigns',0]; _this select 0 animate ['HidePolice',1];",
        "killed": "_this select 0 animate [`HidePoliceSigns`,1]; _this select 0 animate [`HideRescueSigns`,1]; _this select 0 animate [`HidePolice`,1];"
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustsEffect",
            "position": "vyfuk start"
        }
    },
    "explosionshielding": 4,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        1.5,
        -8
    ],
    "faction": "CIV_F",
    "features": "Randomization: No\t\t\t\t\t\t<br />Camo selections: 2 - the body, interior and engines\t\t\t\t\t\t<br />Script door sources: None\t\t\t\t\t\t<br />Script animations: HidePoliceSigns, HideRescueSigns, HidePolice, BeaconsStart\t\t\t\t\t\t<br />Executed scripts: None\t\t\t\t\t\t<br />Firing from vehicles: No\t\t\t\t\t\t<br />Slingload: No\t\t\t\t\t\t<br />Cargo proxy indexes: 1 and 2",
    "featuretype": 0,
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 20,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 12,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 0,
    "fxexplo": {
        "access": 1
    },
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 5,
    "getoutaction": "GetOutBoat",
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
    "gunnerhasflares": 0,
    "hasdriver": 1,
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
        "camo",
        "camo2"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_rescue_co.paa",
        "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_rescue_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 999,
            "convexcomponent": "engine",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "explosionshielding": 2,
            "material": 60,
            "name": "engine",
            "passthrough": 1,
            "visual": ""
        },
        "hitengine1": {
            "armor": 0.2,
            "convexcomponent": "engine1",
            "explosionshielding": 2,
            "material": -1,
            "name": "engine1",
            "passthrough": 1,
            "visual": ""
        },
        "hitengine2": {
            "armor": 0.2,
            "convexcomponent": "engine2",
            "explosionshielding": 2,
            "material": -1,
            "name": "engine2",
            "passthrough": 1,
            "visual": ""
        },
        "hitglass1": {
            "armor": 0.25,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.25,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.25,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "visual": "glass3"
        },
        "hithull": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": 50,
            "name": "karoserie",
            "passthrough": 1,
            "visual": "zbytek"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "A3/boat_f_gamma/Boat_Civil_01/data/UI/map_civilian_boat_CA.paa",
    "idlerpm": 200,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 1,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffect": "LDustEffects",
    "leftengineeffect": "LEngEffectsSmall",
    "leftfastwatereffect": "LFastWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "library": {
        "libtextdesc": "A luxury motorboat is an engine powered boat used by the Police and Altis' richest. Its speed and maneuverability is almost on a par with military speedboat."
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "magazines": [],
    "mapsize": 7.39,
    "markerlights": {
        "positiongreen": {
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
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.6,
            "intensity": 50,
            "name": "PositionLight_Green_1_pos",
            "useflare": 0
        },
        "positionred": {
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
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.6,
            "intensity": 50,
            "name": "PositionLight_Red_1_pos",
            "useflare": 0
        },
        "positionwhite": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "drawlightsize": 0.6,
            "intensity": 50,
            "name": "PositionLight_White_1_pos",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 1,
    "maxgforce": 2,
    "maximumload": 500,
    "maxspeed": 80,
    "memorypointdriveroptics": [
        "driverview",
        "pilot"
    ],
    "memorypointmissile": [
        "spice rakety",
        "usti hlavne"
    ],
    "memorypointmissiledir": [
        "konec rakety",
        "konec hlavne"
    ],
    "memorypointsgetincargo": [
        "pos codriver",
        "pos cargo"
    ],
    "memorypointsgetincargodir": [
        "pos codriver dir",
        "pos cargo dir"
    ],
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetingunner": [
        "pos codriver",
        "pos cargo"
    ],
    "memorypointsgetingunnerdir": [
        "pos codriver dir",
        "pos cargo dir"
    ],
    "memorypointsleftengineeffect": "EngineEffectL",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightengineeffect": "EngineEffectR",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "TaskMarker_1_pos",
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
    "mintotaldamagethreshold": 0.01,
    "model": "A3/boat_f_gamma/Boat_Civil_01/Boat_Civil_01_F",
    "namesound": "veh_ship_boat_s",
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
    "occludesoundswhenin": 0.562341,
    "outsidesoundfilter": 0,
    "overspeedbrakecoef": 0.8,
    "periscopedepth": 2.8,
    "picture": "A3/boat_f_gamma/Boat_Civil_01/data/UI/portrait_civilian_boat_CA.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "pointcommander": "velitel",
    "pointpilot": "pilot",
    "portrait": "",
    "precisegetinout": 0,
    "precision": 15,
    "predictturnplan": 2.4,
    "predictturnsimul": 2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartype": 0,
    "redrpm": 1200,
    "reflectors": {},
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rightdusteffect": "RDustEffects",
    "rightengineeffect": "REngEffectsSmall",
    "rightfastwatereffect": "RFastWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "rudderforcecoef": 0.1,
    "rudderforcecoefatmaxspeed": 0.003,
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
    "sensitivity": 2.5,
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
    "side": 3,
    "simpleobject": {
        "animate": [
            [
                "damagehide",
                0
            ],
            [
                "damagehidepolice",
                0
            ],
            [
                "drivingwheel",
                0
            ],
            [
                "propeller1",
                0
            ],
            [
                "propeller2",
                0
            ],
            [
                "engine1",
                0
            ],
            [
                "engine2",
                0
            ],
            [
                "indicatorspeed",
                0.02
            ],
            [
                "fuel",
                1
            ],
            [
                "indicatorrpm",
                0
            ],
            [
                "throttle",
                0
            ],
            [
                "prop_batt",
                0
            ],
            [
                "prop_oil",
                0
            ],
            [
                "prop_water",
                0
            ],
            [
                "prop_trim",
                -0.07
            ],
            [
                "beacon1",
                1576.38
            ],
            [
                "beaconsstart",
                0
            ],
            [
                "beacon2",
                1576.38
            ],
            [
                "beacon3",
                1576.38
            ],
            [
                "beacon4",
                1576.38
            ]
        ],
        "eden": 1,
        "hide": [
            "zasleh",
            "zadni svetlo",
            "brzdove svetlo",
            "clan",
            "podsvit pristroju",
            "poskozeni"
        ],
        "init": "[this, '', []] call bis_fnc_initVehicle",
        "verticaloffset": 1.296,
        "verticaloffsetworld": -0.656
    },
    "simulation": "shipx",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.3,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.33,
        "ArmorCrash1",
        0.33,
        "ArmorCrash2",
        0.34
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
        0.33,
        "buildCrash1",
        0.33,
        "buildCrash2",
        0.34
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
        "soundGeneralCollision1",
        0.33,
        "soundGeneralCollision2",
        0.33,
        "soundGeneralCollision3",
        0.34
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
        "a3/Sounds_F/vehicles/boat/Motor_Boat/engine_stop",
        0.562341,
        1,
        300
    ],
    "soundengineoffint": [
        "a3/Sounds_F/vehicles/boat/Motor_Boat/engine_stop",
        0.562341,
        1
    ],
    "soundengineonext": [
        "a3/Sounds_F/vehicles/boat/Motor_Boat/engine_start",
        0.562341,
        1,
        300
    ],
    "soundengineonint": [
        "a3/Sounds_F/vehicles/boat/Motor_Boat/engine_start",
        0.562341,
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
    "soundgeneralcollision1": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_01",
        1.77828,
        1,
        100
    ],
    "soundgeneralcollision2": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_02",
        1.77828,
        1,
        100
    ],
    "soundgeneralcollision3": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_armor_03",
        1.77828,
        1,
        100
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
            "frequency": "0.85\t+\t((rpm/\t1000) factor[(200/\t1000),(370/\t1000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_1",
                0.630957,
                1,
                350
            ],
            "volume": "engineOn*(((rpm/\t1000) factor[(190/\t1000),(250/\t1000)])\t*\t((rpm/\t1000) factor[(380/\t1000),(280/\t1000)]))"
        },
        "enginemaxout2": {
            "frequency": "0.86\t+\t((rpm/\t1000) factor[(380/\t1000),(580/\t1000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_4",
                0.891251,
                1,
                440
            ],
            "volume": "engineOn*(((rpm/\t1000) factor[(370/\t1000),(440/\t1000)])\t*\t((rpm/\t1000) factor[(585/\t1000),(495/\t1000)]))"
        },
        "enginemaxout3": {
            "frequency": "0.85\t+\t((rpm/\t1000) factor[(490/\t1000),(800/\t1000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_5",
                1,
                1,
                500
            ],
            "volume": "engineOn*(((rpm/\t1000) factor[(460/\t1000),(550/\t1000)])\t*\t((rpm/\t1000) factor[(780/\t1000),(620/\t1000)]))"
        },
        "enginemaxout4": {
            "frequency": "0.85\t+\t((rpm/\t1000) factor[(650/\t1000),(1000/\t1000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_6",
                1.25893,
                1,
                550
            ],
            "volume": "engineOn*((rpm/\t1000) factor[(600/\t1000),(800/\t1000)])"
        },
        "enginemidout": {
            "frequency": "0.85\t+\t((rpm/\t1000) factor[(280/\t1000),(480/\t1000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_3",
                0.794328,
                1,
                380
            ],
            "volume": "engineOn*(((rpm/\t1000) factor[(250/\t1000),(350/\t1000)])\t*\t((rpm/\t1000) factor[(480/\t1000),(390/\t1000)]))"
        },
        "idleout": {
            "frequency": "0.95\t+\t((rpm/\t1000) factor[(100/\t1000),(250/\t1000)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/boat/Motor_Boat/engine_idle",
                0.446684,
                1,
                300
            ],
            "volume": "engineOn*(((rpm/\t1000) factor[(100/\t1000),(150/\t1000)])\t*\t((rpm/\t1000) factor[(270/\t1000),(200/\t1000)]))"
        },
        "rainext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain2_ext",
                1,
                1,
                100
            ],
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        "rainint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain2_ext",
                1,
                1,
                100
            ],
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        "scrublandext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/boat/noises/boat_land_on_shallow",
                1.77828,
                1,
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
        0.33,
        "woodCrash1",
        0.33,
        "woodCrash2",
        0.34
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_ship_boat_p"
            ],
            "speechsingular": [
                "veh_ship_boat_s"
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
    "steeraheadplan": 2.4,
    "steeraheadsimul": 2,
    "supplyradius": 3,
    "tbody": 150,
    "textplural": "boats",
    "textsingular": "boat",
    "texturelist": [
        "Rescue",
        1
    ],
    "texturesources": {
        "civilian": {
            "author": "Bohemia Interactive",
            "displayname": "Civilian",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_co.paa",
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_co.paa"
            ]
        },
        "police": {
            "author": "Bohemia Interactive",
            "displayname": "Police",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_police_co.paa",
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_police_co.paa"
            ]
        },
        "rescue": {
            "author": "Bohemia Interactive",
            "displayname": "Rescue",
            "factions": [
                "CIV_F"
            ],
            "textures": [
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_ext_rescue_co.paa",
                "/a3/boat_f_gamma/Boat_Civil_01/data/Boat_Civil_01_int_rescue_co.paa"
            ]
        }
    },
    "threat": [
        0,
        0,
        0
    ],
    "thrustdelay": 2,
    "tracksspeed": 0,
    "transportammo": 0,
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 6,
            "name": "FirstAidKit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 5,
    "transportmaxmagazines": 100,
    "transportmaxweapons": 10,
    "transportrepair": 0,
    "transportsoldier": 2,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 0.25,
    "turrets": {},
    "type": 1,
    "typicalcargo": [
        "C_man_1"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoNoWeapon",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "beacons_start": {
            "animperiod": 2,
            "condition": "(this animationPhase 'BeaconsStart' < 0.5)  AND {driver this == player} AND {(this animationSourcePhase 'Proxy') isEqualTo 0}",
            "displayname": "Beacons On",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_ON_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "statement": "this animate ['BeaconsStart',1,true];",
            "useractionid": 50
        },
        "beacons_stop": {
            "animperiod": 2,
            "condition": "(this animationPhase 'BeaconsStart' > 0.5)  AND {driver this == player} AND {(this animationSourcePhase 'Proxy') isEqualTo 0}",
            "displayname": "Beacons Off",
            "displaynamedefault": "<img image='/A3/Ui_f/data/IGUI/Cfg/Actions/beacons_OFF_ca.paa' size='2.5' />",
            "onlyforplayer": 0,
            "position": "mph_axis",
            "priority": 1.5,
            "radius": 1.8,
            "statement": "this animate ['BeaconsStart',0,true];",
            "useractionid": 51
        }
    },
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
    "waterangulardampingcoef": 1.2,
    "waterdamageengine": 0.2,
    "watereffectspeed": 5,
    "waterfasteffectspeed": 28,
    "waterleakiness": 1,
    "waterlineardampingcoefx": 2,
    "waterlineardampingcoefy": 2,
    "waterppinvehicle": 1,
    "waterresistance": 10,
    "waterresistancecoef": 0.012,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "windsockexist": 0,
    "woodcrash0": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_wood_01",
        1.77828,
        1,
        200
    ],
    "woodcrash1": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_wood_02",
        1.77828,
        1,
        200
    ],
    "woodcrash2": [
        "A3/sounds_f/Vehicles/boat/noises/Light_metal_boat_crash_wood_03",
        1.77828,
        1,
        200
    ]
}