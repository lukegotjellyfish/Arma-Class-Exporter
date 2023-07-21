d = {
    "_generalmacro": "Plane_Base_F",
    "acceleration": 1775,
    "access": 0,
    "accuracy": 0.02,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [
        [
            "Left",
            "Left_Flare",
            "Right",
            "Right_Flare",
            "Center",
            "Center_Flare"
        ]
    ],
    "aileroncoef": [
        0,
        0.4,
        0.75,
        0.9,
        1,
        1,
        1,
        1,
        0.85,
        0.65,
        0.4,
        0.1,
        0,
        0,
        0,
        0
    ],
    "aileroncontrolssensitivitycoef": 1.2,
    "aileronsensitivity": 0.35,
    "airbrake": 0,
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
    "altfullforce": 9000,
    "altnoforce": 20000,
    "alwaystarget": 0,
    "angleofindicence": "rad 3",
    "animated": 1,
    "animationsources": {
        "bbcpoccnn_decals1_hide": {
            "animperiod": 0.001,
            "displayname": "hide vvs decal 1",
            "initphase": 1,
            "mass": 1,
            "source": "user"
        },
        "bbcpoccnn_decals2_hide": {
            "animperiod": 0.001,
            "displayname": "hide vvs decal 2",
            "initphase": 1,
            "mass": 1,
            "source": "user"
        },
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        "damper_4_source": {
            "source": "damper",
            "wheel": "Wheel_4"
        },
        "damper_5_source": {
            "source": "damper",
            "wheel": "Wheel_5"
        },
        "damper_6_source": {
            "source": "damper",
            "wheel": "Wheel_6"
        },
        "lader_source": {
            "animperiod": 0.001,
            "displayname": "hide lader",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "(_this select 0) animateSource ['lader_source',(_this select 1)];",
            "source": "user"
        },
        "missile_revolver": {
            "source": "revolving",
            "weapon": "rhs_weap_kh55sm_Launcher"
        },
        "missilebay": {
            "animperiod": 5,
            "initphase": 1,
            "sound": "ServoRampSound_2",
            "soundposition": "missile_pos",
            "source": "door"
        },
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "RHS_Weap_GSh23Lx2"
        },
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_Weap_GSh23Lx2"
        },
        "reload_source": {
            "source": "reload",
            "weapon": "rhs_weap_kh55sm_Launcher"
        },
        "rf_decals_hide": {
            "animperiod": 0.001,
            "displayname": "hide rf decal",
            "initphase": 1,
            "mass": 1,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 50,
    "armorlights": 0.4,
    "armorstructural": 1,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "",
    "attributes": {
        "bbcpoccnn_decals1_hide": {
            "control": "CheckboxNumber",
            "defaultvalue": "1",
            "displayname": "Remove Part One of VVS Decal",
            "expression": "_this animate ['bbcpoccnn_decals1_hide',_value,true]",
            "property": "bbcpoccnn_decals1_hide"
        },
        "bbcpoccnn_decals2_hide": {
            "control": "CheckboxNumber",
            "defaultvalue": "1",
            "displayname": "Remove Part Two of VVS Decal",
            "expression": "_this animate ['bbcpoccnn_decals2_hide',_value,true]",
            "property": "bbcpoccnn_decals2_hide"
        },
        "rf_decals_hide": {
            "control": "CheckboxNumber",
            "defaultvalue": "1",
            "displayname": "Remove RF- Decal",
            "expression": "_this animate ['rf_decals_hide',_value,true]",
            "property": "rf_decals_hide"
        },
        "rhs_decalcoa": {
            "control": "Combo",
            "defaultvalue": "-1",
            "displayname": "Define City Coat of Arms Art",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRTU95COAPlaces, 'AviationsSquadrons',_value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalNoseArt",
            "tooltip": "Define City Coat of Arms texture located on nose. Appears on both sides",
            "typename": "Number",
            "values": {
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                "random": {
                    "defaultvalue": -1,
                    "name": "Random",
                    "value": -1
                }
            }
        },
        "rhs_decalnames": {
            "control": "Combo",
            "defaultvalue": "-1",
            "displayname": "Define City Names Art",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRTU95NamePlaces, 'AviationsSquadrons',_value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalNoseArt",
            "tooltip": "Define City Names texture located on side under the cockpit. Appears on both sides",
            "typename": "Number",
            "values": {
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                "random": {
                    "defaultvalue": -1,
                    "name": "Random",
                    "value": -1
                }
            }
        },
        "rhs_decalnumber": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if(parseNumber _value >= 0)then{if(parseNumber _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHSAIRTU95NumberPlaces}else{[_this, [['Number', cRHSAIRTU95NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaBlue'],parseNumber _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 2 numbers are required. Hides on 0",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of side number",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRTU95NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "typename": "STRING",
            "values": {
                "aviared": {
                    "name": "Aviation Red 1",
                    "value": "AviaRed"
                },
                "aviared2": {
                    "name": "Aviation Red 2",
                    "value": "AviaRed2"
                },
                "aviared3": {
                    "name": "Aviation Red 3",
                    "value": "AviaRed3"
                },
                "aviared4": {
                    "name": "Aviation Red 4",
                    "value": "AviaRed4"
                }
            }
        },
        "rhs_decalstarart": {
            "control": "Combo",
            "defaultvalue": "-1",
            "displayname": "Define Stars Art",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRTU95StarPlaces, 'Aviation',_value] ] ] call rhs_fnc_decalsInit};",
            "property": "rhs_decalStarArt",
            "tooltip": "Define Stars Art texture located on wings",
            "typename": "Number",
            "values": {
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                "new": {
                    "name": "New type star",
                    "value": 1
                },
                "old": {
                    "name": "Old type star",
                    "value": 2
                },
                "random": {
                    "defaultvalue": -1,
                    "name": "Random",
                    "value": -1
                }
            }
        }
    },
    "audible": 60,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 500,
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
    "cabinopening": 0,
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
    "camouflage": 100,
    "camshake": {
        "distance": 50,
        "frequency": 20,
        "minspeed": 200,
        "power": 50
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
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo01"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        0
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "RHS_HIND_Cargo_Enter"
    ],
    "cargogetoutaction": [
        "GetOutHigh"
    ],
    "cargoiscodriver": [
        0,
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
    "category": "Air",
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "passiveradarsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 0,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "animdirection": "",
                    "color": [
                        0.5,
                        1,
                        0.5,
                        0.5
                    ],
                    "componenttype": "PassiveRadarSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 16000,
                        "minrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": 12000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "transportpylonscomponent": {
            "bays": {
                "bay1": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                },
                "bay2": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                },
                "bay3": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                },
                "bay4": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                },
                "bay5": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                },
                "bay6": {
                    "autoclosewhenemptydelay": 0,
                    "bayopentime": 3.5,
                    "openbaywhenweaponselected": 1
                }
            },
            "pylons": {
                "pylon1": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 1,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 6,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.333,
                        0.52
                    ]
                },
                "pylon2": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 2,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 5,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.486,
                        0.46
                    ]
                },
                "pylon3": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 3,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 4,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.486,
                        0.41
                    ]
                },
                "pylon4": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 4,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 3,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.333,
                        0.35
                    ]
                },
                "pylon5": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 5,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 2,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.18,
                        0.41
                    ]
                },
                "pylon6": {
                    "attachment": "rhs_mag_kh55sh",
                    "bay": 6,
                    "hardpoints": [
                        "RHS_HP_TU95MS6_INT"
                    ],
                    "maxweight": 2000,
                    "priority": 1,
                    "turret": [
                        4
                    ],
                    "uiposition": [
                        0.18,
                        0.46
                    ]
                }
            },
            "uipicture": "rhsafrf/addons/rhs_air/tu95ms/loadouts/RHS_Tu95_EDEN_CA.paa"
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
                    "componenttype": "MinimapDisplayComponent"
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
    "cost": 2000000.0,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhs_pilot",
    "crewcrashprotection": 0.15,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_body.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_body_damage.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_destr.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_wing.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_wing_damage.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_destr.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "rhsafrf/addons/rhs_air/tu95ms/data/rhs_tu95ms_destr.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "Tu-95MS6 Bear 'Irkutsk'",
    "dlc": "RHS_AFRF",
    "draconicforcexcoef": 10,
    "draconicforceycoef": 0.25,
    "draconicforcezcoef": 0.1,
    "draconictorquexcoef": 0.15,
    "draconictorqueycoef": 0.1,
    "driveoncomponent": [],
    "driveraction": "RHS_TU95_Pilot",
    "drivercaneject": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "pilotyoke",
    "driverleftleganimname": "pilotpedal_L",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "pilotyoke",
    "driverrightleganimname": "pilotpedal_R",
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dusteffect": "HeliDust",
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
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/RHS_TU95MS_vvs_irkutsk.paa",
    "editorsubcategory": "EdSubcat_Planes",
    "ejectdamagelimit": 0.45,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "ejectionsystem": {},
    "ejectspeed": [
        0,
        60,
        0
    ],
    "elevatorcoef": [
        0,
        0.6,
        1.15,
        1.45,
        1.65,
        1.65,
        1.65,
        1.35,
        0.9,
        0.57,
        0.35,
        0.2,
        0.1,
        0,
        0,
        0
    ],
    "elevatorcontrolssensitivity": 1,
    "elevatorcontrolssensitivitycoef": 4,
    "elevatorsensitivity": 0.45,
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
    "enginemoi": 90,
    "envelope": [
        0.1,
        0.1,
        0.65,
        1.75,
        2.5,
        3,
        3,
        2.5,
        1.75,
        1.35,
        1,
        0.5,
        0
    ],
    "epeimpulsedamagecoef": 10,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay",
            "init": "_this call rhs_fnc_air_init;"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlaneBig",
            "position": "exhaust1"
        },
        "exhaust2": {
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectPlaneBig",
            "position": "exhaust2"
        },
        "exhaust3": {
            "direction": "exhaust3_dir",
            "effect": "ExhaustsEffectPlaneBig",
            "position": "exhaust3"
        },
        "exhaust4": {
            "direction": "exhaust4_dir",
            "effect": "ExhaustsEffectPlaneBig",
            "position": "exhaust4"
        }
    },
    "explosionshielding": 2,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        5,
        -65
    ],
    "faction": "rhs_faction_vvs",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flaps": 1,
    "flapsfrictioncoef": 0.5,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 200,
    "formationz": 300,
    "fuelcapacity": 1000,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 10,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 24,
    "gearretracting": 1,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 26,
    "getinaction": "RHS_HIND_Cargo_Enter",
    "getinoutonproxy": 0,
    "getinradius": 1.2,
    "getoutaction": "GetOutHigh",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunaimdown": 0,
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
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "gunnerhasflares": 1,
    "gunnerusespilotview": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.005,
        0.001,
        0.025
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
        "i1",
        "i2",
        "i3",
        "n1",
        "n2"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_irkutsk_coa_ca.paa",
        "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_irkutsk_name_ca.paa",
        "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_new_ca.paa",
        "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/0_ca.paa",
        "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/1_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitammo": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0.02,
            "name": "revolver_hit",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "-"
        },
        "hitavionics": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0.02,
            "name": "HitAvionics",
            "passthrough": 0.2,
            "radius": 0.2,
            "visual": "-"
        },
        "hitengine": {
            "armor": 1.5,
            "depends": "(HitEngine_1 + HitEngine_2)*0.5",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_1_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "-"
        },
        "hitengine2": {
            "armor": 1.5,
            "depends": "(HitEngine_3 + HitEngine_4)*0.5",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_2_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "-"
        },
        "hitengine_1": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_1_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "engine_1_vis"
        },
        "hitengine_2": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_2_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "engine_2_vis"
        },
        "hitengine_3": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_3_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "engine_3_vis"
        },
        "hitengine_4": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_4_hit",
            "passthrough": 0.5,
            "radius": 0.55,
            "visual": "engine_4_vis"
        },
        "hitfuel": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "fuel_central",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        "hitfuel2": {
            "armor": 3,
            "depends": "(HitFuel_left_wing + HitFuel_right_wing)*0.5",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "fuel_central",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        "hitfuel_left_wing": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "fuel_left_wing",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "Aileron_1"
        },
        "hitfuel_right_wing": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 4,
            "material": -1,
            "minimalhit": 0.1,
            "name": "fuel_right_wing",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "Aileron_2"
        },
        "hithull": {
            "armor": 3,
            "depends": "Total",
            "explosionshielding": 5,
            "material": -1,
            "minimalhit": 0.02,
            "name": "HitHull",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "hull_hit"
        },
        "hitlaileron": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitLAileron",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "Aileron_1"
        },
        "hitlcelevator": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitLCElevator",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "Elevator_1_vis"
        },
        "hitlcrudder": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitRudder",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "Rudder_1_vis"
        },
        "hitraileron": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitRAileron",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "Aileron_2"
        },
        "hitrelevator": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "HitRElevator",
            "passthrough": 0.1,
            "radius": 0.2,
            "visual": "Elevator_2_vis"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "rhsafrf/addons/rhs_air/tu95ms/data/ui/icomap_tu95.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "8 + 16",
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.0316228,
    "irscanground": 1,
    "irscanrangemax": 10000,
    "irscanrangemin": 2000,
    "irscantoeyefactor": 2,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "landingaoa": "rad 10",
    "landingspeed": 240,
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffect": "LDustEffects",
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
    "lightongear": 1,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8 + 4",
    "magazines": [],
    "mapsize": 17.78,
    "markerlights": {
        "collisionwhite1": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.7,
            "drawlightsize": 1.5,
            "intensity": 750,
            "name": "CollisionLight_white_1_pos",
            "useflare": 0
        },
        "collisionwhite2": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.7,
            "drawlightsize": 1.5,
            "intensity": 750,
            "name": "CollisionLight_white_2_pos",
            "useflare": 0
        },
        "positiongreen1": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_green_1_pos",
            "useflare": 0
        },
        "positiongreen2": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_green_2_pos",
            "useflare": 0
        },
        "positionred1": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_red_1_pos",
            "useflare": 0
        },
        "positionred2": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_red_2_pos",
            "useflare": 0
        },
        "positionwhite1": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_white_1_pos",
            "useflare": 0
        },
        "positionwhite2": {
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
            "drawlight": 2.5,
            "drawlightcentersize": 0.14,
            "drawlightsize": 0.35,
            "intensity": 750,
            "name": "PositionLight_white_2_pos",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 0.001,
    "maxgforce": 3,
    "maxgunelev": 0,
    "maxgunturn": 0,
    "maximumload": 500,
    "maxomega": 2000,
    "maxspeed": 920,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": [
        "driverview",
        "pilot"
    ],
    "memorypointgun": "kulomet",
    "memorypointldust": "levy prach",
    "memorypointlrocket": "L raketa",
    "memorypointrdust": "pravy prach",
    "memorypointrrocket": "P raketa",
    "memorypointsgetincargo": [
        "pos driver"
    ],
    "memorypointsgetincargodir": [
        "pos driver dir"
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
    "mfact": 0.2,
    "mfd": {
        "hud": {
            "bones": {
                "aglmove1": {
                    "max": 100,
                    "maxpos": [
                        0.05,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.05,
                        0.1
                    ],
                    "source": "altitudeAGL",
                    "type": "linear"
                },
                "aglmove2": {
                    "pos": [
                        0.05,
                        0.8
                    ],
                    "type": "fixed"
                },
                "aslmove1": {
                    "max": 500,
                    "maxpos": [
                        0.1,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.1,
                        0.1
                    ],
                    "source": "altitudeASL",
                    "type": "linear"
                },
                "aslmove2": {
                    "pos": [
                        0.1,
                        0.8
                    ],
                    "type": "fixed"
                },
                "ils": {
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos3": [
                        0.7,
                        0.6
                    ],
                    "type": "ils"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.27
                    ],
                    "type": "fixed"
                },
                "spdmove2": {
                    "max": 200,
                    "maxpos": [
                        0.94,
                        0.87
                    ],
                    "min": 33,
                    "minpos": [
                        0.94,
                        0.1
                    ],
                    "source": "speed",
                    "type": "linear"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "target",
                    "type": "vector"
                },
                "targetdistancemgun": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 1000,
                    "maxangle": 90,
                    "min": 100,
                    "minangle": -180,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "targetdistancemissile": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 3000,
                    "maxangle": 120,
                    "min": 100,
                    "minangle": -120,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "vertspeed": {
                    "max": 25,
                    "maxpos": [
                        0,
                        0.4
                    ],
                    "min": -25,
                    "minpos": [
                        0,
                        -0.4
                    ],
                    "source": "vSpeed",
                    "type": "linear"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "weapon",
                    "type": "vector"
                }
            },
            "borderbottom": 0.1,
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "bottomleft": "HUD LD",
            "color": [
                0,
                1,
                0,
                0.1
            ],
            "draw": {
                "alpha": 0.8,
                "altitude": {
                    "points": [
                        [
                            "AGLMove1",
                            1
                        ],
                        [
                            "AGLMove2",
                            1
                        ],
                        [],
                        [
                            "ASLMove2",
                            1
                        ],
                        [
                            "ASLMove1",
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1,
                            "VertSpeed",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "clipbr": [
                    1,
                    0.9
                ],
                "cliptl": [
                    0,
                    0.05
                ],
                "color": [
                    0.1,
                    0.5,
                    0.05
                ],
                "condition": "on",
                "dimmedbase": {
                    "alpha": 0.3,
                    "altitudebase": {
                        "points": [
                            [
                                "AGLMove2",
                                1
                            ],
                            [
                                "ASLMove2",
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "horizont": {
                    "clipbr": [
                        0.8,
                        0.9
                    ],
                    "cliptl": [
                        0.2,
                        0.1
                    ],
                    "dimmed": {
                        "alpha": 0.6,
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.4,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.4,
                                        0
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    },
                    "levelm10": {
                        "points": [
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm15": {
                        "points": [
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    -0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm5": {
                        "points": [
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp10": {
                        "points": [
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp15": {
                        "points": [
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp5": {
                        "points": [
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "ils": {
                    "aoabracket": {
                        "points": [
                            [
                                [
                                    0.42,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.88
                                ],
                                1
                            ],
                            [
                                [
                                    0.42,
                                    0.88
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "ils",
                    "glideslope": {
                        "clipbr": [
                            0.71,
                            0.71
                        ],
                        "cliptl": [
                            0.29,
                            0.29
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS",
                                    [
                                        -10,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        10,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS",
                                    [
                                        0,
                                        -10
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        0,
                                        10
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    }
                },
                "mgun": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(-180)",
                                    "-0.03*cos(-180)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(-180)",
                                    "-0.07*cos(-180)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(+90)",
                                    "-0.03*cos(+90)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(+90)",
                                    "-0.07*cos(+90)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.04
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "mgun"
                },
                "missile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(-120)",
                                    "-0.1*0.8*cos(-120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(-120)",
                                    "-0.1*1.2*cos(-120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(+120)",
                                    "-0.1*0.8*cos(+120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(+120)",
                                    "-0.1*1.2*cos(+120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*0.8"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*1.2"
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "missile",
                    "target": {
                        "points": [
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "planew": {
                    "clipbr": [
                        1,
                        0.9
                    ],
                    "cliptl": [
                        0,
                        0.1
                    ],
                    "linehl": {
                        "points": [
                            [
                                "PlaneW",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "velocity": {
                        "points": [
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "speed": {
                    "points": [
                        [
                            [
                                0.95,
                                0.87
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.1
                            ],
                            1
                        ],
                        [],
                        [
                            "SpdMove2",
                            [
                                -0.05,
                                0
                            ],
                            1
                        ],
                        [
                            "SpdMove2",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "speednumber": {
                    "align": "left",
                    "down": [
                        "SpdMove2",
                        [
                            -0.05,
                            0.03
                        ],
                        1
                    ],
                    "pos": [
                        "SpdMove2",
                        [
                            -0.05,
                            -0.03
                        ],
                        1
                    ],
                    "right": [
                        "SpdMove2",
                        [
                            0.01,
                            -0.03
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                }
            },
            "helmetdown": [
                0,
                -0.05,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.025,
                0.025,
                0.1
            ],
            "helmetright": [
                0.05,
                0,
                0
            ],
            "pos10vector": {
                "pos0": [
                    0.5,
                    0.27
                ],
                "pos10": [
                    "0.5+0.9",
                    "0.27+0.7"
                ],
                "type": "vector"
            },
            "topleft": "HUD LH",
            "topright": "HUD PH"
        }
    },
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
    "mgunfire": {
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
        "cloudletduration": 0,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "cloudletgrowup": 0.06,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletFire",
        "cloudletsize": 1,
        "deltat": -4000,
        "initt": 3200,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
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
    "minealerticonrange": 200,
    "minfiretime": 60,
    "mingforce": 0.3,
    "mingunelev": 0,
    "mingunturn": 0,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsafrf/addons/rhs_air/tu95ms/rhs_tu95ms",
    "namesound": "veh_air_plane_s",
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
    "numberphysicalwheels": 3,
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
    "picture": "rhsafrf/addons/rhs_air/tu95ms/data/ui/tu95_icon.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 200,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.6,
    "radartype": 4,
    "reflectors": {
        "center": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_3_dir",
            "flaresize": 2,
            "hitpoint": "svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "gearlight_3_pos",
            "selection": "gearlight_3_sel",
            "size": 1,
            "useflare": 1
        },
        "center_flare": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_3_dir",
            "flaresize": 2,
            "hitpoint": "svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 178,
            "position": "gearlight_3_pos",
            "selection": "gearlight_3_sel",
            "size": 1,
            "useflare": 1
        },
        "left": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_1_dir",
            "flaresize": 2,
            "hitpoint": "l svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "gearlight_1_pos",
            "selection": "gearlight_1_sel",
            "size": 1,
            "useflare": 1
        },
        "left_flare": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_1_dir",
            "flaresize": 2,
            "hitpoint": "l svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 178,
            "position": "gearlight_1_pos",
            "selection": "gearlight_1_sel",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_2_dir",
            "flaresize": 2,
            "hitpoint": "p svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "gearlight_2_pos",
            "selection": "gearlight_2_sel",
            "size": 1,
            "useflare": 1
        },
        "right_flare": {
            "ambient": [
                100,
                100,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 300,
                "hardlimitstart": 150,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "gearlight_2_dir",
            "flaresize": 2,
            "hitpoint": "p svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 178,
            "position": "gearlight_2_pos",
            "selection": "gearlight_2_sel",
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
        "['Number',cRHSAIRTU95NumberPlaces,'AviaRed2']"
    ],
    "rightdusteffect": "RDustEffects",
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
    "ruddercoef": [
        0,
        0.1,
        0.35,
        0.5,
        0.6,
        0.6,
        0.45,
        0.35,
        0.2,
        0.1,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "ruddercontrolssensitivitycoef": 0.8,
    "rudderinfluence": 0.015,
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionrotormove": "vrtule blur",
    "selectionrotorstill": "vrtule staticka",
    "selectionshowdamage": "poskozeni",
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
    "side": 0,
    "simulation": "airplanex",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.6,
    "soundarmorcrash": [
        "emptySound",
        0
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "emptySound",
        0
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
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_stop",
        6.41254,
        1,
        500
    ],
    "soundengineoffint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_int_stop",
        6,
        1,
        500
    ],
    "soundengineonext": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_start",
        6.41254,
        1,
        500
    ],
    "soundengineonint": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_int_start",
        6,
        1,
        500
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
        "A3/Sounds_F_EPC/CAS_01/Flaps_Down",
        4.63096,
        1,
        100
    ],
    "soundflapsup": [
        "A3/Sounds_F_EPC/CAS_01/Flaps_Up",
        4.63096,
        1,
        100
    ],
    "soundgear": {},
    "soundgeardown": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_hydraulicpump",
        5.79433,
        1,
        150
    ],
    "soundgearup": [
        "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_hydraulicpump",
        5.79433,
        1,
        150
    ],
    "soundgetin": [
        "A3/Sounds_F_EPC/CAS_01/getin_wipeout",
        1,
        1,
        40
    ],
    "soundgetout": [
        "A3/Sounds_F/air/Plane_Fighter_03/getout",
        1,
        1,
        40
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_1",
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
        "/A3/Sounds_F/weapons/Rockets/locked_1",
        0.316228,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "enginehighin": {
            "frequency": "1",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_int_low",
                3.16228,
                1.2
            ],
            "volume": "((1-camPos)*(rpm factor[0.85, 1.0]))*3"
        },
        "enginehighout": {
            "frequency": "1",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_low",
                10,
                1.2,
                4300
            ],
            "volume": "(camPos*4*(rpm factor[0.2, 1.1])*(rpm factor[1.1, 0.5]))*1"
        },
        "enginelowin": {
            "frequency": "1.0 + (rpm + 0.5)",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_int_low",
                3.16228,
                1
            ],
            "volume": "((1-camPos)*((rpm factor[0.2, 0.1])*(rpm factor[0.1, 0.7])))*3"
        },
        "enginelowout": {
            "frequency": "1.0 min (rpm + 0.5)",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_low",
                10,
                1,
                4000
            ],
            "volume": "(camPos*4*(rpm factor[0.2, 1.1])*(rpm factor[1.1, 0.5]))*2"
        },
        "forsagein": {
            "frequency": "1",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_high",
                3.34965,
                1.2
            ],
            "volume": "((1-camPos)*(engineOn*(thrust factor[0.6, 1.0])))*0.5"
        },
        "forsageout": {
            "cone": [
                3.14,
                3.92,
                2,
                0.5
            ],
            "frequency": "1",
            "sound": [
                "rhsafrf/addons/rhs_vehiclesounds/sounds/air/Tu95/tu95_ext_high",
                10,
                1.2,
                4500
            ],
            "volume": "(engineOn*camPos*(thrust factor[0.6, 1.0]))*1"
        },
        "rainext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_ext",
                1.77828,
                1,
                100
            ],
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        "rainint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_int",
                1,
                1,
                100
            ],
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        "windnoisein": {
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "sound": [
                "A3/Sounds_F/air/Plane_Fighter_03/noise_int",
                0.816228,
                1
            ],
            "volume": "(1-camPos)*(speed factor[1, 150])"
        },
        "windnoiseout": {
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "sound": [
                "A3/Sounds_F/air/Plane_Fighter_03/noise",
                1.06234,
                1,
                150
            ],
            "volume": "camPos*(speed factor[1, 150])"
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
                "veh_air_plane_p"
            ],
            "speechsingular": [
                "veh_air_plane_s"
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
    "stallwarningtreshold": 0.2,
    "steeraheadplan": 2,
    "steeraheadsimul": 1,
    "supplyradius": 2,
    "tailhook": 0,
    "takeoffspeed": 290,
    "tbody": 150,
    "textplural": "fast movers",
    "textsingular": "fast mover",
    "texturelist": [],
    "texturesources": {
        "old": {
            "author": "Red Hammer Studios",
            "displayname": "Tu-95MS6 Bear",
            "factions": [
                "rhs_faction_vvs"
            ],
            "textures": [
                "",
                "",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_old_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/2_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/3_ca.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Tu-95MS6 Bear 'Chelyabinsk'",
            "factions": [
                "rhs_faction_vvs"
            ],
            "textures": [
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_chelyabinsk_coa_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_chelyabinsk_name_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_new_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/2_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/2_ca.paa"
            ]
        },
        "standard2": {
            "author": "Red Hammer Studios",
            "displayname": "Tu-95MS6 Bear 'Dubna'",
            "factions": [
                "rhs_faction_vvs"
            ],
            "textures": [
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_dubna_coa_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_dubna_name_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_new_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed2/2_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed2/0_ca.paa"
            ]
        },
        "standard3": {
            "author": "Red Hammer Studios",
            "displayname": "Tu-95MS6 Bear 'Irkutsk'",
            "factions": [
                "rhs_faction_vvs"
            ],
            "textures": [
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_irkutsk_coa_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_irkutsk_name_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_new_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/0_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/1_ca.paa"
            ]
        },
        "standard4": {
            "author": "Red Hammer Studios",
            "displayname": "Tu-95MS6 Bear 'Tambov'",
            "factions": [
                "rhs_faction_vvs"
            ],
            "textures": [
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_tambov_coa_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Tu95/rhs_decal_tambov_name_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Labels/Aviation/star_new_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/2_ca.paa",
                "/rhsafrf/addons/rhs_decals/Data/Numbers/AviaRed4/3_ca.paa"
            ]
        }
    },
    "threat": [
        0.1,
        1,
        0.5
    ],
    "thrustcoef": [
        0.45,
        0.65,
        0.65,
        0.75,
        0.95,
        1.25,
        1.25,
        1.4,
        1.35,
        1.25,
        1.2,
        1.1,
        1,
        0.75,
        0.55,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_b_parachute": {
            "backpack": "rhs_d6_Parachute_backpack",
            "count": 8
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 4,
            "name": "FirstAidKit"
        },
        "_xx_itemgps": {
            "count": 1,
            "name": "ItemGPS"
        },
        "_xx_itemradio": {
            "count": 1,
            "name": "ItemRadio"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 6,
    "transportmaxmagazines": 24,
    "transportmaxweapons": 6,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {
        "copilotturret": {
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
            "commanding": -1,
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Copilot",
            "gunnernotspawned": 1,
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
            "gunnerusespilotview": 1,
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
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
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
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
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
        "mainturret": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                            "componenttype": "MinimapDisplayComponent"
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunneraction": "RHS_TU95_Pilot",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "RHS_TU95_Pilot",
            "gunnerlefthandanimname": "copilotyoke",
            "gunnerleftleganimname": "copilotpedal_L",
            "gunnername": "Copilot",
            "gunnernotspawned": 0,
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
            "gunnerrighthandanimname": "copilotyoke",
            "gunnerrightleganimname": "copilotpedal_R",
            "gunnertype": "",
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 1,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
        "mainturret2": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                            "componenttype": "MinimapDisplayComponent"
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunneraction": "Truck_Cargo01",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "Truck_Cargo01",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Flight Engineer",
            "gunnernotspawned": 0,
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
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
        "mainturret3": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                            "componenttype": "MinimapDisplayComponent"
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunneraction": "Truck_Cargo01",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "Truck_Cargo01",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Radio Operator",
            "gunnernotspawned": 0,
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
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
        "mainturret4": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                3000,
                                8000,
                                16000,
                                35000
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
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                3000,
                                8000,
                                16000,
                                35000
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunneraction": "Truck_Cargo01",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "Truck_Cargo01",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Weapons Engineer",
            "gunnernotspawned": 0,
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
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
        "mainturret5": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                3000,
                                8000,
                                16000,
                                35000
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
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                3000,
                                8000,
                                16000,
                                35000
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
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
            "gunneraction": "Truck_Cargo01",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "Truck_Cargo01",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Navigation Plotter",
            "gunnernotspawned": 0,
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
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "missile_pos",
            "missileend": "missile_dir",
            "outgunnermayfire": 0,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 6,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showascargo": 0,
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
            "weapons": [],
            "weaponsondeploy": [
                "rhs_weap_kh55sm_Launcher"
            ],
            "weaponsonundeploy": [
                "rhs_weap_kh55sm_Dummy_Launcher"
            ]
        },
        "mainturret6": {
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
                            "componenttype": "MinimapDisplayComponent"
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
            "disablesoundattenuation": 0,
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
            "gunneraction": "Truck_Cargo01",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "Truck_Cargo01",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Flight Instructor",
            "gunnernotspawned": 0,
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
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
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
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
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
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 5,
            "proxytype": "CPGunner",
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
        "rearturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "rear_turret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "rear_gun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "gunnerballY",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 0,
            "castgunnershadow": 1,
            "commanding": -1,
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
                            "componenttype": "MinimapDisplayComponent"
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "gunnerballX",
            "gunbeg": "chase01dir",
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
            "gunend": "chase01",
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
            "gunneraction": "RHS_TU95_RearGunner",
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "RHS_HIND_Cargo_Enter",
            "gunnergetoutaction": "",
            "gunnerinaction": "RHS_TU95_RearGunner",
            "gunnerlefthandanimname": "collimator_turret",
            "gunnerleftleganimname": "reargunner_leg_left",
            "gunnername": "Rear Gunner",
            "gunnernotspawned": 0,
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
            "gunnerrighthandanimname": "collimator_turret",
            "gunnerrightleganimname": "reargunner_leg_right",
            "gunnertype": "",
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": -180,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1200,
            "lodopticsout": 1200,
            "lodturnedin": 1200,
            "lodturnedout": 1200,
            "magazines": [
                "rhs_mag_AM23_500"
            ],
            "maxcamelev": 90,
            "maxelev": 35,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -115,
            "maxverticalrotspeed": 3,
            "memorypointgun": [
                "chase01",
                "chase02",
                "chase03",
                "chase04"
            ],
            "memorypointgunneroptics": "reargunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "reargunner_pos",
            "memorypointsgetingunnerdir": "reargunner_dir",
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
            "minturn": -245,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "kps53av": {
                    "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.75,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.275,
                    "opticsdisplayname": "KPS53AV",
                    "thermalmode": [
                        0,
                        1
                    ]
                }
            },
            "opticsout": {
                "kps53av": {
                    "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.75,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.275,
                    "thermalmode": [
                        0,
                        1
                    ],
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
            "primaryobserver": 0,
            "proxyindex": 7,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "rearFlash",
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
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
                "RHS_Weap_GSh23Lx2"
            ]
        }
    },
    "type": 2,
    "typicalcargo": [
        "rhs_pilot",
        "rhs_pilot",
        "rhs_pilot",
        "rhs_pilot",
        "rhs_pilot",
        "rhs_pilot",
        "rhs_pilot"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoAirPlane",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "controlpanel": {
            "condition": "(alive this)&&((call rhs_fnc_findPlayer)==(gunner this))",
            "displayname": "Open control panel",
            "onlyforplayer": 0,
            "position": "zamerny",
            "radius": 10.01,
            "statement": "createDialog 'tu95_main_dialog'"
        },
        "creweject": {
            "condition": "(findPlayer in this) AND (findPlayer != this turretUnit [5]) AND (this animationSourcePhase 'gear' < 0.4)",
            "displayname": "Eject",
            "onlyforplayer": 1,
            "position": "",
            "priority": 1.5,
            "radius": 52,
            "showwindow": 0,
            "statement": "moveOut findPlayer"
        }
    },
    "vehicleclass": "rhs_vehclass_aircraft",
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
        "initfov": 0.5,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 0.5,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 0.5,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
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
    "visualtargetsize": 1.6,
    "vtol": 0,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "vtolyawinfluence": 2,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 150,
    "waterlineardampingcoefx": 5,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.04,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "wheels": {
        "disablewheelswhendestroyed": 1,
        "wheel_1": {
            "bonename": "Wheel_1_damper_land",
            "boundary": "Wheel_1_rim",
            "center": "Wheel_1_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.09,
            "maxdroop": 0.11,
            "maxhandbraketorque": 0,
            "moi": 15.2551,
            "side": "left",
            "springdamperrate": 12569.6,
            "springstrength": 16600,
            "sprungmass": 3200,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_center",
            "width": 0.83
        },
        "wheel_1_fake": {
            "bonename": "Wheel_1_damper_land",
            "boundary": "Wheel_1_rim",
            "center": "Wheel_1_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.09,
            "maxdroop": 0.11,
            "maxhandbraketorque": 0,
            "moi": 15.2551,
            "side": "left",
            "springdamperrate": 12569.6,
            "springstrength": 16600,
            "sprungmass": 3200,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_center",
            "width": 0.83
        },
        "wheel_2": {
            "bonename": "Wheel_2_damper_land",
            "boundary": "Wheel_2_rim",
            "center": "Wheel_2_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.25,
            "maxdroop": 0.06,
            "maxhandbraketorque": 0,
            "moi": 25.0563,
            "side": "left",
            "springdamperrate": 9000,
            "springstrength": 261000,
            "sprungmass": 34200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_2_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_2_center",
            "width": 1.2
        },
        "wheel_3": {
            "bonename": "Wheel_2_damper_land",
            "boundary": "Wheel_3_rim",
            "center": "Wheel_3_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.25,
            "maxdroop": 0.06,
            "maxhandbraketorque": 0,
            "moi": 25.0563,
            "side": "left",
            "springdamperrate": 9000,
            "springstrength": 261000,
            "sprungmass": 34200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_3_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_3_center",
            "width": 1.2
        },
        "wheel_4": {
            "bonename": "Wheel_4",
            "boundary": "Wheel_4_rim",
            "center": "Wheel_4_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.25,
            "maxdroop": 0.06,
            "maxhandbraketorque": 0,
            "moi": 25.0563,
            "side": "Wheel_4_damper_land",
            "springdamperrate": 9000,
            "springstrength": 261000,
            "sprungmass": 34200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_4_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_4_center",
            "width": 1.2
        },
        "wheel_5": {
            "bonename": "Wheel_5_damper_land",
            "boundary": "Wheel_5_rim",
            "center": "Wheel_5_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    1
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 25,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 150,
            "maxbraketorque": 21500,
            "maxcompression": 0.25,
            "maxdroop": 0.06,
            "maxhandbraketorque": 0,
            "moi": 25.0563,
            "side": "Wheel_4_damper_land",
            "springdamperrate": 9000,
            "springstrength": 261000,
            "sprungmass": 34200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_5_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_5_center",
            "width": 1.2
        }
    },
    "wheelsteeringsensitivity": 2.5,
    "windsockexist": 0,
    "wingvortices": {
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "cerveny pozicni"
        },
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "zeleny pozicni"
        }
    }
}