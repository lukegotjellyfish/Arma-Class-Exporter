d = {
    "_generalmacro": "APC_Tracked_02_base_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 2.23,
    "accelaidforceyoffset": -4.1,
    "access": 0,
    "accuracy": 0.3,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left",
            "Left2"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationsourcehatch": "",
    "animationsources": {
        "ramp": {
            "animperiod": 5,
            "initphase": 0,
            "sound": "ServoRampSound_2",
            "soundposition": "Ramp_01_axis",
            "source": "door"
        }
    },
    "antirollbarforcecoef": 20,
    "antirollbarforcelimit": 10,
    "antirollbarspeedmax": 55,
    "antirollbarspeedmin": 10,
    "armor": 50,
    "armorcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "armorcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "armorcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "armorcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
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
    "armorstructural": 500,
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
        "rhs_attachcargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Attach cargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_pts_cargoAttach}else{[_this] call rhs_fnc_pts_cargoDetach};",
            "property": "rhs_attachCargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action"
        },
        "rhs_decalnumber": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHSPTSNumberPlaces}else{[_this, [['Number', cRHSPTSNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHSPTSNumberPlaces, _value]]] call rhs_fnc_decalsInit",
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
        },
        "rhs_openramp": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open ramp",
            "expression": "_this animateDoor ['ramp',_value];",
            "property": "rhs_opendoors"
        }
    },
    "audible": 18,
    "author": "RHS (A2 port)",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 0.1,
    "buildcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "buildcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "buildcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "buildcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
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
    "canfloat": 1,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_BMP3_Cargo"
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
        1
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
        0.434783,
        0.434783,
        0,
        0.913043,
        0.608696,
        0.934783,
        0.652174,
        0.934783,
        0.652174,
        1,
        0.73913
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 18,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "2+4+8",
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
        "amphibiousratios": [
            "R1",
            -9.5,
            "N",
            0,
            "D1",
            9.5
        ],
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -3.31,
            "N",
            0,
            "D1",
            3.31,
            "D2",
            1.934,
            "D3",
            1.132,
            "D4",
            0.662
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1,
        "transmissionratios": [
            "High",
            18.5
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
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            },
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            }
        },
        "vehiclesystemsdisplaymanagercomponentright": {
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            },
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            }
        }
    },
    "cost": 1500000.0,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crew": "rhssaf_army_m93_oakleaf_summer_crew",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.999,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_pts/data/rhs_pts.rvmat",
            "rhsafrf/addons/rhs_pts/data/rhs_dam_pts.rvmat",
            "rhsafrf/addons/rhs_pts/data/rhs_destr_pts.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00845,
    "damagetexdelay": 0,
    "dampersbumpcoef": 4.5,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "dampingratezerothrottleclutchengaged": 3,
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
    "displayname": "PTS-M",
    "dlc": "RHS_SAF",
    "driveoncomponent": [
        "Track_L",
        "Track_R",
        "Slide"
    ],
    "driveraction": "RHS_BMP3_driverout",
    "drivercaneject": 1,
    "drivercansee": "2+4+8",
    "drivercompartments": "Compartment1",
    "driverdoor": "hatchD",
    "driverforceoptics": 0,
    "driverinaction": "RHS_BMP3_driver",
    "driverinfopanelcamerapos": "driverview_old",
    "driveriscommander": 1,
    "driverlefthandanimname": "steering",
    "driverleftleganimname": "pedal_brake",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "steering",
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
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/rhs_pts_vmf.paa",
    "editorsubcategory": "rhs_EdSubcat_apc",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 0,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablewatch": 0,
    "engineeffectspeed": 5,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 10,
    "enginepower": 261,
    "engineshifty": 0.1,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "postinit": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "engine": "if((_this select 0) doorPhase 'ramp'> 0)then{_this select 0 engineOn false}else{[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay};",
            "init": "_this call rhs_fnc_pts_init"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide",
            "position": "exhaustl"
        },
        "exhaust2": {
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide",
            "position": "exhaustr"
        }
    },
    "explosioneffect": "FuelExplosionBig",
    "explosionshielding": 1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2,
        -15
    ],
    "faction": "rhssaf_faction_army",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "emptyEffect",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 672,
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
    "gunnercansee": "2+4+8",
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
        "n1",
        "n2",
        "n3"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 0.45,
            "armorcomponent": "hit_engine",
            "explosionshielding": 0.009,
            "material": -1,
            "minimalhit": 0.139,
            "name": "motor",
            "passthrough": 0,
            "radius": 0.27,
            "visual": "-"
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
            "armor": 0.4,
            "armorcomponent": "hit_hull",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.44,
            "name": "telo",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "zbytek"
        },
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "hit_trackL",
            "explosionshielding": 0.15,
            "material": -1,
            "minimalhit": -0.25,
            "name": "pas_L",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_L"
        },
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "hit_trackR",
            "explosionshielding": 0.15,
            "material": -1,
            "minimalhit": -0.25,
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
    "icon": "rhsafrf/addons/rhs_c_pts/ptsm_map_ca.paa",
    "idlerpm": 800,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.9,
    "irscanground": 2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "laserscanner": 0,
    "lasertarget": 0,
    "latency": 0.7,
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
    "loddriveropticsin": 1202,
    "loddriverturnedout": 0,
    "magazines": [],
    "mapsize": 11,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.1,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 240.86,
    "maxspeed": 46,
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
    "minomega": 85,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsafrf/addons/rhs_pts/rhs_pts",
    "namesound": "veh_vehicle_APC_s",
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
    "peaktorque": 1650,
    "picture": "rhsafrf/addons/rhs_pts/ui/pts_ca.paa",
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
    "radartype": 0,
    "redrpm": 2300,
    "reflectors": {
        "left": {
            "ambient": [
                5,
                5,
                5
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
                1900,
                1300,
                950
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec l svetla",
            "flaresize": 1,
            "hitpoint": "l svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 0
        },
        "left2": {
            "ambient": [
                5,
                5,
                5
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
                1900,
                1300,
                950
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec l svetla",
            "flaresize": 1,
            "hitpoint": "l svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number',cRHSPTSNumberPlaces,'Default']"
    ],
    "rhs_fuelcapacity": 672,
    "rhs_maxcargomasscoeff": 5e-08,
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
    "side": 2,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.5,
    "smokelauncherangle": 120,
    "smokelaunchergrenadecount": 8,
    "smokelauncheronturret": 0,
    "smokelaunchervelocity": 14,
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
        "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_stop",
        0.630957,
        1,
        200
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_stop",
        0.707946,
        1
    ],
    "soundengineonext": [
        "/rhsafrf/addons/rhs_bmp/sounds/utd20_start.wss",
        0.630957,
        1,
        200
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_start",
        0.707946,
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
        "A3/sounds_f/vehicles/armor/noises/get_in_out",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/sounds_f/vehicles/armor/noises/get_in_out",
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
        "engine": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(700/\t5200),(1100/\t5200)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                0.794328,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(705/\t5200),(850/\t5200)])\t*\t((rpm/\t5200) factor[(1100 /\t5200),(950/\t5200)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(950/\t5200),(1400/\t5200)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                0.794328,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(900/\t5200),(1050/\t5200)])\t*\t((rpm/\t5200) factor[(1400/\t5200),(1200/\t5200)]))"
        },
        "engine1_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(950/\t5200),(1400/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm2",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(900/\t5200),(1050/\t5200)])\t*\t((rpm/\t5200) factor[(1400/\t5200),(1200/\t5200)]))"
        },
        "engine1_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(950/\t5200),(1400/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm2",
                1.25893,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(900/\t5200),(1050/\t5200)])\t*\t((rpm/\t5200) factor[(1400/\t5200),(1200/\t5200)]))"
        },
        "engine1_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(950/\t5200),(1400/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm2",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(900/\t5200),(1050/\t5200)])\t*\t((rpm/\t5200) factor[(1400/\t5200),(1200/\t5200)]))"
        },
        "engine2_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1200/\t5200),(1700/\t5200)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                0.891251,
                1,
                250
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(1170/\t5200),(1380/\t5200)])\t*\t((rpm/\t5200) factor[(1700/\t5200),(1500/\t5200)]))"
        },
        "engine2_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1200/\t5200),(1700/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm3",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(1170/\t5200),(1380/\t5200)])\t*\t((rpm/\t5200) factor[(1700/\t5200),(1500/\t5200)]))"
        },
        "engine2_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1200/\t5200),(1700/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm3",
                1.41254,
                1,
                250
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1170/\t5200),(1380/\t5200)])\t*\t((rpm/\t5200) factor[(1700/\t5200),(1500/\t5200)]))"
        },
        "engine2_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1200/\t5200),(1700/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm3",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1170/\t5200),(1380/\t5200)])\t*\t((rpm/\t5200) factor[(1700/\t5200),(1500/\t5200)]))"
        },
        "engine3_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1500/\t5200),(2100/\t5200)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                1,
                1,
                300
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(1500/\t5200),(1670/\t5200)])\t*\t((rpm/\t5200) factor[(2100/\t5200),(1800/\t5200)]))"
        },
        "engine3_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1500/\t5200),(2100/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm4",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(1500/\t5200),(1670/\t5200)])\t*\t((rpm/\t5200) factor[(2100/\t5200),(1800/\t5200)]))"
        },
        "engine3_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1500/\t5200),(2100/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm4",
                1.58489,
                1,
                350
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1500/\t5200),(1670/\t5200)])\t*\t((rpm/\t5200) factor[(2100/\t5200),(1800/\t5200)]))"
        },
        "engine3_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1500/\t5200),(2100/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm4",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1500/\t5200),(1670/\t5200)])\t*\t((rpm/\t5200) factor[(2100/\t5200),(1800/\t5200)]))"
        },
        "engine4_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1800/\t5200),(2300/\t5200)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                1.12202,
                1,
                340
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(1780/\t5200),(2060/\t5200)])\t*\t((rpm/\t5200) factor[(2450/\t5200),(2200/\t5200)]))"
        },
        "engine4_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1800/\t5200),(2300/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm5",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(1780/\t5200),(2060/\t5200)])\t*\t((rpm/\t5200) factor[(2450/\t5200),(2200/\t5200)]))"
        },
        "engine4_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1800/\t5200),(2300/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm5",
                1.77828,
                1,
                400
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1780/\t5200),(2060/\t5200)])\t*\t((rpm/\t5200) factor[(2450/\t5200),(2200/\t5200)]))"
        },
        "engine4_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(1800/\t5200),(2300/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm5",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(1780/\t5200),(2060/\t5200)])\t*\t((rpm/\t5200) factor[(2450/\t5200),(2200/\t5200)]))"
        },
        "engine5_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(2100/\t5200),(2640/\t5200)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20.ogg",
                1.41254,
                1,
                400
            ],
            "volume": "engineOn*camPos*((rpm/\t5200) factor[(2150/\t5200),(2500/\t5200)])"
        },
        "engine5_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(2100/\t5200),(2640/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm6",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*((rpm/\t5200) factor[(2150/\t5200),(2500/\t5200)])"
        },
        "engine5_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(2100/\t5200),(2640/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm6",
                1.99526,
                1,
                450
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t5200) factor[(2150/\t5200),(2500/\t5200)])"
        },
        "engine5_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(2100/\t5200),(2640/\t5200)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm6",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t5200) factor[(2150/\t5200),(2500/\t5200)])"
        },
        "engine_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(700/\t5200),(1100/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_rpm1",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(705/\t5200),(850/\t5200)])\t*\t((rpm/\t5200) factor[(1100 /\t5200),(950/\t5200)]))"
        },
        "enginethrust": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(700/\t5200),(1100/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_rpm1",
                1.12202,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(705/\t5200),(850/\t5200)])\t*\t((rpm/\t5200) factor[(1100 /\t5200),(950/\t5200)]))"
        },
        "enginethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(700/\t5200),(1100/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_rpm1",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(705/\t5200),(850/\t5200)])\t*\t((rpm/\t5200) factor[(1100 /\t5200),(950/\t5200)]))"
        },
        "idle_ext": {
            "frequency": "0.95\t+\t((rpm/\t5200) factor[(400/\t5200),(900/\t5200)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_idle",
                0.707946,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(100/\t5200),(200/\t5200)])\t*\t((rpm/\t5200) factor[(900/\t5200),(700/\t5200)]))"
        },
        "idle_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(400/\t5200),(900/\t5200)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_idle",
                0.316228,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t5200) factor[(100/\t5200),(200/\t5200)])\t*\t((rpm/\t5200) factor[(900/\t5200),(700/\t5200)]))"
        },
        "idlethrust": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(400/\t5200),(900/\t5200)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_ext_idle",
                0.891251,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(100/\t5200),(200/\t5200)])\t*\t((rpm/\t5200) factor[(900/\t5200),(700/\t5200)]))"
        },
        "idlethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(400/\t5200),(900/\t5200)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_exhaust_int_idle",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t5200) factor[(100/\t5200),(200/\t5200)])\t*\t((rpm/\t5200) factor[(900/\t5200),(700/\t5200)]))"
        },
        "noiseext": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/noises/noise_tank_ext_1",
                0.794328,
                1,
                150
            ],
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        "noiseint": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/noises/noise_tank_int_1",
                0.562341,
                1
            ],
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        "threadsinh0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_01",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsinh1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_02",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsinh2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_03",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsinh3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_04",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsinh4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_hard_05",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        },
        "threadsins0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_01",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsins1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_02",
                0.354813,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsins2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_03",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsins3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_04",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsins4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/int_treads_soft_05",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        },
        "threadsouth0": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.398107,
                1,
                140
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouth1": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.446684,
                1,
                160
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouth2": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_3.ogg",
                0.501187,
                1,
                180
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouth3": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_4.ogg",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouth4": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_5.ogg",
                0.562341,
                1,
                220
            ],
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        },
        "threadsouts0": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.316228,
                1,
                120
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouts1": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.354813,
                1,
                140
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouts2": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_3.ogg",
                0.398107,
                1,
                160
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouts3": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_4.ogg",
                0.446684,
                1,
                180
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouts4": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_5.ogg",
                0.501187,
                1,
                200
            ],
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        }
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
    "tankturnforce": 200000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.82,
    "tbody": 250,
    "textplural": "PTS",
    "textsingular": "PTS",
    "texturetrackwheel": 0,
    "tf_range_api": 35000,
    "threat": [
        0.8,
        0.6,
        0.6
    ],
    "thrustdelay": 0.3,
    "torquecurve": [
        [
            0,
            0
        ],
        [
            0.478261,
            0.866667
        ],
        [
            0.521739,
            0.984848
        ],
        [
            0.565217,
            1
        ],
        [
            0.608696,
            0.987879
        ],
        [
            0.695652,
            0.909091
        ],
        [
            0.869565,
            0.8
        ],
        [
            1.13217,
            0
        ]
    ],
    "tracksspeed": 1.35,
    "transmissionlosses": 15,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhs_sidor": {
            "backpack": "rhs_sidor",
            "count": 7
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 4,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 1,
            "name": "Medikit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 1,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
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
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
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
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "EmptyDisplay",
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
                1000,
                1100,
                1200,
                1300,
                1400,
                1500,
                1600,
                1700,
                1800,
                1900,
                2000,
                2100,
                2200,
                2300,
                2400,
                2500,
                2600,
                2700,
                2800,
                2900,
                3000
            ],
            "discretedistanceinitindex": 2,
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
            "gunneraction": "Gunner_APC_tracked_02_cannon_F_out",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInAMV_cargo",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "Gunner_APC_tracked_02_cannon_F_in",
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
                    "armorcomponent": "hit_main_gun",
                    "explosionshielding": 0.4,
                    "isgun": 1,
                    "material": -1,
                    "minimalhit": 0.1,
                    "name": "hit_main_gun_point",
                    "passthrough": 0,
                    "radius": 0.2,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.8,
                    "armorcomponent": "hit_main_turret",
                    "explosionshielding": 0.2,
                    "isturret": 1,
                    "material": -1,
                    "minimalhit": 0.1,
                    "name": "hit_main_turret_point",
                    "passthrough": 0,
                    "radius": 0.25,
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
            "lodturnedout": -1,
            "magazines": [
                "2000Rnd_65x39_belt",
                "2000Rnd_65x39_belt"
            ],
            "maxcamelev": 90,
            "maxelev": 36,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 40,
            "maxoutturn": 150,
            "maxturn": 360,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": [
                "usti hlavne3"
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
            "minelev": -16,
            "minoutelev": -20,
            "minoutturn": -120,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "medium": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Gunner_MBT_02_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": "(150 * 0.05625 / 120)",
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": "(150 * 0.05625 / 120)",
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": "(150 * 0.05625 / 120)",
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                },
                "narrow": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Gunner_MBT_02_n_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": "(60 * 0.05625 / 120)",
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": "(60 * 0.05625 / 120)",
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": "(60 * 0.05625 / 120)",
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
                    ]
                },
                "wide": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Gunner_MBT_02_w_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": "(36 / 120)",
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": "(36 / 120)",
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": "(36 / 120)",
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "NVG",
                        "TI"
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
            "selectionfireanim": "zasleh2",
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
            "turretinfotype": "RscOptics_MBT_02_gunner",
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
                    "body": "obsTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 1,
                    "castgunnershadow": 0,
                    "commanding": 2,
                    "components": {
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
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
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
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
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
                    "gunneraction": "Commander_APC_tracked_02_cannon_F_out",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 0,
                    "gunnergetinaction": "GetInAMV_cargo",
                    "gunnergetoutaction": "GetOutLow",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "Commander_APC_tracked_02_cannon_F_in",
                    "gunnerlefthandanimname": "com_turret_control",
                    "gunnerleftleganimname": "",
                    "gunnername": "Commander",
                    "gunneropticscolor": [
                        0,
                        0,
                        0,
                        1
                    ],
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "A3/weapons_f/reticle/Optics_Commander_OPFOR_F",
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
                    "lodturnedout": -1,
                    "magazines": [
                        "SmokeLauncherMag"
                    ],
                    "maxcamelev": 90,
                    "maxelev": 60,
                    "maxhorizontalrotspeed": 1.8,
                    "maxoutelev": 40,
                    "maxoutturn": 120,
                    "maxturn": 360,
                    "maxverticalrotspeed": 1.8,
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
                    "minelev": -25,
                    "minoutelev": -20,
                    "minoutturn": -150,
                    "minturn": -360,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "medium": {
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Commander_02_m_F.p3d",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": "(150 * 0.05625 / 120)",
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": "(150 * 0.05625 / 120)",
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": "(150 * 0.05625 / 120)",
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                0,
                                1
                            ],
                            "visionmode": [
                                "Normal",
                                "NVG",
                                "TI"
                            ]
                        },
                        "narrow": {
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Commander_02_n_F.p3d",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": "(60 * 0.05625 / 120)",
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": "(60 * 0.05625 / 120)",
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": "(60 * 0.05625 / 120)",
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                0,
                                1
                            ],
                            "visionmode": [
                                "Normal",
                                "NVG",
                                "TI"
                            ]
                        },
                        "wide": {
                            "gunneropticseffect": [],
                            "gunneropticsmodel": "A3/Weapons_F/Reticle/Optics_Commander_02_w_F.p3d",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": "(36 / 120)",
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": "(36 / 120)",
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": "(36 / 120)",
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                0,
                                1
                            ],
                            "visionmode": [
                                "Normal",
                                "NVG",
                                "TI"
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
                    "turretinfotype": "RscOptics_MBT_02_commander",
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
                        "initfov": 0.4375,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.4375,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.03482,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "thermalmode": [
                            0,
                            1
                        ],
                        "visionmode": [
                            "Normal",
                            "NVG",
                            "Ti"
                        ]
                    },
                    "weapons": [
                        "SmokeLauncher"
                    ]
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
                "initfov": 0.4375,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.4375,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.03482,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "thermalmode": [
                    0,
                    1
                ],
                "visionmode": [
                    "Normal",
                    "TI"
                ]
            },
            "weapons": [
                "LMG_M200"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [
        "rhs_vmf_flora_crew_commander",
        "rhs_vmf_flora_crew",
        "rhs_vmf_flora_crew",
        ""
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoTank",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "useractions": {
        "closeramp": {
            "condition": "(this doorPhase 'ramp' == 1) AND {Alive(this)} AND {(call RHS_fnc_findPlayer) in this}",
            "displayname": "Close Cargo Ramp",
            "onlyforplayer": 1,
            "position": "ramp",
            "radius": 6,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateDoor ['ramp',0];[this] call rhs_fnc_pts_cargoAttach"
        },
        "openramp": {
            "condition": "(this doorPhase 'ramp' == 0) AND {Alive(this)} AND {(call RHS_fnc_findPlayer) in this} AND {((getPosASLW this) select 2) > -1}",
            "displayname": "Open Cargo Ramp",
            "onlyforplayer": 1,
            "position": "ramp",
            "radius": 6,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateDoor ['ramp',1];this engineOn false;[this] call rhs_fnc_pts_cargoDetach"
        }
    },
    "vehicleclass": "rhs_vehclass_apc",
    "vehicletransport": {
        "cargo": {
            "canbetransported": 1,
            "dimensions": [
                "BBox_1_1_pos",
                "BBox_1_2_pos"
            ],
            "parachuteclass": "O_Parachute_02_F",
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
            "disableheightlimit": 1,
            "exits": [
                "VVT_exit"
            ],
            "loadingangle": 60,
            "loadingdistance": 5,
            "maxloadmass": 25000,
            "parachuteclassdefault": "O_Parachute_02_F",
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
    "viewcargoshadowamb": 0.5,
    "viewcargoshadowdiff": 0.05,
    "viewdriverinexternal": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.25,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.13,
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
        "initanglex": -12,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 25,
        "maxangley": 135,
        "maxfov": 1,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -35,
        "minangley": -135,
        "minfov": 0.3,
        "minmovex": -0.075,
        "minmovey": -0.075,
        "minmovez": -0.075,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1,
    "waterangulardampingcoef": 1.2,
    "waterdamageengine": 0.9,
    "watereffectspeed": 5,
    "waterfasteffectspeed": 28,
    "waterleakiness": 250,
    "waterlineardampingcoefx": 2,
    "waterlineardampingcoefy": 2,
    "waterppinvehicle": 0,
    "waterresistance": 1,
    "waterresistancecoef": 0.175,
    "weapons": [],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1.922,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l7": {
            "bonename": "wheel_podkolol6",
            "boundary": "wheel_1_7_bound",
            "center": "wheel_1_7_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.3595,
            "side": "left",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r7": {
            "bonename": "wheel_podkolop6",
            "boundary": "wheel_2_7_bound",
            "center": "wheel_2_7_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 955,
            "frictionvsslipgraph": [
                [
                    0,
                    0.55
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.65,
                    0.7
                ]
            ],
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "mass": 93,
            "maxbraketorque": 25000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 10.3595,
            "side": "right",
            "springdamperrate": 7663,
            "springstrength": 92969,
            "sprungmass": 1306,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.2
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ],
    "woodcrash1": [
        "A3/sounds_f/Vehicles/crashes/crash_09",
        1,
        1,
        200
    ],
    "woodcrash2": [
        "A3/sounds_f/Vehicles/crashes/crash_10",
        1,
        1,
        200
    ],
    "woodcrash3": [
        "A3/sounds_f/Vehicles/crashes/crash_11",
        1,
        1,
        200
    ],
    "woodcrash4": [
        "A3/sounds_f/Vehicles/crashes/crash_01",
        1,
        1,
        200
    ],
    "woodcrash5": [
        "A3/sounds_f/Vehicles/crashes/crash_08",
        1,
        1,
        200
    ]
}