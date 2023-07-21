d = {
    "_generalmacro": "Offroad_01_base_F",
    "accelaidforcecoef": 5,
    "accelaidforcespd": 4.23,
    "accelaidforceyoffset": -0.85,
    "acceleration": 15,
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "LSvetla"
        ],
        [
            "Left2"
        ],
        [
            "RSvetla"
        ],
        [
            "Right2"
        ],
        [
            "Long_Left2",
            "Long_Right2"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.2,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 1,
            "source": "user"
        },
        "door_lb": {
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundposition": "osa_dvere_lz",
            "source": "door"
        },
        "door_lf": {
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundposition": "osa_dvere_lp",
            "source": "door"
        },
        "door_rb": {
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundposition": "osa_dvere_pz",
            "source": "door"
        },
        "door_rf": {
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundposition": "osa_dvere_pp",
            "source": "door"
        },
        "gearbox": {
            "animperiod": 0.8,
            "sound": "RHS_gearbox",
            "soundposition": "gear_axis",
            "source": "door"
        },
        "hitdoor_1_1": {
            "hitpoint": "HitDoor_1_1",
            "raw": 1,
            "source": "Hit"
        },
        "hitdoor_1_2": {
            "hitpoint": "HitDoor_1_2",
            "raw": 1,
            "source": "Hit"
        },
        "hitdoor_2_1": {
            "hitpoint": "HitDoor_2_1",
            "raw": 1,
            "source": "Hit"
        },
        "hitdoor_2_2": {
            "hitpoint": "HitDoor_2_2",
            "raw": 1,
            "source": "Hit"
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
        "hithood": {
            "hitpoint": "HitHood",
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
            "animperiod": 1e-11,
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
            "animperiod": 1e-11,
            "displayname": "hide spare wheel",
            "initphase": 0,
            "mass": 1,
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
            "sound": "RHS_Wipers",
            "soundposition": "wiper_1_axis",
            "source": "door"
        }
    },
    "antirollbarforcecoef": 0.5,
    "antirollbarforcelimit": 0.5,
    "antirollbarspeedmax": 80,
    "antirollbarspeedmin": 10,
    "armor": 52,
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
    "armorlights": 0.05,
    "armorstructural": 4,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "SemiOpenCarAttenuation2",
    "attributes": {
        "door_lb": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open left back door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "Door_LB"
        },
        "door_lf": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open front left door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "Door_LF"
        },
        "door_rb": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open right back door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "Door_RB"
        },
        "door_rf": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open front right door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "Door_RF"
        },
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
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
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
            "expression": "if(_value >= 0)then{[_this,[['Number', cDecals4CarsNumberPlaces, _this getVariable ['rhs_decalNumber_type','LicensePlate'], _value]]] call rhs_fnc_decalsInit};",
            "property": "rhs_decalNumber",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cDecals4CarsNumberPlaces, _value]]] call rhs_fnc_decalsInit",
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
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
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
    "audible": 5,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 3,
    "brakeidlespeed": 0.5,
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
    "camshakecoef": 0.8,
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
    "canhidedriver": 0,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_UAZ_Cargo01",
        "RHS_UAZ_Cargo01",
        "RHS_UAZ_Cargo01",
        "RHS_UAZ_Cargo01",
        "RHS_UAZ_Cargo01",
        "RHS_UAZ_Cargo02"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1",
        "Compartment2",
        "Compartment2",
        "Compartment2",
        "Compartment2",
        "Compartment2"
    ],
    "cargodoors": [
        "Door_RF",
        "Door_LB",
        "Door_LB",
        "Door_RB"
    ],
    "cargogetinaction": [
        "GetInLow"
    ],
    "cargogetoutaction": [
        "GetOutLow"
    ],
    "cargoiscodriver": [
        1,
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
    "category": "Car",
    "centrebias": 1.3,
    "changegearmineffectivity": [
        0.95,
        0.15,
        0.85,
        0.95,
        0.95,
        0.95
    ],
    "clutchstrength": 15,
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
            -5.224,
            "N",
            0,
            "D1",
            3.78,
            "D2",
            2.6,
            "D3",
            1.55,
            "D4",
            1
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            5.125
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
    "cost": 50000,
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
    "crew": "rhs_vmf_flora_driver",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.8,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_skla.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_skla_in.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_main_metal.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_main_metal_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_main_metal_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_other_metal.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_other_metal_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_other_metal_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_car/data/drziaky.rvmat",
            "rhsafrf/addons/rhs_a2port_car/data/drziaky.rvmat",
            "rhsafrf/addons/rhs_a2port_car/data/drziaky_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_mount.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_mount_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/uaz_mount_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/rhs_uaz_wheels.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/rhs_uaz_wheels_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_car/UAZ/Data/rhs_uaz_wheels_damage.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "damperdamping": 1,
    "damperforce": 1,
    "dampersbumpcoef": 4,
    "dampersize": 0.1,
    "dampingratefullthrottle": 0.08,
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
    "displayname": "UAZ-3151",
    "dlc": "RHS_AFRF",
    "driveraction": "RHS_UAZ_driver",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "Door_LF",
    "driverforceoptics": 0,
    "driverinaction": "RHS_UAZ_driver",
    "driverlefthandanimname": "drivewheel",
    "driverleftleganimname": "pedalL",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "shift",
    "driverrightleganimname": "pedalR",
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
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/rhs_uaz_vmf.paa",
    "editorsubcategory": "rhs_EdSubcat_car",
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
    "enginebrakecoef": 0.9,
    "engineer": 0,
    "enginelosses": 14,
    "enginemoi": 1.1,
    "enginepower": 67,
    "enginestartspeed": 1.5,
    "epeimpulsedamagecoef": 15,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "dammaged": "_this call rhs_fnc_wheelDamaged",
            "engine": "if(_this select 1)then{_this call RHS_fnc_gearSound};",
            "init": "_this call rhs_fnc_a2port_car_init"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectOffroad",
            "position": "vyfuk start"
        }
    },
    "explosioneffect": "FuelExplosion",
    "explosionshielding": 1,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2,
        -8.75
    ],
    "faction": "rhs_faction_vmf",
    "features": "",
    "featuretype": 0,
    "fireresistance": 5,
    "forcehidedriver": 1,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 20,
    "frontbias": 1.5,
    "frontrearsplit": 0.5,
    "fuelcapacity": 30,
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
    "getinaction": "GetInOffroad",
    "getinoutonproxy": 0,
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
        "camo2g",
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
        "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_ind_co.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/RHS_Decals/Data/Labels/Misc/no_ca.paa"
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
            "radius": 0.1,
            "visual": "camo1"
        },
        "hitdoor_1_1": {
            "armor": 0.2,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.075,
            "name": "door11",
            "passthrough": 0.1,
            "radius": 0.17,
            "visual": "-"
        },
        "hitdoor_1_2": {
            "armor": 0.2,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.075,
            "name": "door12",
            "passthrough": 0.1,
            "radius": 0.17,
            "visual": "-"
        },
        "hitdoor_2_1": {
            "armor": 0.2,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.075,
            "name": "door21",
            "passthrough": 0.1,
            "radius": 0.17,
            "visual": "-"
        },
        "hitdoor_2_2": {
            "armor": 0.2,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.075,
            "name": "door22",
            "passthrough": 0.1,
            "radius": 0.17,
            "visual": "-"
        },
        "hitengine": {
            "armor": 0.5,
            "armorcomponent": "Hit_Engine",
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
            "material": -1,
            "name": "Hit_Engine",
            "passthrough": 0.2,
            "radius": 0.16,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 0.5,
            "material": -1,
            "name": "Hit_Fuel",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "-"
        },
        "hitglass1": {
            "armor": 0.1,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.05,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.05,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.05,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 0.05,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 0.05,
            "explosionshielding": 2,
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "radius": 0.2,
            "visual": "glass6"
        },
        "hithood": {
            "armor": 0.3,
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": 0.075,
            "name": "hood1",
            "passthrough": 0.1,
            "radius": 0.17,
            "visual": "-"
        },
        "hithull": {
            "armor": 0.5,
            "material": -1,
            "name": "hull",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "-"
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
            "armor": 0.175,
            "armorcomponent": "wheel_1_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "wheel_1_2_steering",
            "passthrough": 0.3,
            "radius": 0.15,
            "visual": "wheel_1_2_damage"
        },
        "hitlfwheel": {
            "armor": 0.175,
            "armorcomponent": "wheel_1_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "wheel_1_1_steering",
            "passthrough": 0.3,
            "radius": 0.15,
            "visual": "wheel_1_1_damage"
        },
        "hitlglass": {
            "armor": 0.2,
            "explosionshielding": 2,
            "material": -1,
            "name": "sklo predni L",
            "passthrough": 0
        },
        "hitlightl": {
            "armor": 0.02,
            "material": -1,
            "minimalhit": 0.1,
            "name": "L svetlo",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hitlightr": {
            "armor": 0.02,
            "material": -1,
            "minimalhit": 0.1,
            "name": "P svetlo",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
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
            "armor": 0.175,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "wheel_2_2_steering",
            "passthrough": 0.3,
            "radius": 0.15,
            "visual": "wheel_2_2_damage"
        },
        "hitrfwheel": {
            "armor": 0.175,
            "armorcomponent": "wheel_2_1_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "wheel_2_1_steering",
            "passthrough": 0.3,
            "radius": 0.15,
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
        "hitsearchlight": {
            "armor": 0.02,
            "material": -1,
            "minimalhit": 0.1,
            "name": "searchlight",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hitspare": {
            "armor": 0.175,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "spare1",
            "passthrough": 0.3,
            "radius": 0.15,
            "visual": "-"
        },
        "usespare": {
            "armor": 1,
            "armorcomponent": "wheel_2_2_hide",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": -0.00833333,
            "name": "",
            "passthrough": 0.3,
            "radius": 0.15,
            "visual": "-"
        }
    },
    "holdoffroadformation": 1,
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsafrf/addons/rhs_a2port_car/data/mapico/icomap_uaz_ca.paa",
    "idlerpm": 750,
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
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
    "latency": 1,
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
    "library": {
        "libtextdesc": "The 4x4 pickup by Generic Motors is a perfect choice for farmers and hunters. The durable chassis and powerful engine have been designed to withstand anything from the cratered highways of Central Europe to the rugged terrain of the Mediterranean. The armed version is fitted either with a .50 caliber heavy machine gun or an anti-tank recoilless rifle. It provides the combination of mobility and firepower to many paramilitary and guerilla forces in local conflicts around the globe. Specialized versions, which sport a hard rear cover and rack-mounted communications equipment, are in use by law enforcement, national park rangers, and armed forces. These vehicles feature a large floodlight, loudspeakers, and long-range antennas."
    },
    "limitedspeedcoef": 0.5,
    "lockdetectionsystem": 0,
    "longstiff": 15000,
    "magazines": [],
    "mapsize": 4,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0,
    "maxgforce": 3,
    "maximumload": 2500,
    "maxomega": 523.6,
    "maxspeed": 120,
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
        "pos cargo 2",
        "pos cargo 2",
        "pos cargo 1"
    ],
    "memorypointsgetincargodir": [
        "pos codriver dir",
        "pos cargo dir 2",
        "pos cargo dir 2",
        "pos cargo dir 1"
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
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "memorypointtrackbll": "TrackBLL",
    "memorypointtrackblr": "TrackBLR",
    "memorypointtrackbrl": "TrackBRL",
    "memorypointtrackbrr": "TrackBRR",
    "memorypointtrackfll": "TrackFLL",
    "memorypointtrackflr": "TrackFLR",
    "memorypointtrackfrl": "TrackFRL",
    "memorypointtrackfrr": "TrackFRR",
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
    "minomega": 20,
    "mintotaldamagethreshold": 0.21,
    "model": "rhsafrf/addons/rhs_a2port_car/UAZ/UAZ.p3d",
    "namesound": "veh_car",
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
    "normalspeedforwardcoef": 0.8,
    "numberphysicalwheels": 4,
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
    "peaktorque": 173,
    "picture": "rhsafrf/addons/rhs_a2port_car/data/ico/rhs_uaz_pic_ca.paa",
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
        "turndecreaseconst": 8,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "turnincreaseconst": 0.7,
        "turnincreaselinear": 2.5,
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
    "rearbias": 1.5,
    "redrpm": 5000,
    "reflectors": {
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
            "hitpointclass": "HitLightL",
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
            "hitpointclass": "HitLightL",
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
            "hitpointclass": "HitLightL",
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
            "hitpointclass": "HitLightR",
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
            "hitpointclass": "HitLightR",
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
            "hitpointclass": "HitLightL",
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
            "hitpointclass": "HitLightR",
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
            "hitpointclass": "HitLightR",
            "innerangle": 40,
            "intensity": 2.5,
            "outerangle": 120,
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
            "hitpointclass": "HitSearchlight",
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
        "backmirror": {
            "bboxes": [
                "PIP_3_TL",
                "PIP_3_TR",
                "PIP_3_BL",
                "PIP_3_BR"
            ],
            "cameraview1": {
                "fov": 0.7,
                "pointdirection": "m3d",
                "pointposition": "m3p",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget2"
        },
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
        "['Number', cDecals4CarsNumberPlaces, 'LicensePlate']",
        "['Label', cDecalsCarsRightArmyPlaces, 'Army', [3,1]]"
    ],
    "rhs_fuelcapacity": 78,
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
        0,
        1
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 0,
    "simulation": "carx",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [],
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
        1
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
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/uaz469_engine_ext_stop1",
        1.41254,
        1,
        200
    ],
    "soundengineoffint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/uaz469_engine_int_stop1",
        1.58489,
        1
    ],
    "soundengineonext": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/uaz469_engine_ext_start1",
        1.41254,
        1,
        200
    ],
    "soundengineonint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/uaz469_engine_int_start1",
        1.58489,
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
        "rhsafrf/addons/rhs_a2port_car/sounds/Gear_Change",
        2,
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
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/ext-uaz469_engine-getin",
        1.58489,
        1,
        9
    ],
    "soundgetout": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/soft/uaz469/ext-uaz469_engine-getout",
        1.58489,
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
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_16_dirt_acceleration",
                1.12202,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 1])"
        },
        "acceleration_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                1.41254,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        "acceleration_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_16_dirt_acceleration_int",
                3.16228,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        "acceleration_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                3.16228,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        "breaking_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_14_dirt_breaking",
                1.12202,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        "breaking_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_04",
                1.41254,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "breaking_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_14_dirt_breaking_int",
                3.16228,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "breaking_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_04_int",
                3.16228,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "engine": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(900/\t4000),(2100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_acceleration",
                1.41254,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(870/\t4000),(1100/\t4000)])\t*\t((rpm/\t4000) factor[(2100/\t4000),(1300/\t4000)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t\t((rpm/\t4000) factor[(1300/\t4000),(3100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_low1",
                1.41254,
                1,
                240
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(1250/\t4000),(2050/\t4000)])\t*\t((rpm/\t4000) factor[(3100/\t4000),(2300/\t4000)]))"
        },
        "engine1_int": {
            "frequency": "0.8\t+\t\t((rpm/\t4000) factor[(1300/\t4000),(3100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_low1",
                1.41254,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(1250/\t4000),(2050/\t4000)])\t*\t((rpm/\t4000) factor[(3100/\t4000),(2300/\t4000)]))"
        },
        "engine1_thrust_ext": {
            "frequency": "0.8\t+\t\t((rpm/\t4000) factor[(1300/\t4000),(3100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_low1_exhaust",
                1.12202,
                1,
                280
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(1250/\t4000),(2050/\t4000)])\t*\t((rpm/\t4000) factor[(3100/\t4000),(2300/\t4000)]))"
        },
        "engine1_thrust_int": {
            "frequency": "0.8\t+\t\t((rpm/\t4000) factor[(1300/\t4000),(3100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_low1_exhaust",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(1250/\t4000),(2050/\t4000)])\t*\t((rpm/\t4000) factor[(3100/\t4000),(2300/\t4000)]))"
        },
        "engine2_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(2200/\t4000),(4100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1",
                1.25893,
                1,
                280
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(2250/\t4000),(3050/\t4000)])\t*\t((rpm/\t4000) factor[(4100/\t4000),(3300/\t4000)]))"
        },
        "engine2_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(2200/\t4000),(4100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(2250/\t4000),(3050/\t4000)])\t*\t((rpm/\t4000) factor[(4100/\t4000),(3300/\t4000)]))"
        },
        "engine2_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(2200/\t4000),(4100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1_exhaust",
                1.12202,
                1,
                320
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(2250/\t4000),(3050/\t4000)])\t*\t((rpm/\t4000) factor[(4100/\t4000),(3300/\t4000)]))"
        },
        "engine2_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(2200/\t4000),(4100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1_exhaust",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(2250/\t4000),(3050/\t4000)])\t*\t((rpm/\t4000) factor[(4100/\t4000),(3300/\t4000)]))"
        },
        "engine3_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(3300/\t4000),(4900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1",
                1.25893,
                1,
                320
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(3250/\t4000),(4050/\t4000)])\t*\t((rpm/\t4000) factor[(4870/\t4000),(4200/\t4000)]))"
        },
        "engine3_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(3300/\t4000),(4900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(3250/\t4000),(4050/\t4000)])\t*\t((rpm/\t4000) factor[(4870/\t4000),(4200/\t4000)]))"
        },
        "engine3_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(3300/\t4000),(4900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1_exhaust",
                1.12202,
                1,
                360
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(3250/\t4000),(4050/\t4000)])\t*\t((rpm/\t4000) factor[(4870/\t4000),(4200/\t4000)]))"
        },
        "engine3_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(3300/\t4000),(4900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1_exhaust",
                1.12202,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(3250/\t4000),(4050/\t4000)])\t*\t((rpm/\t4000) factor[(4870/\t4000),(4200/\t4000)]))"
        },
        "engine4_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(4200/\t4000),(6200/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1",
                1.12202,
                1,
                360
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(4150/\t4000),(4800/\t4000)])\t*\t((rpm/\t4000) factor[(6150/\t4000),(5150/\t4000)]))"
        },
        "engine4_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(4200/\t4000),(6200/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(4150/\t4000),(4800/\t4000)])\t*\t((rpm/\t4000) factor[(6150/\t4000),(5150/\t4000)]))"
        },
        "engine4_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(4200/\t4000),(6200/\t4000)])*0.3",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1_exhaust",
                1,
                1,
                400
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(4150/\t4000),(4800/\t4000)])\t*\t((rpm/\t4000) factor[(6150/\t4000),(5150/\t4000)]))"
        },
        "engine4_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(4200/\t4000),(6200/\t4000)])*0.3",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1_exhaust",
                1.12202,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(4150/\t4000),(4800/\t4000)])\t*\t((rpm/\t4000) factor[(6150/\t4000),(5150/\t4000)]))"
        },
        "engine5_ext": {
            "frequency": "0.95\t+\t((rpm/\t4000) factor[(5100/\t4000),(6900/\t4000)])*0.15",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1",
                1.12202,
                1,
                420
            ],
            "volume": "engineOn*camPos*((rpm/\t4000) factor[(5100/\t4000),(6100/\t4000)])"
        },
        "engine5_int": {
            "frequency": "0.95\t+\t((rpm/\t4000) factor[(5100/\t4000),(6900/\t4000)])*0.15",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*((rpm/\t4000) factor[(5100/\t4000),(6100/\t4000)])"
        },
        "engine5_thrust_ext": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(5100/\t4000),(6900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_high1_exhaust",
                1.25893,
                1,
                450
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t4000) factor[(5100/\t4000),(6100/\t4000)])"
        },
        "engine5_thrust_int": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(5100/\t4000),(6900/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_high1_exhaust",
                1.12202,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t4000) factor[(5100/\t4000),(6100/\t4000)])"
        },
        "engine_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(900/\t4000),(2100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_acceleration",
                1.41254,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(870/\t4000),(1100/\t4000)])\t*\t((rpm/\t4000) factor[(2100/\t4000),(1300/\t4000)]))"
        },
        "enginethrust": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(900/\t4000),(2100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_low1_exhaust",
                1.12202,
                1,
                250
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(870/\t4000),(1100/\t4000)])\t*\t((rpm/\t4000) factor[(2100/\t4000),(1300/\t4000)]))"
        },
        "enginethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t4000) factor[(900/\t4000),(2100/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_low1_exhaust",
                1.41254,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(870/\t4000),(1100/\t4000)])\t*\t((rpm/\t4000) factor[(2100/\t4000),(1300/\t4000)]))"
        },
        "idle_ext": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(200/\t4000),(1150/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_idle",
                1.58489,
                1,
                150
            ],
            "volume": "engineOn*camPos*(((rpm/\t4000) factor[(450/\t4000),(590/\t4000)])\t*\t((rpm/\t4000) factor[(900/\t4000),(690/\t4000)]))"
        },
        "idle_int": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(200/\t4000),(1150/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_idle",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t4000) factor[(450/\t4000),(590/\t4000)])\t*\t((rpm/\t4000) factor[(900/\t4000),(690/\t4000)]))"
        },
        "idlethrust": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(200/\t4000),(1150/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_ext_idle_exhaust",
                1.25893,
                1,
                200
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(450/\t4000),(590/\t4000)])\t*\t((rpm/\t4000) factor[(900/\t4000),(690/\t4000)]))"
        },
        "idlethrust_int": {
            "frequency": "0.9\t+\t((rpm/\t4000) factor[(200/\t4000),(1150/\t4000)])*0.2",
            "sound": [
                "rhsafrf/addons/rhs_a2port_car/sounds/UAZ/uaz_int_idle_exhaust",
                1.25893,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t4000) factor[(450/\t4000),(590/\t4000)])\t*\t((rpm/\t4000) factor[(900/\t4000),(690/\t4000)]))"
        },
        "noisein": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/noise_int_car_3",
                1,
                1
            ],
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        "noiseout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/noise_ext_car_3",
                1.58489,
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
            "RHS_UAZ469_Engine_RPM0_EXT_SoundSet",
            "RHS_UAZ469_Engine_RPM1_EXT_SoundSet",
            "RHS_UAZ469_Engine_RPM2_EXT_SoundSet",
            "RHS_UAZ469_Engine_RPM3_EXT_SoundSet",
            "RHS_UAZ469_Engine_EXT_Burst_SoundSet",
            "UAZ469_Rattling_EXT_SoundSet",
            "UAZ469_Stress_EXT_SoundSet",
            "UAZ469_Rain_EXT_SoundSet",
            "RHS_UAZ469_Tires_Rock_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Grass_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Sand_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Gravel_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Mud_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Asphalt_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Water_Fast_EXT_SoundSet",
            "RHS_UAZ469_Tires_Rock_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Grass_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Sand_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Gravel_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Mud_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Asphalt_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Water_Slow_EXT_SoundSet",
            "RHS_UAZ469_Tires_Turn_Hard_EXT_SoundSet",
            "RHS_UAZ469_Tires_Turn_Soft_EXT_SoundSet",
            "RHS_UAZ469_Tires_Brake_Hard_EXT_SoundSet",
            "RHS_UAZ469_Tires_Brake_Soft_EXT_SoundSet",
            "",
            "Tires_Movement_Dirt_Ext_01_SoundSet"
        ],
        "soundsetsint": [
            "RHS_UAZ469_Engine_RPM0_INT_SoundSet",
            "RHS_UAZ469_Engine_RPM1_INT_SoundSet",
            "RHS_UAZ469_Engine_RPM2_INT_SoundSet",
            "RHS_UAZ469_Engine_RPM3_INT_SoundSet",
            "RHS_UAZ469_Engine_INT_Burst_SoundSet",
            "UAZ469_Rattling_INT_SoundSet",
            "UAZ469_Stress_INT_SoundSet",
            "UAZ469_Rain_INT_SoundSet",
            "RHS_UAZ469_Tires_Rock_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Grass_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Sand_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Gravel_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Mud_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Asphalt_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Water_Fast_INT_SoundSet",
            "RHS_UAZ469_Tires_Rock_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Grass_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Sand_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Gravel_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Mud_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Asphalt_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Water_Slow_INT_SoundSet",
            "RHS_UAZ469_Tires_Turn_Hard_INT_SoundSet",
            "RHS_UAZ469_Tires_Turn_Soft_INT_SoundSet",
            "RHS_UAZ469_Tires_Brake_Hard_INT_SoundSet",
            "RHS_UAZ469_Tires_Brake_Soft_INT_SoundSet",
            "",
            "Tires_Movement_Dirt_Int_01_SoundSet"
        ],
        "tiresasphaltin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_asfalt_2",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        "tiresasphaltout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_asfalt_2",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        "tiresgrassin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_dirt_soft_2",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        "tiresgrassout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_dirt_soft_2",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        "tiresgravelin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_gravel_1",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        "tiresgravelout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_gravel_1",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        "tiresmudin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int-tires-mud2",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        "tiresmudout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext-tires-mud2",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        "tiresrockin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int_tires_dirt_soft_1",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        "tiresrockout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext_tires_dirt_soft_1",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        "tiressandin": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/int-tires-sand2",
                1.12202,
                1
            ],
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        "tiressandout": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/tires/ext-tires-sand1",
                1.41254,
                1,
                60
            ],
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        "turn_left_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt",
                1.12202,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[1, 15])"
        },
        "turn_left_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                1.41254,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        "turn_left_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt_int",
                3.16228,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        "turn_left_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                3.16228,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        "turn_right_ext_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt",
                1,
                1,
                60
            ],
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        "turn_right_ext_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02",
                1.41254,
                1,
                80
            ],
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "turn_right_int_dirt": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_18_dirt_int",
                3.16228,
                1
            ],
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "turn_right_int_road": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/soft/noises/slipping_tires_loop_02_int",
                3.16228,
                1
            ],
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
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
                "veh_vehicle_car_p"
            ],
            "speechsingular": [
                "veh_vehicle_car_s"
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
    "steeraheadplan": 0.35,
    "steeraheadsimul": 0.5,
    "supplyradius": -1,
    "switchtime": 0.51,
    "tbody": 150,
    "terraincoef": 0.4,
    "textplural": "cars",
    "textsingular": "car",
    "texturelist": [],
    "texturesources": {
        "camo": {
            "author": "Red Hammer Studios",
            "displayname": "Camo",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_co.paa"
            ]
        },
        "camo1": {
            "author": "Red Hammer Studios",
            "displayname": "Chedaki",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_001_co.paa"
            ]
        },
        "camo2": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_002_co.paa"
            ]
        },
        "camo3": {
            "author": "Red Hammer Studios",
            "displayname": "Civil",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_civil_co.paa"
            ]
        },
        "camo4": {
            "author": "Red Hammer Studios",
            "displayname": "UN",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_un_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [
                "rhs_faction_msv",
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_car/uaz/data/uaz_main_ind_co.paa"
            ]
        }
    },
    "tf_haslrradio_api": 0,
    "threat": [
        0,
        0,
        0
    ],
    "thrustdelay": 0.2,
    "torquecurve": [
        [
            0.15,
            0.289017
        ],
        [
            0.3,
            0.895954
        ],
        [
            0.48,
            1
        ],
        [
            0.52,
            1
        ],
        [
            0.7,
            0.953757
        ],
        [
            0.8,
            0.895954
        ],
        [
            0.9,
            0.809249
        ],
        [
            1,
            0.693642
        ]
    ],
    "tracksspeed": 0,
    "transmissionlosses": 20,
    "transportammo": 0,
    "transportbackpacks": {},
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 4,
            "name": "FirstAidKit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 6,
    "transportmaxmagazines": 64,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 6,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 2.5,
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
            "armorlights": 0.4,
            "body": "",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": 1,
            "components": {},
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
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
            "gunneraction": "ManActTestDriverOut",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
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
            "gunnerrighthandanimname": "",
            "gunnerrightleganimname": "",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.4,
                    "explosionshielding": 0.2,
                    "material": -1,
                    "name": "zbran",
                    "passthrough": 0,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.8,
                    "explosionshielding": 0.4,
                    "material": -1,
                    "name": "vez",
                    "passthrough": 0.5,
                    "visual": "vez"
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
            "maxelev": 40,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "machinegun",
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
            "outgunnermayfire": 1,
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
                "A3/sounds_f/dummysound",
                0.316228,
                1,
                15
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
        }
    },
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
        "lights_toggle": {
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this)",
            "displayname": "Toggle short/long lights",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "vehLockTargets",
            "showwindow": 0,
            "statement": "[this,2] call rhs_fnc_carLightToggle"
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
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this)",
            "displayname": "Toggle searchlight",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 12,
            "shortcut": "lockTarget",
            "showwindow": 0,
            "statement": "[this,3] call rhs_fnc_carLightToggle"
        },
        "wipersoff": {
            "condition": "(player == driver this) AND this animationPhase 'wipers' > 0.5",
            "displayname": "Wipers off",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 2,
            "showwindow": 0,
            "statement": "[this,1] spawn rhs_fnc_wipers"
        },
        "wiperson": {
            "condition": "(player == driver this) AND isengineon (this) AND this animationPhase 'wipers' < 0.5",
            "displayname": "Wipers on",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 2,
            "showwindow": 0,
            "statement": "[this,0] spawn rhs_fnc_wipers"
        }
    },
    "vehicleclass": "rhs_vehclass_car",
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
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.2,
    "waterspeedfactor": 0.4,
    "weapons": [
        "SportCarHorn"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.45,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.0416667,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheelmask": "wheel_X_X",
    "wheels": {
        "lf": {
            "bonename": "wheel_1_1_damper",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 0.1,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 20,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 24,
            "side": "left",
            "springdamperrate": 2400,
            "springstrength": 14000,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_1_axis",
            "width": 0.16
        },
        "lr": {
            "bonename": "wheel_1_2_damper",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 0.1,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 20,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "maxhandbraketorque": 3000,
            "moi": 24,
            "side": "left",
            "springdamperrate": 2400,
            "springstrength": 14000,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_1_2_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.16
        },
        "rf": {
            "bonename": "wheel_2_1_damper",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 0.1,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 20,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 24,
            "side": "right",
            "springdamperrate": 2400,
            "springstrength": 14000,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_2_1_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_1_axis",
            "width": 0.16
        },
        "rr": {
            "bonename": "wheel_2_2_damper",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 0.1,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 10000,
            "mass": 20,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "maxhandbraketorque": 3000,
            "moi": 24,
            "side": "right",
            "springdamperrate": 2400,
            "springstrength": 14000,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_2_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_2_axis",
            "width": 0.16
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