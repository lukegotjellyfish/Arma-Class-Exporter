d = {
    "_generalmacro": "Truck_F",
    "accelaidforceyoffset": -0.15,
    "acceleration": 15,
    "access": 0,
    "accuracy": 0.25,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        []
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.2,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "bench_hide": {
            "animperiod": 0.1,
            "displayname": "hide cargo bench",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "cover_hide": {
            "animperiod": 0.1,
            "displayname": "hide cover",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "door_lf": {
            "animperiod": 0.8,
            "sound": "RHS_Ural_Door",
            "soundposition": "DoorL_axis",
            "source": "door"
        },
        "door_rf": {
            "animperiod": 0.8,
            "sound": "RHS_Ural_Door",
            "soundposition": "DoorR_axis",
            "source": "door"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "raw": 1,
            "source": "Hit"
        },
        "hitlbwheel": {
            "hitpoint": "HitLF2Wheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitlf2wheel": {
            "hitpoint": "HitLBWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitlfwheel": {
            "hitpoint": "HitLFWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrbwheel": {
            "hitpoint": "HitRF2Wheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrf2wheel": {
            "hitpoint": "HitRBWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "raw": 1,
            "source": "Hit"
        },
        "hitspare": {
            "hitpoint": "HitSpare",
            "raw": 1,
            "source": "Hit"
        },
        "light_hide": {
            "animperiod": 0.1,
            "displayname": "hide light covers",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "(_this select 0) animateSource ['light_hide',(_this select 1),true];",
            "source": "user"
        },
        "lights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "longlights_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "rear_numplate_hide": {
            "animperiod": 0.1,
            "displayname": "hide rear registration numbers",
            "initphase": 1,
            "mass": 1,
            "source": "user"
        },
        "searchlight_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "searchlight_rot": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "shortlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "spare_hide": {
            "animperiod": 0.1,
            "displayname": "hide spare wheel",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "turnout1": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "turnout2": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "usespare": {
            "hitpoint": "UseSpare",
            "raw": 1,
            "source": "Hit"
        },
        "wiper": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "wipers": {
            "animperiod": 1,
            "initphase": 0,
            "sound": "RHS_Wipers",
            "soundposition": "wiper_axis",
            "source": "door"
        }
    },
    "antirollbarforcecoef": 0.2,
    "antirollbarforcelimit": 0.5,
    "antirollbarspeedmax": 65,
    "antirollbarspeedmin": 30,
    "armor": 50,
    "armorcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "armorcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "armorcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "armorcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "armorcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "armorcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "armorcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "armorcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "armorlights": 0.4,
    "armorstructural": 4,
    "armorwheels": 0.12,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "TruckAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_decalarmy": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set large door roundel symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cTrucksGazRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalArmy",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalarmy_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define large door roundel type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalArmy_type",
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
        },
        "rhs_decalnumber": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set plate number",
            "expression": "if( _value >= 0)then{[_this,[['Number', cTrucksGaz4NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value]]] call rhs_fnc_decalsInit};",
            "property": "rhs_decalNumber",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cTrucksGaz4NumberPlaces, _value]]] call rhs_fnc_decalsInit",
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
            "displayname": "Set small door roundel symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cTrucksGazRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoon",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoon_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define small door roundel type",
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
        },
        "rhs_hidelightcover": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Hide light covers",
            "expression": "_this animate ['light_hide',_value,true]",
            "property": "rhs_hideLightCover"
        },
        "rhs_hidespare": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Remove spare wheel",
            "expression": "_this animate ['spare_hide',_value,true]",
            "property": "rhs_hidespare"
        }
    },
    "audible": 9,
    "author": "RHS (A2 port)",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 3,
    "brakeidlespeed": 1,
    "braketorque": 6000,
    "buildcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "buildcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "buildcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "buildcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "buildcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "buildcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "buildcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "buildcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "bushcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_01",
        0.630957,
        1,
        50
    ],
    "bushcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_02",
        0.630957,
        1,
        50
    ],
    "bushcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.630957,
        1,
        50
    ],
    "bushcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Light_Bush_03",
        0.630957,
        0.8,
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
    "camouflage": 2,
    "camshakecoef": 0.2,
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
        "frequency": 60,
        "minspeed": 60,
        "power": 2
    },
    "canfloat": 0,
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "rhs_passenger_apc_narrow_generic01",
        "rhs_passenger_apc_narrow_generic03still",
        "rhs_passenger_apc_narrow_generic03",
        "passenger_generic01_leanright",
        "rhs_passenger_apc_generic01",
        "rhs_passenger_apc_generic01",
        "rhs_passenger_apc_generic03",
        "rhs_passenger_apc_narrow_generic01",
        "passenger_generic01_leanleft",
        "rhs_passenger_apc_generic03",
        "rhs_passenger_apc_narrow_generic02",
        "rhs_passenger_apc_generic02",
        "rhs_passenger_apc_generic01",
        "passenger_generic01_foldhands",
        "rhs_passenger_apc_generic04",
        "passenger_generic01_leanleft"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        1,
        2
    ],
    "cargodoors": [
        "Door_RF",
        ""
    ],
    "cargogetinaction": [
        "GetInLow",
        "GetInMRAP_01_cargo"
    ],
    "cargogetoutaction": [
        "GetOutLow",
        "GetOutHelicopterCargo"
    ],
    "cargoiscodriver": [
        1,
        1,
        0
    ],
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
        7,
        8,
        10,
        11
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
    "category": "Car",
    "centrebias": 1,
    "changegearmineffectivity": [
        0.95,
        0.15,
        0.95,
        0.95,
        0.95,
        0.95
    ],
    "clutchstrength": 40,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "collisioneffect": "collisionEffect",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
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
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -7.9,
            "N",
            0,
            "D1",
            6.48,
            "D2",
            3.09,
            "D3",
            1.6,
            "D4",
            0.8
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            6.79
        ]
    },
    "components": {
        "aicarsteeringcomponent": {
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "allowovertaking": 1,
            "commandturnfactor": 1,
            "convoypidweights": [
                1,
                0.01,
                0.01
            ],
            "differenceanglecoef": 0.4,
            "dopredictforward": 1,
            "doremapspeed": 1,
            "forwardanglecoef": 0.7,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.1,
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
            "speedpredictionmethod": 2,
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
        "transportcountermeasurescomponent": {}
    },
    "cost": 40000,
    "countsforscoreboard": 1,
    "crash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_01",
        1.99526,
        1,
        75
    ],
    "crash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_02",
        1.99526,
        1,
        75
    ],
    "crash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_03",
        1.99526,
        1,
        75
    ],
    "crash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_04",
        1.99526,
        1,
        75
    ],
    "crash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_05",
        1.99526,
        1,
        75
    ],
    "crash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_06",
        1.99526,
        1,
        75
    ],
    "crash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_07",
        1.99526,
        1,
        75
    ],
    "crash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_08",
        1.99526,
        1,
        75
    ],
    "crew": "rhsgref_cdf_reg_rifleman",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.8,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_repkung.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/rhs_dam_gaz66_repkung.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/rhs_destr_gaz66_repkung.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/gaz66.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/gaz66_dam.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/gaz66_des.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/tent.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/tent.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/tent_des.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass_damage.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass_damage.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass_in.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass_in_damage.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/glass_in_damage.rvmat",
            "a3/data_f/default.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/default_destruct.rvmat",
            "rhsafrf/addons/rhs_gaz66/data/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00845,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "damperdamping": 1,
    "damperforce": 1,
    "dampersbumpcoef": 2,
    "dampersize": 0.1,
    "dampingratefullthrottle": 0.05,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "dampingratezerothrottleclutchengaged": 1.35,
    "destrtype": "DestructDefault",
    "destructioneffects": {
        "fire1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small"
        },
        "fire2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small"
        },
        "firesparks1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "FireSparks"
        },
        "light1": {
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
            "type": "ObjectDestructionRefractSmall"
        },
        "smoke1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall"
        },
        "smoke1_2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5,
            "position": "destructionEffect2",
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small"
        },
        "smoke2": {
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
        "sparks1": {
            "intensity": 0,
            "interval": 1,
            "lifetime": 0,
            "position": "destructionEffect1",
            "simulation": "particles",
            "type": "ObjectDestructionSparks"
        }
    },
    "detectskill": 20,
    "differentialtype": "all_limited",
    "displayname": "GAZ-66-ESB-8IM",
    "dlc": "RHS_GREF",
    "driveraction": "rhs_gaz66_driver",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": 1,
    "driverdoor": "Door_LF",
    "driverforceoptics": 0,
    "driverinaction": "rhs_gaz66_driver",
    "driverlefthandanimname": "drivewheel",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "drivewheel",
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
                "LDustEffects"
            ],
            "gdtbeach": [
                "LDustEffects"
            ],
            "gdtcliff": [
                "LDustEffects"
            ],
            "gdtconcrete": [
                "LDustEffects"
            ],
            "gdtdead": [
                "LDustEffects"
            ],
            "gdtdesert": [
                "LDustEffects"
            ],
            "gdtdesert1": [
                "LDustEffects"
            ],
            "gdtdesert2": [
                "LDustEffects"
            ],
            "gdtdirt": [
                "LDustEffects"
            ],
            "gdtfield": [
                "LDustEffects"
            ],
            "gdtforest": [
                "LDustEffects"
            ],
            "gdtgrassdry": [
                "LDustEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffects"
            ],
            "gdtgrassshort": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtgrasstall": [
                "LDustEffects",
                "LGrassEffects"
            ],
            "gdtgrasswild": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
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
                "LDustEffects"
            ],
            "gdtrubble": [
                "LDustEffects"
            ],
            "gdtseabed": [
                "LDustEffects"
            ],
            "gdtseabeddeep": [
                "LDustEffects"
            ],
            "gdtsoil": [
                "LDustEffects"
            ],
            "gdtstony": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonygreen": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonythistle": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisbeach": [
                "LDustEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffects"
            ],
            "gdtstratisthistles": [
                "LDustEffects"
            ],
            "gdtthorn": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtvolcano": [
                "LDustEffects",
                "LStonesEffects"
            ],
            "gdtvolcanobeach": [
                "LDustEffects"
            ],
            "gdtweed1": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtweed2": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtwildfield": [
                "LDustEffects",
                "LGrassEffects",
                "LDirtEffects"
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
                "RDustEffects"
            ],
            "gdtbeach": [
                "RDustEffects"
            ],
            "gdtcliff": [
                "RDustEffects"
            ],
            "gdtconcrete": [
                "RDustEffects"
            ],
            "gdtdead": [
                "RDustEffects"
            ],
            "gdtdesert": [
                "RDustEffects"
            ],
            "gdtdesert1": [
                "RDustEffects"
            ],
            "gdtdesert2": [
                "RDustEffects"
            ],
            "gdtdirt": [
                "RDustEffects"
            ],
            "gdtfield": [
                "RDustEffects"
            ],
            "gdtforest": [
                "RDustEffects"
            ],
            "gdtgrassdry": [
                "RDustEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffects"
            ],
            "gdtgrassshort": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtgrasstall": [
                "RDustEffects",
                "RGrassEffects"
            ],
            "gdtgrasswild": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
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
                "RDustEffects"
            ],
            "gdtrubble": [
                "RDustEffects"
            ],
            "gdtseabed": [
                "RDustEffects"
            ],
            "gdtseabeddeep": [
                "RDustEffects"
            ],
            "gdtsoil": [
                "RDustEffects"
            ],
            "gdtstony": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonygreen": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonythistle": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisbeach": [
                "RDustEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffects"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffects"
            ],
            "gdtstratisthistles": [
                "RDustEffects"
            ],
            "gdtthorn": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtvolcano": [
                "RDustEffects",
                "RStonesEffects"
            ],
            "gdtvolcanobeach": [
                "RDustEffects"
            ],
            "gdtweed1": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtweed2": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtwildfield": [
                "RDustEffects",
                "RGrassEffects",
                "RDirtEffects"
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
    "editorpreview": "rhsgref/addons/rhsgref_editorPreviews/data/rhsgref_cdf_gaz66_repair.paa",
    "editorsubcategory": "rhs_EdSubcat_truck",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 0,
    "enablemanualfire": 1,
    "enableradio": 0,
    "enablewatch": 0,
    "engineer": 0,
    "enginelosses": 10,
    "enginemoi": 0.95,
    "enginepower": 89,
    "enginestartspeed": 1.5,
    "epeimpulsedamagecoef": 15,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_eventhandlers": {
            "dammaged": "_this call rhs_fnc_wheelDamaged",
            "engine": "_this call rhs_fnc_engineCheckDamage;",
            "init": "_this call rhs_fnc_gaz66_init",
            "postinit": "_this call rhs_fnc_reapplyTextures"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectHTruck",
            "position": "vyfuk start"
        }
    },
    "explosioneffect": "FuelExplosion",
    "explosionshielding": 1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0.5,
        2,
        -10
    ],
    "faction": "rhsgref_faction_cdf_ground",
    "features": "",
    "featuretype": 0,
    "fireresistance": 5,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 20,
    "frontbias": 1.3,
    "frontrearsplit": 0.5,
    "fuelcapacity": 40,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 0.1,
    "fxexplo": {
        "access": 1
    },
    "gearbox": [
        -8,
        0,
        10,
        6.15,
        4.44,
        3.33
    ],
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13
    ],
    "getinradius": 2.5,
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
    "gunnerhasflares": 0,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.01,
        0.01,
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
        "n4",
        "i1",
        "i2",
        "i3",
        "i4"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/rhsafrf/addons/rhs_gaz66/data/gaz66_cdf_co.paa",
        "/rhsafrf/addons/rhs_gaz66/data/tent_cdf_co.paa",
        "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_kung_co.paa",
        "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_ap2kung_co.paa",
        "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_repkung_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitbody": {
            "armor": 1,
            "explosionshielding": 1.5,
            "material": -1,
            "name": "karoserie",
            "passthrough": 1,
            "visual": "zbytek"
        },
        "hitengine": {
            "armor": 0.4,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_engine_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke",
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
                    "position": "engine_smoke",
                    "simulation": "sound",
                    "type": "SmokeWreck1"
                }
            },
            "explosionshielding": 0.5,
            "material": -1,
            "name": "motor",
            "passthrough": 0.2,
            "visual": ""
        },
        "hitfuel": {
            "armor": 0.3,
            "explosionshielding": 1.5,
            "material": -1,
            "name": "palivo",
            "passthrough": 0.1,
            "visual": "-"
        },
        "hitglass1": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "visual": "glass6"
        },
        "hithull": {
            "armor": 1.5,
            "explosionshielding": 8,
            "material": -1,
            "minimalhit": 0.1,
            "name": "palivo",
            "passthrough": 0.5,
            "visual": ""
        },
        "hitlbwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_4_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitlf2wheel": {
            "armor": -200,
            "armorcomponent": "wheel_1_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "wheel_1_2_steering",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "wheel_1_2_damage"
        },
        "hitlfwheel": {
            "armor": -200,
            "armorcomponent": "wheel_1_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "wheel_1_1_steering",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "wheel_1_1_damage"
        },
        "hitlglass": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": -1,
            "name": "sklo predni L",
            "passthrough": 0
        },
        "hitlmwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_3_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitrbwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_4_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitrf2wheel": {
            "armor": -200,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "wheel_2_2_steering",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "wheel_2_2_damage"
        },
        "hitrfwheel": {
            "armor": -200,
            "armorcomponent": "wheel_2_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "wheel_2_1_steering",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "wheel_2_1_damage"
        },
        "hitrglass": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": -1,
            "name": "sklo predni P",
            "passthrough": 0
        },
        "hitrmwheel": {
            "armor": 0.2,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_3_steering",
            "passthrough": 0.3,
            "visual": "-"
        },
        "hitspare": {
            "armor": -200,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "spare1",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "wheel_2_2_damage"
        },
        "usespare": {
            "armor": 1,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.01,
            "name": "",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "-"
        }
    },
    "holdoffroadformation": 1,
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsafrf/addons/rhs_gaz66/data/ico/icomap_GAZ66_repair_CA.paa",
    "idlerpm": 500,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "initcargoangley": 180,
    "inputturncurve": [
        [
            0,
            [
                0,
                0,
                1,
                1
            ]
        ],
        [
            30,
            [
                0,
                0,
                0.2,
                0.008,
                0.4,
                0.032,
                0.6,
                0.216,
                0.8,
                0.512,
                1,
                1
            ]
        ]
    ],
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.2,
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
    "latency": 1.5,
    "latstiffx": 2000,
    "latstiffy": 18000,
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
            "LGrassEffects"
        ],
        [
            "GdtGrassTall",
            "LDustEffects"
        ],
        [
            "GdtGrassTall",
            "LGrassEffects"
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
            "LStonesEffects"
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
            "LDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "LDustEffects"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "LDustEffects"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffects"
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
            "LGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
        ],
        [
            "GdtConcrete",
            "LDirtEffects"
        ],
        [
            "GdtAsphalt",
            "LDustEffects"
        ],
        [
            "GdtAsphalt",
            "LDirtEffects"
        ],
        [
            "GdtRubble",
            "LDustEffects"
        ],
        [
            "GdtRubble",
            "LDirtEffects"
        ],
        [
            "GdtSoil",
            "LDustEffects"
        ],
        [
            "GdtSoil",
            "LDirtEffects"
        ],
        [
            "GdtBeach",
            "LDustEffects"
        ],
        [
            "GdtBeach",
            "LStonesEffects"
        ],
        [
            "GdtRock",
            "LDustEffects"
        ],
        [
            "GdtRock",
            "LDirtEffects"
        ],
        [
            "GdtDead",
            "LDustEffects"
        ],
        [
            "GdtDead",
            "LDirtEffects"
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
            "LStonesEffects"
        ],
        [
            "GdtDesert1",
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
        ],
        [
            "GdtDirt",
            "LDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
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
            "LDustEffects"
        ]
    ],
    "leftfastwatereffect": "LWaterEffects",
    "leftwatereffect": "LWaterEffects",
    "limitedspeedcoef": 0.5,
    "lockdetectionsystem": 0,
    "longstiff": 15000,
    "magazines": [],
    "mapsize": 5.66,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0,
    "maxgforce": 3,
    "maximumload": 3000,
    "maxomega": 335.1,
    "maxspeed": 90,
    "memorypointcirculumreference": "circulumReference",
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
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "memorypointtrackbll": "Stopa ZLL",
    "memorypointtrackblr": "Stopa ZLP",
    "memorypointtrackbrl": "Stopa ZPL",
    "memorypointtrackbrr": "Stopa ZPP",
    "memorypointtrackfll": "Stopa PLL",
    "memorypointtrackflr": "Stopa PLP",
    "memorypointtrackfrl": "Stopa PPL",
    "memorypointtrackfrr": "Stopa PPP",
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
    "minomega": 50,
    "mintotaldamagethreshold": 0.01,
    "model": "rhsafrf/addons/rhs_gaz66/rhs_gaz66_repair.p3d",
    "namesound": "truck",
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
    "normalspeedforwardcoef": 0.75,
    "numberphysicalwheels": 6,
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
    "outsidesoundfilter": 0,
    "peaktorque": 568,
    "picture": "rhsafrf/addons/rhs_gaz66/data/ico/rhs_gaz66_repair_pic_ca.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "plateinfos": {
        "color": [
            0,
            0,
            0,
            0.75
        ],
        "name": "spz"
    },
    "playersteeringcoefficients": {
        "maxturnhundred": 1,
        "turndecreaseconst": 5,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "turnincreaseconst": 0.5,
        "turnincreaselinear": 1,
        "turnincreasetime": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 10,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "preferroads": 1,
    "pulsationsound": {},
    "radartype": 0,
    "rearbias": 1.3,
    "redrpm": 3200,
    "reflectors": {
        "cabin": {
            "ambient": [
                5,
                0,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 2,
                "hardlimitstart": 1.5,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                800,
                900,
                650
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "cabin_light_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "cabin_light",
            "innerangle": 90,
            "intensity": 4,
            "outerangle": 165,
            "position": "cabin_light",
            "selection": "cabin_light",
            "size": 1,
            "useflare": 1
        },
        "left2": {
            "ambient": [
                2,
                2,
                2
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "color": [
                800,
                900,
                650
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_L_Flare_end",
            "flaresize": 0.85,
            "hitpoint": "L svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
            "position": "Light_L_Flare",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "long_left": {
            "ambient": [
                5,
                5,
                5
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
                800,
                900,
                650
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "Light_L_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "L svetlo",
            "innerangle": 22,
            "intensity": 100,
            "outerangle": 29,
            "position": "Light_L_Long",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 0
        },
        "long_left2": {
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
            "color": [
                800,
                900,
                650
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_L_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1,
            "hitpoint": "L svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 139,
            "position": "light_L_Long_flare",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "long_right": {
            "ambient": [
                5,
                5,
                5
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
                800,
                900,
                650
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "Light_R_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "P svetlo",
            "innerangle": 22,
            "intensity": 100,
            "outerangle": 29,
            "position": "Light_R_Long",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 0
        },
        "long_right2": {
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
            "color": [
                800,
                900,
                650
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_R_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1,
            "hitpoint": "P svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 139,
            "position": "light_R_Long_flare",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        },
        "lsvetla": {
            "ambient": [
                2,
                2,
                2
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
                800,
                900,
                650
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec L svetla",
            "flaresize": 0.85,
            "hitpoint": "L svetlo",
            "innerangle": 30,
            "intensity": 1.5,
            "outerangle": 100,
            "position": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "right2": {
            "ambient": [
                2,
                2,
                2
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 0,
                "linear": 1,
                "quadratic": 50,
                "start": 0
            },
            "color": [
                800,
                900,
                650
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_R_Flare_end",
            "flaresize": 0.85,
            "hitpoint": "P svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
            "position": "Light_R_Flare",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        },
        "rsvetla": {
            "ambient": [
                2,
                2,
                2
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
                800,
                900,
                650
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec P svetla",
            "flaresize": 0.85,
            "hitpoint": "P svetlo",
            "innerangle": 30,
            "intensity": 1.5,
            "outerangle": 100,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        },
        "searchlight": {
            "ambient": [
                2,
                2,
                2
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
                800,
                900,
                650
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "Searchlight_dir",
            "flaresize": 0.85,
            "hitpoint": "Searchlight",
            "innerangle": 35,
            "intensity": 1.5,
            "outerangle": 179,
            "position": "Searchlight_pos",
            "selection": "Searchlight",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "leftmirror": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "m1d",
                "pointposition": "m1p",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget0"
        },
        "rightmirror": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "m2d",
                "pointposition": "m2p",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget1"
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number', cTrucksGaz4NumberPlaces, 'CDF']"
    ],
    "rhs_fuelcapacity": 210,
    "rhs_towingsystem": {
        "carrier": {
            "rhs_attachpoint": "",
            "rhs_attachpointpos": [
                0,
                -2.35,
                -0.7
            ],
            "rhs_maxcargomass": 1000
        }
    },
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
            "RGrassEffects"
        ],
        [
            "GdtGrassTall",
            "RDustEffects"
        ],
        [
            "GdtGrassTall",
            "RGrassEffects"
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
            "RStonesEffects"
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
            "RDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "RDustEffects"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "RDustEffects"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffects"
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
            "RGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
        ],
        [
            "GdtConcrete",
            "RDirtEffects"
        ],
        [
            "GdtAsphalt",
            "RDustEffects"
        ],
        [
            "GdtAsphalt",
            "RDirtEffects"
        ],
        [
            "GdtRubble",
            "RDustEffects"
        ],
        [
            "GdtRubble",
            "RDirtEffects"
        ],
        [
            "GdtSoil",
            "RDustEffects"
        ],
        [
            "GdtSoil",
            "RDirtEffects"
        ],
        [
            "GdtBeach",
            "RDustEffects"
        ],
        [
            "GdtBeach",
            "RStonesEffects"
        ],
        [
            "GdtRock",
            "RDustEffects"
        ],
        [
            "GdtRock",
            "RDirtEffects"
        ],
        [
            "GdtDead",
            "RDustEffects"
        ],
        [
            "GdtDead",
            "RDirtEffects"
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
            "RStonesEffects"
        ],
        [
            "GdtDesert1",
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
        ],
        [
            "GdtDirt",
            "RDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
            "RDustEffects"
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
    "scudeffect": "ScudEffect",
    "scudmodel": "",
    "secondaryexplosion": -10,
    "selectionbacklights": "zadni svetlo",
    "selectionbrakelights": "brzdove svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 1.75,
    "sensitivityear": 0.125,
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
    "simulation": "carx",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [
        "SlingLoadCargo1_dir",
        "SlingLoadCargo2_dir",
        "SlingLoadCargo3_dir",
        "SlingLoadCargo4_dir"
    ],
    "slowspeedforwardcoef": 0.45,
    "soundarmorcrash": [
        "ArmorCrash0",
        0.125,
        "ArmorCrash1",
        0.125,
        "ArmorCrash2",
        0.125,
        "ArmorCrash3",
        0.125,
        "ArmorCrash4",
        0.125,
        "ArmorCrash5",
        0.125,
        "ArmorCrash6",
        0.125,
        "ArmorCrash7",
        0.125
    ],
    "soundattenuationcargo": [
        1,
        0.4
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "buildCrash0",
        0.125,
        "buildCrash1",
        0.125,
        "buildCrash2",
        0.125,
        "buildCrash3",
        0.125,
        "buildCrash4",
        0.125,
        "buildCrash5",
        0.125,
        "buildCrash6",
        0.125,
        "buildCrash7",
        0.125
    ],
    "soundburning": {},
    "soundbushcrash": [
        "BushCrash1",
        0.25,
        "BushCrash2",
        0.25,
        "BushCrash3",
        0.25,
        "BushCrash4",
        0.25
    ],
    "soundchoke": {},
    "soundcrash": [
        "A3/sounds_f/dummysound",
        1,
        1
    ],
    "soundcrashes": [
        "Crash0",
        0.125,
        "Crash1",
        0.125,
        "Crash2",
        0.125,
        "Crash3",
        0.125,
        "Crash4",
        0.125,
        "Crash5",
        0.125,
        "Crash6",
        0.125,
        "Crash7",
        0.125
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
        1.77828,
        0.9
    ],
    "soundengineoffext": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_ext_stop",
        1.41254,
        1,
        200
    ],
    "soundengineoffint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_int_stop",
        1.41254,
        1
    ],
    "soundengineonext": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_ext_start",
        1.41254,
        1,
        200
    ],
    "soundengineonint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_int_start",
        1.41254,
        1
    ],
    "soundenviron": [
        "",
        0.000562341,
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
        1e-05,
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
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_int_getout",
        1.77828,
        1,
        9
    ],
    "soundgetout": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/ural4320/ural4320_engine_ext_getout",
        2.51189,
        1,
        25
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
        "acceleration_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/acceleration_dirt_ext_1",
                0.707946,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        "acceleration_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                0.707946,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        "acceleration_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/acceleration_dirt_int_1",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        "acceleration_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                0.630957,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        "breaking_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_14_dirt_breaking",
                0.707946,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        "breaking_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_04",
                0.707946,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        "breaking_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_14_dirt_breaking_int",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        "breaking_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_04_int",
                0.630957,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        "engine": {
            "frequency": "0.85\t+\t((rpm/\t3200) factor[(610/\t3200),(3200/\t3200)])*0.95",
            "sound": [
                "/rhsafrf/addons/rhs_gaz66/data/sounds/zil_gaz66_driving.wss",
                0.630957,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t3200) factor[(620/\t3200),(820/\t3200)])\t*\t((rpm/\t3200) factor[(3200/\t3200),(3200/\t3200)]))*2.0"
        },
        "engine_int": {
            "frequency": "0.85\t+\t((rpm/\t3200) factor[(610/\t3200),(6400/\t3200)])*0.95",
            "sound": [
                "/rhsafrf/addons/rhs_gaz66/data/sounds/Zil_Gaz66_Int_Driving.wss",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/    3200) factor[(400/    3200),(600/    3200)])    *    ((rpm/    3200) factor[(3200/    3200),(3200/    3200)]))*2.0"
        },
        "enginethrust": {
            "frequency": "0.85\t+\t((rpm/\t3200) factor[(610/\t3200),(6400/\t3200)])*0.75",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_01",
                0.630957,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.3,1])))*(((rpm/\t3200) factor[(620/\t3200),(820/\t3200)])\t*\t((rpm/\t3200) factor[(3200/\t3200),(3200/\t3200)]))*1.5"
        },
        "enginethrust_int": {
            "frequency": "0.85\t+\t((rpm/\t3200) factor[(610/\t3200),(3200/\t3200)])*0.75",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_01",
                0.630957,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.3,1])))*(((rpm/\t3200) factor[(620/\t3200),(820/\t3200)])\t*\t((rpm/\t3200) factor[(3200/\t3200),(3200/\t3200)]))*2"
        },
        "idle_ext": {
            "frequency": "0.95\t+\t((rpm/\t3200) factor[(100/\t3200),(800/\t3200)])*0.15",
            "sound": [
                "/rhsafrf/addons/rhs_gaz66/data/sounds/zil_gaz66_idle.wss",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t3200) factor[(10/\t3200),(50/\t3200)])\t*\t((rpm/\t3200) factor[(800/\t3200),(600/\t3200)]))*2.0"
        },
        "idle_int": {
            "frequency": "0.8\t+\t((rpm/\t3200) factor[(500/\t3200),(800/\t3200)])*0.25",
            "sound": [
                "/rhsafrf/addons/rhs_gaz66/data/sounds/Zil_GAz66__Int_Idle.wss",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3200) factor[(10/\t3200),(50/\t3200)])\t*\t((rpm/\t3200) factor[(800/\t3200),(600/\t3200)]))*2"
        },
        "movement": {
            "frequency": "1",
            "sound": "soundEnviron",
            "volume": "0"
        },
        "noisein": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/noise_int_car_3",
                0.707946,
                1
            ],
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        "noiseout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/noise_int_car_3",
                1,
                1,
                90
            ],
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        "rainext": {
            "frequency": 1,
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/rain.wss",
                1.41254,
                1
            ],
            "volume": "rain*camPos"
        },
        "rainin": {
            "frequency": 1,
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/rain.wss",
                1.41254,
                1
            ],
            "volume": "rain*(1-camPos)"
        },
        "soundsetsext": [
            "RHS_gaz66_Engine_RPM0_EXT_SoundSet",
            "RHS_gaz66_Engine_RPM1_EXT_SoundSet",
            "RHS_gaz66_Engine_RPM2_EXT_SoundSet",
            "RHS_gaz66_Engine_RPM3_EXT_SoundSet",
            "RHS_gaz66_Rattling_EXT_SoundSet",
            "RHS_gaz66_Stress_EXT_SoundSet",
            "RHS_gaz66_Rain_EXT_SoundSet",
            "RHS_gaz66_Tires_Rock_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Grass_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Sand_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Gravel_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Mud_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Asphalt_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Water_Fast_EXT_SoundSet",
            "RHS_gaz66_Tires_Rock_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Grass_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Sand_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Gravel_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Mud_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Asphalt_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Water_Slow_EXT_SoundSet",
            "RHS_gaz66_Tires_Turn_Hard_EXT_SoundSet",
            "RHS_gaz66_Tires_Turn_Soft_EXT_SoundSet",
            "RHS_gaz66_Tires_Brake_Hard_EXT_SoundSet",
            "RHS_gaz66_Tires_Brake_Soft_EXT_SoundSet"
        ],
        "soundsetsint": [
            "RHS_gaz66_Engine_RPM0_INT_SoundSet",
            "RHS_gaz66_Engine_RPM1_INT_SoundSet",
            "RHS_gaz66_Engine_RPM2_INT_SoundSet",
            "RHS_gaz66_Engine_RPM3_INT_SoundSet",
            "RHS_gaz66_Rattling_INT_SoundSet",
            "RHS_gaz66_Stress_INT_SoundSet",
            "RHS_gaz66_Rain_INT_SoundSet",
            "RHS_gaz66_Tires_Rock_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Grass_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Sand_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Gravel_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Mud_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Asphalt_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Water_Fast_INT_SoundSet",
            "RHS_gaz66_Tires_Rock_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Grass_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Sand_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Gravel_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Mud_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Asphalt_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Water_Slow_INT_SoundSet",
            "RHS_gaz66_Tires_Turn_Hard_INT_SoundSet",
            "RHS_gaz66_Tires_Turn_Soft_INT_SoundSet",
            "RHS_gaz66_Tires_Brake_Hard_INT_SoundSet",
            "RHS_gaz66_Tires_Brake_Soft_INT_SoundSet"
        ],
        "tiresasphaltin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_asfalt_2",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        "tiresasphaltout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_asfalt_2",
                1,
                1,
                60
            ],
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        "tiresgrassin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_dirt_soft_2",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        "tiresgrassout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_dirt_soft_2",
                1,
                1,
                60
            ],
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        "tiresgravelin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_gravel_1",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        "tiresgravelout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_gravel_1",
                1,
                1,
                60
            ],
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        "tiresmudin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int-tires-mud2",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        "tiresmudout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext-tires-mud2",
                1,
                1,
                60
            ],
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        "tiresrockin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_dirt_soft_1",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        "tiresrockout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_dirt_soft_1",
                1,
                1,
                60
            ],
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        "tiressandin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int-tires-sand2",
                0.707946,
                1
            ],
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        "tiressandout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext-tires-sand1",
                1,
                1,
                60
            ],
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        "turn_left_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt",
                0.707946,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        "turn_left_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                0.707946,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        "turn_left_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt_int",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        "turn_left_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                0.630957,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        "turn_right_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt",
                0.707946,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        "turn_right_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                0.707946,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        "turn_right_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt_int",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        "turn_right_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                0.630957,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
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
        0.125,
        "woodCrash1",
        0.125,
        "woodCrash2",
        0.125,
        "woodCrash3",
        0.125,
        "woodCrash4",
        0.125,
        "woodCrash5",
        0.125,
        "woodCrash6",
        0.125,
        "woodCrash7",
        0.125
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_vehicle_truck_p"
            ],
            "speechsingular": [
                "veh_vehicle_truck_s"
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
    "steeraheadplan": 0.26,
    "steeraheadsimul": 0.5,
    "supplyradius": 6.8,
    "switchtime": 0.83,
    "tbody": 150,
    "terraincoef": 2,
    "textplural": "trucks",
    "textsingular": "truck",
    "texturelist": [],
    "texturesources": {
        "camo": {
            "author": "Red Hammer Studios",
            "displayname": "3-Color Camo",
            "textures": [
                "/rhsafrf/addons/rhs_gaz66/data/gaz66ru_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/tentru_co.paa"
            ]
        },
        "cdf": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "textures": [
                "/rhsafrf/addons/rhs_gaz66/data/gaz66_cdf_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/tent_cdf_co.paa"
            ]
        },
        "chdkz": {
            "author": "Red Hammer Studios",
            "displayname": "ChDKZ",
            "textures": [
                "/rhsafrf/addons/rhs_gaz66/data/gaz66_chdk_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/tent_chdk_co.paa"
            ]
        },
        "rhs_sand": {
            "author": "Red Hammer Studios",
            "displayname": "Sand",
            "textures": [
                "/rhsafrf/addons/rhs_gaz66_camo/data/gaz66_sand_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/tent_co.paa",
                "/rhsafrf/addons/rhs_gaz66_camo/data/rhs_gaz66_kung_sand_co.paa",
                "/rhsafrf/addons/rhs_gaz66_camo/data/rhs_gaz66_ap2kung_sand_co.paa",
                "/rhsafrf/addons/rhs_gaz66_camo/data/rhs_gaz66_repkung_sand_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "textures": [
                "/rhsafrf/addons/rhs_gaz66/data/gaz66_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/tent_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_kung_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_ap2kung_co.paa",
                "/rhsafrf/addons/rhs_gaz66/data/rhs_gaz66_repkung_co.paa"
            ]
        }
    },
    "tf_haslrradio_api": 0,
    "threat": [
        0,
        0,
        0
    ],
    "thrustdelay": 1.5,
    "torquecurve": [
        [
            0,
            0
        ],
        [
            0.3125,
            0.897887
        ],
        [
            0.375,
            0.940141
        ],
        [
            0.5,
            0.961268
        ],
        [
            0.625,
            1
        ],
        [
            0.78125,
            1
        ],
        [
            0.875,
            0.961268
        ],
        [
            1,
            0.464789
        ]
    ],
    "tracksspeed": 0,
    "transmissionlosses": 8,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 10,
            "name": "FirstAidKit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 64,
    "transportmaxmagazines": 256,
    "transportmaxweapons": 64,
    "transportrepair": 2000000000.0,
    "transportsoldier": 1,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 5,
    "turrets": {},
    "type": 0,
    "typicalcargo": [
        "rhs_msv_driver"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoNoWeapon",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "useractions": {
        "cabinlights_toggle": {
            "condition": "(player == driver this) AND (isLightOn this)",
            "displayname": "Toggle cabin lights",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "lockTarget",
            "showwindow": 0,
            "statement": "[this,1] call rhs_fnc_carLightToggle"
        },
        "lights_toggle": {
            "condition": "(player == driver this) AND (isLightOn this)",
            "displayname": "Toggle short/long lights",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "vehLockTargets",
            "showwindow": 0,
            "statement": "[this,0] call rhs_fnc_carLightToggle"
        },
        "searchlight_adjust": {
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this) AND (this animationPhase 'searchlight_hide' == 0)",
            "displayname": "Adjust searchlight",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "",
            "showwindow": 0,
            "statement": "[this] spawn rhs_fnc_adjustSearchlight"
        },
        "searchlight_toggle": {
            "condition": "(player == driver this) AND (isLightOn this)",
            "displayname": "Toggle searchlight",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "",
            "showwindow": 0,
            "statement": "[this,3] call rhs_fnc_carLightToggle"
        },
        "wipersoff": {
            "condition": "Alive(this) AND (player == driver this) AND this animationPhase 'wipers' > 0.5",
            "displayname": "Wipers off",
            "onlyforplayer": 1,
            "position": "",
            "radius": 12,
            "showwindow": 0,
            "statement": "[this,1] spawn rhs_fnc_wipers"
        },
        "wiperson": {
            "condition": "Alive(this) AND (player == driver this) AND isengineon (this) AND this animationPhase 'wipers' < 0.5",
            "displayname": "Wipers on",
            "onlyforplayer": 1,
            "position": "",
            "radius": 12,
            "showwindow": 0,
            "statement": "[this,0] spawn rhs_fnc_wipers"
        }
    },
    "vehicleclass": "rhs_vehclass_truck",
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
    "viewcargoshadowdiff": 0.05,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.85,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.42,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": -15,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.4,
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
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.15,
    "waterspeedfactor": 0.2,
    "weapons": [
        "TruckHorn"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 3.3,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheelmask": "wheel_X_X",
    "wheels": {
        "lf": {
            "bonename": "wheel_1_1_damper",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 6.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1.2
                ],
                [
                    0.5,
                    1.13
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 2986,
            "mass": 80,
            "maxbraketorque": 8500,
            "maxcompression": 0.3,
            "maxdroop": 0.25,
            "maxhandbraketorque": 0,
            "moi": 28,
            "side": "left",
            "springdamperrate": 10342,
            "springstrength": 61938,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_1_axis",
            "width": 0.32
        },
        "lr": {
            "bonename": "wheel_1_2_damper",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 6.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1.2
                ],
                [
                    0.5,
                    1.13
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 5,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 2986,
            "mass": 80,
            "maxbraketorque": 8500,
            "maxcompression": 0.3,
            "maxdroop": 0.25,
            "maxhandbraketorque": 20000,
            "moi": 28,
            "side": "left",
            "springdamperrate": 10342,
            "springstrength": 61938,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_1_2_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.32
        },
        "rf": {
            "bonename": "wheel_2_1_damper",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 6.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1.2
                ],
                [
                    0.5,
                    1.13
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 2986,
            "mass": 80,
            "maxbraketorque": 8500,
            "maxcompression": 0.3,
            "maxdroop": 0.25,
            "maxhandbraketorque": 0,
            "moi": 28,
            "side": "right",
            "springdamperrate": 10342,
            "springstrength": 61938,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_2_1_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_1_axis",
            "width": 0.32
        },
        "rr": {
            "bonename": "wheel_2_2_damper",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 6.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1.2
                ],
                [
                    0.5,
                    1.13
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 5,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 2986,
            "mass": 80,
            "maxbraketorque": 8500,
            "maxcompression": 0.3,
            "maxdroop": 0.25,
            "maxhandbraketorque": 20000,
            "moi": 28,
            "side": "right",
            "springdamperrate": 10342,
            "springstrength": 61938,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_2_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_2_axis",
            "width": 0.32
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_01",
        1.99526,
        1,
        75
    ],
    "woodcrash1": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_02",
        1.99526,
        1,
        75
    ],
    "woodcrash2": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_03",
        1.99526,
        1,
        75
    ],
    "woodcrash3": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_04",
        1.99526,
        1,
        75
    ],
    "woodcrash4": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_05",
        1.99526,
        1,
        75
    ],
    "woodcrash5": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_06",
        1.99526,
        1,
        75
    ],
    "woodcrash6": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_07",
        1.99526,
        1,
        75
    ],
    "woodcrash7": [
        "A3/Sounds_F/vehicles2/soft/shared/collisions/Vehicle_Soft_Collision_Medium_Wood_08",
        1.99526,
        1,
        75
    ]
}