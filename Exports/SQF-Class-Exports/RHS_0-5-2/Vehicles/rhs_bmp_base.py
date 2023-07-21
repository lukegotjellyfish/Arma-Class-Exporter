d = {
    "_generalmacro": "Tank_F",
    "accelaidforcecoef": 4.3,
    "accelaidforcespd": 2.23,
    "accelaidforceyoffset": -3.9,
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
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "cargohandler1": {
            "animperiod": 1,
            "initphase": 1,
            "source": "door"
        },
        "crate_l1_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide l1 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "crate_l2_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide l2 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "crate_l3_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide l3 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "crate_r1_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide r1 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "crate_r2_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide r2 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "crate_r3_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide r3 crate",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "doorl": {
            "animperiod": 1,
            "source": "door"
        },
        "doorr": {
            "animperiod": 1,
            "source": "door"
        },
        "hatchc": {
            "animperiod": 2.1,
            "source": "door"
        },
        "hatchc2": {
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
        "hitcomsight": {
            "hitpoint": "HitComSight",
            "source": "Hit"
        },
        "hitmainsight": {
            "hitpoint": "HitMainSight",
            "source": "Hit"
        },
        "hitperiscope1": {
            "hitpoint": "HitPeriscope1",
            "source": "Hit"
        },
        "hitperiscope10": {
            "hitpoint": "HitPeriscope10",
            "source": "Hit"
        },
        "hitperiscope11": {
            "hitpoint": "HitPeriscope11",
            "source": "Hit"
        },
        "hitperiscope12": {
            "hitpoint": "HitPeriscope12",
            "source": "Hit"
        },
        "hitperiscope13": {
            "hitpoint": "HitPeriscope13",
            "source": "Hit"
        },
        "hitperiscope14": {
            "hitpoint": "HitPeriscope14",
            "source": "Hit"
        },
        "hitperiscope2": {
            "hitpoint": "HitPeriscope2",
            "source": "Hit"
        },
        "hitperiscope3": {
            "hitpoint": "HitPeriscope3",
            "source": "Hit"
        },
        "hitperiscope4": {
            "hitpoint": "HitPeriscope4",
            "source": "Hit"
        },
        "hitperiscope5": {
            "hitpoint": "HitPeriscope5",
            "source": "Hit"
        },
        "hitperiscope6": {
            "hitpoint": "HitPeriscope6",
            "source": "Hit"
        },
        "hitperiscope7": {
            "hitpoint": "HitPeriscope7",
            "source": "Hit"
        },
        "hitperiscope8": {
            "hitpoint": "HitPeriscope8",
            "source": "Hit"
        },
        "hitperiscope9": {
            "hitpoint": "HitPeriscope9",
            "source": "Hit"
        },
        "hitperiscopecom1": {
            "hitpoint": "HitPeriscopeCom1",
            "source": "Hit"
        },
        "hitperiscopecom2": {
            "hitpoint": "HitPeriscopeCom2",
            "source": "Hit"
        },
        "hitperiscopegun1": {
            "hitpoint": "HitPeriscopeGun1",
            "source": "Hit"
        },
        "hitperiscopegun2": {
            "hitpoint": "HitPeriscopeGun2",
            "source": "Hit"
        },
        "hitperiscopegun3": {
            "hitpoint": "HitPeriscopeGun3",
            "source": "Hit"
        },
        "hitperiscopegun4": {
            "hitpoint": "HitPeriscopeGun4",
            "source": "Hit"
        },
        "maingun_fix": {
            "animperiod": 8.6,
            "initphase": 0,
            "source": "user"
        },
        "maljutka_hide": {
            "animperiod": 0.1,
            "initphase": 0,
            "source": "user"
        },
        "maljutka_hide_source": {
            "animperiod": 0.1,
            "displayname": "remove maljutka",
            "initphase": 0,
            "onphasechanged": "params['_v','_p'];if(_p isEqualTo 1)then{_v removeWeaponTurret ['rhs_weap_9k11',[0]];}else{ _v addWeaponTurret ['rhs_weap_9k11',[0]]};",
            "source": "user",
            "usesource": 1
        },
        "maljutka_reload": {
            "animperiod": 7.1,
            "initphase": 0,
            "source": "user"
        },
        "maljutka_reload_fins": {
            "animperiod": 1.25,
            "initphase": 0,
            "source": "user"
        },
        "maljutka_reload_hide": {
            "source": "ammo",
            "weapon": "rhs_weap_9k11"
        },
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "rhs_weap_2a42"
        },
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a42"
        },
        "muzzlemg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt"
        },
        "recoil_source_2a28": {
            "source": "reload",
            "weapon": "rhs_weap_2a28"
        },
        "recoil_source_2a42": {
            "source": "reload",
            "weapon": "rhs_weap_2a42"
        },
        "s_2p130_load": {
            "animperiod": 1.5,
            "initphase": 0,
            "source": "user"
        },
        "s_2p130_load_shell": {
            "animperiod": 0.75,
            "initphase": 0,
            "source": "door"
        },
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        "snorkel": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "wood_1_unhide": {
            "animperiod": 1e-06,
            "displayname": "hide wood log 1",
            "initphase": 0,
            "mass": 1,
            "source": "user"
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
    "armorstructural": 600,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "TankAttenuation",
    "attributes": {
        "crate_l1_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "hide l1 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_l1_unhide"
        },
        "crate_l2_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide l2 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_l2_unhide"
        },
        "crate_l3_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide l3 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_l3_unhide"
        },
        "crate_r1_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide r1 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_r1_unhide"
        },
        "crate_r2_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide r2 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_r2_unhide"
        },
        "crate_r3_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide r3 crate",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "crate_r3_unhide"
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
            "displayname": "Set left back symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBMPLeftBack,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalArmy",
            "tooltip": "Define symbol located on left back side of vehicle. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalarmy_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define left back symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalArmy_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
                    "defaultvalue": "1",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "defaultvalue": "0",
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
        "rhs_decalfront": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set front symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBMPFront,  _this getVariable ['rhs_decalFront_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalFront",
            "tooltip": "Define symbol located on front of vehicle hull. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalfront_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define front symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalFront_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
                    "defaultvalue": "1",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "defaultvalue": "0",
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
        "rhs_decalleftturret": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set left turret symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBMPLeftTurret,  _this getVariable ['rhs_decalLeftTurret_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalLeftTurret",
            "tooltip": "Define symbol located on left side of vehicle turret. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalleftturret_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define left turret symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalLeftTurret_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
                    "defaultvalue": "1",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "defaultvalue": "0",
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
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cBMP3NumberPlaces}else{[_this, [['Number', cBMP3NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of plate number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cBMP3NumberPlaces, _value]]] call rhs_fnc_decalsInit",
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
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBMPPlatoon,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoon",
            "tooltip": "Set platoon symbol located on right & rear of vehicles. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
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
                    "defaultvalue": "1",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "defaultvalue": "0",
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
        "rhs_decalrightturret": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set right turret symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBMPRightTurret,  _this getVariable ['rhs_decalRightTurret_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalRightTurret",
            "tooltip": "Define symbol located on right side of vehicle turret. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalrightturret_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define right turret symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalRightTurret_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
                    "defaultvalue": "1",
                    "name": "Army",
                    "value": "Army"
                },
                "honor": {
                    "defaultvalue": "0",
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
        "rhs_disablehabar": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Disable habar",
            "expression": "[_this,_value,'%s',_value] call rhs_fnc_setHabarEden",
            "property": "rhs_disableHabar"
        },
        "rhs_externalmount": {
            "control": "Checkbox",
            "defaultvalue": "0",
            "displayname": "Disable external mount",
            "expression": "[_this,_value] call rhs_fnc_lockTop",
            "property": "rhs_externalMount"
        },
        "rhs_snorkel": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Rise Snorkel",
            "expression": "_this animateSource ['Snorkel',_value,true]",
            "property": "rhs_snorkel"
        },
        "wood_1_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide wood log 1",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "wood_1_unhide"
        },
        "wood_2_unhide": {
            "control": "CheckboxNumber",
            "defaultvalue": "-1",
            "displayname": "Hide wood log 2",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "wood_2_unhide"
        }
    },
    "audible": 18,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "bounding": "usti hlavne",
    "brakedistance": 5,
    "brakeidlespeed": 0,
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
        "RHS_BMP_Cargo"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [
        "DoorL",
        "DoorR",
        "DoorL",
        "DoorR",
        "DoorL",
        "DoorR",
        "DoorL"
    ],
    "cargogetinaction": [
        "GetInAMV_cargo",
        "GetInAMV_cargo",
        "GetInAMV_cargo",
        "GetInAMV_cargo",
        "GetInAMV_cargo",
        "GetInAMV_cargo",
        "GetInMedium"
    ],
    "cargogetoutaction": [
        "GetOutLow",
        "GetOutLow",
        "GetOutLow",
        "GetOutLow",
        "GetOutLow",
        "GetOutLow",
        "GetOutMedium"
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
        5,
        2,
        6,
        3,
        7,
        4,
        8
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
        0.350877,
        0.350877,
        0,
        0.835088,
        0.350877,
        0.894737,
        0.666667,
        0.912281,
        0.666667,
        0.912281,
        0.666667,
        1,
        0.666667
    ],
    "changegeartype": "rpmratio",
    "clutchstrength": 20,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
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
        "amphibiousratios": [
            "R1",
            -14.5,
            "N",
            0,
            "D1",
            14.5
        ],
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -7.25,
            "N",
            0,
            "D1",
            5.25,
            "D2",
            2.842,
            "D3",
            1.912,
            "D4",
            1.28,
            "D5",
            0.858
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.3,
        "transmissionratios": [
            "High",
            12.6
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
    "crew": "rhs_vdv_crew",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 0,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_bmp/textures/BMP_1.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_1_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_1_des.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_2.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_2_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_2_des.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_3.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_3_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_3_des.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_4.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_4_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_4_des.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_5.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_5_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_5_des.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_6.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_6_dam.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_6_des.rvmat",
            "rhsafrf/addons/rhs_btr70/data/scope_glass.rvmat",
            "rhsafrf/addons/rhs_btr70/data/periscope_int_damage.rvmat",
            "rhsafrf/addons/rhs_btr70/data/periscope_int_damage.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "rhsafrf/addons/rhs_bmp/textures/BMP_6_des.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.02,
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
    "displayname": "BMP-1",
    "dlc": "RHS_AFRF",
    "driveoncomponent": [
        "Track_L",
        "Track_R",
        "Slide"
    ],
    "driveraction": "driver_apcwheeled2_out",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "hatchD",
    "driverforceoptics": 1,
    "driverinaction": "rhs_BMP2_Driver",
    "driverlefthandanimname": "",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsin": {
        "opticview": {
            "hitpoint": "HitPeriscope13",
            "initanglex": 7,
            "initangley": 0,
            "initfov": 0.7,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 0.7,
            "maxmovex": 0.075,
            "maxmovey": 0.075,
            "maxmovez": 0.1,
            "minanglex": -65,
            "minangley": -150,
            "minfov": 0.7,
            "minmovex": -0.075,
            "minmovey": -0.075,
            "minmovez": -0.075,
            "opticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tnpo170a",
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        }
    },
    "driveropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tnpo170a",
    "driverrighthandanimname": "",
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
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/rhs_bmp_base.paa",
    "editorsubcategory": "rhs_EdSubcat_ifv",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 0,
    "enablemanualfire": 0,
    "enableradio": 1,
    "enablewatch": 0,
    "engineeffectspeed": 5,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 8,
    "enginepower": 224,
    "engineshifty": -0.8,
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
            "fired": "_this call rhs_fnc_9m14_fired;",
            "getout": "_this call rhs_fnc_bmp_doors;_this call rhs_fnc_hatchAbandon",
            "init": "_this call rhs_fnc_bmp_init;",
            "reloaded": "_this call rhs_fnc_9m14_reload;"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectTankSide",
            "position": "vyfuk start"
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
        -8
    ],
    "faction": "rhs_faction_vdv",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "FDustEffects",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 29.5,
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
    "getinaction": "GetInMedium",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1,
        5,
        2,
        6,
        3,
        7,
        4,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18
    ],
    "getinradius": 3.5,
    "getoutaction": "GetOutMedium",
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
        "camo4",
        "camo5",
        "camo6",
        "n1",
        "n2",
        "n3",
        "i1",
        "i2",
        "i3",
        "i4",
        "i5"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_bmp/textures/bmp_1_co.paa",
        "rhsafrf/addons/rhs_bmp/textures/bmp_2_co.paa",
        "rhsafrf/addons/rhs_bmp/textures/bmp_3_co.paa",
        "rhsafrf/addons/rhs_bmp/textures/bmp_4_co.paa",
        "rhsafrf/addons/rhs_bmp/textures/bmp_5_co.paa",
        "rhsafrf/addons/rhs_bmp/textures/bmp_6_co.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa",
        "rhsafrf/addons/rhs_decals/Data/Labels/Misc/no_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hit_ammo": {
            "armor": -80,
            "armorcomponent": "Hit_Ammo",
            "explosionshielding": 0,
            "minimalhit": "- 0.4",
            "name": "Hit_Ammo",
            "passthrough": 0,
            "visual": "-"
        },
        "hitcomsight": {
            "armor": -40,
            "explosionshielding": 0.3,
            "material": -1,
            "minimalhit": -0.1,
            "name": "comSight",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "comSight"
        },
        "hitengine": {
            "armor": 0.45,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_engine_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "vyfuk start",
                    "simulation": "particles",
                    "type": "SmallFireFPlace"
                },
                "rhs_engine_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "vyfuk start",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_engine_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "vyfuk start",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_engine_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "vyfuk start",
                    "simulation": "particles",
                    "type": "RHS_FireSparks"
                }
            },
            "explosionshielding": 0.009,
            "material": -1,
            "minimalhit": 0.139,
            "name": "motor",
            "passthrough": 0,
            "radius": 0.17,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 1,
            "explosionshielding": 1,
            "material": -1,
            "name": "palivo",
            "passthrough": 1,
            "radius": 0.11,
            "visual": "-"
        },
        "hithull": {
            "armor": 0.4,
            "depends": "Hit_Ammo factor [0.5,1]",
            "explosionshielding": 0.15,
            "material": -1,
            "minimalhit": 0.54,
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
        "hitmainsight": {
            "armor": -40,
            "explosionshielding": 0.3,
            "material": -1,
            "minimalhit": -0.1,
            "name": "mainSight",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "mainSight"
        },
        "hitperiscope1": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope1",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope1"
        },
        "hitperiscope10": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope10",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope10"
        },
        "hitperiscope11": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope11",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope11"
        },
        "hitperiscope12": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope12",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope12"
        },
        "hitperiscope13": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope13",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope13"
        },
        "hitperiscope14": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope14",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope14"
        },
        "hitperiscope2": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope2",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope2"
        },
        "hitperiscope3": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope3",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope3"
        },
        "hitperiscope4": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope4",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope4"
        },
        "hitperiscope5": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope5",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope5"
        },
        "hitperiscope6": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope6",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope6"
        },
        "hitperiscope7": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope7",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope7"
        },
        "hitperiscope8": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope8",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope8"
        },
        "hitperiscope9": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope9",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope9"
        },
        "hitperiscopecom1": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeCom1",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeCom1"
        },
        "hitperiscopecom2": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeCom2",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeCom2"
        },
        "hitperiscopegun1": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeGun1",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeGun1"
        },
        "hitperiscopegun2": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeGun2",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeGun2"
        },
        "hitperiscopegun3": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeGun3",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeGun3"
        },
        "hitperiscopegun4": {
            "armor": -20,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscopeGun4",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscopeGun4"
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
    "icon": "A3/armor_f_beta/APC_Tracked_01/Data/UI/map_APC_Tracked_01_ca.paa",
    "idlerpm": 700,
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
    "latency": 1.3,
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
    "loddriverturnedout": 0,
    "magazines": [
        "rhs_mag_smokegen"
    ],
    "mapsize": 1.21,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.05,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 298.45,
    "maxspeed": 60,
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
    "memorypointsgetincargo": [
        "pos cargo L",
        "pos cargo R",
        "pos cargo L",
        "pos cargo R",
        "pos cargo L",
        "pos cargo R",
        "pos cargo L"
    ],
    "memorypointsgetincargodir": [
        "pos cargo L dir",
        "pos cargo R dir",
        "pos cargo L dir",
        "pos cargo R dir",
        "pos cargo L dir",
        "pos cargo R dir",
        "pos cargo L dir"
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
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
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
    "minomega": 75,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsafrf/addons/rhs_bmp/BMP1.p3d",
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
    "peaktorque": 981,
    "picture": "rhsafrf/addons/rhs_bmp/pictures/rhs_bmp1_pic_ca.paa",
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
    "redrpm": 2850,
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
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number', cBMP3NumberPlaces, 'Default']",
        "['Label', cBMPPlatoon, 'Platoon',11]",
        "['Label', cBMPLeftBack, 'Army', 2]"
    ],
    "rhs_fuelcapacity": 462,
    "rhs_habartype": 2,
    "rhs_randomizedhabar": [
        "crate_l1_unhide",
        "crate_l2_unhide",
        "crate_l3_unhide",
        "crate_r1_unhide",
        "crate_r2_unhide",
        "crate_r3_unhide",
        "wood_1_unhide",
        "wood_2_unhide"
    ],
    "rhs_toppositions": [
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18
    ],
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
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
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
        0.730957,
        1,
        200
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_int_stop",
        0.787946,
        1
    ],
    "soundengineonext": [
        "/rhsafrf/addons/rhs_bmp/sounds/utd20_start",
        2.73096,
        1,
        300
    ],
    "soundengineonint": [
        "/rhsafrf/addons/rhs_bmp/sounds/utd20_start",
        2.78795,
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
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(600/\t2850),(1000/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.2,
                1,
                800
            ],
            "volume": "engineOn*camPos*(((rpm/\t2850) factor[(705/\t2850),(850/\t2850)])\t*\t((rpm/\t2850) factor[(1100 /\t2850),(950/\t2850)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(950/\t2850),(1400/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.994328,
                1,
                800
            ],
            "volume": "engineOn*camPos*(((rpm/\t2850) factor[(900/\t2850),(1050/\t2850)])\t*\t((rpm/\t2850) factor[(1400/\t2850),(1200/\t2850)]))"
        },
        "engine1_ext_thrust_extra": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(650/\t2850),(750/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.99433,
                1,
                800
            ],
            "volume": "(thrust factor[0.1,0.4])*engineOn*camPos*(rpm factor [800,750])"
        },
        "engine1_ext_thrust_extra2": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(650/\t2850),(750/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_h",
                2.39433,
                1,
                800
            ],
            "volume": "(thrust factor[0.1,0.4])*engineOn*camPos*(rpm factor [800,750])"
        },
        "engine1_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(950/\t2850),(1400/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.598107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(900/\t2850),(1050/\t2850)])\t*\t((rpm/\t2850) factor[(1400/\t2850),(1200/\t2850)]))"
        },
        "engine1_int_thrust_extra": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(650/\t2850),(750/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.994328,
                1,
                800
            ],
            "volume": "(thrust factor[0.1,0.4])*engineOn*(1-camPos)*(rpm factor [800,750])"
        },
        "engine1_int_thrust_extra2": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(650/\t2850),(750/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_h",
                1.39433,
                1,
                800
            ],
            "volume": "(thrust factor[0.1,0.4])*engineOn*(1-camPos)*(rpm factor [800,750])"
        },
        "engine1_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(950/\t2850),(1400/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm2",
                1.55893,
                1,
                800
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(900/\t2850),(1050/\t2850)])\t*\t((rpm/\t2850) factor[(1400/\t2850),(1200/\t2850)]))"
        },
        "engine1_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(950/\t2850),(1400/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm2",
                0.746684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(900/\t2850),(1050/\t2850)])\t*\t((rpm/\t2850) factor[(1400/\t2850),(1200/\t2850)]))"
        },
        "engine2_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1200/\t2850),(1700/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.19125,
                1,
                850
            ],
            "volume": "engineOn*camPos*(((rpm/\t2850) factor[(1170/\t2850),(1380/\t2850)])\t*\t((rpm/\t2850) factor[(1700/\t2850),(1500/\t2850)]))"
        },
        "engine2_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1200/\t2850),(1700/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.646684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(1170/\t2850),(1380/\t2850)])\t*\t((rpm/\t2850) factor[(1700/\t2850),(1500/\t2850)]))"
        },
        "engine2_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1200/\t2850),(1700/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm4",
                1.71254,
                1,
                850
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1170/\t2850),(1380/\t2850)])\t*\t((rpm/\t2850) factor[(1700/\t2850),(1500/\t2850)]))"
        },
        "engine2_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1200/\t2850),(1700/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm4",
                0.746684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1170/\t2850),(1380/\t2850)])\t*\t((rpm/\t2850) factor[(1700/\t2850),(1500/\t2850)]))"
        },
        "engine3_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1500/\t2850),(2100/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.2,
                1,
                800
            ],
            "volume": "engineOn*camPos*(((rpm/\t2850) factor[(1500/\t2850),(1670/\t2850)])\t*\t((rpm/\t2850) factor[(2100/\t2850),(1800/\t2850)]))"
        },
        "engine3_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1500/\t2850),(2100/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.701187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(1500/\t2850),(1670/\t2850)])\t*\t((rpm/\t2850) factor[(2100/\t2850),(1800/\t2850)]))"
        },
        "engine3_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1500/\t2850),(2100/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm4",
                1.88489,
                1,
                950
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1500/\t2850),(1670/\t2850)])\t*\t((rpm/\t2850) factor[(2100/\t2850),(1800/\t2850)]))"
        },
        "engine3_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1500/\t2850),(2100/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm4",
                0.801187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1500/\t2850),(1670/\t2850)])\t*\t((rpm/\t2850) factor[(2100/\t2850),(1800/\t2850)]))"
        },
        "engine4_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1800/\t2850),(2300/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.42202,
                1,
                840
            ],
            "volume": "engineOn*camPos*(((rpm/\t2850) factor[(1780/\t2850),(2060/\t2850)])\t*\t((rpm/\t2850) factor[(2450/\t2850),(2200/\t2850)]))"
        },
        "engine4_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1800/\t2850),(2300/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.762341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(1780/\t2850),(2060/\t2850)])\t*\t((rpm/\t2850) factor[(2450/\t2850),(2200/\t2850)]))"
        },
        "engine4_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1800/\t2850),(2300/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm5",
                1.97828,
                1,
                1000
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1780/\t2850),(2060/\t2850)])\t*\t((rpm/\t2850) factor[(2450/\t2850),(2200/\t2850)]))"
        },
        "engine4_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(1800/\t2850),(2300/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm5",
                0.862341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(1780/\t2850),(2060/\t2850)])\t*\t((rpm/\t2850) factor[(2450/\t2850),(2200/\t2850)]))"
        },
        "engine5_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(2100/\t2850),(2640/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                1.61254,
                1,
                800
            ],
            "volume": "engineOn*camPos*((rpm/\t2850) factor[(2150/\t2850),(2500/\t2850)])"
        },
        "engine5_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(2100/\t2850),(2640/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.830957,
                1
            ],
            "volume": "engineOn*(1-camPos)*((rpm/\t2850) factor[(2150/\t2850),(2500/\t2850)])"
        },
        "engine5_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(2100/\t2850),(2640/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm5",
                3.19526,
                1,
                1050
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t2850) factor[(2150/\t2850),(2500/\t2850)])"
        },
        "engine5_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(2100/\t2850),(2640/\t2850)])*0.1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm5",
                1.1,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t2850) factor[(2150/\t2850),(2500/\t2850)])"
        },
        "engine_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(700/\t2850),(1100/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/UTD20_l",
                0.554813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(705/\t2850),(850/\t2850)])\t*\t((rpm/\t2850) factor[(1100 /\t2850),(950/\t2850)]))"
        },
        "enginethrust": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(700/\t2850),(1100/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm1",
                1.42202,
                1,
                800
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(705/\t2850),(850/\t2850)])\t*\t((rpm/\t2850) factor[(1100 /\t2850),(950/\t2850)]))"
        },
        "enginethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(700/\t2850),(1100/\t2850)])*0.2",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm1",
                0.698107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(705/\t2850),(850/\t2850)])\t*\t((rpm/\t2850) factor[(1100 /\t2850),(950/\t2850)]))"
        },
        "idle_ext": {
            "frequency": "0.95\t+\t((rpm/\t2850) factor[(400/\t2850),(900/\t2850)])*0.15",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/utd20_alap",
                8.91251,
                1,
                400
            ],
            "volume": "(thrust factor [0.1,0])*engineOn*camPos*(rpm interpolate [700,900,1,0])"
        },
        "idle_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(400/\t2850),(900/\t2850)])*0.15",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/utd20_in_alap",
                0.816228,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t2850) factor[(100/\t2850),(200/\t2850)])\t*\t((rpm/\t2850) factor[(900/\t2850),(700/\t2850)]))"
        },
        "idlethrust": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(400/\t2850),(900/\t2850)])*0.15",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/bmp_exhaust_ext_rpm1",
                1.59125,
                1,
                800
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(100/\t2850),(200/\t2850)])\t*\t((rpm/\t2850) factor[(900/\t2850),(700/\t2850)]))"
        },
        "idlethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t2850) factor[(400/\t2850),(900/\t2850)])*0.15",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/utd20_in_alap",
                0.654813,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t2850) factor[(100/\t2850),(200/\t2850)])\t*\t((rpm/\t2850) factor[(900/\t2850),(700/\t2850)]))"
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
                0.198107,
                1,
                140
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouth1": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.146684,
                1,
                160
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouth2": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_3.ogg",
                0.101187,
                1,
                180
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouth3": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_4.ogg",
                0.162341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouth4": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_5.ogg",
                0.262341,
                1,
                220
            ],
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        },
        "threadsouts0": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.116228,
                1,
                120
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouts1": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_2.ogg",
                0.154813,
                1,
                140
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouts2": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_3.ogg",
                0.198107,
                1,
                160
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouts3": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_4.ogg",
                0.146684,
                1,
                180
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouts4": {
            "frequency": "1",
            "sound": [
                "/rhsafrf/addons/rhs_bmp/sounds/lanc_5.ogg",
                0.201187,
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
    "switchtime": 0,
    "tankturnforce": 450000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.92,
    "tbody": 250,
    "textplural": "BMPs",
    "textsingular": "BMP",
    "texturelist": [],
    "texturesources": {
        "cdf": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [],
            "textures": [
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_1_cdf_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_2_cdf_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_3_cdf_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_4_cdf_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_5_cdf_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/bmp_6_cdf_co.paa"
            ]
        },
        "chedaki": {
            "author": "Red Hammer Studios",
            "displayname": "Chedaki",
            "factions": [
                "rhs_faction_insurgents"
            ],
            "textures": [
                "rhsafrf/addons/rhs_bmp/textures/bmp_1_chdkz_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_2_chdkz_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_3_chdkz_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_4_chdkz_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_5_chdkz_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_6_chdkz_co.paa"
            ]
        },
        "rhs_sand": {
            "author": "beaar",
            "displayname": "Sand",
            "factions": [],
            "textures": [
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_1_desert_co.paa",
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_2_desert_co.paa",
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_3_desert_co.paa",
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_4_desert_co.paa",
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_5_desert_co.paa",
                "rhsafrf/addons/rhs_bmp_camo/data/bmp_6_desert_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [
                "rhs_faction_vmf",
                "rhs_faction_vdv",
                "rhs_faction_vdv",
                "rhs_faction_vv",
                "rhs_faction_tv"
            ],
            "textures": [
                "rhsafrf/addons/rhs_bmp/textures/bmp_1_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_2_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_3_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_4_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_5_co.paa",
                "rhsafrf/addons/rhs_bmp/textures/bmp_6_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "tf_range_api": 17000,
    "threat": [
        0.7,
        1,
        0.3
    ],
    "thrustdelay": 0.3,
    "torquecurve": [
        [
            0.0350877,
            0
        ],
        [
            0.315789,
            0.953109
        ],
        [
            0.526316,
            1
        ],
        [
            0.561404,
            1
        ],
        [
            0.631579,
            0.953109
        ],
        [
            0.77193,
            0.897044
        ],
        [
            0.912281,
            0.826707
        ],
        [
            1.08807,
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
            "count": 10,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 1,
            "name": "Medikit"
        },
        "_xx_toolkit": {
            "count": 1,
            "name": "Toolkit"
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
    "transportsoldier": 8,
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
        "cargoturret_01": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_inside_1",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Rear)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 61,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo8",
            "memorypointsgetingunnerdir": "cargo8_dir",
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
            "minelev": -35,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -65,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 14,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_02": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_flatground_2",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Middle)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 61,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo9",
            "memorypointsgetingunnerdir": "cargo9_dir",
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
            "minelev": -35,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -65,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 9,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_03": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_flatground_3",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Rear)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 61,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo10",
            "memorypointsgetingunnerdir": "cargo10_dir",
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
            "minelev": -35,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -65,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 10,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_04": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_flatground_4",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Middle)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 61,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo11",
            "memorypointsgetingunnerdir": "cargo11_dir",
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
            "minelev": -35,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -65,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 11,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_05": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_boat_3",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Center)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 81,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo12",
            "memorypointsgetingunnerdir": "cargo12_dir",
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
            "minelev": -15,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -25,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 12,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_06": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 1,
            "enabledbyanimationsource": "cargoHandler1",
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
            "gunneraction": "rhs_bmp_cargostatic_01",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Rear)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 0.001,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 0.001,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo13",
            "memorypointsgetingunnerdir": "cargo13_dir",
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
            "minelev": 0,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 0,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 13,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_07": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 1,
            "enabledbyanimationsource": "cargoHandler1",
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
            "gunneraction": "rhs_bmp_cargostatic_04",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Front)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 0.001,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 0.001,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo14",
            "memorypointsgetingunnerdir": "cargo14_dir",
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
            "minelev": 0,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 0,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 18,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_08": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 1,
            "enabledbyanimationsource": "cargoHandler1",
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
            "gunneraction": "rhs_bmp_cargostatic_02",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Front)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 0.001,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 0.001,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo15",
            "memorypointsgetingunnerdir": "cargo15_dir",
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
            "minelev": 0,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 0,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 15,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_09": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
            "disablesoundattenuation": 1,
            "dontcreateai": 1,
            "ejectdeadgunner": 1,
            "enabledbyanimationsource": "cargoHandler1",
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
            "gunneraction": "rhs_bmp_cargostatic_03",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Front)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 0.001,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 0.001,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo16",
            "memorypointsgetingunnerdir": "cargo16_dir",
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
            "minelev": 0,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 0,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 16,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "cargoturret_10": {
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
            "canhidegunner": 0,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -2,
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
            "gunneraction": "passenger_flatground_4",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Front Center)",
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 45,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 61,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "cargo17",
            "memorypointsgetingunnerdir": "cargo17_dir",
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
            "minelev": -35,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -65,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 17,
            "proxytype": "CPCargo",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.2,
                        "hardlimitstart": 0.7,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 60,
                    "intensity": 4,
                    "outerangle": 145,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1,
                        "hardlimitstart": 0.5,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 60,
                    "intensity": 5,
                    "outerangle": 145,
                    "position": "cargo_light_1",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_2": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        40,
                        350,
                        960
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 60,
                    "intensity": 9,
                    "outerangle": 145,
                    "position": "cargo_light_2",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "weapons": [
                "rhs_weap_DummyLauncher"
            ]
        },
        "com_bmp1": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "obsturret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "obsGun",
            "animationsourcehatch": "HatchCommander",
            "armorlights": 0.4,
            "body": "RHS_BMP1_com_coppula_BMP1",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 0,
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
            "gun": "RHS_BMP1_OU3_BMP1",
            "gunbeg": "Mgun_end",
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
            "gunend": "Mgun_start",
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
            "gunneraction": "RHS_VehicleTurnout_BMP1_1",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchC",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerinaction": "rhs_bmp1_commanderIn",
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
            "hascommander": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
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
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 12,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 135,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "commanderview",
            "memorypointgunneroutoptics": "commander_out_view",
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
            "minturn": -135,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "night": {
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
                    "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "hitpoint": "HitComSight",
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
                "wide": {
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
                    "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "hitpoint": "HitComSight",
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
                    "speedzoommaxspeed": 10000000000.0
                }
            },
            "outgunnermayfire": 0,
            "personturretaction": "RHS_VehicleTurnout_BMP1_1",
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
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
            "soundservo": [],
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
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "MainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "MainGun",
            "animationsourcehatch": "HatchGunner",
            "armorlights": 0.1,
            "body": "RHS_BMP1_MainTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 0,
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
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "RHS_BMP1_MainGun",
            "gunbeg": "Gun_start",
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
            "gunend": "Gun_end",
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
            "gunneraction": "RHS_passenger_inside_6",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchG",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "rhs_bmp1_gunnerIn",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [
                "OpticsCHAbera1",
                "OpticsBlur2"
            ],
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
                    "armor": 0.6,
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.13,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.15,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": 0.5,
                    "explosionshielding": 0.001,
                    "material": -1,
                    "minimalhit": 0.14,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.15,
                    "visual": "MainTurret"
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
            "lockwhendriverout": 1,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_pg15v_20",
                "rhs_mag_og15v_20",
                "rhs_mag_9m14m",
                "rhs_mag_9m14m",
                "rhs_mag_9m14m",
                "rhs_mag_9m14m",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250",
                "rhs_mag_762x54mm_250"
            ],
            "maxcamelev": 90,
            "maxelev": 35,
            "maxhorizontalrotspeed": 0.54,
            "maxoutelev": 45,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 0.24,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "gunnerview",
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
            "minelev": -24,
            "minoutelev": -45,
            "minoutturn": -60,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "nightvision": 1,
            "opticsin": {
                "periscope": {
                    "campos": "view_periscope",
                    "distancezoommax": 2000,
                    "distancezoommin": 200,
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tvn5.p3d",
                    "hitpoint": "HitPeriscopeGun3",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.47,
                    "maxanglex": 110,
                    "maxangley": 110,
                    "maxfov": 0.47,
                    "minanglex": -110,
                    "minangley": -110,
                    "minfov": 0.47,
                    "opticsdisplayname": "PERISCOPE",
                    "opticszoommax": 0.14,
                    "opticszoommin": 0.14,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "pn22m1": {
                    "campos": "gunnerview",
                    "distancezoommax": 2000,
                    "distancezoommin": 200,
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1pn22m2",
                    "hitpoint": "HitMainSight",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.14,
                    "maxanglex": 110,
                    "maxangley": 110,
                    "maxfov": 0.14,
                    "minanglex": -110,
                    "minangley": -110,
                    "minfov": 0.14,
                    "opticsdisplayname": "DAY",
                    "opticszoommax": 0.14,
                    "opticszoommin": 0.14,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "pn22m1n": {
                    "campos": "gunnerview",
                    "distancezoommax": 2000,
                    "distancezoommin": 200,
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_1pn22m1n",
                    "hitpoint": "HitMainSight",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.14,
                    "maxanglex": 110,
                    "maxangley": 110,
                    "maxfov": 0.14,
                    "minanglex": -110,
                    "minangley": -110,
                    "minfov": 0.14,
                    "opticsdisplayname": "NIGHT",
                    "opticszoommax": 0.14,
                    "opticszoommin": 0.14,
                    "visionmode": [
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 0,
            "personturretaction": "RHS_passenger_inside_6",
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
                "/rhsafrf/addons/rhs_bmp/sounds/turret1.wss",
                4,
                1,
                10
            ],
            "stabilizedinaxes": 0,
            "startengine": 0,
            "turnin": {
                "limitsarraybottom": [
                    [
                        -4,
                        -180
                    ],
                    [
                        -4,
                        17
                    ],
                    [
                        10.3683,
                        18
                    ],
                    [
                        10.7173,
                        36
                    ],
                    [
                        -4,
                        37
                    ],
                    [
                        -4,
                        180
                    ]
                ],
                "limitsarraytop": [
                    [
                        15,
                        -180
                    ],
                    [
                        15,
                        180
                    ]
                ]
            },
            "turnout": {
                "limitsarraybottom": [
                    [
                        -24,
                        -170
                    ],
                    [
                        -24,
                        170
                    ]
                ],
                "limitsarraytop": [
                    [
                        45,
                        -170
                    ],
                    [
                        45,
                        170
                    ]
                ]
            },
            "turretcansee": 0,
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscWeapon1PN22M_FCS",
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
                "rhs_weap_2a28",
                "rhs_weap_pkt",
                "rhs_weap_9k11"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoEastTank",
    "unitinfotypelite": 0,
    "unloadincombat": 1,
    "useprecisegetinaction": 0,
    "useractions": {
        "snorkel_1": {
            "condition": "((this animationSourcePhase 'Snorkel' == 0) && (player == driver this))",
            "displayname": "Raise Snorkel",
            "onlyforplayer": 0,
            "position": "MainTurret",
            "radius": 3.5,
            "showwindow": 0,
            "statement": "this animateSource ['snorkel',1]"
        },
        "snorkel_2": {
            "condition": "((this animationSourcePhase 'Snorkel' == 1) && (player == driver this))",
            "displayname": "Lower Snorkel",
            "onlyforplayer": 0,
            "position": "MainTurret",
            "radius": 3.5,
            "showwindow": 0,
            "statement": "this animateSource ['snorkel',0]"
        },
        "togglelight": {
            "condition": "player in this;",
            "displayname": "Toggle interior light",
            "onlyforplayer": 1,
            "position": "MainTurret",
            "radius": 15,
            "showwindow": 0,
            "statement": "[this,'cabinlights_hide',[2]] call rhs_fnc_toggleIntLight"
        }
    },
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
        "initanglex": 7,
        "initangley": 0,
        "initfov": 0.75,
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
    "waterangulardampingcoef": 3.2,
    "waterdamageengine": 0.9,
    "watereffectspeed": 5,
    "waterfasteffectspeed": 28,
    "waterleakiness": 250,
    "waterlineardampingcoefx": 2,
    "waterlineardampingcoefy": 2,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.015,
    "weapons": [
        "rhs_weap_smokegen"
    ],
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
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l2": {
            "bonename": "wheel_podkoloL1",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l3": {
            "bonename": "wheel_podkolol2",
            "boundary": "wheel_1_3_bound",
            "center": "wheel_1_3_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l4": {
            "bonename": "wheel_podkolol3",
            "boundary": "wheel_1_4_bound",
            "center": "wheel_1_4_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l5": {
            "bonename": "wheel_podkolol4",
            "boundary": "wheel_1_5_bound",
            "center": "wheel_1_5_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l6": {
            "bonename": "wheel_podkolol5",
            "boundary": "wheel_1_6_bound",
            "center": "wheel_1_6_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l7": {
            "bonename": "wheel_podkolol6",
            "boundary": "wheel_1_7_bound",
            "center": "wheel_1_7_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "l9": {
            "bonename": "wheel_podkolol9",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r1": {
            "bonename": "",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r2": {
            "bonename": "wheel_podkolop1",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r3": {
            "bonename": "wheel_podkolop2",
            "boundary": "wheel_2_3_bound",
            "center": "wheel_2_3_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r4": {
            "bonename": "wheel_podkolop3",
            "boundary": "wheel_2_4_bound",
            "center": "wheel_2_4_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r5": {
            "bonename": "wheel_podkolop4",
            "boundary": "wheel_2_5_bound",
            "center": "wheel_2_5_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r6": {
            "bonename": "wheel_podkolop5",
            "boundary": "wheel_2_6_bound",
            "center": "wheel_2_6_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r7": {
            "bonename": "wheel_podkolop6",
            "boundary": "wheel_2_7_bound",
            "center": "wheel_2_7_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
        },
        "r9": {
            "bonename": "wheel_podkolop9",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 344,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 344,
            "frictionvsslipgraph": [
                [
                    0,
                    0.8
                ],
                [
                    0.38,
                    1
                ],
                [
                    0.7,
                    0.65
                ]
            ],
            "latstiffx": 2,
            "latstiffy": 30,
            "longitudinalstiffnessperunitgravity": 32000,
            "mass": 120,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 7.5615,
            "side": "right",
            "springdamperrate": 7000,
            "springstrength": 127500,
            "sprungmass": 1208.33,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.288
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