d = {
    "_generalmacro": "Tank_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 2.83,
    "accelaidforceyoffset": -4,
    "access": 0,
    "accuracy": 0.3,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Driver_FG125_Cover",
            "Driver_FG125_Cover_Flare"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "autoloader": {
            "animperiod": 1.25,
            "initphase": 0,
            "source": "user"
        },
        "elev": {
            "animperiod": 0.0003,
            "source": "user"
        },
        "elev_bank": {
            "animperiod": 0.0003,
            "source": "user"
        },
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
        "hatchla": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchra": {
            "animperiod": 2.1,
            "source": "door"
        },
        "lead": {
            "animperiod": 0.0016,
            "source": "user"
        },
        "muzzle_hide_cannon": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a70"
        },
        "muzzle_rot_coax": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_bmd_coax"
        },
        "muzzle_rot_coax2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_bmd_bow1"
        },
        "muzzle_rot_coax3": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_bmd_bow2"
        },
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a72"
        },
        "offset": {
            "animperiod": 0.0002,
            "source": "user"
        },
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        "recoil_source2": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        }
    },
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmax": 75,
    "antirollbarspeedmin": 30,
    "armor": 200,
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
        "rhs_decalnumber": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHSBMP3NumberPlaces}else{[_this, [['Number', cRHSBMP3NumberPlaces, _this getVariable ['rhs_decalNumber_type','DefaultRed'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHSBMP3NumberPlaces, _value]]] call rhs_fnc_decalsInit",
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
        "rhs_decalplatoon": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set platoon symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHSBMP3PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoon",
            "tooltip": "Set platoon symbol located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoon_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define platoon symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoon_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
                    "defaultvalue": "Army",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        }
    },
    "audible": 18,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 1.78,
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
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "RHS_BMP3_Cargo",
        "YouShallNotSitHere"
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
    "cargoproxyindexes": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
    ],
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
        0.347222,
        0.347222,
        0,
        0.9375,
        0.347222,
        0.885417,
        0.659722,
        0.954861,
        0.659722,
        1,
        0.659722
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 30,
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
    "complexgearbox": {
        "amphibiousratios": [
            "R1",
            -10,
            "N",
            0,
            "D1",
            10
        ],
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -2.51,
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
        "transmissiondelay": 0.3,
        "transmissionratios": [
            "High",
            19
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
    "crew": "rhs_msv_crew",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 0,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_bmp3/data/3M_ERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/dam_3M_ERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_01.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_01.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_01_3M.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_01_3M.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_01_3MERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_01_3MERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_02.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_02.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_02_3MERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_02_3MERA.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_03.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_03.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_03_MOD.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_03_mod.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_03_3M.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_03_3M.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_04.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_dam_bmp3_04.rvmat",
            "rhsafrf/addons/rhs_bmp3/data/rhs_destr_bmp3.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_bmd4m_t.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_dam_bmd4m_t.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_destr_bmd4m_t.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_bmd4_03.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_dam_bmd4_03.rvmat",
            "rhsafrf/addons/rhs_bmd_34/data/rhs_destr_bmd4_03.rvmat",
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
    "displayname": "BMP-3 (early)",
    "dlc": "RHS_AFRF",
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
    "driverlefthandanimname": "steering",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tvn5.p3d",
    "driverrighthandanimname": "steering",
    "driverrightleganimname": "",
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
    "editorsubcategory": "rhs_EdSubcat_ifv",
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
    "enginemoi": 18,
    "enginepower": 368,
    "engineshifty": 0.7,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay",
            "fired": "_this call RHS_fnc_bmp3_autoloader;",
            "getout": "_this call rhs_fnc_hatchAbandon",
            "hitpart": "_this call rhs_fnc_hitSpall",
            "init": "_this call rhs_fnc_bmp3_init;"
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
        -9
    ],
    "faction": "rhs_faction_msv",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "FDustEffects",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 30,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 0.5,
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
    "getinproxyorder": [
        8,
        9,
        1,
        2,
        3,
        4,
        5,
        6,
        7
    ],
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
        0.015,
        0.011,
        0.015
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
        "camo4",
        "camo5",
        "n1",
        "n2",
        "n3",
        "i1",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_01_co.paa",
        "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_02_co.paa",
        "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_03_co.paa",
        "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_04_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitengine": {
            "armor": 0.25,
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
                }
            },
            "explosionshielding": 0.009,
            "material": -1,
            "minimalhit": 0.069,
            "name": "motor",
            "passthrough": 0,
            "radius": 0.17,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 1.2,
            "explosionshielding": 0.001,
            "material": -1,
            "name": "palivo",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "-"
        },
        "hithull": {
            "armor": 0.4,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.44,
            "name": "telo",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "zbytek"
        },
        "hitltrack": {
            "armor": -150,
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
            "explosionshielding": 0.15,
            "material": -1,
            "minimalhit": -0.25,
            "name": "pas_P",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_P"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsafrf/addons/rhs_bmp3/data/bis/icon_bmp3_ca.paa",
    "idlerpm": 800,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.5,
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
    "latency": 0.6,
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
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "loddriveropticsin": 0,
    "loddriveropticsout": 0,
    "loddriverturnedout": 0,
    "magazines": [
        "rhs_mag_smokegen"
    ],
    "mapsize": 7.1,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.05,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 301,
    "maxspeed": 70,
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
    "memorypointtaskmarker": "",
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
        "mfd_left": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_1_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 0.12,
                "color": [
                    0.07,
                    0.14,
                    0.07
                ],
                "condition": "on",
                "fuelnumber": {
                    "align": "right",
                    "down": [
                        [
                            0.655,
                            0.515
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.655,
                            0.205
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.755,
                            0.205
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "fuel",
                    "sourcescale": 677,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "rhs_digital_font_var",
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR"
        },
        "mfd_right": {
            "alpha": 0.5,
            "bones": {},
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "MFD_2_BL",
            "color": [
                1,
                1,
                1
            ],
            "draw": {
                "alpha": 0.12,
                "color": [
                    0.07,
                    0.14,
                    0.07
                ],
                "condition": "on",
                "rpmnumber": {
                    "align": "left",
                    "down": [
                        [
                            0.305,
                            0.515
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.305,
                            0.205
                        ],
                        1
                    ],
                    "refreshrate": 0.05,
                    "right": [
                        [
                            0.405,
                            0.205
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "rpm",
                    "sourcescale": 1,
                    "type": "text"
                },
                "speednumber": {
                    "align": "left",
                    "down": [
                        [
                            0.795,
                            0.515
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.795,
                            0.205
                        ],
                        1
                    ],
                    "refreshrate": 0.05,
                    "right": [
                        [
                            0.895,
                            0.205
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                }
            },
            "enableparallax": 0,
            "font": "rhs_digital_font_var",
            "topleft": "MFD_2_TL",
            "topright": "MFD_2_TR"
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
    "minomega": 84,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsafrf/addons/rhs_bmp3/bmp3_early",
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
    "normalspeedforwardcoef": 0.73,
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
    "peaktorque": 1461,
    "picture": "rhsafrf/addons/rhs_bmp3/pictures/rhs_bmp3_pic_ca.paa",
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
    "redrpm": 2880,
    "reflectors": {
        "driver_fg125_cover": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 160,
                "hardlimitstart": 130,
                "linear": 0,
                "quadratic": 0.2,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 5,
            "daylight": 1,
            "direction": "Light_L_end",
            "flaresize": 0.85,
            "hitpoint": "Light_L",
            "innerangle": 35,
            "intensity": 15,
            "outerangle": 75,
            "position": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "useflare": 0
        },
        "driver_fg125_cover_flare": {
            "ambient": [
                5,
                5,
                5
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 160,
                "hardlimitstart": 130,
                "linear": 0,
                "quadratic": 0.2,
                "start": 1
            },
            "color": [
                1900,
                1300,
                950
            ],
            "conefadecoef": 5,
            "daylight": 1,
            "direction": "Light_L_end",
            "flaresize": 0.3,
            "hitpoint": "Light_L",
            "innerangle": 55,
            "intensity": 5,
            "outerangle": 155,
            "position": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "driverview2": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "camera": {
                "fov": 0.5,
                "pointdirection": "dVis2D",
                "pointposition": "dVis2P",
                "renderquality": 4,
                "rendervisionmode": 0
            },
            "rendertarget": "rendertarget1"
        },
        "driverview3": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "camera": {
                "fov": 0.5,
                "pointdirection": "dVis3D",
                "pointposition": "dVis3P",
                "renderquality": 4,
                "rendervisionmode": 0
            },
            "rendertarget": "rendertarget2"
        },
        "driverview4": {
            "bboxes": [
                "PIP_3_TL",
                "PIP_3_TR",
                "PIP_3_BL",
                "PIP_3_BR"
            ],
            "camera": {
                "fov": 0.5,
                "pointdirection": "dVis4D",
                "pointposition": "dVis4P",
                "renderquality": 2,
                "rendervisionmode": 0
            },
            "rendertarget": "rendertarget3"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number',cRHSBMP3NumberPlaces,'DefaultRed']",
        "['Label',cRHSBMP3PlnSymPlaces, 'Platoon',12]"
    ],
    "rhs_fuelcapacity": 672,
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
    "scope": 0,
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
    "slowspeedforwardcoef": 0.35,
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
        "/rhsafrf/addons/rhs_bmp/sounds/utd20_start",
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
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_3",
        0.316228,
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
                "veh_vehicle_APC_p"
            ],
            "speechsingular": [
                "veh_vehicle_APC_s"
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
    "tankturnforce": 280000,
    "tankturnforceangminspd": 0.6,
    "tankturnforceangspd": 0.82,
    "tbody": 250,
    "textplural": "BMPs",
    "textsingular": "BMP",
    "texturelist": [],
    "texturesources": {
        "rhs_sand": {
            "author": "Red Hammer Studios",
            "displayname": "Sand",
            "factions": [],
            "textures": [
                "rhsafrf/addons/rhs_bmp3_camo/data/rhs_bmp3_01_sand_co.paa",
                "rhsafrf/addons/rhs_bmp3_camo/data/rhs_bmp3_02_sand_co.paa",
                "rhsafrf/addons/rhs_bmp3_camo/data/rhs_bmp3_03_sand_co.paa",
                "rhsafrf/addons/rhs_bmp3_camo/data/rhs_bmp3_04_sand_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [],
            "textures": [
                "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_01_co.paa",
                "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_02_co.paa",
                "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_03_co.paa",
                "rhsafrf/addons/rhs_bmp3/data/rhs_bmp3_04_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "tf_range_api": 35000,
    "threat": [
        0.7,
        1,
        0.3
    ],
    "thrustdelay": 0.6,
    "torquecurve": [
        [
            0,
            0
        ],
        [
            0.229167,
            0.648871
        ],
        [
            0.4,
            0.891855
        ],
        [
            0.555903,
            1
        ],
        [
            0.656944,
            0.993155
        ],
        [
            0.813889,
            0.973306
        ],
        [
            0.904861,
            0.92334
        ],
        [
            1.05,
            0
        ]
    ],
    "tracksspeed": 1.35,
    "transmissionlosses": 15,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhs_rpg": {
            "backpack": "rhs_rpg",
            "count": 1
        },
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
    "transportmagazines": {
        "_xx_rhs_100rnd_762x54mmr": {
            "count": 3,
            "magazine": "rhs_100Rnd_762x54mmR"
        },
        "_xx_rhs_10rnd_762x54mmr_7n1": {
            "count": 10,
            "magazine": "rhs_10Rnd_762x54mmR_7N1"
        },
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "count": 30,
            "magazine": "rhs_30Rnd_545x39_7N10_AK"
        },
        "_xx_rhs_grd40_white": {
            "count": 5,
            "magazine": "rhs_GRD40_white"
        },
        "_xx_rhs_mag_rdg2_white": {
            "count": 2,
            "magazine": "rhs_mag_rdg2_white"
        },
        "_xx_rhs_mag_rgd5": {
            "count": 9,
            "magazine": "rhs_mag_rgd5"
        },
        "_xx_rhs_rpg26_mag": {
            "count": 2,
            "magazine": "rhs_rpg26_mag"
        },
        "_xx_rhs_rpg7_og7v_mag": {
            "count": 2,
            "magazine": "rhs_rpg7_OG7V_mag"
        },
        "_xx_rhs_vg40op_white": {
            "count": 5,
            "magazine": "rhs_vg40op_white"
        },
        "_xx_rhs_vog25": {
            "count": 20,
            "magazine": "rhs_VOG25"
        }
    },
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 7,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_ak74m": {
            "count": 4,
            "weapon": "rhs_weap_ak74m"
        },
        "_xx_rhs_weap_rpg26": {
            "count": 2,
            "weapon": "rhs_weap_rpg26"
        },
        "_xx_rhs_weap_rpg7": {
            "count": 1,
            "weapon": "rhs_weap_rpg7"
        }
    },
    "turncoef": 5,
    "turrets": {
        "gpmgturret1": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "obsTurret2",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "obsGun2",
            "animationsourcehatch": "hatchR",
            "armorlights": 0.4,
            "body": "obsTurret2",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 0,
            "components": {
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
            "disablesoundattenuation": 0,
            "dontcreateai": 1,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "obsGun2",
            "gunbeg": "muzzle2",
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
            "gunend": "end2",
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
            "gunneraction": "rhs_bmp3_gunner03",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchRA",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "rhs_bmp3_gunner03",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Right Hull Gunner",
            "gunneropticscolor": [
                1,
                1,
                1,
                1
            ],
            "gunneropticseffect": [
                "TankGunnerOptics1",
                "WeaponsOptics",
                "OpticsCHAbera3"
            ],
            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tnpp220a_right",
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
            "gunnertype": "rhs_msv_rifleman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun_bow1": {
                    "armor": 0.6,
                    "explosionshielding": 0.001,
                    "isgun": 1,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "hit_obsgun2",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
                },
                "hitturret_bow1": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "isturret": 1,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "hit_obsgun2",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
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
            "lodopticsout": 0,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250"
            ],
            "maxcamelev": 90,
            "maxelev": 35,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 15,
            "maxoutturn": 120,
            "maxturn": 10,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "memoryPointGun2",
            "memorypointgunneroptics": "gunnerview3",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo R",
            "memorypointsgetingunnerdir": "pos cargo R dir",
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
            "minelev": -24,
            "minoutelev": -10,
            "minoutturn": -100,
            "minturn": -10,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
            "personturretaction": "vehicle_turnout_1",
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 8,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "zasleh3",
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
                "limitsarraybottom": [
                    [
                        -10,
                        -10
                    ],
                    [
                        -10,
                        10
                    ]
                ],
                "limitsarraytop": [
                    [
                        10,
                        -10
                    ],
                    [
                        10,
                        10
                    ]
                ]
            },
            "turnout": {
                "limitsarraybottom": [
                    [
                        -24,
                        -150
                    ],
                    [
                        -24,
                        150
                    ]
                ],
                "limitsarraytop": [
                    [
                        45,
                        -150
                    ],
                    [
                        45,
                        150
                    ]
                ]
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 1,
            "useprecisegetinaction": 0,
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
            "viewgunnerinexternal": 1,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "distancezoommax": 2000,
                "distancezoommin": 200,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.166666,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.166666,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.166666,
                "opticszoommax": 0.166666,
                "opticszoommin": 0.166666
            },
            "weapons": [
                "rhs_weap_pkt_bmd_bow1"
            ]
        },
        "gpmgturret2": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "LF_Seat_Turret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "LF_Seat_Gun",
            "animationsourcehatch": "hatchL",
            "armorlights": 0.4,
            "body": "LF_Seat_turret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 1,
            "components": {
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
            "disablesoundattenuation": 0,
            "dontcreateai": 1,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "LF_Seat_gun",
            "gunbeg": "muzzle3",
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
            "gunend": "end3",
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
            "gunneraction": "rhs_bmp3_gunner02",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchLA",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "rhs_bmp3_gunner02",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Left Hull Gunner",
            "gunneropticscolor": [
                1,
                1,
                1,
                1
            ],
            "gunneropticseffect": [
                "TankGunnerOptics1",
                "WeaponsOptics",
                "OpticsCHAbera3"
            ],
            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tnpp220a",
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
            "gunnertype": "rhs_msv_rifleman",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun_bow2": {
                    "armor": 0.6,
                    "explosionshielding": 0.001,
                    "isgun": 1,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "hit_obsgun3",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
                },
                "hitturret_bow2": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "isturret": 1,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "hit_obsgun3",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
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
            "lodopticsout": 0,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250"
            ],
            "maxcamelev": 90,
            "maxelev": 35,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 15,
            "maxoutturn": 120,
            "maxturn": 10,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "memoryPointGun3",
            "memorypointgunneroptics": "gunnerView2",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo L",
            "memorypointsgetingunnerdir": "pos cargo L dir",
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
            "minelev": -24,
            "minoutelev": -10,
            "minoutturn": -100,
            "minturn": -10,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
            "personturretaction": "vehicle_turnout_2",
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 9,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "zasleh4",
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
                "limitsarraybottom": [
                    [
                        -10,
                        -10
                    ],
                    [
                        -10,
                        10
                    ]
                ],
                "limitsarraytop": [
                    [
                        10,
                        -10
                    ],
                    [
                        10,
                        10
                    ]
                ]
            },
            "turnout": {
                "limitsarraybottom": [
                    [
                        -24,
                        -150
                    ],
                    [
                        -24,
                        150
                    ]
                ],
                "limitsarraytop": [
                    [
                        45,
                        -150
                    ],
                    [
                        45,
                        150
                    ]
                ]
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 1,
            "useprecisegetinaction": 0,
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
            "viewgunnerinexternal": 1,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "distancezoommax": 2000,
                "distancezoommin": 200,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.166666,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.166666,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.166666,
                "opticszoommax": 0.166666,
                "opticszoommin": 0.166666
            },
            "weapons": [
                "rhs_weap_pkt_bmd_bow2"
            ]
        },
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "mainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcestickx": "joystick_gunner_X",
            "animationsourcesticky": "joystick_gunner_Y",
            "armorlights": 0.1,
            "body": "mainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 0,
            "castgunnershadow": 0,
            "commanding": 2,
            "components": {
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
            "disablesoundattenuation": 0,
            "discretedistance": [
                0
            ],
            "discretedistanceinitindex": 0,
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
            "gunneraction": "rhs_bmp3_gunnerOut",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchG",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "rhs_bmp3_gunner",
            "gunnerlefthandanimname": "joystick_gunner_Y",
            "gunnerleftleganimname": "",
            "gunnername": "Gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
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
            "gunnerrighthandanimname": "joystick_gunner_Y",
            "gunnerrightleganimname": "",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "headaimdown": 15,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.6,
                    "explosionshielding": 0.001,
                    "isgun": 1,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "isturret": 1,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.25,
                    "visual": "vez"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 10,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_3UOF17_22",
                "rhs_mag_9m117_8",
                "rhs_mag_3uof8_305",
                "rhs_mag_3ubr6_195",
                "rhs_mag_762x54mm_2000",
                "rhs_mag_3d17_6",
                "rhs_laserfcsmag",
                "rhs_laserfcsmag"
            ],
            "maxcamelev": 90,
            "maxelev": 60,
            "maxhorizontalrotspeed": 0.55,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 0.55,
            "memorypointgun": "usti hlavne2",
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
            "minelev": -5,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "day2": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1k13_3s_5x.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.14,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.14,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.14,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "DAY5",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "day3": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1k13_3s_14x.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.05,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.05,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.05,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "DAY14",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "daymain": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1k13_3s_1x.p3d",
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
                    "opticsdisplayname": "DAY1",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "night": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1k13_3s_5x_nvg.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.14,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.14,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.14,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "NIGHT",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 0,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {
                "searchlight_fg125": {
                    "ambient": [
                        5,
                        5,
                        5
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 660,
                        "hardlimitstart": 630,
                        "linear": 0,
                        "quadratic": 0.02,
                        "start": 1
                    },
                    "color": [
                        1900,
                        1300,
                        950
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "Light_FG125_end",
                    "flaresize": 0.85,
                    "hitpoint": "Light_FG125",
                    "innerangle": 8,
                    "intensity": 45,
                    "outerangle": 15,
                    "position": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "useflare": 1
                },
                "searchlight_fg125_flare": {
                    "ambient": [
                        22,
                        22,
                        22
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 0.9,
                        "hardlimitstart": 0,
                        "linear": 0,
                        "quadratic": 10,
                        "start": 0
                    },
                    "color": [
                        7,
                        6,
                        6.5
                    ],
                    "conefadecoef": 10,
                    "daylight": 0,
                    "direction": "Light_FG125_end",
                    "flaresize": 1.85,
                    "hitpoint": "Light_FG125",
                    "innerangle": 30,
                    "intensity": 100,
                    "outerangle": 175,
                    "position": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "useflare": 1
                }
            },
            "selectionfireanim": "zasleh2",
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
                1,
                1,
                50
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "limitsarraybottom": [
                    [
                        -2.1,
                        -180
                    ],
                    [
                        -1.9,
                        -134.687
                    ],
                    [
                        -4.7683,
                        -133.687
                    ],
                    [
                        -5,
                        0
                    ],
                    [
                        -4.7173,
                        133.637
                    ],
                    [
                        -1.9,
                        134.687
                    ],
                    [
                        -2.1,
                        180
                    ]
                ],
                "limitsarraytop": [
                    [
                        60,
                        -180
                    ],
                    [
                        60,
                        180
                    ]
                ]
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeapon1k13_bmp3_FCS",
            "turrets": {
                "commanderoptics": {
                    "aggregatereflectors": [],
                    "allowlauncherin": 0,
                    "allowlauncherout": 0,
                    "allowtablock": 0,
                    "animationsourcebody": "obsTurret",
                    "animationsourcecamelev": "camElev",
                    "animationsourcegun": "obsGun",
                    "animationsourcehatch": "hatchCommander",
                    "armorlights": 0.4,
                    "body": "obsTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 0,
                    "castgunnershadow": 0,
                    "commanding": 4,
                    "components": {
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
                    "disablesoundattenuation": 0,
                    "discretedistance": [],
                    "discretedistanceinitindex": 0,
                    "dontcreateai": 0,
                    "ejectdeadgunner": 0,
                    "forcehidegunner": 0,
                    "forcenvg": 0,
                    "gun": "obsGun",
                    "gunbeg": "usti hlavne3",
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
                    "gunend": "konec hlavne3",
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
                    "gunneraction": "rhs_bmp3_commanderOut",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "hatchC",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 0,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "rhs_bmp3_commander",
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
                    "gunneroutopticsmodel": "",
                    "gunneroutopticsshowcursor": 0,
                    "gunnerrighthandanimname": "",
                    "gunnerrightleganimname": "",
                    "gunnertype": "rhs_msv_crew_commander",
                    "gunnerusespilotview": 0,
                    "hasgunner": 1,
                    "hideweaponsgunner": 1,
                    "hitpoints": {
                        "hitguncom": {
                            "armor": 0.3,
                            "explosionshielding": 0.6,
                            "isgun": 1,
                            "material": -1,
                            "minimalhit": 0.03,
                            "name": "zbranVelitele",
                            "passthrough": 0,
                            "radius": 0.15,
                            "visual": "zbranVelitele"
                        },
                        "hitturretcom": {
                            "armor": 0.3,
                            "explosionshielding": 0.6,
                            "isturret": 1,
                            "material": -1,
                            "minimalhit": 0.03,
                            "name": "vezVelitele",
                            "passthrough": 0,
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
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "lodopticsin": 0,
                    "lodopticsout": 0,
                    "lodturnedin": -1,
                    "lodturnedout": -1,
                    "magazines": [],
                    "maxcamelev": 90,
                    "maxelev": 60,
                    "maxhorizontalrotspeed": 1.8,
                    "maxoutelev": 20,
                    "maxoutturn": 60,
                    "maxturn": 360,
                    "maxverticalrotspeed": 1.8,
                    "memorypointgun": "usti hlavne3",
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
                    "minelev": -5,
                    "minoutelev": -4,
                    "minoutturn": -60,
                    "minturn": -360,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "night": {
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3_night.p3d",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.166667,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.166667,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.166667,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "speedzoommaxfov": 0,
                            "speedzoommaxspeed": 10000000000.0,
                            "visionmode": [
                                "NVG"
                            ]
                        },
                        "periscope": {
                            "gunneropticseffect": [
                                "TankGunnerOptics1",
                                "OpticsBlur2",
                                "OpticsCHAbera2"
                            ],
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tvn5.p3d",
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
                            "speedzoommaxfov": 0,
                            "speedzoommaxspeed": 10000000000.0,
                            "visionmode": [
                                "Normal"
                            ]
                        },
                        "pzu": {
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_pzu3.p3d",
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
                            "speedzoommaxfov": 0,
                            "speedzoommaxspeed": 10000000000.0,
                            "visionmode": [
                                "Normal"
                            ]
                        },
                        "wide": {
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.14,
                            "maxanglex": 30,
                            "maxangley": 100,
                            "maxfov": 0.14,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.14,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "speedzoommaxfov": 0,
                            "speedzoommaxspeed": 10000000000.0,
                            "visionmode": [
                                "Normal"
                            ]
                        }
                    },
                    "outgunnermayfire": 1,
                    "playerposition": 0,
                    "precisegetinout": 0,
                    "primary": 1,
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "proxyindex": 1,
                    "proxytype": "CPCommander",
                    "reflectors": {},
                    "selectionfireanim": "",
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
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        3.16228,
                        1,
                        30
                    ],
                    "soundservovertical": [
                        "A3/Sounds_F/vehicles/armor/APC/noises/servo_APC_comm",
                        3.16228,
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
                    "turretinfotype": "RHS_RscWeaponTKN3_FCS",
                    "turrets": {},
                    "turretspec": {
                        "showheadphones": 0
                    },
                    "usepip": 2,
                    "viewgunner": {
                        "initanglex": 5,
                        "initangley": 0,
                        "initfov": 0.7,
                        "maxanglex": 85,
                        "maxangley": 150,
                        "maxfov": 1.1,
                        "minanglex": -65,
                        "minangley": -150,
                        "minfov": 0.25
                    },
                    "viewgunnerinexternal": 1,
                    "viewgunnershadow": 1,
                    "viewgunnershadowamb": 1,
                    "viewgunnershadowdiff": 1,
                    "viewoptics": {
                        "initanglex": 0,
                        "initangley": 0,
                        "initfov": 0.101,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.102,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.102,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "speedzoommaxfov": 0,
                        "speedzoommaxspeed": 10000000000.0,
                        "visionmode": [
                            "Normal"
                        ]
                    },
                    "weapons": []
                }
            },
            "turretspec": {
                "showheadphones": 0
            },
            "usepip": 2,
            "viewgunner": {
                "initanglex": -15,
                "initangley": -5,
                "initfov": 0.7,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.1,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25
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
            "weapons": [
                "rhs_weap_2a70",
                "rhs_weap_2a72",
                "rhs_weap_pkt_bmd_coax",
                "rhs_weap_902a",
                "rhs_weap_fcs"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [
        "rhs_msv_crew_commander",
        "rhs_msv_crew",
        "rhs_msv_crew",
        ""
    ],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscInfoBMP3",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "vehicleclass": "rhs_vehclass_ifv",
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
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
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
        "initanglex": -12,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 110,
        "maxfov": 1.25,
        "maxmovex": 0.075,
        "maxmovey": 0.075,
        "maxmovez": 0.1,
        "minanglex": -65,
        "minangley": -110,
        "minfov": 0.25,
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
    "waterresistancecoef": 0.15,
    "weapons": [
        "rhs_weap_smokegen"
    ],
    "weaponsgroup1": "1 + 16",
    "weaponsgroup2": 128,
    "weaponsgroup3": 2,
    "weaponsgroup4": 4,
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
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l7": {
            "bonename": "wheel_podkolol6",
            "boundary": "wheel_1_7_bound",
            "center": "wheel_1_7_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "left",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r7": {
            "bonename": "wheel_podkolop6",
            "boundary": "wheel_2_7_bound",
            "center": "wheel_2_7_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 1034,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1034,
            "frictionvsslipgraph": [
                [
                    0,
                    0.65
                ],
                [
                    0.18,
                    1
                ],
                [
                    0.7,
                    0.95
                ]
            ],
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 4000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 11000,
            "springstrength": 127500,
            "sprungmass": 1333.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.315
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