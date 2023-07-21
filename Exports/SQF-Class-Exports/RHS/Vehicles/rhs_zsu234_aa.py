d = {
    "_generalmacro": "APC_Tracked_02_base_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 1.9,
    "accelaidforceyoffset": -3.5,
    "access": 0,
    "accuracy": 0.3,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left",
            "Right"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationsourcehatch": "",
    "animationsources": {
        "hatchc": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchd": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchg": {
            "animperiod": 2.1,
            "source": "door"
        },
        "muzzle_rot1": {
            "source": "ammorandom",
            "weapon": "RHS_weap_AZP23"
        }
    },
    "antirollbarforcecoef": 20,
    "antirollbarforcelimit": 10,
    "antirollbarspeedmax": 55,
    "antirollbarspeedmin": 10,
    "armor": 200,
    "armorcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "armorcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "armorcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "armorcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
        1,
        200
    ],
    "armorcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "armorcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ],
    "armorlights": 0.1,
    "armorstructural": 600,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "TankAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_decalnumber": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHSZSUNumberPlaces}else{[_this, [['Number', cRHSZSUNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value,true];[_this,[['Number', cRHSZSUNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "typename": "STRING",
            "values": {
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                "default": {
                    "defaultvalue": "Default",
                    "name": "Default",
                    "value": "Default"
                },
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        }
    },
    "audible": 18,
    "author": "RHS",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 1.78,
    "buildcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "buildcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "buildcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "buildcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
        1,
        200
    ],
    "buildcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "buildcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ],
    "bushcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_01",
        0.630957,
        1,
        100
    ],
    "bushcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_02",
        0.630957,
        1,
        100
    ],
    "bushcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_Collision_Light_Bush_03",
        0.630957,
        1,
        100
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
    "camouflage": 8,
    "camshake": {
        "distance": 20,
        "frequency": 20,
        "minspeed": 5,
        "power": 5
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
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "passenger_apc_narrow_generic02",
        "passenger_apc_narrow_generic03",
        "passenger_apc_generic02",
        "passenger_apc_generic04",
        "passenger_apc_narrow_generic01",
        "passenger_generic01_foldhands",
        "passenger_generic01_leanleft",
        "passenger_generic01_leanright"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInAMV_cargo"
    ],
    "cargogetoutaction": [
        "GetOutLow"
    ],
    "cargoiscodriver": [
        0
    ],
    "cargolight": {
        "ambient": [
            0.6,
            0,
            0.15,
            1
        ],
        "brightness": 0.007,
        "color": [
            0,
            0,
            0,
            0
        ]
    },
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
    "category": "Armored",
    "changegearomegaratios": [
        1,
        0.7,
        0.75,
        0.55,
        0.65,
        0.5,
        0.75,
        0.7,
        0.75,
        0.7,
        0.75,
        0.55,
        1,
        0.5
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 80,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": 31,
    "commanderoptics": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "obsTurret",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "obsGun",
        "animationsourcehatch": "hatchCommander",
        "armorlights": 0.4,
        "body": "obsTurret",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 2,
        "disablesoundattenuation": 0,
        "dontcreateai": 0,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "obsGun",
        "gunbeg": "",
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
        "gunend": "",
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
        "gunnergetinaction": "GetInHigh",
        "gunnergetoutaction": "GetOutHigh",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "Commander",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "A3/weapons_f/reticle/Optics_Commander_02_F",
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
        "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
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
        "memorypointgun": "gun_muzzle",
        "memorypointgunneroptics": "commanderview",
        "memorypointgunneroutoptics": "commander_weapon_view",
        "memorypointsgetingunner": "pos commander",
        "memorypointsgetingunnerdir": "pos commander dir",
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
        "outgunnermayfire": 1,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 0,
        "primaryobserver": 1,
        "proxyindex": 1,
        "proxytype": "CPCommander",
        "reflectors": {},
        "selectionfireanim": "zasleh_1",
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
            0.01,
            1,
            10
        ],
        "stabilizedinaxes": 0,
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
    "compartmentslights": {
        "comp1": {
            "light1": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 1,
                "point": "light_interior1",
                "size": 0,
                "useflare": 0
            },
            "light10": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    20,
                    20,
                    20
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior10",
                "size": 0,
                "useflare": 0
            },
            "light11": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    20,
                    20,
                    20
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 5,
                "point": "light_interior11",
                "size": 0,
                "useflare": 0
            },
            "light2": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.3,
                "point": "light_interior2",
                "size": 0,
                "useflare": 0
            },
            "light3": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.4,
                "point": "light_interior3",
                "size": 0,
                "useflare": 0
            },
            "light4": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.5,
                "point": "light_interior4",
                "size": 0,
                "useflare": 0
            },
            "light5": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    10,
                    15,
                    17
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 0.3,
                "point": "light_interior5",
                "size": 0,
                "useflare": 0
            },
            "light6": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior6",
                "size": 0,
                "useflare": 0
            },
            "light7": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior7",
                "size": 0,
                "useflare": 0
            },
            "light8": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior8",
                "size": 0,
                "useflare": 0
            },
            "light9": {
                "ambient": [
                    0,
                    0,
                    0
                ],
                "attenuation": {
                    "constant": 0,
                    "hardlimitend": 1.15,
                    "hardlimitstart": 0.15,
                    "linear": 1,
                    "quadratic": 70,
                    "start": 0
                },
                "blinking": 0,
                "color": [
                    12,
                    12,
                    12
                ],
                "daylight": 0,
                "flaremaxdistance": 0,
                "flaresize": 0,
                "intensity": 3,
                "point": "light_interior9",
                "size": 0,
                "useflare": 0
            }
        }
    },
    "complexgearbox": {
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R2",
            -7,
            "N",
            0,
            "D1",
            1.25,
            "D2",
            1.2,
            "D3",
            1.15,
            "D4",
            1.05,
            "D5",
            0.95
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.6,
        "transmissionratios": [
            "High",
            15.8
        ]
    },
    "components": {
        "aitanksteeringcomponent": {
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "allowovertaking": 1,
            "allowturnaroundinpoint": 1,
            "commandturnfactor": 2,
            "convoypidweights": [
                1,
                0,
                0
            ],
            "differenceanglecoef": 1,
            "dopredictforward": 1,
            "doremapspeed": 0,
            "forwardanglecoef": 0.7,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.01,
            "predictforwardmaxspeed": 15,
            "predictforwardrange": [
                1,
                20
            ],
            "remapspeedrange": [
                30,
                70
            ],
            "remapspeedscalar": [
                1,
                0.35
            ],
            "speedpidweights": [
                0.7,
                0.2,
                0
            ],
            "speedpredictionmethod": 3,
            "steeraheadsaturation": [
                0.01,
                0.4
            ],
            "steeringanglecoef": 1,
            "steeringpidweights": [
                2.9,
                0.1,
                0.2
            ],
            "stuckmaxtime": 3,
            "wheelanglecoef": 0.7
        },
        "sensorsmanagercomponent": {
            "components": {
                "activeradarsensorcomponent": {
                    "aimdown": -35,
                    "airtarget": {
                        "maxrange": 14000,
                        "minrange": 14000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 100,
                    "animdirection": "",
                    "color": [
                        0,
                        1,
                        1,
                        1
                    ],
                    "componenttype": "ActiveRadarSensorComponent",
                    "groundnoisedistancecoef": 0.05,
                    "groundtarget": {
                        "maxrange": -1,
                        "minrange": -1,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxfogseethrough": 1,
                    "maxgroundnoisedistance": 60,
                    "maxspeedthreshold": 90,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 555,
                    "minspeedthreshold": 20,
                    "mintrackableatl": 50,
                    "mintrackablespeed": 25,
                    "typerecognitiondistance": 4000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
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
                    "componenttype": "CrewDisplayComponent"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 1500000.0,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crew": "rhs_msv_crew",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.999,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_01.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_01_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_01_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_02.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_02_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_02_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_03.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_03_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_03_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_track.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_track_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_armor/data/ZSU_track_destruct.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.02,
    "damagetexdelay": 0,
    "dampersbumpcoef": 4.5,
    "dampingratefullthrottle": 0.8,
    "dampingratezerothrottleclutchdisengaged": 0.5,
    "dampingratezerothrottleclutchengaged": 4,
    "destrtype": "DestructDefault",
    "destructioneffects": {
        "firebig1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionFire1"
        },
        "firebig2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionFire2"
        },
        "firesparksbig1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "FireSparks"
        },
        "lightbig1": {
            "enabled": "distToWater",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "light",
            "type": "ObjectDestructionLight"
        },
        "refract1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionRefract"
        },
        "smokebig1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke"
        },
        "smokebig1_2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2"
        },
        "smokebig2": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2"
        },
        "sound": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "position": "destructionEffect1",
            "simulation": "sound",
            "type": "Fire"
        },
        "sparksbig1": {
            "intensity": 0,
            "interval": 1,
            "lifetime": 0,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSparks"
        }
    },
    "detectskill": 20,
    "displayname": "ZSU-23-4V",
    "dlc": "RHS_AFRF",
    "driveoncomponent": [
        "Slide"
    ],
    "driveraction": "RHS_ZSU_Driver",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "hatchD",
    "driverforceoptics": 1,
    "driverinaction": "RHS_ZSU_Driver",
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "drivingstick_left",
    "driverleftleganimname": "pedal_brake",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tnpo170a",
    "driverrighthandanimname": "drivingstick_right",
    "driverrightleganimname": "pedal_thrust",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dusteffects": {
        "both": {},
        "left": {
            "default": [
                "LDustEffects"
            ],
            "dirtrunway": [
                "LDustEffects"
            ],
            "gdtasphalt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtbeach": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtcliff": [
                "LDustEffects"
            ],
            "gdtconcrete": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtdead": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtdesert": [
                "LDustEffects",
                "LDirtEffectsBig",
                "LStonesEffects"
            ],
            "gdtdesert1": [
                "LDustEffects",
                "LDirtEffectsBig",
                "LStonesEffectsBig"
            ],
            "gdtdesert2": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtdirt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtfield": [
                "LDustEffects"
            ],
            "gdtforest": [
                "LDustEffects"
            ],
            "gdtgrassdry": [
                "LDustEffects",
                "LGrassEffectsDryBig",
                "LDirtEffectsBig"
            ],
            "gdtgrassgreen": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtgrassshort": [
                "LDustEffects",
                "LGrassEffectsBig"
            ],
            "gdtgrasstall": [
                "LDustEffects",
                "LGrassEffectsBig"
            ],
            "gdtgrasswild": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtkldirt": [
                "LDustEffects"
            ],
            "gdtklforestcon": [
                "LDustEffects"
            ],
            "gdtklforestdec": [
                "LDustEffects"
            ],
            "gdtklgrass1": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtklgrass2": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtklmud": [
                "LDustEffects"
            ],
            "gdtklsoil": [
                "LDustEffects"
            ],
            "gdtklstones": [
                "LStonesEffects"
            ],
            "gdtklstubble": [
                "LDustEffects"
            ],
            "gdtkltarmac": [
                "LDustEffects"
            ],
            "gdtreddirt": [
                "LDustEffectsRed"
            ],
            "gdtrock": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtrubble": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtseabed": [
                "LDustEffects"
            ],
            "gdtseabeddeep": [
                "LDustEffects"
            ],
            "gdtsoil": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstony": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstonygreen": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstonythistle": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisbeach": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtstratisconcrete": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstratisdirt": [
                "LDustEffects",
                "LDirtEffectsBig"
            ],
            "gdtstratisdrygrass": [
                "LDustEffects",
                "LGrassEffectsDryBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisgreengrass": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisrocky": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtstratisseabed": [
                "LDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffects"
            ],
            "gdtstratisthistles": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtthorn": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtvolcano": [
                "LDustEffects",
                "LStonesEffectsBig"
            ],
            "gdtvolcanobeach": [
                "LDustEffects"
            ],
            "gdtweed1": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtweed2": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "gdtwildfield": [
                "LDustEffects",
                "LGrassEffectsBig",
                "LDirtEffectsBig"
            ],
            "surfintconcrete": [
                "LDustEffects"
            ],
            "surfintmetal": [
                "LDustEffects"
            ],
            "surfinttiles": [
                "LDustEffects"
            ],
            "surfintwood": [
                "LDustEffects"
            ],
            "surfmetal": [
                "LDustEffects"
            ],
            "surfroadconcrete": [
                "LDustEffects"
            ],
            "surfroadconcrete_exp": [
                "LDustEffects"
            ],
            "surfroaddirt": [
                "LDustEffects"
            ],
            "surfroaddirt_enoch": [
                "LDustEffects"
            ],
            "surfroaddirt_exp": [
                "LDustEffectsRed"
            ],
            "surfroadtarmac": [
                "LDustEffects"
            ],
            "surfroadtarmac1_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac2_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac3_enoch": [
                "LDustEffects"
            ],
            "surfroadtarmac_exp": [
                "LDustEffects"
            ],
            "surfrooftiles": [
                "LDustEffects"
            ],
            "surfrooftin": [
                "LDustEffects"
            ],
            "surftraildirt_enoch": [
                "LDustEffects"
            ],
            "surfwood": [
                "LDustEffects"
            ]
        },
        "right": {
            "default": [
                "RDustEffects"
            ],
            "dirtrunway": [
                "RDustEffects"
            ],
            "gdtasphalt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtbeach": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtcliff": [
                "RDustEffects"
            ],
            "gdtconcrete": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtdead": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtdesert": [
                "RDustEffects",
                "RDirtEffectsBig",
                "RStonesEffects"
            ],
            "gdtdesert1": [
                "RDustEffects",
                "RDirtEffectsBig",
                "RStonesEffectsBig"
            ],
            "gdtdesert2": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtdirt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtfield": [
                "RDustEffects"
            ],
            "gdtforest": [
                "RDustEffects"
            ],
            "gdtgrassdry": [
                "RDustEffects",
                "RGrassEffectsDryBig",
                "RDirtEffectsBig"
            ],
            "gdtgrassgreen": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtgrassshort": [
                "RDustEffects",
                "RGrassEffectsBig"
            ],
            "gdtgrasstall": [
                "RDustEffects",
                "RGrassEffectsBig"
            ],
            "gdtgrasswild": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtkldirt": [
                "RDustEffects"
            ],
            "gdtklforestcon": [
                "RDustEffects"
            ],
            "gdtklforestdec": [
                "RDustEffects"
            ],
            "gdtklgrass1": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtklgrass2": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtklmud": [
                "RDustEffects"
            ],
            "gdtklsoil": [
                "RDustEffects"
            ],
            "gdtklstones": [
                "RStonesEffects"
            ],
            "gdtklstubble": [
                "RDustEffects"
            ],
            "gdtkltarmac": [
                "RDustEffects"
            ],
            "gdtreddirt": [
                "RDustEffectsRed"
            ],
            "gdtrock": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtrubble": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtseabed": [
                "RDustEffects"
            ],
            "gdtseabeddeep": [
                "RDustEffects"
            ],
            "gdtsoil": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstony": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstonygreen": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstonythistle": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisbeach": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtstratisconcrete": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstratisdirt": [
                "RDustEffects",
                "RDirtEffectsBig"
            ],
            "gdtstratisdrygrass": [
                "RDustEffects",
                "RGrassEffectsDryBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisgreengrass": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisrocky": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtstratisseabed": [
                "RDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffects"
            ],
            "gdtstratisthistles": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtthorn": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtvolcano": [
                "RDustEffects",
                "RStonesEffectsBig"
            ],
            "gdtvolcanobeach": [
                "RDustEffects"
            ],
            "gdtweed1": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtweed2": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "gdtwildfield": [
                "RDustEffects",
                "RGrassEffectsBig",
                "RDirtEffectsBig"
            ],
            "surfintconcrete": [
                "RDustEffects"
            ],
            "surfintmetal": [
                "RDustEffects"
            ],
            "surfinttiles": [
                "RDustEffects"
            ],
            "surfintwood": [
                "RDustEffects"
            ],
            "surfmetal": [
                "RDustEffects"
            ],
            "surfroadconcrete": [
                "RDustEffects"
            ],
            "surfroadconcrete_exp": [
                "RDustEffects"
            ],
            "surfroaddirt": [
                "RDustEffects"
            ],
            "surfroaddirt_enoch": [
                "RDustEffects"
            ],
            "surfroaddirt_exp": [
                "RDustEffectsRed"
            ],
            "surfroadtarmac": [
                "RDustEffects"
            ],
            "surfroadtarmac1_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac2_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac3_enoch": [
                "RDustEffects"
            ],
            "surfroadtarmac_exp": [
                "RDustEffects"
            ],
            "surfrooftiles": [
                "RDustEffects"
            ],
            "surfrooftin": [
                "RDustEffects"
            ],
            "surftraildirt_enoch": [
                "RDustEffects"
            ],
            "surfwood": [
                "RDustEffects"
            ]
        }
    },
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/rhs_zsu234_aa.paa",
    "editorsubcategory": "rhs_EdSubcat_aa",
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
    "enablewatch": 0,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 7,
    "enginepower": 209,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "postinit": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "rhs_eventhandlers": {
            "engine": "_this call rhs_fnc_engineCheckDamage;",
            "getout": "_this call rhs_fnc_hatchAbandon",
            "init": "_this call rhs_fnc_bmp3_init",
            "postinit": "_this call rhs_fnc_reapplyTextures"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectTankBack",
            "position": "exhaust"
        }
    },
    "explosioneffect": "FuelExplosionBig",
    "explosionshielding": 1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2.75,
        -9.5
    ],
    "faction": "rhs_faction_vpvo",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "emptyEffect",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 30,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "gearbox": [
        -7,
        0,
        11,
        8,
        5.7,
        4.2
    ],
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 3.5,
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
    "gunnercansee": "1+16+4+8",
    "gunnerhasflares": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.0075,
        0.005,
        0.0075
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
        "camo1",
        "camo2",
        "camo3",
        "n1",
        "n2",
        "n3"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/rhsafrf/addons/rhs_a2port_armor/data/zsu_01_co.paa",
        "/rhsafrf/addons/rhs_a2port_armor/data/zsu_02_co.paa",
        "/rhsafrf/addons/rhs_a2port_armor/data/zsu_03_co.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 0.45,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_engine_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallFireFPlace"
                },
                "rhs_engine_fire2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "SmallFireFPlace"
                },
                "rhs_engine_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_engine_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke3",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_smoke_small3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_engine_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_engine_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "RHS_FireSparks"
                },
                "rhs_engine_sparks2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "RHS_FireSparks"
                }
            },
            "explosionshielding": 0.05,
            "material": -1,
            "minimalhit": 0.03,
            "name": "motor",
            "passthrough": 0.01,
            "radius": 0.2,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 0.5,
            "armorcomponent": "hit_fuel",
            "explosionshielding": 0.6,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_fuel_point",
            "passthrough": 0.1,
            "radius": 0.3,
            "visual": "-"
        },
        "hithull": {
            "armor": 0.45,
            "armorcomponent": "hit_hull",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.14,
            "name": "telo",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "zbytek"
        },
        "hitltrack": {
            "armor": 0.5,
            "armorcomponent": "hit_trackL",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.15,
            "name": "pas_L",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_L"
        },
        "hitrtrack": {
            "armor": 0.5,
            "armorcomponent": "hit_trackR",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.15,
            "name": "pas_P",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_P"
        },
        "hitslat_back": {
            "armor": -200,
            "armorcomponent": "cage_back_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_back_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_front": {
            "armor": -200,
            "armorcomponent": "cage_front_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_front_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_1": {
            "armor": -200,
            "armorcomponent": "cage_left_1_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_1_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_2": {
            "armor": -200,
            "armorcomponent": "cage_left_2_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_2_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_left_3": {
            "armor": -200,
            "armorcomponent": "cage_left_3_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_left_3_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_1": {
            "armor": -200,
            "armorcomponent": "cage_right_1_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_1_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_2": {
            "armor": -200,
            "armorcomponent": "cage_right_2_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_2_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        },
        "hitslat_right_3": {
            "armor": -200,
            "armorcomponent": "cage_right_3_geo",
            "explosionshielding": 2,
            "minimalhit": 0.3,
            "name": "cage_right_3_point",
            "passthrough": 0,
            "radius": 0.25,
            "simulation": "Armor_SLAT",
            "visual": "-"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsafrf/addons/rhs_a2port_armor/data/icomap_zsu_CA.paa",
    "idlerpm": 600,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.9,
    "irscanground": 0,
    "irscanrangemax": 19000,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 1,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "latency": 1.1,
    "leftdusteffect": "LDustEffects",
    "leftdusteffects": [
        [
            "GdtKLDirt",
            "LDustEffects"
        ],
        [
            "GdtKLGrass1",
            "LDustEffects"
        ],
        [
            "GdtKLGrass1",
            "LGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "LDustEffects"
        ],
        [
            "GdtKLGrass2",
            "LGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "LDustEffects"
        ],
        [
            "GdtKLForestDec",
            "LDustEffects"
        ],
        [
            "GdtKlMud",
            "LDustEffects"
        ],
        [
            "GdtKlSoil",
            "LDustEffects"
        ],
        [
            "GdtKlTarmac",
            "LDustEffects"
        ],
        [
            "GdtKlStubble",
            "LDustEffects"
        ],
        [
            "GdtKlStones",
            "LStonesEffects"
        ],
        [
            "SurfRoadDirt_Enoch",
            "LDustEffects"
        ],
        [
            "SurfTrailDirt_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "LDustEffects"
        ],
        [
            "GdtGrassShort",
            "LDustEffects"
        ],
        [
            "GdtGrassShort",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassTall",
            "LDustEffects"
        ],
        [
            "GdtGrassTall",
            "LGrassEffectsBig"
        ],
        [
            "GdtRedDirt",
            "LDustEffectsRed"
        ],
        [
            "GdtField",
            "LDustEffects"
        ],
        [
            "GdtForest",
            "LDustEffects"
        ],
        [
            "GdtVolcano",
            "LDustEffects"
        ],
        [
            "GdtVolcano",
            "LStonesEffectsBig"
        ],
        [
            "GdtCliff",
            "LDustEffects"
        ],
        [
            "GdtVolcanoBeach",
            "LDustEffects"
        ],
        [
            "SurfRoadDirt_exp",
            "LDustEffectsRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac_exp",
            "LDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "LDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisBeach",
            "LDustEffects"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffectsBig"
        ],
        [
            "GdtStratisDirt",
            "LDustEffects"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisSeabedCluttered",
            "LDustEffects"
        ],
        [
            "GdtStratisSeabed",
            "LDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LGrassEffectsDryBig"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "LDustEffects"
        ],
        [
            "GdtStratisRocky",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "LDirtEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "LDustEffects"
        ],
        [
            "GdtStratisThistles",
            "LGrassEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "LDirtEffectsBig"
        ],
        [
            "GdtConcrete",
            "LDustEffects"
        ],
        [
            "GdtConcrete",
            "LDirtEffectsBig"
        ],
        [
            "GdtAsphalt",
            "LDustEffects"
        ],
        [
            "GdtAsphalt",
            "LDirtEffectsBig"
        ],
        [
            "GdtRubble",
            "LDustEffects"
        ],
        [
            "GdtRubble",
            "LDirtEffectsBig"
        ],
        [
            "GdtSoil",
            "LDustEffects"
        ],
        [
            "GdtSoil",
            "LDirtEffectsBig"
        ],
        [
            "GdtBeach",
            "LDustEffects"
        ],
        [
            "GdtBeach",
            "LStonesEffectsBig"
        ],
        [
            "GdtRock",
            "LDustEffects"
        ],
        [
            "GdtRock",
            "LDirtEffectsBig"
        ],
        [
            "GdtDead",
            "LDustEffects"
        ],
        [
            "GdtDead",
            "LDirtEffectsBig"
        ],
        [
            "Default",
            "LDustEffects"
        ],
        [
            "GdtDesert",
            "LDustEffects"
        ],
        [
            "GdtDesert",
            "LDirtEffectsBig"
        ],
        [
            "GdtDesert",
            "LStonesEffects"
        ],
        [
            "GdtDesert1",
            "LDustEffects"
        ],
        [
            "GdtDesert1",
            "LDirtEffectsBig"
        ],
        [
            "GdtDesert1",
            "LStonesEffectsBig"
        ],
        [
            "GdtDesert2",
            "LDustEffects"
        ],
        [
            "GdtDesert2",
            "LGrassEffectsBig"
        ],
        [
            "GdtDesert2",
            "LDirtEffectsBig"
        ],
        [
            "GdtDirt",
            "LDustEffects"
        ],
        [
            "GdtDirt",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "LDustEffects"
        ],
        [
            "GdtGrassGreen",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassDry",
            "LDustEffects"
        ],
        [
            "GdtGrassDry",
            "LGrassEffectsDryBig"
        ],
        [
            "GdtGrassDry",
            "LDirtEffectsBig"
        ],
        [
            "GdtGrassWild",
            "LDustEffects"
        ],
        [
            "GdtGrassWild",
            "LGrassEffectsBig"
        ],
        [
            "GdtGrassWild",
            "LDirtEffectsBig"
        ],
        [
            "GdtWildField",
            "LDustEffects"
        ],
        [
            "GdtWildField",
            "LGrassEffectsBig"
        ],
        [
            "GdtWildField",
            "LDirtEffectsBig"
        ],
        [
            "GdtWeed1",
            "LDustEffects"
        ],
        [
            "GdtWeed1",
            "LGrassEffectsBig"
        ],
        [
            "GdtWeed1",
            "LDirtEffectsBig"
        ],
        [
            "GdtWeed2",
            "LDustEffects"
        ],
        [
            "GdtWeed2",
            "LGrassEffectsBig"
        ],
        [
            "GdtWeed2",
            "LDirtEffectsBig"
        ],
        [
            "GdtThorn",
            "LDustEffects"
        ],
        [
            "GdtThorn",
            "LGrassEffectsBig"
        ],
        [
            "GdtThorn",
            "LDirtEffectsBig"
        ],
        [
            "GdtStony",
            "LDustEffects"
        ],
        [
            "GdtStony",
            "LGrassEffectsBig"
        ],
        [
            "GdtStony",
            "LDirtEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "LDustEffects"
        ],
        [
            "GdtStonyGreen",
            "LGrassEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "LDirtEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "LDustEffects"
        ],
        [
            "GdtStonyThistle",
            "LGrassEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "LDirtEffectsBig"
        ],
        [
            "GdtSeabedDeep",
            "LDustEffects"
        ],
        [
            "GdtSeabed",
            "LDustEffects"
        ],
        [
            "SurfRoadDirt",
            "LDustEffects"
        ],
        [
            "SurfRoadConcrete",
            "LDustEffects"
        ],
        [
            "SurfRoadTarmac",
            "LDustEffects"
        ],
        [
            "SurfWood",
            "LDustEffects"
        ],
        [
            "SurfMetal",
            "LDustEffects"
        ],
        [
            "SurfRoofTin",
            "LDustEffects"
        ],
        [
            "SurfRoofTiles",
            "LDustEffects"
        ],
        [
            "SurfIntWood",
            "LDustEffects"
        ],
        [
            "SurfIntConcrete",
            "LDustEffects"
        ],
        [
            "SurfIntTiles",
            "LDustEffects"
        ],
        [
            "SurfIntMetal",
            "LDustEffects"
        ],
        [
            "dirtrunway",
            "RDustEffects"
        ]
    ],
    "leftfastwatereffect": "LWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "library": {
        "libtextdesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "loddriveropticsin": 0,
    "loddriveropticsout": 0,
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "magazines": [],
    "mapsize": 6.5,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 209.44,
    "maxspeed": 50,
    "memorypointcargolight": "cargo light",
    "memorypointdriveroptics": "driverview",
    "memorypointmissile": [
        "spice rakety",
        "usti hlavne"
    ],
    "memorypointmissiledir": [
        "konec rakety",
        "konec hlavne"
    ],
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
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
    "mfact": 1,
    "mfd": {
        "mfd_commander_ammoindicator_main_armament": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            0.39,
                            0.28
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.13
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.13
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_2": {
                    "align": "left",
                    "down": [
                        [
                            0.39,
                            0.38
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.23
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.23
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_3": {
                    "align": "left",
                    "down": [
                        [
                            0.39,
                            0.48
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.39,
                            0.33
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.45,
                            0.33
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 2,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_armament_ammo_type_1": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.28
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.13
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.13
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0411\u0420",
                    "type": "text"
                },
                "main_armament_ammo_type_2": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.38
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.23
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.23
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0424",
                    "type": "text"
                },
                "main_armament_ammo_type_3": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.48
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.33
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.33
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0420",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_coax_ammo": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_ammo_count_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            1.32,
                            1
                        ],
                        1
                    ],
                    "pos": [
                        [
                            1.32,
                            0.2
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.97,
                            0.2
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_ammo_count_TL",
            "topright": "mfd_com_ammo_count_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_coax_magazines": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_mag_count_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            0.1,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.11
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.85,
                            0.11
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_mag_count_TL",
            "topright": "mfd_com_mag_count_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_display": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "azimut": {
                    "align": "center",
                    "down": [
                        [
                            0.71,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.71,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.77,
                            0.8
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "commander_armament": {
                    "align": "center",
                    "down": [
                        [
                            0.795,
                            0.125
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.795,
                            0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.845,
                            0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0420\u0423\u0414\u0418\u0415 \u041a\u041e\u041c\u0410\u041d\u0414\u0418\u0420\u0410",
                    "type": "text"
                },
                "commander_armament_magazines": {
                    "align": "center",
                    "down": [
                        [
                            0.47,
                            0.55
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.47,
                            0.4
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.53,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041c\u0410\u0413.",
                    "type": "text"
                },
                "commander_machinegun": {
                    "align": "center",
                    "down": [
                        [
                            0.81,
                            0.34
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.81,
                            0.19
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.87,
                            0.19
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "----",
                    "type": "text"
                },
                "condition": "1",
                "damage": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.82
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.82
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u041e\u0412\u0420\u0415\u0416\u0414\u0415\u041d\u0418\u042f",
                    "type": "text"
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.925,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.925,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.985,
                            0.8
                        ],
                        1
                    ],
                    "scale": 0.2,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_distance_elevation": {
                    "align": "center",
                    "down": [
                        [
                            0.73,
                            0.75
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.73,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.785,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0414\u0410\u041b\u042c\u041d\u041e\u0421\u0422\u042c",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.925,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.925,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.985,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "machinegun": {
                    "align": "center",
                    "down": [
                        [
                            0.51,
                            0.145
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.51,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.57,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u0423\u041b\u0415\u041c\u0415\u0422",
                    "type": "text"
                },
                "main_armament": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.145
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0413\u041b\u0410\u0412\u041d\u041e\u0415 \u041e\u0420\u0423\u0414\u0418\u0415",
                    "type": "text"
                },
                "main_armament_ammo_type": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0422\u0418\u041f \u0410\u041c\u0423\u041d\u0418\u0426\u0418\u0418",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_main_armament_ammo_type": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.36,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.36,
                            0.61
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.42,
                            0.61
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "turret": [
                0
            ]
        },
        "mfd_commander_ready_to_fire": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_cli_BL",
            "color": [
                0,
                0,
                0
            ],
            "draw": {
                "alpha": 1,
                "bottom_text": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.92
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.41
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.7,
                            0.41
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0413\u041e\u0422\u041e\u0412",
                    "type": "text"
                },
                "color": [
                    0,
                    0,
                    0
                ],
                "condition": "1",
                "top_text": {
                    "align": "center",
                    "down": [
                        [
                            0.48,
                            0.56
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.48,
                            0.05
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.68,
                            0.05
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u041a \u0421\u0422\u0420\u0415\u041b\u042c\u0411\u0415",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_cli_TL",
            "topright": "mfd_com_cli_TR"
        },
        "mfd_commander_second_display": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_7_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "crosshair": {
                    "points": [
                        [
                            [
                                0.5,
                                0.423413
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.346429
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.5,
                                0.577381
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.654365
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.55,
                                0.500397
                            ],
                            1
                        ],
                        [
                            [
                                0.6,
                                0.500397
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4,
                                0.500397
                            ],
                            1
                        ],
                        [
                            [
                                0.45,
                                0.500397
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.346429
                            ],
                            1
                        ],
                        [
                            [
                                0.3,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.269444
                            ],
                            1
                        ],
                        [
                            [
                                0.35,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.7,
                                0.346429
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.65,
                                0.269444
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.269444
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.7,
                                0.654365
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.65,
                                0.731349
                            ],
                            1
                        ],
                        [
                            [
                                0.7,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.654365
                            ],
                            1
                        ],
                        [
                            [
                                0.3,
                                0.731349
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3,
                                0.731349
                            ],
                            1
                        ],
                        [
                            [
                                0.35,
                                0.731349
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line",
                    "width": 3
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.83,
                            0.33
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.83,
                            0.25
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.88,
                            0.25
                        ],
                        1
                    ],
                    "scale": 0.2,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.494,
                            0.88
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.494,
                            0.8
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.544,
                            0.8
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_range_background": {
                    "background": {
                        "points": [
                            [
                                [
                                    [
                                        0.43,
                                        0.81
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.57,
                                        0.81
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.57,
                                        0.87
                                    ],
                                    1
                                ],
                                [
                                    [
                                        0.43,
                                        0.87
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
                }
            },
            "enableparallax": 0,
            "font": "EtelkaMonospacePro",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_7_TL",
            "topright": "MFD_7_TR",
            "turret": [
                0,
                0
            ]
        },
        "mfd_commander_smoke_indicator": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_com_smoke_BL",
            "color": [
                0,
                0,
                0
            ],
            "draw": {
                "alpha": 1,
                "bottom_text": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.4
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.7,
                            0.4
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0417\u0410\u0412\u0415\u0421\u0410",
                    "type": "text"
                },
                "color": [
                    0,
                    0,
                    0
                ],
                "condition": "1",
                "top_text": {
                    "align": "center",
                    "down": [
                        [
                            0.47,
                            0.5
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.47,
                            0
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.67,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcescale": 1,
                    "text": "\u0414\u042b\u041c\u041e\u0412\u0410\u042f",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_com_smoke_TL",
            "topright": "mfd_com_smoke_TR"
        },
        "mfd_driver_heading": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_1_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.61,
                    0.62,
                    0
                ],
                "condition": "on",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR"
        },
        "mfd_driver_heading_second": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_Driver_2_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.81
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.95,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_Driver_2_TL",
            "topright": "MFD_Driver_2_TR"
        },
        "mfd_driver_heading_text": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_Driver_1_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "driver_heading": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.87
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0.02
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.7,
                            0.02
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_Driver_1_TL",
            "topright": "MFD_Driver_1_TR"
        },
        "mfd_gunner_ammoindicator": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_3_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.92,
                    0.01,
                    0
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.3
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.3,
                            0
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1000,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_2": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.6
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.3
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.3,
                            0.3
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1001,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_3": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.6
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.3,
                            0.6
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1002,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_3_TL",
            "topright": "MFD_3_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_ammoindicator_main_armament": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "left",
                    "down": [
                        [
                            0.395,
                            0.143
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.065
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourceprecision": 1,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_2": {
                    "align": "left",
                    "down": [
                        [
                            0.395,
                            0.203
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.125
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.125
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 0,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "gunner_text_3": {
                    "align": "left",
                    "down": [
                        [
                            0.395,
                            0.263
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.395,
                            0.185
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.455,
                            0.185
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 2,
                    "sourcelength": 2,
                    "sourcescale": 1,
                    "type": "text"
                },
                "main_armament_ammo_type_1": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.143
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.065
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0411\u0420",
                    "type": "text"
                },
                "main_armament_ammo_type_2": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.203
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.125
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.125
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041e\u0424",
                    "type": "text"
                },
                "main_armament_ammo_type_3": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.263
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.185
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.185
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0420",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_ammotype": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_5_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    0.92,
                    0.01,
                    0
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.455,
                            0.76
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.455,
                            0.05
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            1.355,
                            0.05
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "LCD14",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_coax_ammo": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_text_1": {
                    "align": "center",
                    "down": [
                        [
                            0.31,
                            0.388
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.31,
                            0.31
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.37,
                            0.31
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_display": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 1,
                "azimut": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.993
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.915
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.915
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0410\u0417\u0418\u041c\u0423\u0422",
                    "type": "text"
                },
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "damage": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.468
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.39
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.39
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u041e\u0412\u0420\u0415\u0416\u0414\u0415\u041d\u0418\u042f",
                    "type": "text"
                },
                "heading": {
                    "align": "center",
                    "down": [
                        [
                            0.34,
                            0.993
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.34,
                            0.915
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.4,
                            0.915
                        ],
                        1
                    ],
                    "scale": 0.2,
                    "source": "[x]turretworld",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                },
                "lased_distance_elevation": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.918
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.84
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.84
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0414\u0410\u041b\u042c\u041d\u041e\u0421\u0422\u042c",
                    "type": "text"
                },
                "lased_range": {
                    "align": "center",
                    "down": [
                        [
                            0.34,
                            0.918
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.34,
                            0.84
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.4,
                            0.84
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "laserDist",
                    "sourcelength": 4,
                    "sourcescale": 1,
                    "type": "text"
                },
                "machinegun": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.388
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            0.31
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            0.31
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041f\u0423\u041b\u0415\u041c\u0415\u0422",
                    "type": "text"
                },
                "main_armament": {
                    "align": "right",
                    "down": [
                        [
                            0.015,
                            0.073
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.015,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.075,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0413\u041b\u0410\u0412\u041d\u041e\u0415 \u041e\u0420\u0423\u0414\u0418\u0415",
                    "type": "text"
                },
                "main_armament_ammo_type": {
                    "align": "center",
                    "down": [
                        [
                            0.55,
                            0.073
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.55,
                            -0.005
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.61,
                            -0.005
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0422\u0418\u041f \u0410\u041c\u0423\u041d\u0418\u0426\u0418\u0418",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_main_armament_ammo_type": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_BL",
            "color": [
                0.84,
                0.86,
                0.84
            ],
            "draw": {
                "alpha": 1,
                "color": [
                    1,
                    1,
                    1
                ],
                "condition": "1",
                "gunner_ammotype": {
                    "align": "center",
                    "down": [
                        [
                            0.555,
                            0.185
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.555,
                            0.065
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.635,
                            0.065
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "ammoFormat",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "turret": [
                0
            ]
        },
        "mfd_gunner_ready_to_fire": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "mfd_gun_cli_BL",
            "color": [
                0,
                0,
                0
            ],
            "draw": {
                "alpha": 1,
                "bottom_text": {
                    "align": "center",
                    "down": [
                        [
                            0.465,
                            0.95
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.465,
                            0.45
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.685,
                            0.45
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u0413\u041e\u0422\u041e\u0412",
                    "type": "text"
                },
                "color": [
                    0,
                    0,
                    0
                ],
                "condition": "1",
                "top_text": {
                    "align": "center",
                    "down": [
                        [
                            0.45,
                            0.55
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.45,
                            0.05
                        ],
                        1
                    ],
                    "refreshrate": 0.1,
                    "right": [
                        [
                            0.67,
                            0.05
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "sourcelength": 3,
                    "sourcescale": 1,
                    "text": "\u041a \u0421\u0422\u0420\u0415\u041b\u042c\u0411\u0415",
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            "material": {
                "ambient": [
                    1,
                    1,
                    1,
                    1
                ],
                "diffuse": [
                    1,
                    1,
                    1,
                    1
                ],
                "emissive": [
                    1000,
                    1000,
                    1000,
                    1
                ]
            },
            "topleft": "mfd_gun_cli_TL",
            "topright": "mfd_gun_cli_TR"
        }
    },
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
    "minomega": 61,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsafrf/addons/rhs_a2port_armor/rhs_zsu",
    "namesound": "veh_vehicle_tank_s",
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
    "normalspeedforwardcoef": 0.7,
    "numberphysicalwheels": 16,
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
    "nvgmarkers": {
        "nvgmarker01": {
            "ambient": [
                0.003,
                0.0003,
                0.0003,
                1
            ],
            "blinking": 1,
            "brightness": 0.001,
            "color": [
                0.03,
                0.003,
                0.003,
                1
            ],
            "name": "nvg_marker"
        }
    },
    "nvscanner": 0,
    "nvtarget": 0,
    "obstructsoundlfratio": 0,
    "obstructsoundswhenin": 0,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0,
    "outsidesoundfilter": 1,
    "peaktorque": 1176,
    "picture": "rhsafrf/addons/rhs_a2port_armor/pictures/rhs_zsu23_pic_ca.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 10,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.2,
    "radartype": 4,
    "receiveremotetargets": 1,
    "redrpm": 2000,
    "reflectors": {
        "left": {
            "ambient": [
                0.1,
                0.1,
                0.1,
                1
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 60,
                "hardlimitstart": 30,
                "linear": 0,
                "quadratic": 0.25,
                "start": 1
            },
            "color": [
                190,
                130,
                95
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec L svetla",
            "flaresize": 1,
            "hitpoint": "L svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 0
        },
        "right": {
            "ambient": [
                0.1,
                0.1,
                0.1,
                1
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 60,
                "hardlimitstart": 30,
                "linear": 0,
                "quadratic": 0.25,
                "start": 1
            },
            "color": [
                190,
                130,
                95
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec P svetla",
            "flaresize": 1,
            "hitpoint": "P svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 0
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number',cRHSZSUNumberPlaces,'Default']"
    ],
    "rhs_fuelcapacity": 520,
    "rightdusteffect": "RDustEffects",
    "rightdusteffects": [
        [
            "GdtKLDirt",
            "RDustEffects"
        ],
        [
            "GdtKLGrass1",
            "RDustEffects"
        ],
        [
            "GdtKLGrass1",
            "RGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "RDustEffects"
        ],
        [
            "GdtKLGrass2",
            "RGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "RDustEffects"
        ],
        [
            "GdtKLForestDec",
            "RDustEffects"
        ],
        [
            "GdtKlMud",
            "RDustEffects"
        ],
        [
            "GdtKlSoil",
            "RDustEffects"
        ],
        [
            "GdtKlTarmac",
            "RDustEffects"
        ],
        [
            "GdtKlStubble",
            "RDustEffects"
        ],
        [
            "GdtKlStones",
            "RStonesEffects"
        ],
        [
            "SurfRoadDirt_Enoch",
            "RDustEffects"
        ],
        [
            "SurfTrailDirt_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "RDustEffects"
        ],
        [
            "GdtGrassShort",
            "RDustEffects"
        ],
        [
            "GdtGrassShort",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassTall",
            "RDustEffects"
        ],
        [
            "GdtGrassTall",
            "RGrassEffectsBig"
        ],
        [
            "GdtRedDirt",
            "RDustEffectsRed"
        ],
        [
            "GdtField",
            "RDustEffects"
        ],
        [
            "GdtForest",
            "RDustEffects"
        ],
        [
            "GdtVolcano",
            "RDustEffects"
        ],
        [
            "GdtVolcano",
            "RStonesEffectsBig"
        ],
        [
            "GdtCliff",
            "RDustEffects"
        ],
        [
            "GdtVolcanoBeach",
            "RDustEffects"
        ],
        [
            "SurfRoadDirt_exp",
            "RDustEffectsRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac_exp",
            "RDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "RDustEffects"
        ],
        [
            "GdtStratisConcrete",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisBeach",
            "RDustEffects"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffectsBig"
        ],
        [
            "GdtStratisDirt",
            "RDustEffects"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisSeabedCluttered",
            "RDustEffects"
        ],
        [
            "GdtStratisSeabed",
            "RDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDustEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RGrassEffectsDryBig"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisGreenGrass",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "RDustEffects"
        ],
        [
            "GdtStratisRocky",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisRocky",
            "RDirtEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "RDustEffects"
        ],
        [
            "GdtStratisThistles",
            "RGrassEffectsBig"
        ],
        [
            "GdtStratisThistles",
            "RDirtEffectsBig"
        ],
        [
            "GdtConcrete",
            "RDustEffects"
        ],
        [
            "GdtConcrete",
            "RDirtEffectsBig"
        ],
        [
            "GdtAsphalt",
            "RDustEffects"
        ],
        [
            "GdtAsphalt",
            "RDirtEffectsBig"
        ],
        [
            "GdtRubble",
            "RDustEffects"
        ],
        [
            "GdtRubble",
            "RDirtEffectsBig"
        ],
        [
            "GdtSoil",
            "RDustEffects"
        ],
        [
            "GdtSoil",
            "RDirtEffectsBig"
        ],
        [
            "GdtBeach",
            "RDustEffects"
        ],
        [
            "GdtBeach",
            "RStonesEffectsBig"
        ],
        [
            "GdtRock",
            "RDustEffects"
        ],
        [
            "GdtRock",
            "RDirtEffectsBig"
        ],
        [
            "GdtDead",
            "RDustEffects"
        ],
        [
            "GdtDead",
            "RDirtEffectsBig"
        ],
        [
            "Default",
            "RDustEffects"
        ],
        [
            "GdtDesert",
            "RDustEffects"
        ],
        [
            "GdtDesert",
            "RDirtEffectsBig"
        ],
        [
            "GdtDesert",
            "RStonesEffects"
        ],
        [
            "GdtDesert1",
            "RDustEffects"
        ],
        [
            "GdtDesert1",
            "RDirtEffectsBig"
        ],
        [
            "GdtDesert1",
            "RStonesEffectsBig"
        ],
        [
            "GdtDesert2",
            "RDustEffects"
        ],
        [
            "GdtDesert2",
            "RGrassEffectsBig"
        ],
        [
            "GdtDesert2",
            "RDirtEffectsBig"
        ],
        [
            "GdtDirt",
            "RDustEffects"
        ],
        [
            "GdtDirt",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "RDustEffects"
        ],
        [
            "GdtGrassGreen",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassGreen",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassDry",
            "RDustEffects"
        ],
        [
            "GdtGrassDry",
            "RGrassEffectsDryBig"
        ],
        [
            "GdtGrassDry",
            "RDirtEffectsBig"
        ],
        [
            "GdtGrassWild",
            "RDustEffects"
        ],
        [
            "GdtGrassWild",
            "RGrassEffectsBig"
        ],
        [
            "GdtGrassWild",
            "RDirtEffectsBig"
        ],
        [
            "GdtWildField",
            "RDustEffects"
        ],
        [
            "GdtWildField",
            "RGrassEffectsBig"
        ],
        [
            "GdtWildField",
            "RDirtEffectsBig"
        ],
        [
            "GdtWeed1",
            "RDustEffects"
        ],
        [
            "GdtWeed1",
            "RGrassEffectsBig"
        ],
        [
            "GdtWeed1",
            "RDirtEffectsBig"
        ],
        [
            "GdtWeed2",
            "RDustEffects"
        ],
        [
            "GdtWeed2",
            "RGrassEffectsBig"
        ],
        [
            "GdtWeed2",
            "RDirtEffectsBig"
        ],
        [
            "GdtThorn",
            "RDustEffects"
        ],
        [
            "GdtThorn",
            "RGrassEffectsBig"
        ],
        [
            "GdtThorn",
            "RDirtEffectsBig"
        ],
        [
            "GdtStony",
            "RDustEffects"
        ],
        [
            "GdtStony",
            "RGrassEffectsBig"
        ],
        [
            "GdtStony",
            "RDirtEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "RDustEffects"
        ],
        [
            "GdtStonyGreen",
            "RGrassEffectsBig"
        ],
        [
            "GdtStonyGreen",
            "RDirtEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "RDustEffects"
        ],
        [
            "GdtStonyThistle",
            "RGrassEffectsBig"
        ],
        [
            "GdtStonyThistle",
            "RDirtEffectsBig"
        ],
        [
            "GdtSeabedDeep",
            "RDustEffects"
        ],
        [
            "GdtSeabed",
            "RDustEffects"
        ],
        [
            "SurfRoadDirt",
            "RDustEffects"
        ],
        [
            "SurfRoadConcrete",
            "RDustEffects"
        ],
        [
            "SurfRoadTarmac",
            "RDustEffects"
        ],
        [
            "SurfWood",
            "RDustEffects"
        ],
        [
            "SurfMetal",
            "RDustEffects"
        ],
        [
            "SurfRoofTin",
            "RDustEffects"
        ],
        [
            "SurfRoofTiles",
            "RDustEffects"
        ],
        [
            "SurfIntWood",
            "RDustEffects"
        ],
        [
            "SurfIntConcrete",
            "RDustEffects"
        ],
        [
            "SurfIntTiles",
            "RDustEffects"
        ],
        [
            "SurfIntMetal",
            "RDustEffects"
        ],
        [
            "dirtrunway",
            "RDustEffects"
        ]
    ],
    "rightfastwatereffect": "RWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionbrakelights": "brzdove svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 2.5,
    "sensitivityear": "0.0075 /3",
    "sensorposition": "gunnerView",
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
    "side": 0,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.6435,
    "smokelauncherangle": 120,
    "smokelaunchergrenadecount": 8,
    "smokelauncheronturret": 0,
    "smokelaunchervelocity": 14,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.166,
        "ArmorCrash1",
        0.166,
        "ArmorCrash2",
        0.166,
        "ArmorCrash3",
        0.166,
        "ArmorCrash4",
        0.166,
        "ArmorCrash5",
        0.166
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
        0.166,
        "buildCrash1",
        0.166,
        "buildCrash2",
        0.166,
        "buildCrash3",
        0.166,
        "buildCrash4",
        0.166,
        "buildCrash5",
        0.166
    ],
    "soundburning": {},
    "soundbushcrash": [
        "BushCrash1",
        0.33,
        "BushCrash2",
        0.33,
        "BushCrash3",
        0.33
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
        0.562341,
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
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Ext_Stop",
        1.99526,
        1,
        70
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Int_Stop",
        0.707946,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Ext_Start",
        1.99526,
        1,
        70
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles2/armor/MBT_03/MBT_03_Engine_Int_Start",
        0.501187,
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
        0.000316228,
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
        "A3/Sounds_F_EPB/Tracked/noises/get_in_out",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F_EPB/Tracked/noises/get_in_out",
        0.562341,
        1,
        20
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_4",
        0.398107,
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
        "/A3/Sounds_F/weapons/Rockets/locked_1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "soundsetsext": [
            "APC_Tracked_02_Engine_RPM0_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM1_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM2_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM3_EXT_SoundSet",
            "APC_Tracked_02_Engine_RPM4_EXT_SoundSet",
            "APC_Tracked_02_Tracks_01_EXT_SoundSet",
            "APC_Tracked_02_Tracks_02_EXT_SoundSet",
            "APC_Tracked_02_Tracks_03_EXT_SoundSet",
            "APC_Tracked_02_Tracks_04_EXT_SoundSet",
            "APC_Tracked_02_Tracks_05_EXT_SoundSet",
            "APC_Tracked_02_Tracks_06_EXT_SoundSet",
            "APC_Tracked_02_Rattling_EXT_SoundSet",
            "APC_Tracked_02_Rain_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Hard_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Soft_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Hard_EXT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Soft_EXT_SoundSet",
            "APC_Tracked_02_Drive_Water_EXT_SoundSet",
            "APC_Tracked_02_Drive_Dirt_EXT_SoundSet",
            "Tracks_Movement_Dirt_Ext_01_SoundSet",
            "Tracks_Surface_Soft_Ext_SoundSet",
            "Tracks_Surface_Sand_Ext_SoundSet",
            "Tracks_Surface_Squeaks_Soft_Ext_SoundSet",
            "Tracks_Surface_Squeaks_Hard_Ext_SoundSet"
        ],
        "soundsetsint": [
            "APC_Tracked_02_Engine_RPM0_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM1_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM2_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM3_INT_SoundSet",
            "APC_Tracked_02_Engine_RPM4_INT_SoundSet",
            "APC_Tracked_02_Tracks_01_INT_SoundSet",
            "APC_Tracked_02_Tracks_02_INT_SoundSet",
            "APC_Tracked_02_Tracks_03_INT_SoundSet",
            "APC_Tracked_02_Tracks_04_INT_SoundSet",
            "APC_Tracked_02_Tracks_05_INT_SoundSet",
            "APC_Tracked_02_Tracks_06_INT_SoundSet",
            "APC_Tracked_02_Interior_Tone_Engine_Off_SoundSet",
            "APC_Tracked_02_Interior_Tone_Engine_On_SoundSet",
            "APC_Tracked_02_Rattling_INT_SoundSet",
            "APC_Tracked_02_Stress_INT_SoundSet",
            "APC_Tracked_02_Rain_INT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Hard_INT_SoundSet",
            "APC_Tracked_02_Tracks_Brake_Soft_INT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Hard_INT_SoundSet",
            "APC_Tracked_02_Tracks_Turn_Soft_INT_SoundSet",
            "APC_Tracked_02_Drive_Water_INT_SoundSet",
            "APC_Tracked_02_Drive_Dirt_INT_SoundSet",
            "Tracks_Movement_Dirt_Int_01_SoundSet",
            "Tracks_Surface_Soft_Int_SoundSet",
            "Tracks_Surface_Sand_Int_SoundSet",
            "Tracks_Surface_Squeaks_Soft_Int_SoundSet",
            "Tracks_Surface_Squeaks_Hard_Int_SoundSet",
            "Tanks_Material_Strain_Int_SoundSet"
        ]
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundturnin": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnininternal": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnout": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
    ],
    "soundturnoutinternal": [
        "A3/Sounds_F/vehicles/noises/Turn_in_out",
        1.77828,
        1,
        20
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
                "veh_vehicle_tank_p"
            ],
            "speechsingular": [
                "veh_vehicle_tank_s"
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
    "steeraheadplan": 0.4,
    "steeraheadsimul": 0.3,
    "supplyradius": -1,
    "switchtime": 0,
    "tankturnforce": 330000,
    "tankturnforceangminspd": 0.6,
    "tankturnforceangspd": 0.91,
    "tbody": 250,
    "textplural": "tanks",
    "textsingular": "tank",
    "texturelist": [],
    "texturesources": {
        "cdf": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [],
            "textures": [
                "/rhsgref/addons/rhsgref_vehicles_ret/data/cdf/zsu_01_cdf_co.paa",
                "/rhsgref/addons/rhsgref_vehicles_ret/data/cdf/zsu_02_cdf_co.paa",
                "/rhsgref/addons/rhsgref_vehicles_ret/data/cdf/zsu_03_cdf_co.paa"
            ]
        },
        "chdkz": {
            "displayname": "Chedaki",
            "factions": [],
            "textures": [
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_01_gue_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_02_gue_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_03_gue_co.paa"
            ]
        },
        "rhs_sand": {
            "author": "beaar",
            "displayname": "Sand",
            "factions": [],
            "textures": [
                "/rhsafrf/addons/rhs_a2port_armor_camo/data/zsu_01_des_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor_camo/data/zsu_02_des_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor_camo/data/zsu_03_des_co.paa"
            ]
        },
        "standard": {
            "displayname": "Standard",
            "factions": [
                "rhs_faction_vpvo"
            ],
            "textures": [
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_01_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_02_co.paa",
                "/rhsafrf/addons/rhs_a2port_armor/data/zsu_03_co.paa"
            ]
        },
        "takistan": {
            "author": "Red Hammer Studios",
            "displayname": "Takistan",
            "factions": [],
            "textures": [
                "/rhsgref/addons/rhsgref_vehicles_ret/data/tak/zsu_01_tk_co.paa",
                "/rhsgref/addons/rhsgref_vehicles_ret/data/tak/zsu_02_tk_co.paa",
                "/rhsgref/addons/rhsgref_vehicles_ret/data/tak/zsu_03_tk_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "threat": [
        0.5,
        0.5,
        1
    ],
    "thrustdelay": 0.6,
    "torquecurve": [
        [
            0,
            0
        ],
        [
            0.3,
            0.757238
        ],
        [
            0.4,
            0.868597
        ],
        [
            0.6,
            0.957684
        ],
        [
            0.7,
            1
        ],
        [
            0.8,
            0.746102
        ],
        [
            1,
            0.534521
        ],
        [
            1.5,
            0
        ]
    ],
    "tracksspeed": 1,
    "transmissionlosses": 15,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 4,
            "name": "FirstAidKit"
        }
    },
    "transportmagazines": {
        "_xx_30rnd_545x39_ak": {
            "count": "10",
            "magazine": "rhs_30Rnd_545x39_7N10_AK"
        },
        "_xx_handgrenade_east": {
            "count": "10",
            "magazine": "rhs_mag_rgd5"
        },
        "_xx_signal_rounds": {
            "count": "10",
            "magazine": "rhs_mag_nspn_red"
        }
    },
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_ak74m": {
            "count": 1,
            "weapon": "rhs_weap_ak74m"
        }
    },
    "turncoef": 5,
    "turrets": {
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "armorlights": 0.4,
            "body": "mainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": 1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                2000,
                                4000,
                                8000,
                                16000
                            ],
                            "resource": "RscCustomInfoSensors"
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
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                2000,
                                4000,
                                8000,
                                16000
                            ],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "SensorDisplay",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "discretedistance": [
                100,
                200,
                300,
                400,
                500,
                600,
                700,
                800,
                900,
                1000
            ],
            "discretedistanceinitindex": 5,
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
            "gunneraction": "RHS_ZSU_GunnerOut",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchG",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInAMV_cargo",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_ZSU_Gunner",
            "gunnerlefthandanimname": "turret_control",
            "gunnerleftleganimname": "",
            "gunnername": "Gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [
                "TankGunnerOptics2",
                "OpticsBlur1",
                "OpticsCHAbera1"
            ],
            "gunneropticsmodel": "A3/weapons_f/reticle/Optics_Gunner_02_F",
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
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.2,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.2,
                    "visual": "vez"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 1,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "ispersonturret": 1,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 0,
            "lodturnedin": -1,
            "lodturnedout": 1100,
            "magazines": [
                "rhs_mag_AZP23_2000"
            ],
            "maxcamelev": 90,
            "maxelev": 85,
            "maxhorizontalrotspeed": 0.94,
            "maxoutelev": 40,
            "maxoutturn": 150,
            "maxturn": 360,
            "maxverticalrotspeed": 0.6,
            "memorypointgun": [
                "chase01",
                "chase02",
                "chase03",
                "chase04"
            ],
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
            "minelev": -4.5,
            "minoutelev": -20,
            "minoutturn": -120,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "auto": {
                    "directionstabilized": 1,
                    "gunneropticseffect": [
                        "TankGunnerOptics1",
                        "OpticsBlur2",
                        "OpticsCHAbera2"
                    ],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_a2port_armor/2Dscope_RUAA8",
                    "gunneroutopticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.175,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.175,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.175,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal"
                    ]
                },
                "wide": {
                    "gunneropticseffect": [
                        "TankGunnerOptics1",
                        "OpticsBlur2",
                        "OpticsCHAbera2"
                    ],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_a2port_armor/2Dscope_RUAA8",
                    "gunneroutopticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.35,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.35,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.35,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal"
                    ]
                }
            },
            "outgunnermayfire": 0,
            "personturretaction": "vehicle_turnout_2",
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
            "showcrewaim": 2,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_gunner",
                0.562341,
                1,
                10
            ],
            "soundservovertical": [
                "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_gunner_vertical",
                0.562341,
                1,
                30
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
            "turretinfotype": "RscWeaponZeroing",
            "turrets": {
                "commanderoptics": {
                    "aggregatereflectors": [],
                    "allowlauncherin": 0,
                    "allowlauncherout": 0,
                    "allowtablock": 1,
                    "animationsourcebody": "obsTurret",
                    "animationsourcecamelev": "camElev",
                    "animationsourcegun": "obsGun",
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "armorlights": 0.4,
                    "body": "ObsTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 1,
                    "castgunnershadow": 0,
                    "commanding": 2,
                    "components": {
                        "aicarsteeringcomponent": {
                            "allowcollisionavoidance": 1,
                            "allowdrifting": 0,
                            "allowovertaking": 1,
                            "commandturnfactor": 1,
                            "differenceanglecoef": 1,
                            "dopredictforward": 1,
                            "doremapspeed": 1,
                            "forwardanglecoef": 0.7,
                            "maxwheelanglediff": 0.2616,
                            "minspeedtokeep": 0.1,
                            "predictforwardrange": [
                                0.1,
                                20
                            ],
                            "remapspeedrange": [
                                40,
                                50
                            ],
                            "remapspeedscalar": [
                                1,
                                0.35
                            ],
                            "speedpidweights": [
                                1.7,
                                1.3,
                                1.1
                            ],
                            "speedpredictionmethod": 1,
                            "steeraheadsaturation": [
                                0.01,
                                0.4
                            ],
                            "steeringanglecoef": 1,
                            "steeringpidweights": [
                                1.2,
                                0.1,
                                0.2
                            ],
                            "stuckmaxtime": 3,
                            "wheelanglecoef": 0.7
                        },
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            "components": {
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent",
                                    "resource": "RscCustomInfoCrew"
                                },
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                "sensordisplay": {
                                    "componenttype": "SensorsDisplayComponent",
                                    "range": [
                                        2000,
                                        4000,
                                        8000,
                                        14000
                                    ],
                                    "resource": "RscCustomInfoSensors"
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
                                "sensordisplay": {
                                    "componenttype": "SensorsDisplayComponent",
                                    "range": [
                                        2000,
                                        4000,
                                        8000,
                                        14000
                                    ],
                                    "resource": "RscCustomInfoSensors"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "defaultdisplay": "SensorDisplay",
                            "right": 1,
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "disablesoundattenuation": 0,
                    "dontcreateai": 0,
                    "ejectdeadgunner": 0,
                    "forcehidegunner": 0,
                    "forcenvg": 0,
                    "gun": "ObsGun",
                    "gunbeg": "gun_muzzle",
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
                    "gunend": "gun_chamber",
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
                    "gunneraction": "RHS_ZSU_CommanderOut",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "hatchC",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 1,
                    "gunnergetinaction": "GetInAMV_cargo",
                    "gunnergetoutaction": "GetOutLow",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "RHS_ZSU_Commander",
                    "gunnerlefthandanimname": "com_turret_control",
                    "gunnerleftleganimname": "",
                    "gunnername": "Commander",
                    "gunneropticscolor": [
                        0,
                        0,
                        0,
                        1
                    ],
                    "gunneropticseffect": [
                        "TankCommanderOptics1"
                    ],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
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
                        "hitcomgun": {
                            "armor": 0.04,
                            "armorcomponent": "hit_com_gun",
                            "explosionshielding": 1,
                            "isgun": 1,
                            "material": -1,
                            "minimalhit": 0.1,
                            "name": "hit_com_gun_point",
                            "passthrough": 0,
                            "radius": 0.15,
                            "visual": "zbranVelitele"
                        },
                        "hitcomturret": {
                            "armor": 0.08,
                            "armorcomponent": "hit_com_turret",
                            "explosionshielding": 1,
                            "isturret": 1,
                            "material": -1,
                            "minimalhit": 0.1,
                            "name": "hit_com_turret_point",
                            "passthrough": 0.4,
                            "radius": 0.15,
                            "visual": "vezVelitele"
                        }
                    },
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
                    "lodopticsin": 0,
                    "lodturnedin": -1,
                    "lodturnedout": 1100,
                    "magazines": [],
                    "maxcamelev": 90,
                    "maxelev": 60,
                    "maxhorizontalrotspeed": 2,
                    "maxoutelev": 40,
                    "maxoutturn": 120,
                    "maxturn": 360,
                    "maxverticalrotspeed": 2,
                    "memorypointgun": "gun_muzzle",
                    "memorypointgunneroptics": "commanderview",
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
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
                    "minelev": -10,
                    "minoutelev": -20,
                    "minoutturn": -150,
                    "minturn": -360,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "periscope": {
                            "gunneropticseffect": [
                                "TankGunnerOptics1",
                                "OpticsBlur2",
                                "OpticsCHAbera2"
                            ],
                            "gunneropticsmodel": "a3/weapons_f/reticle/Optics_Driver_01_f",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.26,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.26,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.26,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                0,
                                1
                            ],
                            "visionmode": [
                                "Normal"
                            ]
                        },
                        "wide": {
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.111,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.111,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.111,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                0,
                                1
                            ],
                            "visionmode": [
                                "Normal",
                                "NVG"
                            ]
                        }
                    },
                    "outgunnermayfire": 0,
                    "personturretaction": "vehicle_turnout_1",
                    "playerposition": 0,
                    "precisegetinout": 0,
                    "primary": 1,
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "proxyindex": 1,
                    "proxytype": "CPCommander",
                    "reflectors": {},
                    "selectionfireanim": "zasleh_1",
                    "showalltargets": 0,
                    "showcrewaim": 1,
                    "showhmd": 0,
                    "slingloadoperator": 0,
                    "soundelevation": [
                        "",
                        0.00316228,
                        1
                    ],
                    "soundservo": [
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        0.562341,
                        1,
                        30
                    ],
                    "soundservovertical": [
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        0.562341,
                        1,
                        30
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
                    "turretfollowfreelook": 2,
                    "turretinfotype": "RscWeaponEmpty",
                    "turrets": {},
                    "turretspec": {
                        "showheadphones": 0
                    },
                    "usepip": 2,
                    "viewgunner": {
                        "initanglex": -5,
                        "initangley": 0,
                        "initfov": 0.9,
                        "maxanglex": 85,
                        "maxangley": 150,
                        "maxfov": 1.25,
                        "maxmovex": 0.075,
                        "maxmovey": 0.075,
                        "maxmovez": 0.1,
                        "minanglex": -65,
                        "minangley": -150,
                        "minfov": 0.25,
                        "minmovex": -0.075,
                        "minmovey": -0.075,
                        "minmovez": -0.075,
                        "speedzoommaxfov": 0,
                        "speedzoommaxspeed": 10000000000.0
                    },
                    "viewgunnerinexternal": 1,
                    "viewgunnershadow": 1,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "viewoptics": {
                        "initanglex": 0,
                        "initangley": 0,
                        "initfov": 0.111,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.111,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.111,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "thermalmode": [
                            0,
                            1
                        ],
                        "visionmode": [
                            "Normal",
                            "NVG"
                        ]
                    },
                    "weapons": []
                }
            },
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 1,
            "viewgunner": {
                "continuous": 0,
                "initanglex": -5,
                "initangley": 0,
                "initfov": 0.9,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0.075,
                "maxmovey": 0.075,
                "maxmovez": 0.1,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": -0.075,
                "minmovey": -0.075,
                "minmovez": -0.075,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 1,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.2,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.2,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.058,
                "visionmode": [
                    "Normal",
                    "NVG"
                ]
            },
            "weapons": [
                "RHS_weap_AZP23"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoEastTank",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "vehicleclass": "rhs_vehclass_aa",
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
    "viewcargoshadowamb": 0.5,
    "viewcargoshadowdiff": 0.05,
    "viewdriverinexternal": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.7,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.7,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0,
        "visionmode": [
            "Normal",
            "NVG"
        ]
    },
    "viewpilot": {
        "initanglex": -5,
        "initangley": 0,
        "initfov": 0.9,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": -0.075,
        "minmovey": -0.075,
        "minmovez": -0.075,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 0,
    "waterresistance": 0,
    "waterresistancecoef": 0.25,
    "weapons": [],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.18,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l7": {
            "bonename": "wheel_podkolol6",
            "boundary": "wheel_1_7_bound",
            "center": "wheel_1_7_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r7": {
            "bonename": "wheel_podkolop6",
            "boundary": "wheel_2_7_bound",
            "center": "wheel_2_7_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 2114,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 2114,
            "frictionvsslipgraph": [
                [
                    0,
                    0.45
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.6,
                    0.6
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 150,
            "maxbraketorque": 8000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 150000,
            "sprungmass": -1,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_01",
        3.16228,
        1,
        200
    ],
    "woodcrash1": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_02",
        3.16228,
        1,
        200
    ],
    "woodcrash2": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_03",
        3.16228,
        1,
        200
    ],
    "woodcrash3": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_04",
        3.16228,
        1,
        200
    ],
    "woodcrash4": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_05",
        3.16228,
        1,
        200
    ],
    "woodcrash5": [
        "A3/Sounds_F/vehicles2/armor/shared/collisions/Vehicle_Armor_General_Collision_06",
        3.16228,
        1,
        200
    ]
}