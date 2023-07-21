d = {
    "_generalmacro": "Helicopter_Base_H",
    "_mainbladecenter": "rotor_center",
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "ace_cargo_hascargo": 1,
    "ace_cargo_space": 16,
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
    "altfullforce": 2000,
    "altnoforce": 6000,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "cabinlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "cargolights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
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
        "hide_cargo": {
            "animperiod": 1e-05,
            "displayname": "hide cargo benches",
            "initphase": 0,
            "mass": -20,
            "onphasechanged": "(_this select 0) lockCargo ((_this select 1)==1)",
            "source": "user"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass10": {
            "hitpoint": "HitGlass10",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass11": {
            "hitpoint": "HitGlass11",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass12": {
            "hitpoint": "HitGlass12",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass13": {
            "hitpoint": "HitGlass13",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass14": {
            "hitpoint": "HitGlass14",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass15": {
            "hitpoint": "HitGlass15",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass16": {
            "hitpoint": "HitGlass16",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass17": {
            "hitpoint": "HitGlass17",
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
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass9": {
            "hitpoint": "HitGlass9",
            "raw": 1,
            "source": "Hit"
        },
        "hmg_hide": {
            "animperiod": 0,
            "initphase": 1,
            "source": "user"
        },
        "maingun": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "mainrotor_folded": {
            "animperiod": 10,
            "initphase": 0,
            "source": "door"
        },
        "mainrotor_folded_handler": {
            "animperiod": 1e-05,
            "displayname": "fold rotors",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "_this call rhsusf_fnc_ch53_fold",
            "sound": "CH53_Rampsound",
            "source": "user"
        },
        "mainturret": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "muzzle_rot_hmg_1": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "ramp": {
            "animperiod": 4,
            "initphase": 0,
            "sound": "CH53_Rampsound",
            "source": "user"
        },
        "ramp_hmg": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "reload_hmg_1": {
            "animperiod": 0,
            "initphase": 0,
            "source": "user"
        },
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 40,
    "armorlights": 0.4,
    "armorstructural": 3,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "HeliAttenuation",
    "attributes": {
        "foldheli": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Fold helicopter rotors",
            "expression": "[_this,_value,true] call rhsusf_fnc_ch53_fold",
            "property": "FoldHeli"
        },
        "hide_cargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Hide cargo benches",
            "expression": "_this animate ['%s',_value,true];_this lockCargo (_value == 1)",
            "property": "hide_cargo"
        },
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
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "property": "rhs_attachCargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action"
        },
        "rhs_decalnumber": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{[_this, [['Number', cCH53NumberPlaces, _this getVariable ['rhs_decalNumber_type','USMCGrey'], _value] ] ] call rhsusf_fnc_decalsInit};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 2 numbers are required. If 0, random number will be generated",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of side number",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cCH53NumberPlaces, _value]]] call rhsusf_fnc_decalsInit",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "typename": "STRING",
            "values": {
                "usmcblackshadow": {
                    "name": "USMC (Black Shadow)",
                    "value": "USMCBlackShadow"
                },
                "usmcgrey": {
                    "defaultvalue": "USMCGrey",
                    "name": "USMC (Grey)",
                    "value": "USMCGrey"
                }
            }
        },
        "rhs_openramp": {
            "control": "slider",
            "defaultvalue": "0",
            "displayname": "Open rear ramp",
            "expression": "_this animate ['ramp_bottom',_value];_this animate ['ramp_top',_value];",
            "property": "rhs_openRamp"
        }
    },
    "audible": 50,
    "author": "Rocket, RHS",
    "autocenter": 1,
    "availableforsupporttypes": [
        "Drop",
        "Transport"
    ],
    "backrotorforcecoef": 0.3,
    "backrotorspeed": 1.5,
    "bodyfrictioncoef": 1,
    "brakedistance": 200,
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
    "camouflage": 100,
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
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "ChopperHeavy_LP_Static_H"
    ],
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
    "castcargoshadow": 1,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "irsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 7000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 98,
                    "anglerangevertical": 72,
                    "animdirection": "ObsGun",
                    "color": [
                        1,
                        0,
                        0,
                        1
                    ],
                    "componenttype": "IRSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 7000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxfogseethrough": 0.95,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 695,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": 0,
                    "typerecognitiondistance": -1
                },
                "lasersensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "animdirection": "",
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "componenttype": "LaserSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 6000,
                        "minrange": 6000,
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
                    "typerecognitiondistance": 0
                },
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
                },
                "visualsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 4000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 98,
                    "anglerangevertical": 72,
                    "animdirection": "ObsGun",
                    "color": [
                        1,
                        1,
                        0.5,
                        0.8
                    ],
                    "componenttype": "VisualSensorComponent",
                    "groundnoisedistancecoef": -1,
                    "groundtarget": {
                        "maxrange": 4000,
                        "minrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxfogseethrough": 0.94,
                    "maxgroundnoisedistance": -1,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 70,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "nightrangecoef": 0,
                    "typerecognitiondistance": 2000
                }
            }
        },
        "transportcountermeasurescomponent": {},
        "transportpylonscomponent": {
            "pylons": {
                "cmdispenser": {
                    "attachment": "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x2",
                    "hardpoints": [
                        "RHSUSF_cm_ANALE39",
                        "RHSUSF_cm_ANALE39_x2"
                    ],
                    "maxweight": 800,
                    "priority": 1,
                    "uiposition": [
                        0.33,
                        0
                    ]
                }
            },
            "uipicture": "rhsusf/addons/rhsusf_ch53/data/loadouts/RHS_CH53_EDEN_CA.paa"
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
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
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
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
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
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
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
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
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
    "cost": 10000000.0,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_usmc_marpat_wd_helipilot",
    "crewcrashprotection": 0.25,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "cyclicasideforcecoef": 0.5,
    "cyclicforwardforcecoef": 0.3,
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_ch53/data/ch53_1.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/ch53_1_damage.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/ch53_1_destruct.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/ch53_2.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/ch53_2_damage.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/ch53_2_destruct.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glass.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glass_damage.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glass_damage.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glassint.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glassint_damage.rvmat",
            "rhsusf/addons/rhsusf_ch53/data/glassint_damage.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00555,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "CH-53E",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "wheels"
    ],
    "driveraction": "RHS_CH53_Pilot",
    "drivercaneject": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": 0,
    "driverdoor": "",
    "driverforceoptics": 0,
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
    "driveropticsmodel": "",
    "driverrighthandanimname": "stick_pilot",
    "driverrightleganimname": "pedalR",
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
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/rhsusf_CH53E_USMC.paa",
    "editorsubcategory": "EdSubcat_Helicopters",
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
    "epeimpulsedamagecoef": 50,
    "eventhandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhsusf_eventhandlers": {
            "init": "_this call rhsusf_fnc_ch53_init"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust_1_dir",
            "effect": "ExhaustsEffectHeliBig",
            "position": "exhaust_1_pos"
        },
        "exhaust2": {
            "direction": "exhaust_2_dir",
            "effect": "ExhaustsEffectHeliBig",
            "position": "exhaust_2_pos"
        },
        "exhaust3": {
            "direction": "exhaust_3_dir",
            "effect": "ExhaustsEffectHeliBig",
            "position": "exhaust_3_pos"
        }
    },
    "expansion": 3,
    "explosionshielding": 4,
    "extcameraparams": [
        -1
    ],
    "extcameraposition": [
        0,
        5,
        -30
    ],
    "faction": "rhs_faction_usmc_wd",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 2500,
    "fuelconsumptionrate": 0.138,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "geardown": [
        "gearDownInt",
        "gearDownExt"
    ],
    "geardownext": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_gear",
        1,
        1,
        1000
    ],
    "geardownint": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_gear",
        1,
        1,
        100
    ],
    "geardowntime": 3,
    "gearminalt": 0.5,
    "gearretracting": 1,
    "gearsupfrictioncoef": 0.5,
    "gearup": [
        "gearUpInt",
        "gearUpExt"
    ],
    "gearupext": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_gear",
        1,
        1,
        1000
    ],
    "gearupint": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_gear",
        1,
        1,
        100
    ],
    "gearuptime": 3,
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 5,
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
        "camo",
        "n1",
        "n2"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_ch53/data/ch53_1_co.paa",
        "rhsusf/addons/rhsusf_decals/Data/Numbers/USMCBlackShadow/5_ca.paa",
        "rhsusf/addons/rhsusf_decals/Data/Numbers/USMCBlackShadow/5_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": 0.15,
            "convexcomponent": "avionics_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "elektronika",
            "passthrough": 1,
            "visual": "elektronika"
        },
        "hitengine": {
            "armor": 0.45,
            "convexcomponent": "engine_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "motor",
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
            "armor": 1.4,
            "convexcomponent": "fuel_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "palivo",
            "passthrough": 1,
            "visual": "palivo"
        },
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        "hitglass1": {
            "armor": 0.3,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "visual": "glass1"
        },
        "hitglass10": {
            "armor": 0.3,
            "material": -1,
            "name": "glass10",
            "passthrough": 0,
            "visual": "glass10"
        },
        "hitglass11": {
            "armor": 0.3,
            "material": -1,
            "name": "glass11",
            "passthrough": 0,
            "visual": "glass11"
        },
        "hitglass12": {
            "armor": 0.3,
            "material": -1,
            "name": "glass12",
            "passthrough": 0,
            "visual": "glass12"
        },
        "hitglass13": {
            "armor": 0.3,
            "material": -1,
            "name": "glass13",
            "passthrough": 0,
            "visual": "glass13"
        },
        "hitglass14": {
            "armor": 0.3,
            "material": -1,
            "name": "glass14",
            "passthrough": 0,
            "visual": "glass14"
        },
        "hitglass15": {
            "armor": 0.3,
            "material": -1,
            "name": "glass15",
            "passthrough": 0,
            "visual": "glass15"
        },
        "hitglass16": {
            "armor": 0.3,
            "material": -1,
            "name": "glass16",
            "passthrough": 0,
            "visual": "glass16"
        },
        "hitglass17": {
            "armor": 0.3,
            "material": -1,
            "name": "glass17",
            "passthrough": 0,
            "visual": "glass17"
        },
        "hitglass2": {
            "armor": 0.3,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.3,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.3,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 0.3,
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 0.3,
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "visual": "glass6"
        },
        "hitglass7": {
            "armor": 0.3,
            "material": -1,
            "name": "glass7",
            "passthrough": 0,
            "visual": "glass7"
        },
        "hitglass8": {
            "armor": 0.3,
            "material": -1,
            "name": "glass8",
            "passthrough": 0,
            "visual": "glass8"
        },
        "hitglass9": {
            "armor": 0.3,
            "material": -1,
            "name": "glass9",
            "passthrough": 0,
            "visual": "glass9"
        },
        "hithrotor": {
            "armor": 2.6,
            "convexcomponent": "main_rotor_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "velka vrtule",
            "passthrough": 0,
            "visual": "velka vrtule staticka"
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
            "armor": 1,
            "convexcomponent": "hull_hit",
            "explosionshielding": 1,
            "material": -1,
            "name": "NEtrup",
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
            "armor": 1.3,
            "convexcomponent": "tail_rotor_hit",
            "explosionshielding": 1,
            "material": 51,
            "name": "mala vrtule",
            "passthrough": 0,
            "visual": "mala vrtule staticka"
        },
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        "hitwinch": {
            "armor": -40,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "explo": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.06,
                    "position": "slingLoad0",
                    "simulation": "particles",
                    "type": "WinchDestructionExplo"
                },
                "sparks": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.1,
                    "position": "slingLoad0",
                    "simulation": "particles",
                    "type": "WinchDestructionSparks"
                }
            },
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
    "icon": "rhsusf/addons/rhsusf_ch53/data/ui/ch53_icon_ca.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "2 + 8 + 16",
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.2,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "landingsoundint": [
        "landingSoundInt0",
        0.5,
        "landingSoundInt1",
        0.5
    ],
    "landingsoundint0": [
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_small_int1",
        1,
        1,
        100
    ],
    "landingsoundint1": [
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_small_int2",
        1,
        1,
        100
    ],
    "landingsoundout": [
        "landingSoundOut0",
        0.5,
        "landingSoundOut1",
        0.5
    ],
    "landingsoundout0": [
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_ext1",
        1.77828,
        1,
        100
    ],
    "landingsoundout1": [
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_ext2",
        1.77828,
        1,
        100
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
    "lesh_axisoffsettarget": [
        0,
        9.8,
        0.9
    ],
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_wheeloffset": [
        0,
        -3.6
    ],
    "liftforcecoef": 1.5,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8",
    "magazines": [
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM",
        "rhsusf_mag_DIRCM"
    ],
    "mainbladecenter": "velka osa",
    "mainbladeradius": 6,
    "mainrotorspeed": 1,
    "mapsize": 40,
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
        "interiorblue": {
            "ambient": [
                0.007,
                0.099,
                0.089
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 3,
                "hardlimitstart": 2.25,
                "linear": 25,
                "quadratic": 50,
                "start": 0
            },
            "blinking": 0,
            "color": [
                0.07,
                0.99,
                0.89
            ],
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "light_interior_blue"
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
        }
    },
    "maxbackrotordive": 0,
    "maxdetectrange": 20,
    "maxfordingdepth": 1.65,
    "maxgforce": 2,
    "maximumload": 14500,
    "maxmainrotordive": 0,
    "maxomega": 2000,
    "maxsmokedamage": 0.99,
    "maxspeed": 315,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": "slingCamera",
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
    "memorypointtaskmarker": "",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 0.2,
    "mfd": {
        "rhsusf_ch53_hud_1": {
            "bones": {
                "forwardvec": {
                    "pos0": [
                        0,
                        0
                    ],
                    "pos10": [
                        0.25,
                        0.25
                    ],
                    "source": "forward",
                    "type": "vector"
                },
                "horizonbankrot": {
                    "aspectratio": 1,
                    "center": [
                        0.5,
                        0.5
                    ],
                    "max": 3.1416,
                    "maxangle": 180,
                    "min": -3.1416,
                    "minangle": -180,
                    "source": "horizonBank",
                    "type": "rotational"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm20": {
                    "angle": -20,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm25": {
                    "angle": -25,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm30": {
                    "angle": -30,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm35": {
                    "angle": -35,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm40": {
                    "angle": -40,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm45": {
                    "angle": -45,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm50": {
                    "angle": -50,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm55": {
                    "angle": -55,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm60": {
                    "angle": -60,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm65": {
                    "angle": -65,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm70": {
                    "angle": -70,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm75": {
                    "angle": -75,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm80": {
                    "angle": -80,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm85": {
                    "angle": -85,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelm90": {
                    "angle": -90,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp20": {
                    "angle": 20,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp25": {
                    "angle": 25,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp30": {
                    "angle": 30,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp35": {
                    "angle": 35,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp40": {
                    "angle": 40,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp45": {
                    "angle": 45,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp50": {
                    "angle": 50,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp55": {
                    "angle": 55,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp60": {
                    "angle": 60,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp65": {
                    "angle": 65,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp70": {
                    "angle": 70,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp75": {
                    "angle": 75,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp80": {
                    "angle": 80,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp85": {
                    "angle": 85,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "levelp90": {
                    "angle": 90,
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.78,
                        0.78
                    ],
                    "type": "horizon"
                },
                "radaraltitudebone": {
                    "max": 60,
                    "maxpos": [
                        0.965,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.965,
                        0.2
                    ],
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "type": "linear"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.65,
                        0.65
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "velocity_slip": {
                    "pos0": [
                        0.5,
                        0.845
                    ],
                    "pos10": [
                        0.53,
                        0.845
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "vspeedbone": {
                    "max": 10,
                    "maxpos": [
                        0.93,
                        0.8
                    ],
                    "min": -10,
                    "minpos": [
                        0.93,
                        0.2
                    ],
                    "source": "vspeed",
                    "sourcescale": 1,
                    "type": "linear"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "HUD_bottom_left",
            "color": [
                0.15,
                1,
                0.15,
                1
            ],
            "draw": {
                "alpha": 1,
                "altnumber": {
                    "align": "right",
                    "down": [
                        [
                            0.83,
                            0.525
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.83,
                            0.475
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.88,
                            0.475
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "type": "text"
                },
                "aslnumber": {
                    "align": "right",
                    "down": [
                        [
                            0.835,
                            0.22
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.835,
                            0.18
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.875,
                            0.18
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "type": "text"
                },
                "center_box": {
                    "points": [
                        [
                            [
                                0.45,
                                "0.02 + 0.085 - 0.06"
                            ],
                            1
                        ],
                        [
                            [
                                "0.45 + 0.10",
                                "0.02 + 0.085 - 0.06"
                            ],
                            1
                        ],
                        [
                            [
                                "0.45 + 0.10",
                                "0.02 + 0.085"
                            ],
                            1
                        ],
                        [
                            [
                                0.45,
                                "0.02 + 0.085"
                            ],
                            1
                        ],
                        [
                            [
                                0.45,
                                "0.02 + 0.085 - 0.06"
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 1.5
                },
                "collisionlightsgroup": {
                    "collisionlightstext": {
                        "align": "right",
                        "down": [
                            [
                                0.03,
                                "0.53 + 0.145"
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                "0.53 + 0.105"
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                "0.53 + 0.105"
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "A-COL",
                        "type": "text"
                    },
                    "condition": "collisionlights",
                    "type": "group"
                },
                "color": [
                    0.18,
                    1,
                    0.18
                ],
                "condition": "on",
                "fuel_number": {
                    "align": "right",
                    "down": [
                        [
                            0.92,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.92,
                            0.86
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.96,
                            0.86
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "fuel",
                    "sourcescale": 100,
                    "type": "text"
                },
                "fuel_text": {
                    "align": "right",
                    "down": [
                        [
                            0.85,
                            0.9
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.85,
                            0.86
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.89,
                            0.86
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "static",
                    "text": "Fuel",
                    "type": "text"
                },
                "geargroup": {
                    "condition": "ils",
                    "geartext": {
                        "align": "right",
                        "down": [
                            [
                                0.03,
                                "0.53 + 0.195"
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                "0.53 + 0.155"
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                "0.53 + 0.155"
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "GEAR",
                        "type": "text"
                    },
                    "type": "group"
                },
                "headingarrow": {
                    "points": [
                        [
                            [
                                "0.5",
                                "0.128 + 0.03"
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.128
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 7
                },
                "headingnumber": {
                    "align": "center",
                    "down": [
                        [
                            0.5,
                            "0.045 + 0.06"
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.5,
                            0.045
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.56,
                            0.045
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "heading",
                    "sourcescale": 1,
                    "type": "text"
                },
                "headingscale_bottom": {
                    "clipbr": [
                        "0.45 + 0.10",
                        1
                    ],
                    "cliptl": [
                        0.45,
                        "0.02 + 0.085"
                    ],
                    "heading_group": {
                        "align": "center",
                        "bottom": 0.88,
                        "center": 0.5,
                        "down": [
                            0.12,
                            "0.04 + 0.065"
                        ],
                        "horizontal": 1,
                        "linexleft": "0.03 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "pos": [
                            0.12,
                            "0.0 + 0.065"
                        ],
                        "right": [
                            0.16,
                            "0.0 + 0.065"
                        ],
                        "scale": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "step": 10,
                        "stepsize": "0.05",
                        "top": 0.12,
                        "type": "scale",
                        "width": 5
                    }
                },
                "headingscale_left": {
                    "clipbr": [
                        0.45,
                        1
                    ],
                    "cliptl": [
                        0,
                        0
                    ],
                    "heading_group": {
                        "align": "center",
                        "bottom": 0.88,
                        "center": 0.5,
                        "down": [
                            0.12,
                            "0.04 + 0.065"
                        ],
                        "horizontal": 1,
                        "linexleft": "0.03 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "pos": [
                            0.12,
                            "0.0 + 0.065"
                        ],
                        "right": [
                            0.16,
                            "0.0 + 0.065"
                        ],
                        "scale": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "step": 10,
                        "stepsize": "0.05",
                        "top": 0.12,
                        "type": "scale",
                        "width": 5
                    }
                },
                "headingscale_right": {
                    "clipbr": [
                        1,
                        1
                    ],
                    "cliptl": [
                        0.55,
                        0
                    ],
                    "heading_group": {
                        "align": "center",
                        "bottom": 0.88,
                        "center": 0.5,
                        "down": [
                            0.12,
                            "0.04 + 0.065"
                        ],
                        "horizontal": 1,
                        "linexleft": "0.03 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "pos": [
                            0.12,
                            "0.0 + 0.065"
                        ],
                        "right": [
                            0.16,
                            "0.0 + 0.065"
                        ],
                        "scale": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "step": 10,
                        "stepsize": "0.05",
                        "top": 0.12,
                        "type": "scale",
                        "width": 5
                    }
                },
                "horizonbankrot": {
                    "points": [
                        [
                            "HorizonBankRot",
                            [
                                0,
                                0.25
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                -0.01,
                                0.23
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                0.01,
                                0.23
                            ],
                            1
                        ],
                        [
                            "HorizonBankRot",
                            [
                                0,
                                0.25
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "horizont": {
                    "clipbr": [
                        0.85,
                        0.85
                    ],
                    "cliptl": [
                        0.15,
                        0.15
                    ],
                    "dimmed": {
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.42,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.08,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.42,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.08,
                                        0
                                    ],
                                    1
                                ],
                                []
                            ],
                            "type": "line"
                        },
                        "levelm10": {
                            "points": [
                                [
                                    "LevelM10",
                                    [
                                        -0.2,
                                        -0.03
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
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM10",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM10",
                                    [
                                        0.15,
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
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm20": {
                            "points": [
                                [
                                    "LevelM20",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM20",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM20",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm30": {
                            "points": [
                                [
                                    "LevelM30",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM30",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM30",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm40": {
                            "points": [
                                [
                                    "LevelM40",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM40",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM40",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelm50": {
                            "points": [
                                [
                                    "LevelM50",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM50",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM50",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp10": {
                            "points": [
                                [
                                    "LevelP10",
                                    [
                                        -0.2,
                                        0.03
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
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP10",
                                    [
                                        0.05,
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
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp20": {
                            "points": [
                                [
                                    "LevelP20",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP20",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP20",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp30": {
                            "points": [
                                [
                                    "LevelP30",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP30",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP30",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp40": {
                            "points": [
                                [
                                    "LevelP40",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP40",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP40",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "levelp50": {
                            "points": [
                                [
                                    "LevelP50",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP50",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP50",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line",
                            "width": 3
                        },
                        "valm_1_10": {
                            "align": "left",
                            "down": [
                                "LevelM10",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    -0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    -0.16,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_1_20": {
                            "align": "left",
                            "down": [
                                "LevelM20",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    -0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    -0.16,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_1_30": {
                            "align": "left",
                            "down": [
                                "LevelM30",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    -0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    -0.16,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_1_40": {
                            "align": "left",
                            "down": [
                                "LevelM40",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    -0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    -0.16,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_1_50": {
                            "align": "left",
                            "down": [
                                "LevelM50",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    -0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    -0.16,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valm_2_10": {
                            "align": "right",
                            "down": [
                                "LevelM10",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    0.26,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_2_20": {
                            "align": "right",
                            "down": [
                                "LevelM20",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    0.26,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_2_30": {
                            "align": "right",
                            "down": [
                                "LevelM30",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    0.26,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_2_40": {
                            "align": "right",
                            "down": [
                                "LevelM40",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    0.26,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_2_50": {
                            "align": "right",
                            "down": [
                                "LevelM50",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    0.21,
                                    -0.05
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    0.26,
                                    -0.05
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valp_1_10": {
                            "align": "left",
                            "down": [
                                "LevelP10",
                                [
                                    -0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    -0.16,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_1_20": {
                            "align": "left",
                            "down": [
                                "LevelP20",
                                [
                                    -0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    -0.16,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_1_30": {
                            "align": "left",
                            "down": [
                                "LevelP30",
                                [
                                    -0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    -0.16,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_1_40": {
                            "align": "left",
                            "down": [
                                "LevelP40",
                                [
                                    -0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    -0.16,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_1_50": {
                            "align": "left",
                            "down": [
                                "LevelP50",
                                [
                                    -0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    -0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    -0.16,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "50",
                            "type": "text"
                        },
                        "valp_2_10": {
                            "align": "right",
                            "down": [
                                "LevelP10",
                                [
                                    0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    0.26,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_2_20": {
                            "align": "right",
                            "down": [
                                "LevelP20",
                                [
                                    0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    0.26,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_2_30": {
                            "align": "right",
                            "down": [
                                "LevelP30",
                                [
                                    0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    0.26,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_2_40": {
                            "align": "right",
                            "down": [
                                "LevelP40",
                                [
                                    0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    0.26,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_2_50": {
                            "align": "right",
                            "down": [
                                "LevelP50",
                                [
                                    0.21,
                                    0.05
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    0.21,
                                    0
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    0.26,
                                    0
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "50",
                            "type": "text"
                        }
                    }
                },
                "lightsgroup": {
                    "condition": "lights",
                    "lightstext": {
                        "align": "right",
                        "down": [
                            [
                                0.03,
                                "0.53 + 0.095"
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.03,
                                "0.53 + 0.055"
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.07,
                                "0.53 + 0.055"
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "LIGHTS",
                        "type": "text"
                    },
                    "type": "group"
                },
                "radaraltitudeband": {
                    "clipbr": [
                        1,
                        0.8
                    ],
                    "cliptl": [
                        0,
                        0.2
                    ],
                    "radarbanda": {
                        "points": [
                            [
                                "RadarAltitudeBone",
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [
                                "RadarAltitudeBone",
                                [
                                    0,
                                    0.6
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 17
                    }
                },
                "slip_ball_group": {
                    "slip_ball": {
                        "points": [
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.75",
                                    "-0.02 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.75",
                                    "-0.01732 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.75",
                                    "-0.0099999998 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.75",
                                    "0 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.75",
                                    "0.0099999998 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.75",
                                    "0.01732 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.75",
                                    "0.02 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.75",
                                    "0.01732 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.75",
                                    "0.0099999998 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.75",
                                    "0 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.75",
                                    "-0.0099999998 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.75",
                                    "-0.01732 * 0.75"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.75",
                                    "-0.02 * 0.75"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.6",
                                    "-0.02 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.6",
                                    "-0.01732 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.6",
                                    "-0.0099999998 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.6",
                                    "0 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.6",
                                    "0.0099999998 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.6",
                                    "0.01732 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.6",
                                    "0.02 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.6",
                                    "0.01732 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.6",
                                    "0.0099999998 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.6",
                                    "0 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.6",
                                    "-0.0099999998 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.6",
                                    "-0.01732 * 0.6"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.6",
                                    "-0.02 * 0.6"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.5",
                                    "-0.02 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.5",
                                    "-0.01732 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.5",
                                    "-0.0099999998 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.5",
                                    "0 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.5",
                                    "0.0099999998 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.5",
                                    "0.01732 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.5",
                                    "0.02 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.5",
                                    "0.01732 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.5",
                                    "0.0099999998 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.5",
                                    "0 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.5",
                                    "-0.0099999998 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.5",
                                    "-0.01732 * 0.5"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.5",
                                    "-0.02 * 0.5"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.4",
                                    "-0.02 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.4",
                                    "-0.01732 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.4",
                                    "-0.0099999998 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.4",
                                    "0 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.4",
                                    "0.0099999998 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.4",
                                    "0.01732 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.4",
                                    "0.02 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.4",
                                    "0.01732 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.4",
                                    "0.0099999998 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.4",
                                    "0 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.4",
                                    "-0.0099999998 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.4",
                                    "-0.01732 * 0.4"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.4",
                                    "-0.02 * 0.4"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.30",
                                    "-0.02 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.30",
                                    "-0.01732 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.30",
                                    "-0.0099999998 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.30",
                                    "0 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.30",
                                    "0.0099999998 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.30",
                                    "0.01732 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.30",
                                    "0.02 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.30",
                                    "0.01732 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.30",
                                    "0.0099999998 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.30",
                                    "0 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.30",
                                    "-0.0099999998 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.30",
                                    "-0.01732 * 0.30"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.30",
                                    "-0.02 * 0.30"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.20",
                                    "-0.02 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.20",
                                    "-0.01732 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.20",
                                    "-0.0099999998 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.20",
                                    "0 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.20",
                                    "0.0099999998 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.20",
                                    "0.01732 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.20",
                                    "0.02 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.20",
                                    "0.01732 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.20",
                                    "0.0099999998 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.20",
                                    "0 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.20",
                                    "-0.0099999998 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.20",
                                    "-0.01732 * 0.20"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.20",
                                    "-0.02 * 0.20"
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.1",
                                    "-0.02 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.1",
                                    "-0.01732 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.1",
                                    "-0.0099999998 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.02 * 0.1",
                                    "0 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.01732 * 0.1",
                                    "0.0099999998 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0.0099999998 * 0.1",
                                    "0.01732 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.1",
                                    "0.02 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.1",
                                    "0.01732 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.1",
                                    "0.0099999998 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.02 * 0.1",
                                    "0 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.01732 * 0.1",
                                    "-0.0099999998 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "-0.0099999998 * 0.1",
                                    "-0.01732 * 0.1"
                                ],
                                1
                            ],
                            [
                                "Velocity_slip",
                                1,
                                [
                                    "0 * 0.1",
                                    "-0.02 * 0.1"
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 6
                    },
                    "slip_bars": {
                        "points": [
                            [
                                [
                                    "0.5-0.018",
                                    "0.9-0.04"
                                ],
                                1
                            ],
                            [
                                [
                                    "0.5-0.018",
                                    "0.9-0.075"
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    "0.5+0.018",
                                    "0.9-0.04"
                                ],
                                1
                            ],
                            [
                                [
                                    "0.5+0.018",
                                    "0.9-0.075"
                                ],
                                1
                            ],
                            [],
                            [
                                [
                                    "0.5+0.2",
                                    "0.9-0.04"
                                ],
                                1
                            ],
                            [
                                [
                                    "0.5-0.2",
                                    "0.9-0.04"
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    }
                },
                "speednumber": {
                    "align": "right",
                    "down": [
                        [
                            0.03,
                            0.525
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.03,
                            0.475
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.08,
                            0.475
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                },
                "staticbank": {
                    "points": [
                        [
                            [
                                0.4782,
                                0.251
                            ],
                            1
                        ],
                        [
                            [
                                0.4773,
                                0.241
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4566,
                                0.2538
                            ],
                            1
                        ],
                        [
                            [
                                0.4549,
                                0.2439
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4353,
                                0.2585
                            ],
                            1
                        ],
                        [
                            [
                                0.4301,
                                0.2392
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.4145,
                                0.2651
                            ],
                            1
                        ],
                        [
                            [
                                0.4111,
                                0.2557
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3943,
                                0.2734
                            ],
                            1
                        ],
                        [
                            [
                                0.3901,
                                0.2644
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.375,
                                0.2835
                            ],
                            1
                        ],
                        [
                            [
                                0.365,
                                0.2662
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.3232,
                                0.3232
                            ],
                            1
                        ],
                        [
                            [
                                0.3091,
                                0.3091
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.2835,
                                0.375
                            ],
                            1
                        ],
                        [
                            [
                                0.2662,
                                0.365
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.4782)",
                                0.251
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.4773)",
                                0.241
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.4566)",
                                0.2538
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.4549)",
                                0.2439
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.4353)",
                                0.2585
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.4301)",
                                0.2392
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.4145)",
                                0.2651
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.4111)",
                                0.2557
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.3943)",
                                0.2734
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.3901)",
                                0.2644
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.3750)",
                                0.2835
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.3650)",
                                0.2662
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.3232)",
                                0.3232
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.3091)",
                                0.3091
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                "0.5 + (0.5- 0.2835)",
                                0.375
                            ],
                            1
                        ],
                        [
                            [
                                "0.5 + (0.5- 0.2662)",
                                0.365
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.5,
                                "0.5 - 0.25"
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                "0.5 - 0.28"
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 3
                },
                "torquenumber": {
                    "condition": "simulRTD",
                    "torque_number": {
                        "align": "left",
                        "down": [
                            [
                                0.065,
                                0.225
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.065,
                                0.175
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.115,
                                0.175
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "rtdRotorTorque",
                        "sourcescale": 488,
                        "type": "text"
                    },
                    "torquetext": {
                        "align": "right",
                        "down": [
                            [
                                0.07,
                                0.225
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.07,
                                0.175
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.12,
                                0.175
                            ],
                            1
                        ],
                        "scale": 1,
                        "source": "static",
                        "text": "%",
                        "type": "text"
                    }
                },
                "vspeedband": {
                    "points": [
                        [
                            "VspeedBone",
                            [
                                -0.01,
                                0
                            ],
                            1
                        ],
                        [
                            "VspeedBone",
                            [
                                -0.025,
                                -0.015
                            ],
                            1
                        ],
                        [
                            "VspeedBone",
                            [
                                -0.025,
                                0.015
                            ],
                            1
                        ],
                        [
                            "VspeedBone",
                            [
                                -0.01,
                                0
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line",
                    "width": 3
                },
                "vspeedscaleposta": {
                    "points": [
                        [
                            [
                                0.98,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                1,
                                0.2
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.93,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.2
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.98,
                                0.35
                            ],
                            1
                        ],
                        [
                            [
                                1,
                                0.35
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.93,
                                0.35
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.35
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.38
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.38
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.41
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.41
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.44
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.44
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.47
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.47
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.98,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                1,
                                0.5
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.93,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.5
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.53
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.53
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.56
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.56
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.59
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.59
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.94,
                                0.62
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.62
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.98,
                                0.65
                            ],
                            1
                        ],
                        [
                            [
                                1,
                                0.65
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.93,
                                0.65
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.65
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.99,
                                0.68
                            ],
                            1
                        ],
                        [
                            [
                                0.98,
                                0.68
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.99,
                                0.71
                            ],
                            1
                        ],
                        [
                            [
                                0.98,
                                0.71
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.99,
                                0.74
                            ],
                            1
                        ],
                        [
                            [
                                0.98,
                                0.74
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.99,
                                0.77
                            ],
                            1
                        ],
                        [
                            [
                                0.98,
                                0.77
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.98,
                                0.8
                            ],
                            1
                        ],
                        [
                            [
                                1,
                                0.8
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.93,
                                0.8
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.8
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line",
                    "width": 5
                },
                "waterline": {
                    "points": [
                        [
                            [
                                0.45,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.48,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.49,
                                0.525
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.51,
                                0.525
                            ],
                            1
                        ],
                        [
                            [
                                0.52,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.55,
                                0.5
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 7
                }
            },
            "enableparallax": 0,
            "helmetdown": [
                0,
                -0.08,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.04,
                0.04,
                0.1
            ],
            "helmetright": [
                0.08,
                0,
                0
            ],
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right"
        },
        "rhsusf_ch53_hud_2": {
            "bones": {
                "forwardvec": {
                    "pos0": [
                        0,
                        0
                    ],
                    "pos10": [
                        0.253,
                        0.253
                    ],
                    "source": "forward",
                    "type": "vector"
                },
                "forwardvec1": {
                    "pos0": [
                        0,
                        0
                    ],
                    "pos10": [
                        0.25,
                        0.25
                    ],
                    "source": "forward",
                    "type": "vector"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.5
                    ],
                    "pos10": [
                        0.75,
                        0.75
                    ],
                    "source": "velocity",
                    "type": "vector"
                }
            },
            "borderbottom": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "bottomleft": "HUD_bottom_left",
            "color": [
                0.15,
                1,
                0.15,
                1
            ],
            "draw": {
                "ac_centerline": {
                    "ac_cross": {
                        "points": [
                            [
                                "ForwardVec",
                                1,
                                [
                                    " -0.006 + 0.5",
                                    "0 + 0.5"
                                ],
                                1
                            ],
                            [
                                "ForwardVec",
                                1,
                                [
                                    " 0.006 + 0.5",
                                    "0 + 0.5"
                                ],
                                1
                            ],
                            [],
                            [
                                "ForwardVec",
                                1,
                                [
                                    " -0.0 + 0.5",
                                    "0.006 + 0.5"
                                ],
                                1
                            ],
                            [
                                "ForwardVec",
                                1,
                                [
                                    " 0.0 + 0.5",
                                    "-0.006 + 0.5"
                                ],
                                1
                            ]
                        ],
                        "type": "line",
                        "width": 4
                    },
                    "condition": "on",
                    "type": "group"
                },
                "alpha": 1,
                "color": [
                    0.18,
                    1,
                    0.18
                ],
                "condition": "on",
                "planemovementcrosshair": {
                    "points": [
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0,
                                -0.02
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.01,
                                -0.01732
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.01732,
                                -0.01
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.02,
                                0
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.01732,
                                0.01
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.01,
                                0.01732
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0,
                                0.02
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.01,
                                0.01732
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.01732,
                                0.01
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.02,
                                0
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.01732,
                                -0.01
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.01,
                                -0.01732
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0,
                                -0.02
                            ],
                            1
                        ],
                        [],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.04,
                                0
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0.02,
                                0
                            ],
                            1
                        ],
                        [],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.04,
                                0
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                -0.02,
                                0
                            ],
                            1
                        ],
                        [],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0,
                                -0.04
                            ],
                            1
                        ],
                        [
                            "ForwardVec1",
                            1,
                            "Velocity",
                            1,
                            [
                                0,
                                -0.02
                            ],
                            1
                        ]
                    ],
                    "type": "line",
                    "width": 7
                }
            },
            "enableparallax": 0,
            "helmetdown": [
                0,
                -0.07,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.035,
                0.035,
                0.1
            ],
            "helmetright": [
                0.07,
                0,
                0
            ],
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right"
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
    "minbackrotordive": 0,
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minmainrotordive": 0,
    "minsmokedamage": 0.3,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsusf/addons/rhsusf_ch53/rhsusf_ch53_e.p3d",
    "namesound": "veh_air_helicopter_s",
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
    "occludesoundswhenin": 0.562341,
    "outsidesoundfilter": 1,
    "picture": "rhsusf/addons/rhsusf_ch53/data/ui/ch53_picture_ca.paa",
    "pilotcamera": {
        "controllable": 0,
        "initelev": 80,
        "initturn": 0,
        "maxelev": 80,
        "maxturn": 0,
        "maxxrotspeed": 0.5,
        "maxyrotspeed": 0.5,
        "minelev": 80,
        "minturn": 0,
        "opticsin": {
            "showminimapinoptics": 0,
            "showslingloadmanagerinoptics": 1,
            "showuavviewpinoptics": 0,
            "wide": {
                "directionstabilized": 1,
                "gunneropticsmodel": "A3/drones_f/Weapons_F_Gamma/Reticle/UAV_Optics_Gunner_wide_F.p3d",
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.5,
                "maxanglex": 0,
                "maxangley": 0,
                "maxfov": 0.5,
                "minanglex": 0,
                "minangley": 0,
                "minfov": 0.5,
                "opticsdisplayname": "W",
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
        "pilotopticsshowcursor": 1
    },
    "pilotspec": {
        "showheadphones": 1
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 100,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.12,
    "radartype": 4,
    "reflectors": {
        "left": {
            "ambient": [
                100,
                100,
                100,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "LandLeftDir",
            "flaremaxdistance": 300,
            "flaresize": 8,
            "hitpoint": "LandLeft",
            "innerangle": 5,
            "intensity": 50,
            "outerangle": 75,
            "position": "LandLeft",
            "selection": "LandLeft",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                100,
                100,
                100,
                0
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "LandRightDir",
            "flaremaxdistance": 300,
            "flaresize": 8,
            "hitpoint": "LandRight",
            "innerangle": 5,
            "intensity": 50,
            "outerangle": 75,
            "position": "LandRight",
            "selection": "LandRight",
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
        "['Number', cCH53NumberPlaces, _typeNum,_randomNum]"
    ],
    "rhs_gearanim": "Gear_Nose_1",
    "rhs_hasnoradar": 1,
    "rhs_paraoff": -15,
    "rhs_pararamp": "ramp",
    "rhs_parascript": "rhs_fnc_vehPara",
    "rhs_rampanim": "ramp_bottom",
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
    "rotordamage": [
        "rotorDamageInt",
        "rotorDamageOut"
    ],
    "rotordamageint": [
        "A3/Sounds_F/vehicles/air/noises/Heli_damage_rotor_int_1",
        1,
        1
    ],
    "rotordamageout": [
        "A3/Sounds_F/vehicles/air/noises/Heli_damage_rotor_ext_1",
        2.51189,
        1,
        300
    ],
    "rotorlibhelicopterproperties": {
        "autohovercorrection": [
            4.7,
            3.8,
            0
        ],
        "defaultcollective": 0.665,
        "hasapu": 0,
        "horizontalwingsanglecollmax": 0,
        "horizontalwingsanglecollmin": 0,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxmainrotorstress": 570000,
        "maxtailrotorstress": 120000,
        "maxtorque": 4900,
        "maxverticalstabilizerstress": 10000,
        "retreatbladestallwarningspeed": 87.4556,
        "rtd_center": "rtd_center",
        "rtdconfig": "rhsusf/addons/rhsusf_c_ch53/RTD_CH53E2.xml",
        "stressdamagepersec": 0.00333333,
        "vrsshakepowercoef": 1
    },
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionhrotormove": "velka vrtule blur",
    "selectionhrotorstill": "velka vrtule staticka",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionshowdamage": "poskozeni",
    "selectionvrotormove": "mala vrtule blur",
    "selectionvrotorstill": "mala vrtule staticka",
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
    "side": 1,
    "simulation": "helicopterrtd",
    "slingcargoattach": [
        "slingCargoAttach0",
        "slingCargoAttach1"
    ],
    "slingcargoattach0": [
        "A3/Sounds_F/vehicles/air/noises/SL_engineDownEndINT",
        1,
        1
    ],
    "slingcargoattach1": [
        "A3/Sounds_F/vehicles/air/noises/SL_1hookLock",
        1,
        1,
        80
    ],
    "slingcargodetach": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargodetach0": [
        "A3/Sounds_F/vehicles/air/noises/SL_engineUpEndINT",
        1,
        1
    ],
    "slingcargodetach1": [
        "A3/Sounds_F/vehicles/air/noises/SL_1hookUnlock",
        1,
        1,
        80
    ],
    "slingcargodetachair": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargodetachair0": [
        "A3/Sounds_F/vehicles/air/noises/SL_unhook_air_int",
        1,
        1
    ],
    "slingcargodetachair1": [
        "A3/Sounds_F/vehicles/air/noises/SL_unhook_air_ext",
        1,
        1,
        80
    ],
    "slingcargoropebreak": [
        "slingCargoDetach0",
        "slingCargoDetach1"
    ],
    "slingcargoropebreak0": [
        "A3/Sounds_F/vehicles/air/noises/SL_rope_break_int",
        1,
        1
    ],
    "slingcargoropebreak1": [
        "A3/Sounds_F/vehicles/air/noises/SL_rope_break_ext",
        1,
        1,
        80
    ],
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slingloadmaxcargomass": 14000,
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmincargomass": 0,
    "slowspeedforwardcoef": 0.3,
    "soundarmorcrash": [
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "soundburning": {},
    "soundbushcollision1": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_bush_int_1",
        1,
        1,
        100
    ],
    "soundbushcollision2": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_bush_int_2",
        1,
        1,
        100
    ],
    "soundbushcollision3": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_bush_int_3",
        1,
        1,
        100
    ],
    "soundbushcrash": [
        "soundBushCollision1",
        0.33,
        "soundBushCollision2",
        0.33,
        "soundBushCollision3",
        0.33
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
        0.33
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "/rhsusf/addons/rhsusf_ch53/data/betty/dws_warning_beeps",
        10,
        1,
        20
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
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_ext_stop",
        2,
        1,
        800
    ],
    "soundengineoffint": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_int_stop",
        2,
        1
    ],
    "soundengineonext": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_ext_start",
        2,
        1,
        800
    ],
    "soundengineonint": [
        "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_int_start",
        2,
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
    "soundgeneralcollision1": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_default_int_1",
        1,
        1,
        100
    ],
    "soundgeneralcollision2": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_default_int_2",
        1,
        1,
        100
    ],
    "soundgeneralcollision3": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_default_int_3",
        1,
        1,
        100
    ],
    "soundgetin": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_02/open",
        1,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_02/close",
        1,
        1,
        50
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/weapons/Rockets/locked_3",
        1,
        1.5
    ],
    "soundinjured": {},
    "soundlandcrash": [
        "",
        1,
        1
    ],
    "soundlandcrashes": [
        "emptySound",
        0
    ],
    "soundlandinggear": [
        "",
        1,
        1
    ],
    "soundlocked": [
        "/A3/Sounds_F/weapons/Rockets/locked_1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "damagealarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_alarm_bluefor",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        "damagealarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_alarm_bluefor",
                0.316228,
                1
            ],
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        "engineext": {
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
            "sound": [
                "A3/Sounds_F/dummysound",
                1.41254,
                1,
                800
            ],
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        "engineint": {
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
            "sound": [
                "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_int_engine",
                1,
                1
            ],
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        "gstress": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/vehicle_stress2d",
                1.12202,
                1,
                50
            ],
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        },
        "rainext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_ext",
                1,
                1,
                100
            ],
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        "rainint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/rain1_int",
                1,
                1,
                100
            ],
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        "rotorext": {
            "cone": [
                1.6,
                3.14,
                1.6,
                0.95
            ],
            "frequency": "rotorSpeed / (1-rotorThrust/5)*0.8",
            "sound": [
                "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_ext_rotor",
                1,
                1,
                3500
            ],
            "volume": "camPos*((rotorSpeed-0.72)*6)"
        },
        "rotorint": {
            "frequency": "rotorSpeed * (1-rotorThrust/5) * 1.2",
            "sound": [
                "A3/Sounds_F/dummysound",
                0.501187,
                1
            ],
            "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)*0.9"
        },
        "rotorlowalarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_alarm_rotor_low",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        "rotorlowalarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_alarm_rotor_low",
                0.316228,
                1
            ],
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        "rotornoiseext": {
            "cone": [
                0.7,
                1.3,
                1,
                0
            ],
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/dummysound",
                1,
                1,
                400
            ],
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
        },
        "scrubbuildingext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/dummysound",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        "scrubbuildingint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wheelsInt",
                1,
                1,
                100
            ],
            "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        "scrublandext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/dummysound",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        "scrublandint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wheelsInt",
                1,
                1,
                100
            ],
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        "scrubtreeext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                1,
                1,
                100
            ],
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        "scrubtreeint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubTreeInt",
                1,
                1,
                100
            ],
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        "slingloaddownext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineDownEXT",
                1,
                1,
                500
            ],
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        "slingloaddownint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineDownINT",
                1,
                1,
                500
            ],
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        "slingloadupext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineUpEXT",
                1,
                1,
                500
            ],
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        "slingloadupint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/SL_engineUpINT",
                1,
                1,
                500
            ],
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        "speedstress": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/vehicle_stress3",
                1,
                1,
                50
            ],
            "volume": "(1-camPos)*(speed factor[40,80])"
        },
        "transmissiondamageext_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_ext_1",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageext_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_ext_2",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_int_1",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_int_2",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "windint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/dummysound",
                0.707946,
                1,
                50
            ],
            "volume": "(1-camPos)*(speed factor[5, 60])*(speed factor[5, 60])"
        }
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundsext": {
        "soundevents": {},
        "sounds": {
            "damagealarmext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_alarm_bluefor",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            "damagealarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_alarm_bluefor",
                    0.316228,
                    1
                ],
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            "engineext": {
                "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
                "sound": [
                    "A3/Sounds_F/dummysound",
                    1.41254,
                    1,
                    800
                ],
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            "engineint": {
                "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
                "sound": [
                    "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_int_engine",
                    1,
                    1
                ],
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            "gstress": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/vehicle_stress2d",
                    1.12202,
                    1,
                    50
                ],
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            "rainext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/rain1_ext",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            "rainint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/rain1_int",
                    1,
                    1,
                    100
                ],
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            "rotorext": {
                "cone": [
                    1.6,
                    3.14,
                    1.6,
                    0.95
                ],
                "frequency": "rotorSpeed / (1-rotorThrust/5)*0.8",
                "sound": [
                    "rhsusf/addons/rhsusf_ch53/sounds/Heli_CH53_01_ext_rotor",
                    1,
                    1,
                    3500
                ],
                "volume": "camPos*((rotorSpeed-0.72)*6)"
            },
            "rotorint": {
                "frequency": "rotorSpeed * (1-rotorThrust/5) * 1.2",
                "sound": [
                    "A3/Sounds_F/dummysound",
                    0.501187,
                    1
                ],
                "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)*0.9"
            },
            "rotorlowalarmext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_alarm_rotor_low",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            "rotorlowalarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_alarm_rotor_low",
                    0.316228,
                    1
                ],
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            "rotornoiseext": {
                "cone": [
                    0.7,
                    1.3,
                    1,
                    0
                ],
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/dummysound",
                    1,
                    1,
                    400
                ],
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
            },
            "scrubbuildingext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/dummysound",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            "scrubbuildingint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wheelsInt",
                    1,
                    1,
                    100
                ],
                "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            "scrublandext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/dummysound",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            "scrublandint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wheelsInt",
                    1,
                    1,
                    100
                ],
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            "scrubtreeext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            "scrubtreeint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubTreeInt",
                    1,
                    1,
                    100
                ],
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            "slingloaddownext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineDownEXT",
                    1,
                    1,
                    500
                ],
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            "slingloaddownint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineDownINT",
                    1,
                    1,
                    500
                ],
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            "slingloadupext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineUpEXT",
                    1,
                    1,
                    500
                ],
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            "slingloadupint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/SL_engineUpINT",
                    1,
                    1,
                    500
                ],
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            "speedstress": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/vehicle_stress3",
                    1,
                    1,
                    50
                ],
                "volume": "(1-camPos)*(speed factor[40,80])"
            },
            "transmissiondamageext_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_ext_1",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageext_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_ext_2",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_int_1",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/Heli_damage_transmission_int_2",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "windint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/dummysound",
                    0.707946,
                    1,
                    50
                ],
                "volume": "(1-camPos)*(speed factor[5, 60])*(speed factor[5, 60])"
            }
        }
    },
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
    "soundwatercollision1": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_water_ext_1",
        1,
        1,
        100
    ],
    "soundwatercollision2": [
        "A3/Sounds_F/vehicles/crashes/Helis/Heli_coll_water_ext_2",
        1,
        1,
        100
    ],
    "soundwatercrash": [
        "",
        0.177828,
        1
    ],
    "soundwatercrashes": [
        "soundWaterCollision1",
        0.5,
        "soundWaterCollision2",
        0.5
    ],
    "soundwoodcrash": [
        "soundGeneralCollision1",
        1,
        "soundGeneralCollision2",
        1,
        "soundGeneralCollision3",
        1
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_air_helicopter_p"
            ],
            "speechsingular": [
                "veh_air_helicopter_s"
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
    "startduration": 20,
    "steeraheadplan": 0.7,
    "steeraheadsimul": 0.5,
    "supplyradius": -1,
    "tailbladecenter": "mala osa",
    "tailbladeradius": 1,
    "tailbladevertical": 1,
    "taildamage": [
        "tailDamageInt",
        "tailDamageOut"
    ],
    "taildamageint": [
        "A3/Sounds_F/vehicles/air/noises/Heli_damage_tail",
        1,
        1
    ],
    "taildamageout": [
        "A3/Sounds_F/vehicles/air/noises/Heli_damage_tail",
        1,
        1,
        300
    ],
    "tbody": 150,
    "textplural": "helicopters",
    "textsingular": "helicopter",
    "texturelist": [],
    "texturesources": {
        "standard": {
            "displayname": "Standard",
            "factions": [
                "rhs_faction_usmc_wd",
                "rhs_faction_usmc_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_ch53/data/ch53_1_co.paa"
            ]
        }
    },
    "threat": [
        0.3,
        0.2,
        0.3
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {},
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
        },
        "_xx_toolkit": {
            "count": 1,
            "name": "Toolkit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 24,
    "transportmaxmagazines": 48,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 24,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {
        "copilotturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "ObsTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "ObsGun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "ObsTurret",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
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
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                4000,
                                8000,
                                16000,
                                25000
                            ],
                            "resource": "RscCustomInfoSensors"
                        },
                        "vehiclegunnerdisplay": {
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
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [
                                4000,
                                8000,
                                16000,
                                25000
                            ],
                            "resource": "RscCustomInfoSensors"
                        },
                        "vehiclegunnerdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "PrimaryGunner"
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
            "enablemanualfire": 1,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "ObsGun",
            "gunbeg": "flir_end",
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
            "gunend": "flir_begin",
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
            "gunneraction": "RHS_CH53_Pilot",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnerforceoutoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerhasflares": 0,
            "gunnerinaction": "RHS_CH53_Pilot",
            "gunnerlefthandanimname": "lever_copilot",
            "gunnerleftleganimname": "pedalL",
            "gunnername": "Copilot",
            "gunneropticscolor": [
                0.227,
                0.769,
                0.24,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "",
            "gunneropticsshowcursor": 1,
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
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerrightleganimname": "pedalR",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "passthrough": 0.1,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "passthrough": 0.3,
                    "visual": "vez"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 1,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_LaserMag_ai"
            ],
            "maxcamelev": 90,
            "maxelev": 38.2,
            "maxhorizontalrotspeed": 3.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 70,
            "maxverticalrotspeed": 3.2,
            "memorypointgun": "flir_end",
            "memorypointgunneroptics": "commanderview",
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
            "minelev": -90,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -70,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "medium": {
                    "directionstabilized": 1,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.1,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 0.1,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 0.1,
                    "opticsdisplayname": "M",
                    "stabilizedinaxes": 3,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "narrow": {
                    "directionstabilized": 1,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.02,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 0.02,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 0.02,
                    "opticsdisplayname": "N",
                    "stabilizedinaxes": 3,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "narrower": {
                    "directionstabilized": 1,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.01,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 0.01,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 0.01,
                    "opticsdisplayname": "N",
                    "stabilizedinaxes": 3,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "wide": {
                    "directionstabilized": 1,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.466,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 0.466,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 0.466,
                    "opticsdisplayname": "W",
                    "stabilizedinaxes": 3,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "widel": {
                    "directionstabilized": 1,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_m_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.2,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 0.2,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 0.2,
                    "opticsdisplayname": "WL",
                    "stabilizedinaxes": 3,
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                },
                "widengs": {
                    "directionstabilized": 0,
                    "gunneropticscolor": [
                        1,
                        0,
                        0,
                        0
                    ],
                    "gunneropticsmodel": "a3/weapons_f/Reticle/Optics_Gunner_AAA_01_w_F.p3d",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 1,
                    "maxanglex": 20,
                    "maxangley": 100,
                    "maxfov": 1,
                    "minanglex": -80,
                    "minangley": -100,
                    "minfov": 1,
                    "opticsdisplayname": "W",
                    "thermalmode": [
                        0,
                        1
                    ],
                    "visionmode": [
                        "Normal",
                        "Ti"
                    ]
                }
            },
            "opticsout": {
                "monocular": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 1.1,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.133,
                    "visionmode": [
                        "Normal",
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 1,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 2.5,
                        "hardlimitstart": 2,
                        "linear": 1,
                        "quadratic": 50,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        830,
                        100,
                        100
                    ],
                    "conefadecoef": 1,
                    "daylight": 1,
                    "direction": "cabin_light_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cabin_light",
                    "innerangle": 90,
                    "intensity": 9,
                    "outerangle": 165,
                    "position": "cabin_light",
                    "selection": "cabin_light",
                    "size": 1,
                    "useflare": 1
                },
                "cargo_light_1": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 3,
                        "hardlimitstart": 2,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        830,
                        100,
                        100
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_1_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_1",
                    "innerangle": 90,
                    "intensity": 21,
                    "outerangle": 165,
                    "position": "cargo_light_1",
                    "selection": "cargo_light_1",
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
                        "hardlimitend": 3,
                        "hardlimitstart": 2,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        830,
                        100,
                        100
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_2_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_2",
                    "innerangle": 90,
                    "intensity": 21,
                    "outerangle": 165,
                    "position": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "size": 1,
                    "useflare": 0
                },
                "cargo_light_3": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 3,
                        "hardlimitstart": 2,
                        "linear": 1,
                        "quadratic": 70,
                        "start": 0
                    },
                    "blinking": 0,
                    "color": [
                        830,
                        100,
                        100
                    ],
                    "conefadecoef": 0.1,
                    "daylight": 1,
                    "direction": "cargo_light_3_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_3",
                    "innerangle": 90,
                    "intensity": 21,
                    "outerangle": 165,
                    "position": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "size": 1,
                    "useflare": 0
                }
            },
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showgunneroptics": 1,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "",
                0.01,
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
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "RHS_RscUH1Y_Observer",
            "turrets": {},
            "turretspec": {
                "showheadphones": 1
            },
            "usepip": 1,
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
            "weapons": [
                "rhs_weap_laserDesignator_AI"
            ]
        },
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
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -1,
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
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
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "passthrough": 0.1,
                    "visual": "zbran"
                },
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "passthrough": 0.3,
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
            "maxelev": 20,
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
                "showheadphones": 1
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
    "type": 2,
    "typicalcargo": [
        "rhsusf_usmc_marpat_wd_helicrew"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHSUSF_RscUnitInfoAir",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigital",
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "basketdeploy": {
            "condition": "alive this and (driver this == player or gunner this == player) and (this getVariable ['rhs_basket_deployed', 0]) isEqualTo 0",
            "displayname": "<t color='#cbb8b4'>Deploy Basket</t>",
            "onlyforplayer": 0,
            "position": "ramp action",
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this spawn RHSUSF_fnc_basket_deploy;"
        },
        "basketlower": {
            "condition": "alive this and (driver this == player or gunner this == player) and (this getVariable ['rhs_basket_deployed', 0]) isEqualTo 1",
            "displayname": "<t color='#cbb8b4'>Lower Basket</t>",
            "onlyforplayer": 0,
            "position": "ramp action",
            "priority": 5,
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this spawn RHSUSF_fnc_basket_lower;"
        },
        "basketraise": {
            "condition": "alive this and (driver this == player or gunner this == player) and (this getVariable ['rhs_basket_deployed', 0]) isEqualTo 1",
            "displayname": "<t color='#cbb8b4'>Raise Basket</t>",
            "onlyforplayer": 0,
            "position": "ramp action",
            "priority": 5,
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this spawn RHSUSF_fnc_basket_raise;"
        },
        "basketrecover": {
            "condition": "alive this and (driver this == player or gunner this == player) and (this getVariable ['rhs_basket_deployed', 0]) isEqualTo 1",
            "displayname": "<t color='#cbb8b4'>Recover Basket</t>",
            "onlyforplayer": 0,
            "position": "ramp action",
            "priority": 4,
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this spawn RHSUSF_fnc_basket_recover;"
        },
        "pack": {
            "condition": "(!isEngineOn this) AND {(this doorPhase 'mainRotor_folded' isEqualTo 0) AND ((driver this) isEqualTo (call rhs_fnc_findPlayer)) AND (speed this == 0)}",
            "displayname": "Pack",
            "displaynamedefault": "Pack",
            "onlyforplayer": 1,
            "position": "PackAction",
            "radius": 10,
            "statement": "[this,1] call rhsusf_fnc_ch53_fold"
        },
        "rampclose": {
            "condition": "this animationPhase 'ramp_bottom' >= 0.56 && ((driver this) isEqualTo (call rhs_fnc_findPlayer));",
            "displayname": "Close Ramp",
            "onlyforplayer": 0,
            "position": "ramp action",
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animate ['ramp_bottom',0];this animate ['ramp_top',0];[this] call rhs_fnc_cargoAttach"
        },
        "ramplevel": {
            "condition": "this animationPhase 'ramp_bottom' != 0.56 && ((driver this) isEqualTo (call rhs_fnc_findPlayer));",
            "displayname": "Level Ramp",
            "onlyforplayer": 0,
            "position": "ramp action",
            "radius": 5,
            "shortcut": "user13",
            "showwindow": 0,
            "statement": "this animate ['ramp_bottom',0.56];this animate ['ramp_top',1];"
        },
        "rampopen": {
            "condition": "this animationPhase 'ramp_bottom' <= 0.56 && ((driver this) isEqualTo (call rhs_fnc_findPlayer));",
            "displayname": "Open Ramp",
            "onlyforplayer": 0,
            "position": "ramp action",
            "radius": 5,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animate ['ramp_bottom',1];this animate ['ramp_top',1];{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects this"
        },
        "togglelight": {
            "condition": "player in this;",
            "displayname": "Toggle interior light",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight"
        },
        "unpack": {
            "condition": "(this doorPhase 'mainRotor_folded' isEqualTo 1) AND ((driver this) isEqualTo (call rhs_fnc_findPlayer))",
            "displayname": "UnPack",
            "displaynamedefault": "Unpack",
            "onlyforplayer": 1,
            "position": "PackAction",
            "radius": 10,
            "statement": "[this,0] call rhsusf_fnc_ch53_fold"
        },
        "vehicleparadrop": {
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "displayname": "Paradrop cargo",
            "onlyforplayer": 0,
            "position": "ramp action",
            "radius": 5,
            "shortcut": "",
            "showwindow": 0,
            "statement": "[this] spawn rhs_fnc_vehPara"
        }
    },
    "vehicleclass": "rhs_vehclass_helicopter",
    "vehicletransport": {
        "carrier": {
            "cargoalignment": [
                "front",
                "center"
            ],
            "cargobaydimensions": [
                "VTV_limit_1",
                "VTV_limit_2"
            ],
            "cargospacing": [
                0.075,
                0.075,
                0.075
            ],
            "disableheightlimit": 1,
            "exits": [
                "VTV_exit_1"
            ],
            "loadingangle": 60,
            "loadingdistance": 15,
            "maxloadmass": 9000,
            "parachuteclassdefault": "B_Parachute_02_F",
            "parachuteheightlimitdefault": 25,
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
        "initfov": 0.5,
        "maxanglex": 17,
        "maxangley": 100,
        "maxfov": 1.2,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -40,
        "minangley": -100,
        "minfov": 0.3,
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
    "visualtarget": 1,
    "visualtargetsize": 1.3,
    "washdowndiameter": "40.0f",
    "washdownstrength": "1.0f",
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 0.2,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
    "weapons": [
        "rhsusf_weap_ANAAQ24"
    ],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "wheels": {
        "disablewheelswhendestroyed": 1,
        "wheel_1": {
            "bonename": "damper_nose_piston",
            "boundary": "wheel_nose_bound",
            "center": "wheel_nose_axis",
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "maxhandbraketorque": 0,
            "moi": 0.768,
            "side": "left",
            "springdamperrate": 1280,
            "springstrength": 12000,
            "sprungmass": 3000,
            "steering": 1,
            "suspforceapppointoffset": "wheel_nose_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_nose_axis",
            "width": 0.637
        },
        "wheel_2": {
            "bonename": "damper_left_piston",
            "boundary": "wheel_left_bound",
            "center": "wheel_left_axis",
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "maxhandbraketorque": 0,
            "moi": 0.768,
            "side": "left",
            "springdamperrate": 1280,
            "springstrength": 12000,
            "sprungmass": 3000,
            "steering": 0,
            "suspforceapppointoffset": "wheel_left_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_left_axis",
            "width": 0.637
        },
        "wheel_3": {
            "bonename": "damper_right_piston",
            "boundary": "wheel_right_bound",
            "center": "wheel_right_axis",
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "maxhandbraketorque": 0,
            "moi": 0.768,
            "side": "right",
            "springdamperrate": 1280,
            "springstrength": 12000,
            "sprungmass": 3000,
            "steering": 0,
            "suspforceapppointoffset": "wheel_right_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_right_axis",
            "width": 0.637
        }
    },
    "windsockexist": 0
}