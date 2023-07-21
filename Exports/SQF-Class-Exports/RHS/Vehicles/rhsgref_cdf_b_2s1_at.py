d = {
    "_generalmacro": "Tank_F",
    "accelaidforcecoef": 4,
    "accelaidforcespd": 2.23,
    "accelaidforceyoffset": -3.6,
    "access": 0,
    "accuracy": 0.3,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 100,
    "aggregatereflectors": [
        [
            "Left"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alphatracks": 0.7,
    "alwaystarget": 0,
    "animated": 1,
    "animationlist": [
        "hide_shields_hull",
        0.5,
        "hide_backframe",
        0.4,
        "hide_shields_turret",
        0.2
    ],
    "animationsources": {
        "hatchc": {
            "animperiod": 0.8,
            "source": "door"
        },
        "hatchd": {
            "animperiod": 0.8,
            "source": "door"
        },
        "hide_backframe": {
            "animperiod": 1e-06,
            "displayname": "Hide Watershield Frame",
            "forceanimate": [
                "hide_shields_turret",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "hide_shields_hull": {
            "animperiod": 1e-06,
            "displayname": "Hide Hull Watershields",
            "forceanimate": [
                "hide_shields_turret",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 1,
            "mass": 1,
            "source": "user"
        },
        "hide_shields_turret": {
            "animperiod": 1e-06,
            "displayname": "Hide Turret Watershields",
            "forceanimate": [
                "hide_shields_hull",
                1
            ],
            "forceanimatephase": 0,
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "light_cateyes": {
            "animperiod": 1e-05,
            "initphase": 1,
            "source": "user"
        },
        "muzzle_hide_arty": {
            "source": "reload",
            "weapon": "rhs_weap_2a31_at"
        },
        "reload_magazine_source": {
            "source": "reloadMagazine",
            "weapon": "rhs_weap_2a31_at"
        },
        "reload_source": {
            "source": "reload",
            "weapon": "rhs_weap_2a31_at"
        },
        "turrethide": {
            "animperiod": 1e-10,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 300,
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
    "armorlights": 0.4,
    "armorstructural": 6,
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
        "rhs_ammoslot_1": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Ammo slot #1 count",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "property": "rhs_ammoslot_1",
            "tooltip": "Define number of rounds stored inside of type #1. Max 40. Leave -1 for default loadout",
            "typename": "NUMBER",
            "validate": "NUMBER"
        },
        "rhs_ammoslot_1_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Ammo slot #1 type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_ammoslot_1_type",
            "tooltip": "Define type of shell for #1 slot [HE rounds]",
            "typename": "STRING",
            "values": {
                "rhs_mag_3of56": {
                    "defaultvalue": "rhs_mag_3of56",
                    "name": "3OF56 HE",
                    "value": "rhs_mag_3of56"
                },
                "rhs_mag_of462": {
                    "defaultvalue": "rhs_mag_of462",
                    "name": "53-OF-462 HE",
                    "value": "rhs_mag_of462"
                }
            }
        },
        "rhs_ammoslot_2": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Ammo slot #2 count",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "property": "rhs_ammoslot_2",
            "tooltip": "Define number of rounds stored inside of type #2. Max 40. Leave -1 for default loadout",
            "typename": "NUMBER",
            "validate": "NUMBER"
        },
        "rhs_ammoslot_2_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Ammo slot #2 type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_ammoslot_2_type",
            "tooltip": "Define type of shell for #2 slot [Smoke rounds]",
            "typename": "STRING",
            "values": {
                "rhs_mag_d462": {
                    "defaultvalue": "rhs_mag_d462",
                    "name": "53-D-462 Smoke",
                    "value": "rhs_mag_d462"
                }
            }
        },
        "rhs_ammoslot_3": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Ammo slot #3 count",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "property": "rhs_ammoslot_3",
            "tooltip": "Define number of rounds stored inside of type #3. Max 40. Leave -1 for default loadout",
            "typename": "NUMBER",
            "validate": "NUMBER"
        },
        "rhs_ammoslot_3_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Ammo slot #3 type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_ammoslot_3_type",
            "tooltip": "Define type of shell for #3 slot [Illumination rounds]",
            "typename": "STRING",
            "values": {
                "rhs_mag_s463": {
                    "defaultvalue": "rhs_mag_s463",
                    "name": "53-S-463 Flare",
                    "value": "rhs_mag_s463"
                }
            }
        },
        "rhs_ammoslot_4": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Ammo slot #4 count",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "property": "rhs_ammoslot_4",
            "tooltip": "Define number of rounds stored inside of type #4. Max 40. Leave -1 for default loadout",
            "typename": "NUMBER",
            "validate": "NUMBER"
        },
        "rhs_ammoslot_4_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Ammo slot #4 type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_ammoslot_4_type",
            "tooltip": "Define type of shell for #4 slot [HEAT rounds]",
            "typename": "STRING",
            "values": {
                "rhs_mag_bk13": {
                    "defaultvalue": "rhs_mag_bk13",
                    "name": "3BK13 HEAT",
                    "value": "rhs_mag_bk13"
                },
                "rhs_mag_bk6m": {
                    "defaultvalue": "rhs_mag_bk6m",
                    "name": "3BK6M HEAT",
                    "value": "rhs_mag_bk6m"
                }
            }
        },
        "rhs_decalnumber": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set side hull number (3 digits)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1NumberPlaces}else{[_this, [['Number', cRHS2S1NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber2": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set back small number (3 digits)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1BackSmallNumberPlaces}else{[_this, [['Number', cRHS2S1BackSmallNumberPlaces, _this getVariable ['rhs_decalNumber_type2','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber2",
            "tooltip": "Set back small number. 3 numbers are required. Hides on 0",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber3": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set back large number (3 digits)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1BackLargeNumberPlaces}else{[_this, [['Number', cRHS2S1BackLargeNumberPlaces, _this getVariable ['rhs_decalNumber_type3','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber3",
            "tooltip": "Set back large number. 3 numbers are required. Hides on 0",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber4": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set back turret number (3 digits)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1BackTurretNumberPlaces}else{[_this, [['Number', cRHS2S1BackTurretNumberPlaces, _this getVariable ['rhs_decalNumber_type4','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber4",
            "tooltip": "Set back turret number. 3 numbers are required. Hides on 0",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber5": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set front turret number (3 digits)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1FrontTurretNumberPlaces}else{[_this, [['Number', cRHS2S1FrontTurretNumberPlaces, _this getVariable ['rhs_decalNumber_type5','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber5",
            "tooltip": "Set front turret number. 3 numbers are required. Hides on 0",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber6": {
            "collapsed": 1,
            "control": "Edit",
            "defaultvalue": "0",
            "displayname": "Set front turret number (5 digits, Serbian)",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHS2S1SerbianNumberPlaces}else{[_this, [['Number', cRHS2S1SerbianNumberPlaces, _this getVariable ['rhs_decalNumber_type6','CDF'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber6",
            "tooltip": "Set front turret number. 5 numbers are required. Hides on 0",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of side hull number (3 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalnumber_type2": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of back small numbers (3 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackSmallNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type2",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalnumber_type3": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of back large numbers (3 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackLargeNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type3",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalnumber_type4": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of back turret number (3 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackTurretNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type4",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalnumber_type5": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of front turret number (3 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1FrontTurretNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type5",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalnumber_type6": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of front turret number (5 digits)",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1SerbianNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type6",
            "tooltip": "Define kind of font that will be drawn on vehicle. 5 digits",
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
                },
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decalplatoonback": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set platoon symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1BackSymbol],  _this getVariable ['rhs_decalPlatoonBack_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoon",
            "tooltip": "Set platoon symbol located on the back of the vehicle. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonback_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define back door platoon symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonBack_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonhullleft": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set hull left symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1HullLeftSymbol],  _this getVariable ['rhs_decalPlatoonHullLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonHullLeft",
            "tooltip": "Define symbol located on left side of vehicle hull. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonhullleft_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define hull left symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonHullLeft_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonhullright": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set hull right symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1HullRightSymbol],  _this getVariable ['rhs_decalPlatoonHullRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonHullRight",
            "tooltip": "Define symbol located on right side of vehicle hull. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonhullright_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define hull right symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonHullRight_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonturretbackleft": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set back turret left symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretBackLeftSymbol],  _this getVariable ['rhs_decalPlatoonTurretBackLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonTurretBackLeft",
            "tooltip": "Define symbol located on left back side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonturretbackleft_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define back turret left symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonTurretBackLeft_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonturretbackright": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set back turret right symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretBackRightSymbol],  _this getVariable ['rhs_decalPlatoonTurretBackRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonTurretBackRight",
            "tooltip": "Define symbol located on right back side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonturretbackright_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define back turret right symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonTurretBackRight_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonturretfrontleft": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set front turret left symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretFrontLeftSymbol],  _this getVariable ['rhs_decalPlatoonTurretFrontLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonTurretFrontLeft",
            "tooltip": "Define symbol located on left front side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonturretfrontleft_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define front turret left symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonTurretFrontLeft_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
        "rhs_decalplatoonturretfrontright": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set front turret right symbol",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretFrontRightSymbol],  _this getVariable ['rhs_decalPlatoonTurretFrontRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalPlatoonTurretFrontRight",
            "tooltip": "Define symbol located on right front side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "validate": "none"
        },
        "rhs_decalplatoonturretfrontright_type": {
            "control": "Combo",
            "defaultvalue": "0",
            "displayname": "Define front turret right symbol type",
            "expression": "_this setVariable ['%s', _value];",
            "property": "rhs_decalPlatoonTurretFrontRight_type",
            "tooltip": "Decal type",
            "typename": "STRING",
            "values": {
                "army": {
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
                    "defaultvalue": "1",
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
    "cargoaction": [],
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
        0.5,
        0.5,
        0,
        0.9,
        0.5,
        0.9,
        0.7,
        0.9,
        0.7,
        0.95,
        0.75,
        0.95,
        0.75,
        1,
        0.8
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
            -40,
            "N",
            0,
            "D1",
            40
        ],
        "drivestring": "D",
        "gearboxmode": "auto",
        "gearboxratios": [
            "R1",
            -2.235,
            "N",
            0,
            "D1",
            2.6,
            "D2",
            1.5,
            "D3",
            1.125,
            "D4",
            0.85,
            "D5",
            0.64,
            "D6",
            0.5
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1,
        "transmissionratios": [
            "High",
            12
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
    "crew": "rhsgref_cdf_b_reg_crew",
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 0,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_hull.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_hull_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_hull_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_turret.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_turret_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_turret_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_hull.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_hull_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_hull_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_turret.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_turret_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_turret_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret_des.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_dam.rvmat",
            "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_des.rvmat",
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
    "displayname": "2S1 (Direct Fire)",
    "dlc": "RHS_GREF",
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
    "driverinaction": "rhs_2s1_driver",
    "driverlefthandanimname": "",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [
        "OpticsCHAbera1"
    ],
    "driveropticsin": {
        "opticview": {
            "hitpoint": "Hit_Optic_Driver",
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
    "driveroutopticseffect": [],
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
    "editorpreview": "rhsgref/addons/rhsgref_editorPreviews/data/rhsgref_cdf_2s1.paa",
    "editorsubcategory": "rhs_EdSubcat_artillery",
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
    "engineeffectspeed": 5,
    "engineer": 0,
    "enginelosses": 25,
    "enginemoi": 10,
    "enginepower": 220,
    "engineshifty": 0.7,
    "enginestartspeed": 5,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {
        "bis_randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;}"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_eventhandlers": {
            "engine": "[_this # 0,_this # 1,2] call rhs_fnc_engineStartupDelay",
            "fired": "_this call RHS_fnc_2s1_ejection;",
            "init": "_this call rhs_fnc_2s1_init",
            "killed": "[_this # 0,'rhs_Wreck_2s1_turret_F',50] call rhs_fnc_turretBlow",
            "postinit": "_this call rhs_fnc_reapplyTextures"
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
    "explosionshielding": 10,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2,
        -15
    ],
    "faction": "rhsgref_faction_cdf_ground_b",
    "features": "",
    "featuretype": 0,
    "firedusteffect": "FDustEffects",
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 30,
    "fuelcapacity": 25,
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
        "camo_sprocket",
        "camo_idler",
        "camo_wheel1",
        "camo_wheel2",
        "camo_wheel3",
        "camo_wheel4",
        "camo_wheel5",
        "camo_wheel6",
        "camo_wheel7",
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8",
        "n9",
        "n10",
        "n11",
        "n12",
        "n13",
        "n14",
        "n15",
        "n16",
        "n17",
        "n18",
        "n19",
        "n20",
        "i1",
        "i2",
        "i3",
        "i4",
        "i5",
        "i6",
        "i7"
    ],
    "hiddenselectionsmaterials": [
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat"
    ],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
        "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 1,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hit_optic_driver": {
            "armor": -40,
            "armorcomponent": "Hit_Optic_Driver",
            "explosionshielding": 0,
            "name": "Hit_Optic_Driver",
            "passthrough": 0,
            "visual": "-"
        },
        "hit_optic_op5_37": {
            "armor": -40,
            "armorcomponent": "Hit_Optic_OP5_37",
            "explosionshielding": 0,
            "name": "Hit_Optic_OP5_37",
            "passthrough": 0,
            "visual": "-"
        },
        "hit_optic_periscope": {
            "armor": -40,
            "armorcomponent": "Hit_Optic_Periscope",
            "explosionshielding": 0,
            "name": "Hit_Optic_Periscope",
            "passthrough": 0,
            "visual": "-"
        },
        "hit_optic_pg2": {
            "armor": -40,
            "armorcomponent": "Hit_Optic_PG2",
            "explosionshielding": 0,
            "name": "Hit_Optic_PG2",
            "passthrough": 0,
            "visual": "-"
        },
        "hit_optic_tkn3": {
            "armor": -40,
            "armorcomponent": "Hit_Optic_TKN3",
            "explosionshielding": 0,
            "name": "Hit_Optic_TKN3",
            "passthrough": 0,
            "visual": "-"
        },
        "hitengine": {
            "armor": -150,
            "armorcomponent": "Hit_Engine",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                "rhs_engine_fire": {
                    "enabled": "engineDamage",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallFireFPlace"
                },
                "rhs_engine_smoke": {
                    "enabled": "engineDamage",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_engine_smoke_small1": {
                    "enabled": "engineDamage",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_smoke_small2": {
                    "enabled": "engineDamage",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke3",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_engine_sounds": {
                    "enabled": "engineDamage",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke1",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_engine_sparks": {
                    "enabled": "engineDamage",
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
            "minimalhit": 0.14,
            "name": "motor",
            "passthrough": 0,
            "radius": 0.18,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 999,
            "armorcomponent": "Hit_FuelTank_1",
            "depends": "HitFuelTank_1*0.3+HitFuelTank_2*0.3+HitFuelTank_3*0.2+HitFuelTank_4*0.2",
            "explosionshielding": 0,
            "minimalhit": 1,
            "name": "Hit_FuelTank_1",
            "passthrough": 0,
            "radius": 0.01,
            "visual": "-"
        },
        "hitfueltank_1": {
            "armor": -80,
            "armorcomponent": "Hit_FuelTank_1",
            "explosionshielding": 0,
            "material": -1,
            "minimalhit": 0.3,
            "name": "Hit_FuelTank_1",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hitfueltank_2": {
            "armor": -80,
            "armorcomponent": "Hit_FuelTank_2",
            "explosionshielding": 0,
            "material": -1,
            "minimalhit": 0.3,
            "name": "Hit_FuelTank_2",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hitfueltank_3": {
            "armor": -80,
            "armorcomponent": "Hit_FuelTank_3",
            "explosionshielding": 0,
            "material": -1,
            "minimalhit": 0.3,
            "name": "Hit_FuelTank_3",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hitfueltank_4": {
            "armor": -80,
            "armorcomponent": "Hit_FuelTank_4",
            "explosionshielding": 0,
            "material": -1,
            "minimalhit": 0.3,
            "name": "Hit_FuelTank_4",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "-"
        },
        "hithull": {
            "armor": -100,
            "armorcomponent": "Hit_Ammo",
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.04,
            "name": "telo",
            "passthrough": 0,
            "radius": 0.1,
            "visual": "zbytek"
        },
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "Hit_TrackL",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_L"
        },
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "explosionshielding": 0.5,
            "material": -1,
            "minimalhit": -0.25,
            "name": "Hit_TrackR",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "pas_P"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsafrf/addons/rhs_2s3/ico/ico_2s3_ca.paa",
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
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "magazines": [],
    "mapsize": 1.21,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0.05,
    "maxgforce": 2,
    "maximumload": 3000,
    "maxomega": 209.44,
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
    "minomega": 72,
    "mintotaldamagethreshold": 0.5,
    "model": "rhsafrf/addons/rhs_2s1/rhs_2s1",
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
    "peaktorque": 1079,
    "picture": "rhsafrf/addons/rhs_2s1/ico/rhs_2s1_pic_ca.paa",
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
    "redrpm": 2000,
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
        "['Number',[cRHS2S1NumberPlaces, cRHS2S1BackLargeNumberPlaces],'CDF']"
    ],
    "rhs_fuelcapacity": 1885,
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
    "rudderforcecoef": 4.5,
    "scope": 2,
    "scopecurator": 2,
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
    "side": 1,
    "simulation": "tankX",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.5,
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
        "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_start",
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
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm1",
                0.794328,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t5200) factor[(705/\t5200),(850/\t5200)])\t*\t((rpm/\t5200) factor[(1100 /\t5200),(950/\t5200)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t((rpm/\t5200) factor[(950/\t5200),(1400/\t5200)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm2",
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
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm3",
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
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm4",
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
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm5",
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
                "A3/Sounds_F/vehicles/armor/MBT_03/MBT_engine_ext_rpm6",
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
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_01",
                0.398107,
                1,
                140
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouth1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_02",
                0.446684,
                1,
                160
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouth2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_03",
                0.501187,
                1,
                180
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouth3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_04",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouth4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_hard_05",
                0.562341,
                1,
                220
            ],
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/\t60) factor[(((-49) max 49)/\t60),(((-53) max 53)/\t60)])"
        },
        "threadsouts0": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_01",
                0.316228,
                1,
                120
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-0) max 0)/\t60),(((-5) max 5)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-15) max 15)/\t60),(((-10) max 10)/\t60)]))"
        },
        "threadsouts1": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_02",
                0.354813,
                1,
                140
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-10) max 10)/\t60),(((-15) max 15)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-30) max 30)/\t60),(((-25) max 25)/\t60)]))"
        },
        "threadsouts2": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_03",
                0.398107,
                1,
                160
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-25) max 25)/\t60),(((-30) max 30)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-45) max 45)/\t60),(((-40) max 40)/\t60)]))"
        },
        "threadsouts3": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_04",
                0.446684,
                1,
                180
            ],
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/\t60) factor[(((-40) max 40)/\t60),(((-45) max 45)/\t60)])\t*\t((((-speed*3.6) max speed*3.6)/\t60) factor[(((-55) max 55)/\t60),(((-50) max 50)/\t60)]))"
        },
        "threadsouts4": {
            "frequency": "1",
            "sound": [
                "A3/sounds_f/vehicles/armor/treads/ext_treads_soft_05",
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
    "tankturnforce": 310000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.72,
    "tbody": 250,
    "textplural": "tanks",
    "textsingular": "tank",
    "texturelist": [
        "CDF",
        1
    ],
    "texturesources": {
        "cdf": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [],
            "textures": [
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_hull_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_turret_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_green_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_green_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_green_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_red_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_green_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_red_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_red_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_green_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/cdf/rhs_2s1_cdf_suspension_red_co.paa"
            ]
        },
        "chdkz": {
            "author": "Red Hammer Studios",
            "displayname": "ChDKZ",
            "factions": [],
            "materials": [
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_hull.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_turret.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension.rvmat"
            ],
            "textures": [
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_hull_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_turret_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa",
                "rhsgref/addons/rhsgref_vehicles_ret/data/chdkz/rhs_2s1_chdkz_suspension_co.paa"
            ]
        },
        "light": {
            "author": "Red Hammer Studios",
            "displayname": "Light Green",
            "factions": [
                "rhs_faction_tv",
                "rhs_faction_vmf"
            ],
            "materials": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat"
            ],
            "textures": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_hull_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_turret_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_suspension_co.paa"
            ]
        },
        "light_dirty": {
            "author": "Red Hammer Studios",
            "displayname": "Green Weathered 2",
            "factions": [
                "rhs_faction_tv",
                "rhs_faction_vmf"
            ],
            "materials": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_hull.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_turret.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension.rvmat"
            ],
            "textures": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_hull_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_turret_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_light_dirty_suspension_co.paa"
            ]
        },
        "rhs_saf_camo": {
            "author": "Red Hammer Studios",
            "displayname": "SAF (Camo)",
            "factions": [
                "rhssaf_faction_army"
            ],
            "textures": [
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_hull_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_turret_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_red_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_green_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_green_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_black_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_green_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_black_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_black_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_green_co.paa",
                "rhssaf/addons/rhssaf_t_vehicle_ret/2s1/data/rhs_2s1_saf_suspension_red_co.paa"
            ]
        },
        "sand": {
            "author": "Red Hammer Studios",
            "displayname": "Sand",
            "factions": [
                "rhs_faction_tv",
                "rhs_faction_vmf"
            ],
            "materials": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat"
            ],
            "textures": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_hull_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_turret_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_sand_suspension_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [
                "rhs_faction_tv",
                "rhs_faction_vmf"
            ],
            "materials": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension.rvmat"
            ],
            "textures": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_hull_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_turret_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_suspension_co.paa"
            ]
        },
        "standard_dirty": {
            "author": "Red Hammer Studios",
            "displayname": "Green Weathered 1",
            "factions": [
                "rhs_faction_tv",
                "rhs_faction_vmf"
            ],
            "materials": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_hull.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_turret.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension.rvmat"
            ],
            "textures": [
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_hull_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_turret_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa",
                "rhsafrf/addons/rhs_2s1/data/rhs_2s1_dirty_suspension_co.paa"
            ]
        }
    },
    "texturetrackwheel": 0,
    "threat": [
        0.7,
        1,
        0.3
    ],
    "thrustdelay": 0.3,
    "torquecurve": [
        [
            0.35,
            0.546867
        ],
        [
            0.475,
            0.80136
        ],
        [
            0.6,
            1
        ],
        [
            0.7,
            1
        ],
        [
            0.75,
            0.97863
        ],
        [
            0.8,
            0.947062
        ],
        [
            0.9,
            0.917921
        ],
        [
            1.114,
            0
        ]
    ],
    "tracksspeed": 1.35,
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
        "_xx_rhs_mag_nspn_red": {
            "count": 10,
            "magazine": "rhs_mag_nspn_red"
        },
        "_xx_rhs_mag_rgd5": {
            "count": 10,
            "magazine": "rhs_mag_rgd5"
        },
        "_xx_rhsusf_mag_17rnd_9x19_fmj": {
            "count": 10,
            "magazine": "rhsusf_mag_17Rnd_9x19_FMJ"
        }
    },
    "transportmaxbackpacks": 12,
    "transportmaxmagazines": 128,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 0,
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
            "armorlights": 0.4,
            "body": "mainTurret",
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
            "discretedistance": [
                100
            ],
            "discretedistanceinitindex": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "elevationmode": 0,
            "forcehidegunner": 1,
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
            "gunneraction": "mbt2_slot2a_out",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "hatchC",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "mbt2_slot2a_in",
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
                    "armor": -150,
                    "armorcomponent": "Hit_Gun",
                    "explosionshielding": 0.0001,
                    "material": -1,
                    "minimalhit": -0.2,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.1,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": -150,
                    "armorcomponent": "Hit_Turret",
                    "explosionshielding": 0.0009,
                    "material": -1,
                    "minimalhit": -0.2,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.1,
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
            "lockwhenvehiclespeed": 1,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "magazines": [
                "rhs_mag_3of56_direct_30",
                "rhs_mag_bk13_10",
                "rhs_laserfcsmag",
                "rhs_laserfcsmag"
            ],
            "maxcamelev": 3.55,
            "maxelev": 70,
            "maxhorizontalrotspeed": 0.45,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 0.15,
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
            "mincamelev": -3.55,
            "minelev": -5,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "op5_37": {
                    "camdir": "op5_dir",
                    "campos": "op5_pos",
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_empty.p3d",
                    "hitpoint": "Hit_Optic_OP5_37",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.127273,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.127273,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.127273,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "OP5",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "Normal"
                    ]
                },
                "pg2": {
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_pg2.p3d",
                    "hitpoint": "Hit_Optic_PG2",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.189189,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.189189,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.189189,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "opticsdisplayname": "PG2",
                    "speedzoommaxfov": 0,
                    "speedzoommaxspeed": 10000000000.0,
                    "visionmode": [
                        "Normal"
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
            "reflectors": {},
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
                0.01,
                1,
                50
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
            "turretinfotype": "rhs_gui_optic_2s1_op5_computer",
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
                    "armorlights": 0.4,
                    "body": "obsTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 1,
                    "castgunnershadow": 0,
                    "commanding": 3,
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
                        1500
                    ],
                    "discretedistanceinitindex": 2,
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
                    "gunneraction": "rhs_2s1_commander_out",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "hatchC",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 1,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "rhs_2s1_commander",
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
                    "gunnertype": "rhsgref_cdf_b_reg_crew_commander",
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
                            "radius": 0.25,
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
                            "radius": 0.25,
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
                    "lodturnedin": 0,
                    "lodturnedout": 0,
                    "magazines": [],
                    "maxcamelev": 90,
                    "maxelev": 15,
                    "maxhorizontalrotspeed": 0.45,
                    "maxoutelev": 20,
                    "maxoutturn": 60,
                    "maxturn": 124,
                    "maxverticalrotspeed": 0.07,
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
                    "minelev": -6,
                    "minoutelev": -4,
                    "minoutturn": -60,
                    "minturn": -171,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "wide": {
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                            "hitpoint": "Hit_Optic_TKN3",
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
                            "opticsdisplayname": "TKN3",
                            "speedzoommaxfov": 0,
                            "speedzoommaxspeed": 10000000000.0,
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
                    "playerposition": 0,
                    "precisegetinout": 0,
                    "primary": 1,
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "proxyindex": 1,
                    "proxytype": "CPCommander",
                    "reflectors": {},
                    "selectionfireanim": "zasleh3",
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
                    "turretinfotype": "RscWeaponZeroing",
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
                        "initfov": 0.155,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.155,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.034,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "speedzoommaxfov": 0,
                        "speedzoommaxspeed": 10000000000.0,
                        "thermalmode": [
                            0,
                            1
                        ],
                        "visionmode": [
                            "Normal"
                        ]
                    },
                    "weapons": []
                },
                "loaderoptics": {
                    "aggregatereflectors": [],
                    "allowlauncherin": 0,
                    "allowlauncherout": 0,
                    "allowtablock": 1,
                    "animationsourcebody": "LdrTurret",
                    "animationsourcecamelev": "camElev",
                    "animationsourcegun": "LdrGun",
                    "animationsourcehatch": "hatchLoader",
                    "armorlights": 0.4,
                    "body": "LdrTurret",
                    "caneject": 1,
                    "canhidegunner": -1,
                    "canusescanners": 1,
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
                        1500
                    ],
                    "discretedistanceinitindex": 2,
                    "dontcreateai": 0,
                    "ejectdeadgunner": 0,
                    "forcehidegunner": 0,
                    "forcenvg": 0,
                    "gun": "LdrGun",
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
                    "gunneraction": "Commander_MBT_01_cannon_F_out",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "HatchL",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 1,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerhasflares": 1,
                    "gunnerinaction": "rhs_2s1_commander",
                    "gunnerlefthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnername": "Loader",
                    "gunneropticscolor": [
                        0,
                        0,
                        0,
                        1
                    ],
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tvn5.p3d",
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
                    "gunnertype": "rhsgref_cdf_b_reg_crew",
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
                    "ispersonturret": 1,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "lodopticsin": 0,
                    "lodopticsout": 0,
                    "lodturnedin": 0,
                    "lodturnedout": 0,
                    "magazines": [],
                    "maxcamelev": 90,
                    "maxelev": 15,
                    "maxhorizontalrotspeed": 0.45,
                    "maxoutelev": 20,
                    "maxoutturn": 60,
                    "maxturn": 124,
                    "maxverticalrotspeed": 0.07,
                    "memorypointgun": "usti hlavne3",
                    "memorypointgunneroptics": "loaderview",
                    "memorypointgunneroutoptics": "loaderview",
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
                    "minelev": -6,
                    "minoutelev": -4,
                    "minoutturn": -60,
                    "minturn": -171,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "periscope": {
                            "gunneropticseffect": [
                                "TankGunnerOptics1",
                                "OpticsBlur2",
                                "OpticsCHAbera2"
                            ],
                            "gunneropticsmodel": "rhsafrf/addons/rhs_optics/vehicles/rhs_tvn5.p3d",
                            "hitpoint": "Hit_Optic_Periscope",
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
                    "personturretaction": "vehicle_passenger_stand_2",
                    "playerposition": 0,
                    "precisegetinout": 0,
                    "primary": 1,
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "proxyindex": 2,
                    "proxytype": "CPCommander",
                    "reflectors": {},
                    "selectionfireanim": "zasleh3",
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
                    "turretinfotype": "RscWeaponZeroing",
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
                        "initfov": 0.155,
                        "maxanglex": 30,
                        "maxangley": 100,
                        "maxfov": 0.155,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.034,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "speedzoommaxfov": 0,
                        "speedzoommaxspeed": 10000000000.0,
                        "thermalmode": [
                            0,
                            1
                        ],
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
                "rhs_weap_2a31_at",
                "rhs_weap_fcs_noLRF"
            ]
        }
    },
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoArtillery",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "light_cateyes_off": {
            "condition": "(call rhs_fnc_findPlayer isEqualTo driver this) && {this animationPhase 'light_cateyes'<0.5};",
            "displayname": "Cat Eyes Off",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "priority": 0.5,
            "radius": 2,
            "showwindow": 0,
            "statement": "this animate ['light_cateyes', 1];"
        },
        "light_cateyes_on": {
            "condition": "(call rhs_fnc_findPlayer isEqualTo driver this) && this animationPhase 'light_cateyes'==1;",
            "displayname": "Cat Eyes On",
            "onlyforplayer": 0,
            "position": "pos_driverpos",
            "priority": 0.5,
            "radius": 2,
            "showwindow": 0,
            "statement": "this animate ['light_cateyes', 0];"
        }
    },
    "vehicleclass": "rhs_vehclass_artillery",
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
        "distancezoommax": 2000,
        "distancezoommin": 20,
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.7,
        "maxanglex": 110,
        "maxangley": 110,
        "maxfov": 0.7,
        "minanglex": -110,
        "minangley": -110,
        "minfov": 0.7,
        "opticszoommax": 0.7,
        "opticszoommin": 0.7
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
    "waterangulardampingcoef": 7.2,
    "waterdamageengine": 0.9,
    "watereffectspeed": 5,
    "waterfasteffectspeed": 28,
    "waterleakiness": 250,
    "waterlineardampingcoefx": 2,
    "waterlineardampingcoefy": 2,
    "waterppinvehicle": 1,
    "waterresistance": 2,
    "waterresistancecoef": 1.75,
    "weapons": [],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 2.01,
    "wheeldamageradiuscoef": 0.9,
    "wheeldamagethreshold": 0.2,
    "wheeldestroyradiuscoef": 0.4,
    "wheeldestroythreshold": 0.99,
    "wheels": {
        "l1": {
            "bonename": "",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l8": {
            "bonename": "wheel_podkolol7",
            "boundary": "wheel_1_8_bound",
            "center": "wheel_1_8_axis",
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
            "steering": 0,
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "l9": {
            "bonename": "",
            "boundary": "wheel_1_9_bound",
            "center": "wheel_1_9_axis",
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 8.16966,
            "side": "left",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r8": {
            "bonename": "wheel_podkolop7",
            "boundary": "wheel_2_8_bound",
            "center": "wheel_2_8_axis",
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
            "steering": 0,
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "width": 0.33
        },
        "r9": {
            "bonename": "",
            "boundary": "wheel_2_9_bound",
            "center": "wheel_2_9_axis",
            "dampingrate": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "dampingrateinair": 1120,
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
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "mass": 150,
            "maxbraketorque": 12000,
            "maxcompression": 0,
            "maxdroop": 0,
            "moi": 8.16966,
            "side": "right",
            "springdamperrate": 7500,
            "springstrength": 140000,
            "sprungmass": 1142.86,
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