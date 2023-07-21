d = {
    "_generalmacro": "Plane_Base_F",
    "access": 0,
    "accuracy": 0.15,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "aileroncoef": [
        0,
        0.5,
        1,
        1.2,
        1.4,
        1.5,
        1.6
    ],
    "aileroncontrolssensitivitycoef": 1,
    "aileronsensitivity": 1,
    "airbrake": 1,
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
    "altfullforce": 8535,
    "altnoforce": 17000,
    "alwaystarget": 0,
    "angleofindicence": -0.0174533,
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
        "collisionlightred_source": {
            "markerlight": "CollisionRed",
            "source": "MarkerLight"
        },
        "collisionlightwhite_source": {
            "markerlight": "CollisionWhite",
            "source": "MarkerLight"
        },
        "damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        "damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        "damper_2_2_source": {
            "source": "damper",
            "wheel": "Wheel_2_2"
        },
        "damper_3_1_source": {
            "source": "damper",
            "wheel": "Wheel_3_1"
        },
        "damper_3_2_source": {
            "source": "damper",
            "wheel": "Wheel_3_2"
        },
        "door_1": {
            "animperiod": 4,
            "initphase": 0,
            "sound": "ServoRampSound_2",
            "soundposition": "Door_1_axis",
            "source": "door"
        },
        "door_2_1": {
            "animperiod": 4,
            "initphase": 0,
            "sound": "ServoRampSound_2",
            "soundposition": "door_2_1_axis2",
            "source": "door"
        },
        "door_2_2": {
            "animperiod": 4,
            "initphase": 0,
            "sound": "ServoRampSound_2",
            "soundposition": "door_2_2_axis2",
            "source": "door"
        },
        "hide_cargo": {
            "animperiod": 1e-05,
            "displayname": "",
            "initphase": 1,
            "mass": -20,
            "onphasechanged": "for '_i' from 1 to 24 do {(_this select 0) lockCargo [_i,(_this select 1)==1]}",
            "source": "user"
        },
        "jumplight": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "ramp": {
            "animperiod": 5,
            "initphase": 0,
            "sound": "ServoRampSound_2",
            "soundposition": "ramp_bottom_axis",
            "source": "user"
        },
        "wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        "wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        "wheel_2_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2_2"
        },
        "wheel_3_1_source": {
            "source": "wheel",
            "wheel": "Wheel_3_1"
        },
        "wheel_3_2_source": {
            "source": "wheel",
            "wheel": "Wheel_3_2"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 250,
    "armorlights": 0.4,
    "armorstructural": 4,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "OpenHeliAttenuation",
    "attributes": {
        "door_1": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open crew door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_1"
        },
        "door_2_1": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open left door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_2_1"
        },
        "door_2_2": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open right door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_2_2"
        },
        "hide_cargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Hide cargo benches",
            "expression": "_this animate ['%s',_value,true];for '_i' from 1 to 24 do {_this lockCargo [_i,(_value == 1)]}",
            "property": "hide_cargo"
        },
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "ramp": {
            "control": "slider",
            "defaultvalue": "0",
            "displayname": "Open cargo bay",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Ramp"
        },
        "rhs_attachcargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Attach cargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "property": "rhs_attachCargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action"
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
    "canfloat": "false",
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo02",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo01",
        "Truck_Cargo04",
        "Truck_Cargo02"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [
        "Door_1",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2",
        "Door_2_1",
        "Door_2_2"
    ],
    "cargogetinaction": [
        "GetInLow"
    ],
    "cargogetoutaction": [
        "GetOutLow"
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
            "pylons": {
                "cmdispenser": {
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",
                    "hardpoints": [
                        "RHSUSF_cm_ANALE40_x2",
                        "RHSUSF_cm_ANALE40_x4",
                        "RHSUSF_cm_ANALE40_x8",
                        "RHSUSF_cm_ANALE40_x16"
                    ],
                    "maxweight": 800,
                    "priority": 1,
                    "uiposition": [
                        0.33,
                        0
                    ]
                }
            },
            "uipicture": "rhsusf/addons/rhsusf_a2port_air/data/loadouts/RHS_C130_EDEN_CA.paa"
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
                        3000,
                        8000,
                        16000,
                        35000
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
    "cost": 20000,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_airforce_pilot",
    "crewcrashprotection": 0.15,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo_in.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo_in_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_sklo_in_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_body.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_body_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_body_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_interior.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_interior_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_interior_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_wings.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_wings_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air/C130J/data/c130j_wings_destruct.rvmat"
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
    "displayname": "C-130J (Cargo)",
    "dlc": "RHS_USAF",
    "draconicforcexcoef": 4.3,
    "draconicforceycoef": 0.5,
    "draconicforcezcoef": 0.2,
    "draconictorquexcoef": [
        16,
        15.5,
        15,
        14.5,
        14,
        14,
        14.5,
        15,
        16,
        17,
        18
    ],
    "draconictorqueycoef": [
        3.2,
        2.5,
        1,
        "",
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "driveoncomponent": [],
    "driveraction": "RHS_C130_Pilot",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "Door_1",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "pilot_control",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "pilot_control",
    "driverrightleganimname": "",
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
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/RHS_C130J.paa",
    "editorsubcategory": "EdSubcat_Planes",
    "ejectdamagelimit": 0.45,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "ejectspeed": [
        0,
        0,
        0
    ],
    "elevatorcoef": [
        0,
        1,
        1.2,
        1.4,
        1.5,
        1.6,
        1.6
    ],
    "elevatorcontrolssensitivitycoef": 3,
    "elevatorsensitivity": 1,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablesweep": 0,
    "enablewatch": 0,
    "engineer": 0,
    "envelope": [
        0.1,
        0.1,
        0.9,
        2.8,
        3.5,
        3.7,
        3.8,
        3.8,
        3.6,
        3.3,
        2.7
    ],
    "epeimpulsedamagecoef": 1,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhsusf_eventhandlers": {
            "getin": "_this call rhs_fnc_C130_doors",
            "getout": "_this call rhs_fnc_C130_doors",
            "postinit": "_this call rhs_fnc_reapplyTextures"
        }
    },
    "exhausts": {
        "engine_l1": {
            "direction": "fx_engine_l1_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 0,
            "position": "fx_engine_l1_pos"
        },
        "engine_l2": {
            "direction": "fx_engine_l2_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 0,
            "position": "fx_engine_l2_pos"
        },
        "engine_r1": {
            "direction": "fx_engine_r1_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 1,
            "position": "fx_engine_r1_pos"
        },
        "engine_r2": {
            "direction": "fx_engine_r2_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 1,
            "position": "fx_engine_r2_pos"
        }
    },
    "explosionshielding": 2,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        5,
        -40
    ],
    "faction": "rhs_faction_usaf",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flaps": 1,
    "flapsfrictioncoef": 0.2,
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
    "geardowntime": 3,
    "gearretracting": 1,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 4.5,
    "getinaction": "GetInLow",
    "getinoutonproxy": 0,
    "getinradius": 2.5,
    "getoutaction": "GetInLow",
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
        "camo1",
        "camo2"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_a2port_air/c130j/data/c130j_body_co.paa",
        "rhsusf/addons/rhsusf_a2port_air/c130j/data/c130j_wings_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": -80,
            "depends": "0",
            "explosionshielding": 0.6,
            "material": -1,
            "minimalhit": -0.1,
            "name": "hit_avionics",
            "passthrough": 0.01,
            "radius": 0.08,
            "visual": "vis_avionics"
        },
        "hitcontrolrear": {
            "armor": -40,
            "depends": "0",
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_control_rear",
            "passthrough": 0.01,
            "radius": 0.17,
            "visual": ""
        },
        "hitengine": {
            "armor": 999,
            "depends": "(HitEngine_L1 + HitEngine_L1)*0.5",
            "explosionshielding": 0.25,
            "material": -1,
            "minimalhit": -0.01,
            "name": "hit_engine_l",
            "passthrough": 0.01,
            "radius": 0.01,
            "visual": "vis_engine_1"
        },
        "hitengine2": {
            "armor": 999,
            "depends": "(HitEngine_R1 + HitEngine_R1)*0.5",
            "explosionshielding": 0.25,
            "material": -1,
            "minimalhit": -0.01,
            "name": "hit_engine_r",
            "passthrough": 0.01,
            "radius": 0.01,
            "visual": "vis_engine_3"
        },
        "hitengine_l1": {
            "armor": -80,
            "armorcomponent": "hit_engine_l1",
            "depends": "0",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                "rhs_hull_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_hull_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_hull_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "AirFireSparks"
                }
            },
            "explosionshielding": 1.25,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_engine_l1",
            "passthrough": 0.01,
            "radius": 0.07,
            "visual": "vis_engine_l"
        },
        "hitengine_l2": {
            "armor": -80,
            "armorcomponent": "hit_engine_l2",
            "depends": "0",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                "rhs_hull_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_hull_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_hull_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "AirFireSparks"
                }
            },
            "explosionshielding": 1.25,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_engine_l2",
            "passthrough": 0.01,
            "radius": 0.07,
            "visual": "vis_engine_2"
        },
        "hitengine_r1": {
            "armor": -80,
            "armorcomponent": "hit_engine_r1",
            "depends": "0",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                "rhs_hull_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_hull_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_hull_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "AirFireSparks"
                }
            },
            "explosionshielding": 1.25,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_engine_r1",
            "passthrough": 0.01,
            "radius": 0.07,
            "visual": "vis_engine_3"
        },
        "hitengine_r2": {
            "armor": -80,
            "armorcomponent": "hit_engine_r2",
            "depends": "0",
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                "rhs_hull_fire": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_fire_3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "MediumDestructionFire"
                },
                "rhs_hull_smoke": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke"
                },
                "rhs_hull_smoke_small1": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_smoke_small2": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "WeaponWreckSmoke"
                },
                "rhs_hull_sounds": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "sound",
                    "type": "Fire"
                },
                "rhs_hull_sparks": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "AirFireSparks"
                }
            },
            "explosionshielding": 1.25,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_engine_r2",
            "passthrough": 0.01,
            "radius": 0.07,
            "visual": "vis_engine_4"
        },
        "hitfuel": {
            "armor": -60,
            "depends": "0",
            "explosionshielding": 0.2,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_fuel_l",
            "passthrough": 0.01,
            "radius": 0.1,
            "visual": "vis_wing_l"
        },
        "hitfuel2": {
            "armor": -60,
            "depends": "0",
            "explosionshielding": 0.2,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_fuel_r",
            "passthrough": 0.01,
            "radius": 0.1,
            "visual": "vis_wing_r"
        },
        "hithull": {
            "armor": -380,
            "armorcomponent": "hit_hull",
            "depends": "Total",
            "explosionshielding": 0.7,
            "material": -1,
            "minimalhit": -0.05,
            "name": "hit_hull",
            "passthrough": 1,
            "radius": 0.15,
            "visual": "zbytek"
        },
        "hitlaileron": {
            "armor": -40,
            "armorcomponent": "hit_wing_l",
            "depends": "HitLAileron_link*0.7",
            "explosionshielding": 1.6,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_aileron_l",
            "passthrough": 0.01,
            "radius": 0.13,
            "visual": "vis_wing_l"
        },
        "hitlaileron_link": {
            "armor": -40,
            "depends": "0",
            "explosionshielding": 0.9,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_aileron_link_l",
            "passthrough": 0.01,
            "radius": 0.12,
            "visual": ""
        },
        "hitlbwheel": {
            "armor": 1,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.1,
            "name": "wheel_3_1",
            "passthrough": 0,
            "radius": 0.12,
            "visual": "wheel_3_1"
        },
        "hitlcelevator": {
            "armor": -60,
            "armorcomponent": "hit_elevator_l",
            "depends": "HitControlRear",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_elevator_l",
            "passthrough": 0.01,
            "radius": 0.12,
            "visual": "vis_elevator_l"
        },
        "hitlcrudder": {
            "armor": -70,
            "armorcomponent": "hit_rudder",
            "depends": "HitControlRear",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": -0.02,
            "name": "hit_rudder",
            "passthrough": 0.01,
            "radius": 0.12,
            "visual": "vis_rudder"
        },
        "hitlf2wheel": {
            "armor": 1,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.1,
            "name": "wheel_2_1",
            "passthrough": 0,
            "radius": 0.12,
            "visual": "wheel_2_1"
        },
        "hitlfwheel": {
            "armor": 1,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.1,
            "name": "wheel_1_1",
            "passthrough": 0,
            "radius": 0.12,
            "visual": "wheel_1_1"
        },
        "hitlrf2wheel": {
            "armor": 1,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.1,
            "name": "wheel_2_2",
            "passthrough": 0,
            "radius": 0.12,
            "visual": "wheel_2_2"
        },
        "hitraileron": {
            "armor": -40,
            "armorcomponent": "hit_wing_r",
            "depends": "HitRAileron_link*0.7",
            "explosionshielding": 1.6,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_aileron_r",
            "passthrough": 0.01,
            "radius": 0.13,
            "visual": "vis_wing_r"
        },
        "hitraileron_link": {
            "armor": -40,
            "depends": "0",
            "explosionshielding": 0.9,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_aileron_link_r",
            "passthrough": 0.01,
            "radius": 0.12,
            "visual": ""
        },
        "hitrbwheel": {
            "armor": 1,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.1,
            "name": "wheel_3_2",
            "passthrough": 0,
            "radius": 0.12,
            "visual": "wheel_3_2"
        },
        "hitrelevator": {
            "armor": -60,
            "armorcomponent": "hit_elevator_r",
            "depends": "HitControlRear",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": -0.03,
            "name": "hit_elevator_r",
            "passthrough": 0.01,
            "radius": 0.12,
            "visual": "vis_elevator_r"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "rhsusf/addons/rhsusf_a2port_air/data/mapico/icon_c130j_CA.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "2 + 8 + 16",
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
    "landingaoa": "rad 7",
    "landingspeed": 200,
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
    "lesh_axisoffsettarget": [
        0,
        15,
        1.17
    ],
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_wheeloffset": [
        0,
        2
    ],
    "lightongear": 1,
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
    "mapsize": 25,
    "markerlights": {
        "collisionred": {
            "activelight": 0,
            "ambient": [
                0.09,
                0.015,
                0.01
            ],
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "CollisionLight_Red_1_pos",
            "useflare": 0
        },
        "collisionwhite": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "CollisionLight_White_1_pos",
            "useflare": 0
        },
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "PositionLight_White_1_pos",
            "useflare": 0
        },
        "positionwhite2": {
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "PositionLight_White_2_pos",
            "useflare": 0
        },
        "positionwhite3": {
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "PositionLight_White_3_pos",
            "useflare": 0
        },
        "positionwhite4": {
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
            "daylight": 1,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.4,
            "intensity": 75,
            "name": "PositionLight_White_4_pos",
            "useflare": 0
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 0.001,
    "maxgforce": 3,
    "maxgunelev": 0,
    "maxgunturn": 0,
    "maximumload": 15000,
    "maxomega": 2000,
    "maxspeed": 648,
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
        "pos driver",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2",
        "pos cargo1",
        "pos cargo2"
    ],
    "memorypointsgetincargodir": [
        "pos driver dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir",
        "pos cargo1 dir",
        "pos cargo2 dir"
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
        "airplanehud": {
            "bones": {
                "ils_h": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos3": [
                        0.62,
                        0.3
                    ],
                    "type": "ils"
                },
                "ils_w": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos3": [
                        0.5,
                        0.435
                    ],
                    "type": "ils"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm20": {
                    "angle": -20,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm25": {
                    "angle": -25,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm30": {
                    "angle": -30,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm35": {
                    "angle": -35,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm40": {
                    "angle": -40,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm45": {
                    "angle": -45,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm50": {
                    "angle": -50,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp20": {
                    "angle": 20,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp25": {
                    "angle": 25,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp30": {
                    "angle": 30,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp35": {
                    "angle": 35,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp40": {
                    "angle": 40,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp45": {
                    "angle": 45,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp50": {
                    "angle": 50,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.34
                    ],
                    "type": "fixed"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
                    ],
                    "source": "target",
                    "type": "vector"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
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
                "aamissile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.28125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.125,
                                    -0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.2175,
                                    -0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.2175,
                                    0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.125,
                                    0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.28125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.125,
                                    0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.2175,
                                    0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.2175,
                                    -0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.125,
                                    -0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.28125
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "AAmissile"
                },
                "alpha": 0.95,
                "altscale": {
                    "align": "right",
                    "bottom": 0.2,
                    "center": 0.5,
                    "down": [
                        0.86,
                        0.87
                    ],
                    "horizontal": "false",
                    "linexleft": 0.825,
                    "linexleftmajor": 0.825,
                    "lineyright": 0.835,
                    "lineyrightmajor": 0.845,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.86,
                        0.82
                    ],
                    "right": [
                        0.94,
                        0.82
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "step": 20,
                    "stepsize": 0.0325,
                    "top": 0.85,
                    "type": "scale"
                },
                "ammo": {
                    "align": "right",
                    "down": [
                        [
                            0.1,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.93
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.16,
                            0.93
                        ],
                        1
                    ],
                    "scale": 0.5,
                    "source": "ammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "atmissile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.2025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.09,
                                    -0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1566,
                                    -0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.18,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1566,
                                    0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.09,
                                    0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.2025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.09,
                                    0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1566,
                                    0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.18,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1566,
                                    -0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.09,
                                    -0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.2025
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "ATmissile"
                },
                "bomb": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.05,
                                    -0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.087,
                                    -0.05625
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
                                    0.087,
                                    0.05625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.05,
                                    0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.05,
                                    0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.087,
                                    0.05625
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
                                    -0.087,
                                    -0.05625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.05,
                                    -0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1125
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity",
                                0.001,
                                "WeaponAim",
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "bomb"
                },
                "color": [
                    0,
                    0.3,
                    0.05
                ],
                "condition": "on",
                "flaps": {
                    "condition": "flaps",
                    "text": {
                        "align": "right",
                        "down": [
                            [
                                0.84,
                                0.97
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.84,
                                0.93
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.9,
                                0.93
                            ],
                            1
                        ],
                        "scale": 0.5,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "FLAPS",
                        "type": "text"
                    }
                },
                "gear": {
                    "condition": "ils",
                    "text": {
                        "align": "right",
                        "down": [
                            [
                                0.84,
                                0.92
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.84,
                                0.88
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.9,
                                0.88
                            ],
                            1
                        ],
                        "scale": 0.5,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "GEAR",
                        "type": "text"
                    }
                },
                "headingscale": {
                    "align": "center",
                    "bottom": 0.8,
                    "center": 0.5,
                    "down": [
                        0.2,
                        0.05
                    ],
                    "horizontal": "true",
                    "linexleft": 0.06,
                    "linexleftmajor": 0.06,
                    "lineyright": 0.05,
                    "lineyrightmajor": 0.04,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.2,
                        0
                    ],
                    "right": [
                        0.28,
                        0
                    ],
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "step": 2,
                    "stepsize": 0.03,
                    "top": 0.2,
                    "type": "scale"
                },
                "horizont": {
                    "clipbr": [
                        1,
                        1
                    ],
                    "cliptl": [
                        0,
                        0
                    ],
                    "dimmed": {
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ]
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
                            "type": "line"
                        },
                        "levelm15": {
                            "points": [
                                [
                                    "LevelM15",
                                    [
                                        -0.2,
                                        -0.03
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
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.15,
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
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm25": {
                            "points": [
                                [
                                    "LevelM25",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm35": {
                            "points": [
                                [
                                    "LevelM35",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm45": {
                            "points": [
                                [
                                    "LevelM45",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.2,
                                        -0.03
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
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.2,
                                        0
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
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
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
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp15": {
                            "points": [
                                [
                                    "LevelP15",
                                    [
                                        -0.2,
                                        0.03
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
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP15",
                                    [
                                        0.05,
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
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp25": {
                            "points": [
                                [
                                    "LevelP25",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP25",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp35": {
                            "points": [
                                [
                                    "LevelP35",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP35",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp45": {
                            "points": [
                                [
                                    "LevelP45",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP45",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        0.2,
                                        0.03
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
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP5",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "valm_1_0": {
                            "align": "left",
                            "down": [
                                "Level0",
                                [
                                    -0.23,
                                    0.025
                                ],
                                1
                            ],
                            "pos": [
                                "Level0",
                                [
                                    -0.23,
                                    -0.025
                                ],
                                1
                            ],
                            "right": [
                                "Level0",
                                [
                                    -0.13,
                                    -0.025
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": 0,
                            "type": "text"
                        },
                        "valm_1_10": {
                            "align": "left",
                            "down": [
                                "LevelM10",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_1_15": {
                            "align": "left",
                            "down": [
                                "LevelM15",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_1_20": {
                            "align": "left",
                            "down": [
                                "LevelM20",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_1_25": {
                            "align": "left",
                            "down": [
                                "LevelM25",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_1_30": {
                            "align": "left",
                            "down": [
                                "LevelM30",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_1_35": {
                            "align": "left",
                            "down": [
                                "LevelM35",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_1_40": {
                            "align": "left",
                            "down": [
                                "LevelM40",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_1_45": {
                            "align": "left",
                            "down": [
                                "LevelM45",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_1_5": {
                            "align": "left",
                            "down": [
                                "LevelM5",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_1_50": {
                            "align": "left",
                            "down": [
                                "LevelM50",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valm_2_0": {
                            "align": "right",
                            "down": [
                                "Level0",
                                [
                                    0.22,
                                    0.025
                                ],
                                1
                            ],
                            "pos": [
                                "Level0",
                                [
                                    0.22,
                                    -0.025
                                ],
                                1
                            ],
                            "right": [
                                "Level0",
                                [
                                    0.32,
                                    -0.025
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": 0,
                            "type": "text"
                        },
                        "valm_2_10": {
                            "align": "right",
                            "down": [
                                "LevelM10",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_2_15": {
                            "align": "right",
                            "down": [
                                "LevelM15",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_2_20": {
                            "align": "right",
                            "down": [
                                "LevelM20",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_2_25": {
                            "align": "right",
                            "down": [
                                "LevelM25",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_2_30": {
                            "align": "right",
                            "down": [
                                "LevelM30",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_2_35": {
                            "align": "right",
                            "down": [
                                "LevelM35",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_2_40": {
                            "align": "right",
                            "down": [
                                "LevelM40",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_2_45": {
                            "align": "right",
                            "down": [
                                "LevelM45",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_2_5": {
                            "align": "right",
                            "down": [
                                "LevelM5",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_2_50": {
                            "align": "right",
                            "down": [
                                "LevelM50",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    0.32,
                                    -0.085
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
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_1_15": {
                            "align": "left",
                            "down": [
                                "LevelP15",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_1_20": {
                            "align": "left",
                            "down": [
                                "LevelP20",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_1_25": {
                            "align": "left",
                            "down": [
                                "LevelP25",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_1_30": {
                            "align": "left",
                            "down": [
                                "LevelP30",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_1_35": {
                            "align": "left",
                            "down": [
                                "LevelP35",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_1_40": {
                            "align": "left",
                            "down": [
                                "LevelP40",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_1_45": {
                            "align": "left",
                            "down": [
                                "LevelP45",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_1_5": {
                            "align": "left",
                            "down": [
                                "LevelP5",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_1_50": {
                            "align": "left",
                            "down": [
                                "LevelP50",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    -0.13,
                                    0.035
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
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_2_15": {
                            "align": "right",
                            "down": [
                                "LevelP15",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_2_20": {
                            "align": "right",
                            "down": [
                                "LevelP20",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_2_25": {
                            "align": "right",
                            "down": [
                                "LevelP25",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_2_30": {
                            "align": "right",
                            "down": [
                                "LevelP30",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_2_35": {
                            "align": "right",
                            "down": [
                                "LevelP35",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_2_40": {
                            "align": "right",
                            "down": [
                                "LevelP40",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_2_45": {
                            "align": "right",
                            "down": [
                                "LevelP45",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_2_5": {
                            "align": "right",
                            "down": [
                                "LevelP5",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_2_50": {
                            "align": "right",
                            "down": [
                                "LevelP50",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    0.32,
                                    0.035
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
                "ils": {
                    "condition": "ils",
                    "glideslope": {
                        "clipbr": [
                            1,
                            1
                        ],
                        "cliptl": [
                            0,
                            0
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        -0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        0.27
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0.135
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0.135
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0.27
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        -0.135
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        -0.135
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        -0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        -0.27
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
                                    0.01,
                                    0
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
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.049,
                                    -0.055125
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
                                    0.049,
                                    0.055125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.049,
                                    0.055125
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
                                    -0.049,
                                    -0.055125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    -0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1218,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.14,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1218,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1218,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.14,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1218,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    -0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.18
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    -0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.08,
                                    -0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.121244,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.138564,
                                    -0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.14,
                                    6.88454e-09
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.16,
                                    7.86805e-09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.121244,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.138564,
                                    0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.08,
                                    0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    1.22392e-08,
                                    0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    1.39876e-08,
                                    0.18
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.08,
                                    0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.121244,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.138564,
                                    0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.14,
                                    -1.87817e-09
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.16,
                                    -2.14648e-09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.121244,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.138564,
                                    -0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    -0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.08,
                                    -0.155885
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line"
                    },
                    "condition": "mgun"
                },
                "planeheading": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        1
                    ],
                    "points": [
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0.014,
                                -0.01575
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
                                0.014,
                                0.01575
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                0.0225
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                -0.014,
                                0.01575
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
                                -0.014,
                                -0.01575
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        [],
                        [
                            "Velocity",
                            [
                                0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                -0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                0,
                                -0.045
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line"
                },
                "planew": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        1
                    ],
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.08,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.03,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.015,
                                0.03375
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.015,
                                0.03375
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.03,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.08,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line"
                },
                "rockets": {
                    "circle": {
                        "points": [
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
                                    -0.01,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.135
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.06,
                                    -0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1044,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.12,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1044,
                                    0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.06,
                                    0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.135
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.06,
                                    0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1044,
                                    0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.12,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1044,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.06,
                                    -0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.135
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line"
                    },
                    "condition": "Rocket"
                },
                "speedscale": {
                    "align": "right",
                    "bottom": 0.85,
                    "center": 0.5,
                    "down": [
                        0.06,
                        0.22
                    ],
                    "horizontal": "false",
                    "linexleft": 0.175,
                    "linexleftmajor": 0.175,
                    "lineyright": 0.165,
                    "lineyrightmajor": 0.155,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.06,
                        0.17
                    ],
                    "right": [
                        0.14,
                        0.17
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "step": 20,
                    "stepsize": 0.0325,
                    "top": 0.2,
                    "type": "scale"
                },
                "static": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        0.1
                    ],
                    "points": [
                        [
                            [
                                0.21,
                                0.52
                            ],
                            1
                        ],
                        [
                            [
                                0.19,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.21,
                                0.48
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.18,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                0.18,
                                0.85
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.79,
                                0.52
                            ],
                            1
                        ],
                        [
                            [
                                0.81,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.79,
                                0.48
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.82,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                0.82,
                                0.85
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.52,
                                0.09
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.07
                            ],
                            1
                        ],
                        [
                            [
                                0.48,
                                0.09
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.2,
                                0.065
                            ],
                            1
                        ],
                        [
                            [
                                0.8,
                                0.065
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line"
                },
                "vspeednumber": {
                    "align": "right",
                    "down": [
                        [
                            0.86,
                            0.17
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.86,
                            0.12
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.94,
                            0.12
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "vspeed",
                    "sourcescale": 1,
                    "type": "text"
                },
                "weapons": {
                    "align": "right",
                    "down": [
                        [
                            0.1,
                            0.92
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.88
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.16,
                            0.88
                        ],
                        1
                    ],
                    "scale": 0.5,
                    "source": "weapon",
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "helmetdown": [
                0,
                -0.05,
                0
            ],
            "helmetmounteddisplay": 0,
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
                    0.3
                ],
                "pos10": [
                    0.9,
                    0.75
                ],
                "type": "vector"
            },
            "topleft": "HUD LH",
            "topright": "HUD PH"
        },
        "airplanehud2": {
            "bones": {
                "ils_h": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos3": [
                        0.62,
                        0.3
                    ],
                    "type": "ils"
                },
                "ils_w": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos3": [
                        0.5,
                        0.435
                    ],
                    "type": "ils"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm20": {
                    "angle": -20,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm25": {
                    "angle": -25,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm30": {
                    "angle": -30,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm35": {
                    "angle": -35,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm40": {
                    "angle": -40,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm45": {
                    "angle": -45,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelm50": {
                    "angle": -50,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp20": {
                    "angle": 20,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp25": {
                    "angle": 25,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp30": {
                    "angle": 30,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp35": {
                    "angle": 35,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp40": {
                    "angle": 40,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp45": {
                    "angle": 45,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "levelp50": {
                    "angle": 50,
                    "pos0": [
                        0.5,
                        0.34
                    ],
                    "pos10": [
                        0.9,
                        0.79
                    ],
                    "type": "horizon"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.34
                    ],
                    "type": "fixed"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
                    ],
                    "source": "target",
                    "type": "vector"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.3
                    ],
                    "pos10": [
                        0.9,
                        0.75
                    ],
                    "source": "weapon",
                    "type": "vector"
                }
            },
            "borderbottom": 0.1,
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "bottomleft": "HUD2 LD",
            "bottomright": "HUD2 PD",
            "color": [
                0,
                1,
                0,
                0.1
            ],
            "draw": {
                "aamissile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.28125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.125,
                                    -0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.2175,
                                    -0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.2175,
                                    0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.125,
                                    0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.28125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.125,
                                    0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.2175,
                                    0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.25,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.2175,
                                    -0.140625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.125,
                                    -0.244687
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.28125
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "AAmissile"
                },
                "alpha": 0.95,
                "altscale": {
                    "align": "right",
                    "bottom": 0.2,
                    "center": 0.5,
                    "down": [
                        0.86,
                        0.87
                    ],
                    "horizontal": "false",
                    "linexleft": 0.825,
                    "linexleftmajor": 0.825,
                    "lineyright": 0.835,
                    "lineyrightmajor": 0.845,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.86,
                        0.82
                    ],
                    "right": [
                        0.94,
                        0.82
                    ],
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "step": 20,
                    "stepsize": 0.0325,
                    "top": 0.85,
                    "type": "scale"
                },
                "ammo": {
                    "align": "right",
                    "down": [
                        [
                            0.1,
                            0.97
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.93
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.16,
                            0.93
                        ],
                        1
                    ],
                    "scale": 0.5,
                    "source": "ammo",
                    "sourcescale": 1,
                    "type": "text"
                },
                "atmissile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.2025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.09,
                                    -0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1566,
                                    -0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.18,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1566,
                                    0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.09,
                                    0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.2025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.09,
                                    0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1566,
                                    0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.18,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1566,
                                    -0.10125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.09,
                                    -0.176175
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.2025
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "ATmissile"
                },
                "bomb": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.05,
                                    -0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.087,
                                    -0.05625
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
                                    0.087,
                                    0.05625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.05,
                                    0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.05,
                                    0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.087,
                                    0.05625
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
                                    -0.087,
                                    -0.05625
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.05,
                                    -0.097875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1125
                                ],
                                1
                            ],
                            [],
                            [
                                "Velocity",
                                0.001,
                                "WeaponAim",
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "bomb"
                },
                "color": [
                    0,
                    0.3,
                    0.05
                ],
                "condition": "on",
                "flaps": {
                    "condition": "flaps",
                    "text": {
                        "align": "right",
                        "down": [
                            [
                                0.84,
                                0.97
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.84,
                                0.93
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.9,
                                0.93
                            ],
                            1
                        ],
                        "scale": 0.5,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "FLAPS",
                        "type": "text"
                    }
                },
                "gear": {
                    "condition": "ils",
                    "text": {
                        "align": "right",
                        "down": [
                            [
                                0.84,
                                0.92
                            ],
                            1
                        ],
                        "pos": [
                            [
                                0.84,
                                0.88
                            ],
                            1
                        ],
                        "right": [
                            [
                                0.9,
                                0.88
                            ],
                            1
                        ],
                        "scale": 0.5,
                        "source": "static",
                        "sourcescale": 1,
                        "text": "GEAR",
                        "type": "text"
                    }
                },
                "headingscale": {
                    "align": "center",
                    "bottom": 0.8,
                    "center": 0.5,
                    "down": [
                        0.2,
                        0.05
                    ],
                    "horizontal": "true",
                    "linexleft": 0.06,
                    "linexleftmajor": 0.06,
                    "lineyright": 0.05,
                    "lineyrightmajor": 0.04,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.2,
                        0
                    ],
                    "right": [
                        0.28,
                        0
                    ],
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "step": 2,
                    "stepsize": 0.03,
                    "top": 0.2,
                    "type": "scale"
                },
                "horizont": {
                    "clipbr": [
                        1,
                        1
                    ],
                    "cliptl": [
                        0,
                        0
                    ],
                    "dimmed": {
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ]
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
                            "type": "line"
                        },
                        "levelm15": {
                            "points": [
                                [
                                    "LevelM15",
                                    [
                                        -0.2,
                                        -0.03
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
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM15",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM15",
                                    [
                                        0.15,
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
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm25": {
                            "points": [
                                [
                                    "LevelM25",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM25",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM25",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm35": {
                            "points": [
                                [
                                    "LevelM35",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM35",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM35",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelm45": {
                            "points": [
                                [
                                    "LevelM45",
                                    [
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.15,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM45",
                                    [
                                        0.15,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM45",
                                    [
                                        0.2,
                                        -0.03
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
                                        -0.2,
                                        -0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.2,
                                        0
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
                                [],
                                [
                                    "LevelM5",
                                    [
                                        -0.1,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelM5",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.1,
                                        0
                                    ],
                                    1
                                ],
                                [],
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
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelM5",
                                    [
                                        0.2,
                                        -0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp15": {
                            "points": [
                                [
                                    "LevelP15",
                                    [
                                        -0.2,
                                        0.03
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
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP15",
                                    [
                                        0.05,
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
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp25": {
                            "points": [
                                [
                                    "LevelP25",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP25",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP25",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp35": {
                            "points": [
                                [
                                    "LevelP35",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP35",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP35",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "levelp45": {
                            "points": [
                                [
                                    "LevelP45",
                                    [
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP45",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP45",
                                    [
                                        0.2,
                                        0.03
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
                                        -0.2,
                                        0.03
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        -0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        -0.05,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "LevelP5",
                                    [
                                        0.05,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        0.2,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "LevelP5",
                                    [
                                        0.2,
                                        0.03
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
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
                            "type": "line"
                        },
                        "valm_1_0": {
                            "align": "left",
                            "down": [
                                "Level0",
                                [
                                    -0.23,
                                    0.025
                                ],
                                1
                            ],
                            "pos": [
                                "Level0",
                                [
                                    -0.23,
                                    -0.025
                                ],
                                1
                            ],
                            "right": [
                                "Level0",
                                [
                                    -0.13,
                                    -0.025
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": 0,
                            "type": "text"
                        },
                        "valm_1_10": {
                            "align": "left",
                            "down": [
                                "LevelM10",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_1_15": {
                            "align": "left",
                            "down": [
                                "LevelM15",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_1_20": {
                            "align": "left",
                            "down": [
                                "LevelM20",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_1_25": {
                            "align": "left",
                            "down": [
                                "LevelM25",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_1_30": {
                            "align": "left",
                            "down": [
                                "LevelM30",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_1_35": {
                            "align": "left",
                            "down": [
                                "LevelM35",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_1_40": {
                            "align": "left",
                            "down": [
                                "LevelM40",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_1_45": {
                            "align": "left",
                            "down": [
                                "LevelM45",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_1_5": {
                            "align": "left",
                            "down": [
                                "LevelM5",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_1_50": {
                            "align": "left",
                            "down": [
                                "LevelM50",
                                [
                                    -0.23,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    -0.23,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    -0.13,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -50,
                            "type": "text"
                        },
                        "valm_2_0": {
                            "align": "right",
                            "down": [
                                "Level0",
                                [
                                    0.22,
                                    0.025
                                ],
                                1
                            ],
                            "pos": [
                                "Level0",
                                [
                                    0.22,
                                    -0.025
                                ],
                                1
                            ],
                            "right": [
                                "Level0",
                                [
                                    0.32,
                                    -0.025
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": 0,
                            "type": "text"
                        },
                        "valm_2_10": {
                            "align": "right",
                            "down": [
                                "LevelM10",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM10",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM10",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -10,
                            "type": "text"
                        },
                        "valm_2_15": {
                            "align": "right",
                            "down": [
                                "LevelM15",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM15",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM15",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -15,
                            "type": "text"
                        },
                        "valm_2_20": {
                            "align": "right",
                            "down": [
                                "LevelM20",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM20",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM20",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -20,
                            "type": "text"
                        },
                        "valm_2_25": {
                            "align": "right",
                            "down": [
                                "LevelM25",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM25",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM25",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -25,
                            "type": "text"
                        },
                        "valm_2_30": {
                            "align": "right",
                            "down": [
                                "LevelM30",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM30",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM30",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -30,
                            "type": "text"
                        },
                        "valm_2_35": {
                            "align": "right",
                            "down": [
                                "LevelM35",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM35",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM35",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -35,
                            "type": "text"
                        },
                        "valm_2_40": {
                            "align": "right",
                            "down": [
                                "LevelM40",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM40",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM40",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -40,
                            "type": "text"
                        },
                        "valm_2_45": {
                            "align": "right",
                            "down": [
                                "LevelM45",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM45",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM45",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -45,
                            "type": "text"
                        },
                        "valm_2_5": {
                            "align": "right",
                            "down": [
                                "LevelM5",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM5",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM5",
                                [
                                    0.32,
                                    -0.085
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": -5,
                            "type": "text"
                        },
                        "valm_2_50": {
                            "align": "right",
                            "down": [
                                "LevelM50",
                                [
                                    0.22,
                                    -0.035
                                ],
                                1
                            ],
                            "pos": [
                                "LevelM50",
                                [
                                    0.22,
                                    -0.085
                                ],
                                1
                            ],
                            "right": [
                                "LevelM50",
                                [
                                    0.32,
                                    -0.085
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
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_1_15": {
                            "align": "left",
                            "down": [
                                "LevelP15",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_1_20": {
                            "align": "left",
                            "down": [
                                "LevelP20",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_1_25": {
                            "align": "left",
                            "down": [
                                "LevelP25",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_1_30": {
                            "align": "left",
                            "down": [
                                "LevelP30",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_1_35": {
                            "align": "left",
                            "down": [
                                "LevelP35",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_1_40": {
                            "align": "left",
                            "down": [
                                "LevelP40",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_1_45": {
                            "align": "left",
                            "down": [
                                "LevelP45",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_1_5": {
                            "align": "left",
                            "down": [
                                "LevelP5",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    -0.13,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_1_50": {
                            "align": "left",
                            "down": [
                                "LevelP50",
                                [
                                    -0.23,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    -0.23,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    -0.13,
                                    0.035
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
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP10",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP10",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "10",
                            "type": "text"
                        },
                        "valp_2_15": {
                            "align": "right",
                            "down": [
                                "LevelP15",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP15",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP15",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "15",
                            "type": "text"
                        },
                        "valp_2_20": {
                            "align": "right",
                            "down": [
                                "LevelP20",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP20",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP20",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "20",
                            "type": "text"
                        },
                        "valp_2_25": {
                            "align": "right",
                            "down": [
                                "LevelP25",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP25",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP25",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "25",
                            "type": "text"
                        },
                        "valp_2_30": {
                            "align": "right",
                            "down": [
                                "LevelP30",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP30",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP30",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "30",
                            "type": "text"
                        },
                        "valp_2_35": {
                            "align": "right",
                            "down": [
                                "LevelP35",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP35",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP35",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "35",
                            "type": "text"
                        },
                        "valp_2_40": {
                            "align": "right",
                            "down": [
                                "LevelP40",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP40",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP40",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "40",
                            "type": "text"
                        },
                        "valp_2_45": {
                            "align": "right",
                            "down": [
                                "LevelP45",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP45",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP45",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "45",
                            "type": "text"
                        },
                        "valp_2_5": {
                            "align": "right",
                            "down": [
                                "LevelP5",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP5",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP5",
                                [
                                    0.32,
                                    0.035
                                ],
                                1
                            ],
                            "scale": 1,
                            "source": "static",
                            "sourcescale": 1,
                            "text": "5",
                            "type": "text"
                        },
                        "valp_2_50": {
                            "align": "right",
                            "down": [
                                "LevelP50",
                                [
                                    0.22,
                                    0.085
                                ],
                                1
                            ],
                            "pos": [
                                "LevelP50",
                                [
                                    0.22,
                                    0.035
                                ],
                                1
                            ],
                            "right": [
                                "LevelP50",
                                [
                                    0.32,
                                    0.035
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
                "ils": {
                    "condition": "ils",
                    "glideslope": {
                        "clipbr": [
                            1,
                            1
                        ],
                        "cliptl": [
                            0,
                            0
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.12,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        0.24,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.12,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        0.027
                                    ],
                                    1
                                ],
                                [
                                    "ILS_W",
                                    [
                                        -0.24,
                                        -0.027
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        -0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        0,
                                        0.27
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0.135
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0.135
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        0.27
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        -0.135
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        -0.135
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS_H",
                                    [
                                        0.024,
                                        -0.27
                                    ],
                                    1
                                ],
                                [
                                    "ILS_H",
                                    [
                                        -0.024,
                                        -0.27
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
                                    0.01,
                                    0
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
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.049,
                                    -0.055125
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
                                    0.049,
                                    0.055125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.049,
                                    0.055125
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
                                    -0.049,
                                    -0.055125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07875
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    -0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1218,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.14,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1218,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1218,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.14,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1218,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    -0.137025
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.18
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    -0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.08,
                                    -0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.121244,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.138564,
                                    -0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.14,
                                    6.88454e-09
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.16,
                                    7.86805e-09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.121244,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.138564,
                                    0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.08,
                                    0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    1.22392e-08,
                                    0.1575
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    1.39876e-08,
                                    0.18
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.08,
                                    0.155885
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.121244,
                                    0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.138564,
                                    0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.14,
                                    -1.87817e-09
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.16,
                                    -2.14648e-09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.121244,
                                    -0.07875
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.138564,
                                    -0.09
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    -0.136399
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.08,
                                    -0.155885
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line"
                    },
                    "condition": "mgun"
                },
                "planeheading": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        1
                    ],
                    "points": [
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0.014,
                                -0.01575
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
                                0.014,
                                0.01575
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                0.0225
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                -0.014,
                                0.01575
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
                                -0.014,
                                -0.01575
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        [],
                        [
                            "Velocity",
                            [
                                0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                -0.04,
                                0
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
                        [],
                        [
                            "Velocity",
                            [
                                0,
                                -0.045
                            ],
                            1
                        ],
                        [
                            "Velocity",
                            [
                                0,
                                -0.0225
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line"
                },
                "planew": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        1
                    ],
                    "points": [
                        [
                            "PlaneW",
                            [
                                -0.08,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.03,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                -0.015,
                                0.03375
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.015,
                                0.03375
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.03,
                                0
                            ],
                            1
                        ],
                        [
                            "PlaneW",
                            [
                                0.08,
                                0
                            ],
                            1
                        ]
                    ],
                    "type": "line"
                },
                "rockets": {
                    "circle": {
                        "points": [
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
                                    -0.01,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01125
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01125
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.135
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.06,
                                    -0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1044,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.12,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1044,
                                    0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.06,
                                    0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.135
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.06,
                                    0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1044,
                                    0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.12,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1044,
                                    -0.0675
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.06,
                                    -0.11745
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.135
                                ],
                                1
                            ],
                            []
                        ],
                        "type": "line"
                    },
                    "condition": "Rocket"
                },
                "speedscale": {
                    "align": "right",
                    "bottom": 0.85,
                    "center": 0.5,
                    "down": [
                        0.06,
                        0.22
                    ],
                    "horizontal": "false",
                    "linexleft": 0.175,
                    "linexleftmajor": 0.175,
                    "lineyright": 0.165,
                    "lineyrightmajor": 0.155,
                    "majorlineeach": 5,
                    "max": "none",
                    "min": "none",
                    "numbereach": 5,
                    "pos": [
                        0.06,
                        0.17
                    ],
                    "right": [
                        0.14,
                        0.17
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "step": 20,
                    "stepsize": 0.0325,
                    "top": 0.2,
                    "type": "scale"
                },
                "static": {
                    "clipbr": [
                        1,
                        0
                    ],
                    "cliptl": [
                        0,
                        0.1
                    ],
                    "points": [
                        [
                            [
                                0.21,
                                0.52
                            ],
                            1
                        ],
                        [
                            [
                                0.19,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.21,
                                0.48
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.18,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                0.18,
                                0.85
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.79,
                                0.52
                            ],
                            1
                        ],
                        [
                            [
                                0.81,
                                0.5
                            ],
                            1
                        ],
                        [
                            [
                                0.79,
                                0.48
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.82,
                                0.2
                            ],
                            1
                        ],
                        [
                            [
                                0.82,
                                0.85
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.52,
                                0.09
                            ],
                            1
                        ],
                        [
                            [
                                0.5,
                                0.07
                            ],
                            1
                        ],
                        [
                            [
                                0.48,
                                0.09
                            ],
                            1
                        ],
                        [],
                        [
                            [
                                0.2,
                                0.065
                            ],
                            1
                        ],
                        [
                            [
                                0.8,
                                0.065
                            ],
                            1
                        ],
                        []
                    ],
                    "type": "line"
                },
                "vspeednumber": {
                    "align": "right",
                    "down": [
                        [
                            0.86,
                            0.17
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.86,
                            0.12
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.94,
                            0.12
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "vspeed",
                    "sourcescale": 1,
                    "type": "text"
                },
                "weapons": {
                    "align": "right",
                    "down": [
                        [
                            0.1,
                            0.92
                        ],
                        1
                    ],
                    "pos": [
                        [
                            0.1,
                            0.88
                        ],
                        1
                    ],
                    "right": [
                        [
                            0.16,
                            0.88
                        ],
                        1
                    ],
                    "scale": 0.5,
                    "source": "weapon",
                    "sourcescale": 1,
                    "type": "text"
                }
            },
            "helmetdown": [
                0,
                -0.05,
                0
            ],
            "helmetmounteddisplay": 0,
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
                    0.3
                ],
                "pos10": [
                    0.9,
                    0.75
                ],
                "type": "vector"
            },
            "topleft": "HUD2 LH",
            "topright": "HUD2 PH"
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
    "model": "rhsusf/addons/rhsusf_a2port_air/C130J/c130j.p3d",
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
    "picture": "rhsusf/addons/rhsusf_a2port_air/data/ico/rhs_c130j_pic_ca.paa",
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
    "pylonmagazines": [
        [
            "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x2",
            "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x4",
            "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x8",
            "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",
            "rhsusf_ANALE40_CMFlare_Magazine_x2",
            "rhsusf_ANALE40_CMFlare_Magazine_x4",
            "rhsusf_ANALE40_CMFlare_Magazine_x8",
            "rhsusf_ANALE40_CMFlare_Magazine_x16"
        ]
    ],
    "radartarget": 1,
    "radartargetsize": 1.5,
    "radartype": 4,
    "reflectors": {
        "left": {
            "ambient": [
                70,
                75,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "brightness": 50,
            "color": [
                7000,
                7500,
                10000
            ],
            "conefadecoef": 10,
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "innerangle": 5,
            "outerangle": 75,
            "position": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "left2": {
            "ambient": [
                70,
                75,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "brightness": 1,
            "color": [
                7000,
                7500,
                10000
            ],
            "conefadecoef": 10,
            "direction": "konec L2 svetla",
            "hitpoint": "L2 svetlo",
            "innerangle": 5,
            "outerangle": 75,
            "position": "L2 svetlo",
            "selection": "L2 svetlo",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                70,
                75,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "brightness": 1,
            "color": [
                7000,
                7500,
                10000
            ],
            "conefadecoef": 10,
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "innerangle": 5,
            "outerangle": 75,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        },
        "right2": {
            "ambient": [
                70,
                75,
                100
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 250,
                "hardlimitstart": 200,
                "linear": 1,
                "quadratic": 0,
                "start": 0
            },
            "brightness": 1,
            "color": [
                7000,
                7500,
                10000
            ],
            "conefadecoef": 10,
            "direction": "konec P2 svetla",
            "hitpoint": "P2 svetlo",
            "innerangle": 5,
            "outerangle": 75,
            "position": "P2 svetlo",
            "selection": "P2 svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reportownposition": 1,
    "reversed": 1,
    "rhs_gearanim": "Gear_1_1",
    "rhs_paraoff": -7,
    "rhs_pararamp": "ramp",
    "rhs_parascript": "rhs_fnc_vehPara",
    "rhs_rampanim": "ramp_bottom",
    "rhs_vehclass_aircraft": "",
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
        0.4,
        1,
        1.4,
        1.8,
        2,
        2.2,
        2.3,
        2.4,
        2.5,
        2.5,
        2.5,
        2.6
    ],
    "ruddercontrolssensitivitycoef": 1.5,
    "rudderinfluence": 0.866,
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
    "selectionshowdamage": "zbytek",
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "shadow": 1,
    "showalltargets": 0,
    "showcrewaim": 0,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        1
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 1,
    "simulation": "airplanex",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.3,
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
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/int-alarm_loop",
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
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext_stop_1",
        0.398107,
        1,
        700
    ],
    "soundengineoffint": [
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int_stop_1",
        0.398107,
        1
    ],
    "soundengineonext": [
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext_start_1",
        0.398107,
        1,
        700
    ],
    "soundengineonint": [
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int_start_1",
        0.398107,
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
    "soundgetin": [
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/close",
        0.316228,
        1
    ],
    "soundgetout": [
        "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/open",
        0.316228,
        1,
        40
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/weapons/Rockets/locked_3",
        0.1,
        1.5
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
        "enginehighin": {
            "frequency": "1",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int_engine_hi",
                1,
                1
            ],
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        "enginehighout": {
            "frequency": "1",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext_engine_hi",
                1.77828,
                1,
                1100
            ],
            "volume": "camPos*engineOn*(rpm factor[0.55, 1.0])"
        },
        "enginelowin": {
            "frequency": "1.0 min (rpm + 0.5)",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int_engine_low",
                1,
                1
            ],
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        "enginelowout": {
            "frequency": "1.0 min (rpm + 0.5)",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext_engine_low",
                1.77828,
                1,
                900
            ],
            "volume": "camPos*engineOn*(rpm factor[0.85, 0])"
        },
        "forsagein": {
            "frequency": "1",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int_forsage_1",
                1.41254,
                1.1
            ],
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        "forsageout": {
            "cone": [
                1.14,
                3.92,
                2,
                0.4
            ],
            "frequency": "1",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext_forsage_1",
                1.41254,
                1,
                1500
            ],
            "volume": "camPos*engineOn*(thrust factor[0.5, 1.0])"
        },
        "windnoisein": {
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/int-wind1",
                0.001,
                0.6
            ],
            "volume": "(1-camPos)*(speed factor[1, 100])"
        },
        "windnoiseout": {
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "sound": [
                "/rhsusf/addons/rhsusf_a2port_air/data/sounds/c130/ext-wind1",
                0.001,
                0.6,
                150
            ],
            "volume": "camPos*(speed factor[1, 100])"
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
    "stallspeed": 180,
    "stallwarningtreshold": 0.5,
    "steeraheadplan": 2,
    "steeraheadsimul": 1,
    "supplyradius": 2,
    "tailhook": 0,
    "tbody": 150,
    "textplural": "fast movers",
    "textsingular": "fast mover",
    "texturelist": [
        "standard",
        1
    ],
    "texturesources": {
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [
                "rhs_faction_usaf"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_a2port_air/c130j/data/c130j_body_co.paa",
                "rhsusf/addons/rhsusf_a2port_air/c130j/data/c130j_wings_co.paa"
            ]
        }
    },
    "threat": [
        0.1,
        0.5,
        0.8
    ],
    "thrustcoef": [
        0.9,
        0.8,
        0.9,
        1.3,
        1.2,
        1.2,
        1.1,
        1,
        0.9,
        0.2,
        0.1,
        0,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 14
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 20,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 4,
            "name": "Medikit"
        },
        "_xx_toolkit": {
            "count": 1,
            "name": "Toolkit"
        }
    },
    "transportmagazines": {
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 30,
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag"
        },
        "_xx_rhs_mag_an_m8hc": {
            "count": 4,
            "magazine": "rhs_mag_an_m8hc"
        },
        "_xx_rhs_mag_m18_green": {
            "count": 2,
            "magazine": "rhs_mag_m18_green"
        },
        "_xx_rhs_mag_m18_red": {
            "count": 2,
            "magazine": "rhs_mag_m18_red"
        },
        "_xx_rhs_mag_m441_he": {
            "count": 16,
            "magazine": "rhs_mag_M441_HE"
        },
        "_xx_rhs_mag_m662_red": {
            "count": 2,
            "magazine": "rhs_mag_M662_red"
        },
        "_xx_rhs_mag_m67": {
            "count": 4,
            "magazine": "rhs_mag_m67"
        },
        "_xx_rhs_mag_m714_white": {
            "count": 4,
            "magazine": "rhs_mag_M714_white"
        },
        "_xx_rhsusf_100rnd_556x45_soft_pouch": {
            "count": 8,
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch"
        }
    },
    "transportmaxbackpacks": 6,
    "transportmaxmagazines": 24,
    "transportmaxweapons": 6,
    "transportrepair": 0,
    "transportsoldier": 1,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_m4_carryhandle": {
            "count": 2,
            "weapon": "rhs_weap_m4_carryhandle"
        }
    },
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
            "caneject": 0,
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
            "gunneraction": "RHS_C130_Pilot",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "Door_1",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerinaction": "RHS_C130_Pilot",
            "gunnerlefthandanimname": "copilot_control",
            "gunnerleftleganimname": "",
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
            "gunnerrighthandanimname": "copilot_control",
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
            "reflectors": {
                "cabin": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 3.5,
                        "hardlimitstart": 3,
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
                        "hardlimitend": 3.5,
                        "hardlimitstart": 3,
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
                        "hardlimitend": 3.5,
                        "hardlimitstart": 3,
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
                        "hardlimitend": 3.5,
                        "hardlimitstart": 3,
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
                },
                "cargo_light_4": {
                    "ambient": [
                        5,
                        0,
                        0
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 3.5,
                        "hardlimitstart": 3,
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
                    "direction": "cargo_light_4_dir",
                    "flaremaxdistance": 5,
                    "flaresize": 1,
                    "hitpoint": "cargo_light_4",
                    "innerangle": 90,
                    "intensity": 21,
                    "outerangle": 165,
                    "position": "cargo_light_4",
                    "selection": "cargo_light_4",
                    "size": 1,
                    "useflare": 0
                }
            },
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
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
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
        "rhsusf_airforce_pilot",
        "rhsusf_airforce_pilot"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHSUSF_RscUnitInfoAirPlane",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "closeramp": {
            "condition": "(this animationSourcePhase 'ramp' >= 0.65) AND Alive(this)",
            "displayname": "Close Cargo Ramp",
            "onlyforplayer": 1,
            "position": "pos_gunner",
            "radius": 6,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateSource ['ramp',0];[this] call rhs_fnc_cargoAttach"
        },
        "levelramp": {
            "condition": "this animationSourcePhase 'ramp' != 0.65 and (alive this)",
            "displayname": "Level Ramp",
            "onlyforplayer": 1,
            "position": "pos_gunner",
            "radius": 6,
            "shortcut": "user13",
            "showwindow": 0,
            "statement": "this animateSource ['ramp', 0.65];"
        },
        "openmenu": {
            "animperiod": 2,
            "condition": "((call rhsusf_fnc_findPlayer) in this)",
            "displayname": "<t color='#FDDE00'>Open control panel</t>",
            "onlyforplayer": 1,
            "position": "pos_gunner",
            "priority": 11.008,
            "radius": 10,
            "statement": "[this] call rhs_fnc_c130j_openMenu",
            "useractionid": 74
        },
        "openramp": {
            "condition": "(this animationSourcePhase 'ramp' <= 0.65) AND Alive(this)",
            "displayname": "Open Cargo Ramp",
            "onlyforplayer": 1,
            "position": "pos_gunner",
            "radius": 6,
            "shortcut": "user12",
            "showwindow": 0,
            "statement": "this animateSource ['ramp',1];[this] call rhs_fnc_cargoDetach"
        },
        "vehicleparadrop": {
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "displayname": "Paradrop cargo",
            "onlyforplayer": 1,
            "position": "pos_gunner",
            "radius": 6,
            "shortcut": "",
            "showwindow": 0,
            "statement": "[this] spawn rhs_fnc_vehPara"
        }
    },
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
                0,
                0.1,
                0
            ],
            "disableheightlimit": 0,
            "exits": [
                "VTV_exit_1"
            ],
            "loadingangle": 60,
            "loadingdistance": 15,
            "maxloadmass": 28000,
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
    "visualtargetsize": 1.5,
    "vtol": 0,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "vtolyawinfluence": 2,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 25,
    "waterlineardampingcoefx": 5,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.004,
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
        "wheel_1_1": {
            "bonename": "Wheel_1_1",
            "boundary": "Wheel_1_1_rim",
            "center": "Wheel_1_1_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "left",
            "springdamperrate": 128000,
            "springstrength": 120000,
            "sprungmass": 7400,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_1_center",
            "width": 0.9
        },
        "wheel_1_1_fake": {
            "bonename": "Wheel_1_1",
            "boundary": "Wheel_1_1_rim",
            "center": "Wheel_1_1_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "left",
            "springdamperrate": 128000,
            "springstrength": 120000,
            "sprungmass": 7400,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_1_center",
            "width": 0.9
        },
        "wheel_2_1": {
            "bonename": "Wheel_2_1",
            "boundary": "Wheel_2_1_rim",
            "center": "Wheel_2_1_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "left",
            "springdamperrate": 51200,
            "springstrength": 1580000.0,
            "sprungmass": 7200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_2_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_2_1_center",
            "width": 0.48
        },
        "wheel_2_2": {
            "bonename": "Wheel_2_2",
            "boundary": "Wheel_2_2_rim",
            "center": "Wheel_2_2_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "right",
            "springdamperrate": 51200,
            "springstrength": 1580000.0,
            "sprungmass": 7200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_2_2_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_2_2_center",
            "width": 0.48
        },
        "wheel_3_1": {
            "bonename": "Wheel_3_1",
            "boundary": "Wheel_3_1_rim",
            "center": "Wheel_3_1_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "left",
            "springdamperrate": 51200,
            "springstrength": 1580000.0,
            "sprungmass": 7200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_3_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_3_1_center",
            "width": 0.48
        },
        "wheel_3_2": {
            "bonename": "Wheel_3_2",
            "boundary": "Wheel_3_2_rim",
            "center": "Wheel_3_2_center",
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
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 3,
            "side": "right",
            "springdamperrate": 51200,
            "springstrength": 1580000.0,
            "sprungmass": 7200,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_3_2_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_3_2_center",
            "width": 0.48
        }
    },
    "wheelsteeringsensitivity": 2,
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